"""Minimal PDF text extractor (pure stdlib) for the Gundam Assemble rulebook.

Scans objects, inflates FlateDecode streams, resolves page -> font -> ToUnicode
CMaps, and walks content-stream text operators in order.
"""
import re
import sys
import zlib

data = open(sys.argv[1], "rb").read()

# --- collect objects -------------------------------------------------------
objs = {}
for m in re.finditer(rb"(\d+)\s+(\d+)\s+obj\b", data):
    num = int(m.group(1))
    start = m.end()
    end = data.find(b"endobj", start)
    if end == -1:
        continue
    objs[num] = data[start:end]

STREAM_RE = re.compile(rb"stream\r?\n(.*?)\r?\nendstream", re.S)


def body(num):
    return objs.get(num, b"")


def stream_of(num):
    o = body(num)
    m = STREAM_RE.search(o)
    if not m:
        return None
    raw = m.group(1)
    if b"/FlateDecode" in o[: m.start()]:
        try:
            return zlib.decompress(raw)
        except Exception:
            return None
    return raw


def dict_of(num):
    o = body(num)
    i = o.find(b"stream")
    return o[:i] if i != -1 else o


# --- page order ------------------------------------------------------------
pages = [n for n in sorted(objs) if b"/Type" in dict_of(n) and re.search(rb"/Type\s*/Page[^s]", dict_of(n))]
if not pages:
    pages = [n for n in sorted(objs) if b"/Type" in dict_of(n) and b"/Type /Page" in dict_of(n)]


def refs(txt, key):
    m = re.search(rb"/" + key + rb"\s*(\[[^\]]*\]|\d+\s+\d+\s+R)", txt)
    if not m:
        return []
    return [int(x) for x in re.findall(rb"(\d+)\s+\d+\s+R", m.group(1))]


def font_map(page_num):
    """Determine encoding per font resource name on a page: {/F1: {code: str}}"""
    d = dict_of(page_num)
    out = {}
    res_refs = refs(d, b"Resources")
    res = dict_of(res_refs[0]) if res_refs else d
    fm = re.search(rb"/Font\s*<<(.*?)>>", res, re.S)
    if not fm:
        fr = refs(res, b"Font")
        if fr:
            fm = re.search(rb"/[A-Za-z0-9]+", dict_of(fr[0]))
            fonts_blob = dict_of(fr[0])
        else:
            return out
    else:
        fonts_blob = fm.group(1)
    for name, num in re.findall(rb"/([A-Za-z0-9#+._-]+)\s+(\d+)\s+\d+\s+R", fonts_blob):
        fd = dict_of(int(num))
        tu = re.search(rb"/ToUnicode\s+(\d+)\s+\d+\s+R", fd)
        cmap = {}
        if tu:
            cs = stream_of(int(tu.group(1)))
            if cs:
                cmap = parse_cmap(cs)
        out[b"/" + name] = cmap
    return out


def parse_cmap(cs):
    cmap = {}
    for m in re.finditer(rb"beginbfchar(.*?)endbfchar", cs, re.S):
        for src, dst in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", m.group(1)):
            try:
                cmap[int(src, 16)] = bytes.fromhex(dst.decode()).decode("utf-16-be", "ignore")
            except Exception:
                pass
    for m in re.finditer(rb"beginbfrange(.*?)endbfrange", cs, re.S):
        blob = m.group(1)
        for lo, hi, dst in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", blob):
            lo_i, hi_i = int(lo, 16), int(hi, 16)
            base = bytes.fromhex(dst.decode())
            start = int.from_bytes(base, "big")
            for k in range(hi_i - lo_i + 1):
                try:
                    cmap[lo_i + k] = (start + k).to_bytes(len(base), "big").decode("utf-16-be", "ignore")
                except Exception:
                    pass
        for m2 in re.finditer(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*\[(.*?)\]", blob, re.S):
            lo_i = int(m2.group(1), 16)
            for i, d in enumerate(re.findall(rb"<([0-9A-Fa-f]+)>", m2.group(3))):
                try:
                    cmap[lo_i + i] = bytes.fromhex(d.decode()).decode("utf-16-be", "ignore")
                except Exception:
                    pass
    return cmap


def unescape(s):
    out = bytearray()
    i = 0
    while i < len(s):
        c = s[i]
        if c == 0x5C and i + 1 < len(s):
            n = s[i + 1]
            mp = {0x6E: 10, 0x72: 13, 0x74: 9, 0x62: 8, 0x66: 12}
            if n in mp:
                out.append(mp[n]); i += 2
            elif 0x30 <= n <= 0x37:
                j = i + 1; oct_s = b""
                while j < len(s) and len(oct_s) < 3 and 0x30 <= s[j] <= 0x37:
                    oct_s += bytes([s[j]]); j += 1
                out.append(int(oct_s, 8) & 0xFF); i = j
            else:
                out.append(n); i += 2
        else:
            out.append(c); i += 1
    return bytes(out)


TOKEN = re.compile(
    rb"/([A-Za-z0-9#+._-]+)\s+[\d.]+\s+Tf"
    rb"|(\((?:\\.|[^\\()])*\))\s*Tj"
    rb"|<([0-9A-Fa-f\s]+)>\s*Tj"
    rb"|\[((?:\((?:\\.|[^\\()])*\)|<[0-9A-Fa-f\s]+>|[^\]])*)\]\s*TJ"
    rb"|(T\*|Td|TD|'|\")"
    rb"|(ET)",
    re.S,
)


def decode_str(raw, cmap):
    if cmap:
        if len(raw) % 2 == 0 and max(cmap, default=0) > 255:
            codes = [int.from_bytes(raw[i:i + 2], "big") for i in range(0, len(raw), 2)]
        else:
            codes = list(raw)
        return "".join(cmap.get(c, "") for c in codes)
    return raw.decode("latin-1", "ignore")


def page_text(page_num):
    d = dict_of(page_num)
    cont = refs(d, b"Contents")
    if not cont:
        m = re.search(rb"/Contents\s+(\d+)\s+\d+\s+R", d)
        cont = [int(m.group(1))] if m else []
    if not cont:
        return ""
    fonts = font_map(page_num)
    chunks = []
    cur = {}
    for c in cont:
        cs = stream_of(c)
        if not cs:
            continue
        for t in TOKEN.finditer(cs):
            if t.group(1):
                cur = fonts.get(b"/" + t.group(1), {})
            elif t.group(2) is not None:
                raw = t.group(2)[1:-1]
                chunks.append(decode_str(unescape(raw), cur))
            elif t.group(3) is not None:
                chunks.append(decode_str(bytes.fromhex(re.sub(rb"\s", b"", t.group(3)).decode()), cur))
            elif t.group(4) is not None:
                s = t.group(4)
                for part in re.finditer(rb"\((?:\\.|[^\\()])*\)|<([0-9A-Fa-f\s]+)>", s):
                    if part.group(1) is not None:
                        chunks.append(decode_str(bytes.fromhex(re.sub(rb"\s", b"", part.group(1)).decode()), cur))
                    else:
                        raw = part.group(0)[1:-1]
                        if raw.strip() == b"":
                            chunks.append(" ")
                        else:
                            chunks.append(decode_str(unescape(raw), cur))
            elif t.group(5):
                chunks.append("\n")
            elif t.group(6):
                chunks.append("\n")
        chunks.append("\n")
    txt = "".join(chunks)
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt


print(f"objects={len(objs)} pages={len(pages)}", file=sys.stderr)
out = open(sys.argv[2], "w", encoding="utf-8") if len(sys.argv) > 2 else sys.stdout
for idx, p in enumerate(pages, 1):
    t = page_text(p).strip()
    print(f"\n===== PAGE {idx} (obj {p}) len={len(t)} =====", file=out)
    print(t, file=out)
