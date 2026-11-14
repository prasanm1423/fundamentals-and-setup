"""Phase 1 milestone — simple Hello World project."""


def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
    print(greet("Internship"))