try:
    import bs4 as _bs4
except ImportError as _ie:
    raise ImportError("[rrjr] Beautiful soup not found, but you tried to import beautiful soup stuff.") from _ie
# from rrjr_fm import sp_open as _sp_open Example for the future
# Get Tag from the imported module, not "from bs4"
_Tag = _bs4.Tag
def g_tag_head(tag: _Tag):
    attrs = " ".join(f"{k}={v}" for k,v in tag.attrs.items())
    if attrs != "":
        attrs = " " + attrs
    return f"<{tag.name}{attrs}>"