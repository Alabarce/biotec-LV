"""Ferramenta de estilo do Boletim LV (Google Docs).

Gera um batch para o update_doc do conector Google Docs a partir de um modelo do documento:
uma lista de parágrafos na ordem final, cada um com "role", "text" e, se for fonte, "link".
Parágrafos novos levam "insert_at": o índice ORIGINAL (do read_doc atual) em que devem ser inseridos.

Uso:
  python3 -I ferramentas/lv_docs.py spec.json saida.json
spec.json = {"doc": "<documentId>", "rev": "<revisionId do read_doc mais recente>", "paras": [...]}
Campos opcionais do spec: "tab" (tabId da aba; padrão: primeira aba) e "absorb_last": true
quando o último parágrafo novo deve usar a quebra de linha final que já existe no documento
(caso de reescrever o corpo inteiro a partir de um índice). Com "reset_from", todos os
parágrafos a partir desse índice têm bordas, sombreamento e recuos zerados antes do estilo.
Papéis: title, subtitle, status, h1, h1draft, h2, note, tag, entry, gloss, alert, linkline.
Veja ESTILO.md para o que cada papel significa.
"""

import json, sys

def rgb(h):
    h = h.lstrip('#')
    return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}

TEAL = rgb("0F4C5C"); AMBER = rgb("B45309"); GRAY = rgb("5F6B73"); INK = rgb("1F2933")
TAG_BG = rgb("DCEFF1"); STATUS_BG = rgb("EEF6F7"); ALERT_BG = rgb("FFF4E5")
SERIF = "Lora"; SANS = "Lato"

def u16(s):
    return len(s.encode("utf-16-le")) // 2

def color(c):
    return {"color": {"rgbColor": c}}

def pt(x):
    return {"magnitude": x, "unit": "PT"}

def border(c, w, pad):
    return {"color": color(c), "width": pt(w), "padding": pt(pad), "dashStyle": "SOLID"}

# papel -> (namedStyle, fonte, tamanho, cor, itálico, negrito, cor do rótulo, estilo de parágrafo)
def box(bar, bg):
    return {"borderLeft": border(bar, 3, 8), "borderTop": border(bg, 0.5, 4),
            "borderBottom": border(bg, 0.5, 4), "shading": {"backgroundColor": color(bg)},
            "indentStart": pt(12), "indentFirstLine": pt(12), "spaceAbove": pt(0), "spaceBelow": pt(0)}

CARD = {"borderLeft": border(TEAL, 2.25, 10), "indentStart": pt(12), "indentFirstLine": pt(12),
        "spaceAbove": pt(0), "spaceBelow": pt(4)}

ROLES = {
    "title":    ("TITLE", SERIF, 30, TEAL, False, False, None, {"spaceBelow": pt(2)}),
    "subtitle": ("SUBTITLE", SANS, 13, GRAY, False, False, None, {"spaceBelow": pt(14)}),
    "status":   ("NORMAL_TEXT", SANS, 10, INK, False, False, TEAL, box(TEAL, STATUS_BG)),
    "h1":       ("HEADING_1", SERIF, 19, TEAL, False, False, None, {}),
    "h1draft":  ("HEADING_1", SERIF, 19, AMBER, False, False, None, {}),
    "h2":       ("HEADING_2", SERIF, 14, TEAL, False, False, None, {}),
    "note":     ("NORMAL_TEXT", SANS, 10, GRAY, True, False, None, {"spaceBelow": pt(8)}),
    "tag":      ("NORMAL_TEXT", SANS, 8, TEAL, False, True, None, {"spaceBelow": pt(6), "keepWithNext": True}),
    "entry":    ("NORMAL_TEXT", SANS, 11, INK, False, False, TEAL, CARD),
    "gloss":    ("NORMAL_TEXT", SANS, 11, INK, False, False, TEAL, {"spaceBelow": pt(6)}),
    "alert":    ("NORMAL_TEXT", SANS, 10, INK, False, False, AMBER, box(AMBER, ALERT_BG)),
    "linkline": ("NORMAL_TEXT", SANS, 11, TEAL, False, False, None, {"spaceAbove": pt(10)}),
}

def label_len(text):
    i = text.find(". ")
    return u16(text[: i + 1]) if i > 0 else 0

def build(paras, rev, doc):
    reqs=[]; ins={}
    for p in paras:
        if "insert_at" in p: ins.setdefault(p["insert_at"],[]).append(p["text"]+"\n")
    for at in sorted(ins, reverse=True):
        reqs.append({"insertText":{"location":{"index":at},"text":"".join(ins[at])}})
    pos=1; spans=[]
    for p in paras:
        s=pos; e=pos+u16(p["text"])+1; pos=e; spans.append((s,e,p))
    END=pos; groups=[]
    for s,e,p in spans:
        if groups and groups[-1][2]==p["role"]: groups[-1][1]=e
        else: groups.append([s,e,p["role"]])
    pr=[];tr=[]
    for s,e,role in groups:
        named,font,size,col,ital,bold,lab,pst=ROLES[role]
        pr.append({"updateParagraphStyle":{"range":{"startIndex":s,"endIndex":e},"paragraphStyle":{"namedStyleType":named},"fields":"namedStyleType"}})
        if pst: pr.append({"updateParagraphStyle":{"range":{"startIndex":s,"endIndex":e},"paragraphStyle":pst,"fields":",".join(pst)}})
        ts={"weightedFontFamily":{"fontFamily":font,"weight":400},"fontSize":pt(size),"foregroundColor":color(col),"italic":ital,"bold":bold,"underline":False}
        if role=="tag": ts["backgroundColor"]=color(TAG_BG)
        tr.append({"updateTextStyle":{"range":{"startIndex":s,"endIndex":min(e,END-1)},"textStyle":ts,"fields":"weightedFontFamily,fontSize,foregroundColor,italic,bold,underline,link,backgroundColor"}})
    for s,e,p in spans:
        if p.get("link"):
            tr.append({"updateTextStyle":{"range":{"startIndex":s,"endIndex":e-1},"textStyle":{"link":{"url":p["link"]},"underline":True,"foregroundColor":color(TEAL)},"fields":"link,underline,foregroundColor"}})
        lab=ROLES[p["role"]][6]
        if lab:
            n=label_len(p["text"])
            lc=AMBER if (p["role"]=="entry" and p["text"].startswith("Implicação.")) else lab
            if n: tr.append({"updateTextStyle":{"range":{"startIndex":s,"endIndex":s+n},"textStyle":{"bold":True,"foregroundColor":color(lc)},"fields":"bold,foregroundColor"}})
    def rnd(o):
        if isinstance(o,float): return round(o,3)
        if isinstance(o,dict): return {k:rnd(v) for k,v in o.items()}
        if isinstance(o,list): return [rnd(x) for x in o]
        return o
    return rnd({"documentId":doc,"requests":reqs+pr+tr,"writeControl":{"requiredRevisionId":rev}}),END
def finish(out, end, spec):
    reqs = out["requests"]
    if spec.get("absorb_last"):
        for r in reqs:
            if "insertText" in r and r["insertText"]["text"].endswith("\n"):
                r["insertText"]["text"] = r["insertText"]["text"][:-1]
                break
    if "reset_from" in spec:
        n = sum(1 for r in reqs if "insertText" in r)
        reqs.insert(n, {"updateParagraphStyle": {"range": {"startIndex": spec["reset_from"], "endIndex": end},
            "paragraphStyle": {}, "fields": "borderTop,borderBottom,borderLeft,shading,indentStart,indentFirstLine,keepWithNext"}})
    tab = spec.get("tab")
    if tab:
        for r in reqs:
            body = next(iter(r.values()))
            for k in ("location", "range"):
                if k in body:
                    body[k]["tabId"] = tab
    for p in spec["paras"]:
        assert "\u2014" not in p["text"] or p.get("keep_dash"), p["text"]
    return out

if __name__=="__main__":
    spec=json.load(open(sys.argv[1])); out,end=build(spec["paras"],spec["rev"],spec["doc"])
    out=finish(out,end,spec)
    json.dump(out,open(sys.argv[2],"w"),ensure_ascii=False,separators=(',',':'))
    print(len(out["requests"]),end)
