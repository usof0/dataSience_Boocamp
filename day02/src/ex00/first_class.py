class Must_read:
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    Must_read
