import os


dirpath = os.path.dirname(os.path.realpath(__file__))


def reverse_string(s, r_s=[]):
    if len(s) == 1:
        r_s.append(s)
        return ''.join(r_s)

    r_s.append(s[-1])
    return reverse_string(s[:-1])

if __name__ == "__main__":
    filename = os.path.join(dirpath, 'input.txt')
    f = open(filename, 'r')
    string = f.readline()
    f.close()

    r_string = reverse_string(string)

    filename = os.path.join(dirpath, 'output.txt')
    f = open(filename, 'w')
    f.write(r_string)
    f.close()
