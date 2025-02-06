import sys
import os

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' does not exist.")
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if len(lines) < 1:
            raise ValueError(f"File '{self.file_path}' is empty.")
        
        header = lines[0].strip().split(',')
        if len(header) < 2 or header != ['head', 'tail']:
            raise ValueError("Invalid header . Expected 'head, tail'.")
        
        for line in lines[1:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['0', '1'], ['1', '0']]:
                raise ValueError(f"Invalid data in file: {line.strip()}")
        
        return ''.join(lines)

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 first_constructor.py <input_file>")
        input_file = sys.argv[1]     
        research = Research(input_file)
        print(research.file_reader())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    