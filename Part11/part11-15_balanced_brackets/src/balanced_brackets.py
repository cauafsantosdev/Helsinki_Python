
def balanced_brackets(my_string: str):
    my_string = "".join([i for i in my_string if i in "()[]"])

    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    return balanced_brackets(my_string[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    ok = balanced_brackets("(()]")
    print(ok)

    ok = balanced_brackets("([bad egg)]")
    print(ok)