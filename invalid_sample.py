def greet(name: str) -> str:  # Missing spaces, line too long
    return f"Hello, {name}" * 100  # Line exceeds 100 chars (violates --line-length=100)


print(greet("World"))  # Extra spaces
