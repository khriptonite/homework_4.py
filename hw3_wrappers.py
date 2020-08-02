
def wrap_brackets( text ):
    return "(" + text + ")"

def wrap_brackets2( text ):
    return "[" * 3 + text + "]" * 3

def wrap_brackets3( text ):
    return "<" * 3 + text + ">" * 3

print(wrap_brackets3(wrap_brackets2(wrap_brackets("12345"))))