import sys

def getContent(url):
    with open(url, "r") as reader:
        content = reader.read()

    return content


def cat(file1, file2):
    return "".join((getContent(file1), getContent(file2)))


def cmp(str1, str2):
    return str1 == str2


def main():
    return cat(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    sys.stdout.write(main())

