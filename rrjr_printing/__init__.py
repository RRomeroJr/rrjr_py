def pr_separate():
    print("-------------")

def indent(spaces:int, inp:str):
    return "".join([" "] * spaces) + inp
def ellipsis_truc(inp, max = 50, strip = True):
    inp = str(inp)
    if len(inp) <= max:
        return inp
    if strip:
        return inp[:max].strip()+"..."
    else:
        return inp[:max]+"..."