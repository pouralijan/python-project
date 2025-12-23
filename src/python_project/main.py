def hello_world() -> str:
    """Return a greeting message."""
    return "Hello, World!"


def main() -> None:
    """Run the main program."""
    print(hello_world())  # noqa: T201


if __name__ == "__main__":
    main()
