import sys
from tools import cat

def main():
    return cat(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    sys.stdout.write(main())

