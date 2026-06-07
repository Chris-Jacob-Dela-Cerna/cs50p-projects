# Week 9 scratch file - understanding unpacking method and *args/**kwargs

def main():
    show_names("Chris", "Jacob")
    show_names(name="Chris", name2="Jacob")


def show_names(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    main()