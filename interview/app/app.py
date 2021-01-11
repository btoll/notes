import sys

# python3 app.py foo.txt bar.txt

# {{{
def get_content(url):
    with open(url, "r") as reader:
        content = reader.read()

    return content


def cat(file1, file2):
    return "".join((get_content(file1), get_content(file2)))


def cmp(str1, str2):
    return str1 == str2


def check_password(password, get_external_resource):
    return cmp(password, get_external_resource())
# }}}


def get_external_resource():
    # This could query a database, for example.
    return "foo\nbar\n"


def main():
    with open(sys.argv[1], "r") as reader:
        data1 = reader.read()

    with open(sys.argv[2], "r") as reader:
        data2 = reader.read()

    print("cat:\n", data1 + data2)

    data_from_external_resource = get_external_resource()

    print("check_password:\n", (data1 + data2) == data_from_external_resource)

# {{{
#    print(check_password(cat(sys.argv[1], sys.argv[2]), get_external_resource))
# }}}



if __name__ == "__main__":
    main()


