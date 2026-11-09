def greet(name: str) -> str:
    if not name:
        raise ValueError("имя не может быть пустым")
    return f"Привет, {name}!"

if __name__ == "__main__":
    print(greet("Мир"))