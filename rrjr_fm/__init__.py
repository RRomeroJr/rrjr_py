import os as _os
from typing import IO as _IO
from typing import Any as _Any
def sp_open(file, mode, **kwargs) -> _IO[_Any]:
    if (mode == "seq"):
        return open_avoid_overwrite(file, **kwargs)
    else:
        return open(file, mode, **kwargs)

def g_seq_filename(filename: str, underscore = False, start = 0, include_0 = False):
    num = start
    name, ext = _os.path.splitext(filename)
    while True:
        test_name = ''.join(name + ("_" if underscore else "") + (str(num) if num > 0 or include_0 else "") + ext)
        # print(test_name)
        if not _os.path.exists(test_name):
            break
        num += 1
        
    output_name = test_name
    return output_name
def open_avoid_overwrite(filename: str, **kwargs):
    # print("oaow", filename)
    output_name = g_seq_filename(filename, kwargs.get("underscore", False), kwargs.get("start", 0), kwargs.get("include_0", False))
    # print(output_name)

    return open(
        output_name,
        "w",
        kwargs.get("buffering", -1),
        kwargs.get("encoding", None),
        kwargs.get("errors", None),
        kwargs.get("newline", None),
        kwargs.get("closefd", True),
        kwargs.get("opener", None)
    )
if __name__ == "__main__":
    import shutil as _shutil
    try:
        _shutil.rmtree("rrjr_hello_testfn_smile")
    except FileNotFoundError:
        pass
    _os.makedirs("rrjr_hello_testfn_smile")
    path = "rrjr_hello_testfn_smile/testThis_a_test_FFILLEEE.txt"
    for x in range(10):
        with sp_open(path, "seq", encoding="UTF-8", start = 7) as f:
            f.write("all good")
            print(f.name)
    input("any to delete")
    _shutil.rmtree("rrjr_hello_testfn_smile")