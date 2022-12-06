import sys


def print_arg(arg):
    print(f"arg received : {arg}")
    return "print_arg"


def start():
    print("this works")
    return "start finished"


def print_args(args):
    print(f"args : {args}")
    return {"vals": args[1]}


if __name__ == "__main__":
    start()
    args = sys.argv
    if len(args) > 1:
        print_args(args)
