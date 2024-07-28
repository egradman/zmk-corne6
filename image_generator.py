from pyparsing import nestedExpr, Word, alphas, Literal


def main():
    with open("config/corne.keymap", "r") as f:
        s = f.read()

    s = remove_bracketed_content("macros", s)
    s = remove_bracketed_content("conditional_layers", s)
    with open("/tmp/corne.keymap", "w") as f:
        f.write(s)


def remove_bracketed_content(keyword, s):
    keyword = Literal(keyword)
    braces_content = nestedExpr("{", "}")
    expr = keyword + braces_content + ";"
    parsed = expr.suppress().transformString(s)
    return parsed


if __name__ == "__main__":
    main()
