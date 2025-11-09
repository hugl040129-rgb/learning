import argparse

from learning.version import __version__  # noqa


def main():
    parser = argparse.ArgumentParser(
        prog="learning",
        description=(
            "To learn how to use Github\n\n"
            "For more information, visit: "
            "https://github.com/hugl040129-rgb/learning/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the program's version number and exit",
    )

    args = parser.parse_args()

    if args.version:
        print(f"learning {__version__}")
    else:
        # Default behavior when no arguments are given
        parser.print_help()


if __name__ == "__main__":
    main()
