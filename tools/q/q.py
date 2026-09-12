#!/usr/bin/env python3
# q — universal free-search CLI: searxng -> sogou-news fallback -> STOP (never silently degrade to paid/native).
# Single source for all runtimes that can run a shell. Configure via env:
#   Q_SEARXNG_URL       default http://127.0.0.1:8888
#   Q_SEARXNG_CONTAINER default searxng   (set empty to disable docker auto-start)
#   Q_LANG              default zh-CN
# Usage:
#   q.py "query" [-n 5] [--json] [--probe] [--sogou-only] [--no-start] [--timeout 20]
# Exit: 0 ok / 1 probe failed / 2 STOP (all free channels failed)
# Every output ends with a stamp line like: [搜索:q/searxng | ¥0]

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

SEARXNG = os.environ.get("Q_SEARXNG_URL", "http://127.0.0.1:8080")
CONTAINER = os.environ.get("Q_SEARXNG_CONTAINER", "searxng")
LANG = os.environ.get("Q_LANG", "zh-CN")
UA = "q-cli/1.0"


def log(s):
    print(s, flush=True)


def http_get_json(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def searxng_alive(timeout=5):
    try:
        q = urllib.parse.urlencode({"q": "ping", "format": "json", "language": LANG})
        http_get_json(f"{SEARXNG}/search?{q}", timeout)
        return True
    except Exception:
        return False


def ensure_searxng(autostart, timeout):
    if searxng_alive():
        return True, "already-up"
    if not CONTAINER or not autostart:
        return False, "down (--no-start or no container name)"
    try:
        subprocess.run(["docker", "start", CONTAINER], check=True,
                       capture_output=True, timeout=30)
    except Exception as e:
        return False, f"docker start failed: {e}"
    for _ in range(15):  # ~15s readiness
        time.sleep(1)
        if searxng_alive():
            return True, "started"
    return False, "started but not healthy in 15s"


def searxng_search(term, n, timeout):
    q = urllib.parse.urlencode({"q": term, "format": "json", "language": LANG})
    d = http_get_json(f"{SEARXNG}/search?{q}", timeout)
    out, seen = [], set()
    for it in d.get("results", []):
        url = (it.get("url") or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        out.append({"title": (it.get("title") or "").strip(),
                    "url": url,
                    "snippet": (it.get("content") or "").strip()[:260]})
        if len(out) >= n:
            break
    return out


def sogou_news(term, n, timeout):
    # Domestic site: bypass any system proxy (trust_env=False equivalent for stdlib+requests)
    import requests
    from bs4 import BeautifulSoup
    s = requests.Session()
    s.trust_env = False
    r = s.get("https://news.sogou.com/news",
              params={"query": term}, timeout=timeout,
              headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    for wrap in soup.select("div.vrwrap"):
        h = wrap.find("h3")
        a = h.find("a") if h else None
        if not a:
            continue
        href = a.get("href") or ""
        if href.startswith("/"):
            href = "https://news.sogou.com" + href
        out.append({"title": a.get_text(" ", strip=True),
                    "url": href,
                    "snippet": wrap.get_text(" ", strip=True)[:260]})
        if len(out) >= n:
            break
    return out


def stop_diag(err_searxng):
    log("[STOP] 免费链全部失效——停车报告，等用户授权后再继续（禁止降级到付费/原生搜索）")
    log("  searxng 侧最后状态: " + err_searxng)
    log("  判别: docker logs " + (CONTAINER or "<searxng>") + " ——")
    log("    · CAPTCHA / 429 / unusual traffic => 上游节流墙：静默 ≥30 分钟自愈，等")
    log("    · httpx.ConnectTimeout 全引擎     => 容器出网断：查宿主代理是否开启")
    sys.exit(2)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(prog="q", description="free search: searxng -> sogou -> stop")
    ap.add_argument("query", nargs="?", help="search term (--probe 可省略)")
    ap.add_argument("-n", type=int, default=5, help="max results (default 5)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--probe", action="store_true", help="health probe: week-range single query, >0 = healthy")
    ap.add_argument("--sogou-only", action="store_true", help="skip searxng, sogou news only (test/force)")
    ap.add_argument("--no-start", action="store_true", help="never docker-start the container")
    ap.add_argument("--timeout", type=int, default=20)
    a = ap.parse_args()

    if a.probe:
        ok = searxng_alive()
        if ok:
            try:
                q = urllib.parse.urlencode({"q": "news", "format": "json",
                                            "language": LANG, "time_range": "week"})
                d = http_get_json(f"{SEARXNG}/search?{q}", a.timeout)
                ok = len(d.get("results", [])) > 0
            except Exception:
                ok = False
        log("probe: " + ("HEALTHY" if ok else "UNHEALTHY"))
        sys.exit(0 if ok else 1)

    if not a.query:
        ap.error("query required (or use --probe)")

    err_searxng = "skipped"
    results, backend = [], None
    if not a.sogou_only:
        up, why = ensure_searxng(autostart=not a.no_start, timeout=a.timeout)
        if up:
            try:
                results = searxng_search(a.query, a.n, a.timeout)
                backend = "searxng"
                err_searxng = "ok"
            except Exception as e:
                err_searxng = f"query error: {e}"
        else:
            err_searxng = why

    if not results:
        try:
            results = sogou_news(a.query, a.n, a.timeout)
            backend = "sogou"
        except Exception as e:
            log(f"[warn] sogou fallback failed: {e}")
            if a.sogou_only or backend is None:
                stop_diag(err_searxng)

    stamp = f"[搜索:q/{backend} | ¥0]"
    if a.json:
        print(json.dumps({"query": a.query, "backend": backend, "results": results,
                          "stamp": stamp}, ensure_ascii=False, indent=2))
    else:
        for i, it in enumerate(results, 1):
            print(f"{i}. {it['title']}\n   {it['url']}\n   {it['snippet']}")
        print(stamp)
    sys.exit(0)


if __name__ == "__main__":
    main()
