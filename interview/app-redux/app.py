import json
import sys

# {{{
def get_content(url):
    with open(url, "r") as reader:
        return reader.read()
# }}}

# {{{
def get_json(o):
    return json.dumps(o, sort_keys=True, indent=4)

# }}}

def main():
    f = open("./lang.json", "r")
    data = f.read()
    f.close()
    lang = json.loads(data)

    f = open("./programmer.json", "r")
    data = f.read()
    f.close()
    programmer = json.loads(data)

    # Let's show the programmers.
    i = 0
    for prog in programmer:
        print(f"{i}: {prog}")
        i += 1

# {{{
    for i, prog in enumerate(programmer):
        print(f"{i}: {prog}")

# }}}

    # We want the two lists in the following format:
    #
    # [ (programmer, lang) ]
    # [('alice', 'c'), ('bob', 'elm'), ...]

    z = []
    for i in range(len(programmer)):
        z.append((programmer[i], lang[i]))
    print(z)

# {{{
#    print(list(zip(programmer, lang)))
# }}}


if __name__ == "__main__":
    main()


