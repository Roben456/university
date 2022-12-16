import os

dirpath = os.path.dirname(os.path.realpath(__file__))


mapping = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


def brackets1(exp):
    if exp == '\n':
        return True

    ptr = 0
    result = True

    while ptr < len(exp):

        match = mapping.get(exp[ptr])

        if match == None:
            return False

        match_index = exp.find(match)

        if match_index == -1:
            return False

        result = result and brackets1(exp[ptr + 1: match_index])
        ptr = match_index + 1

    return result


def brackets2(input_str):
    print(input_str)
    if len(input_str) == 0:
        return True
    new_str = str(input_str)
    new_str = new_str.replace('()', '').replace(
        '[]', '').replace('{}', '').replace('<>', '')

    print(input_str)
    if new_str == input_str:
        return False

    return brackets2(new_str)


if __name__ == '__main__':
    filename = os.path.join(dirpath, 'input.txt')
    f = open(filename, 'r')
    input_str = f.readline()
    print(input_str)
    print(brackets2(input_str))
