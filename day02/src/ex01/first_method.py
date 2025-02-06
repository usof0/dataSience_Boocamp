class Research:
    def file_reader(self):
        try:
            with open('data.csv', 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError as e:
            print(f"Error: {e}")
        
if __name__ == "__main__":
    research = Research()
    text = research.file_reader()

    if text != None:
        print(text)