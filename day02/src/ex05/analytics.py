from random import randint

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.file_reader(self.has_header())
        self.Analytics = self.Analytics(self.data)

    def has_header(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline()
            if first_line.strip().split(',') == ['head', 'tail']:
                return True
            else:
                return False
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.file_path} does not exist")
        
    def file_reader(self, has_header=True):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        if len(lines) < 1:
            raise ValueError("File is empty.")
        
        start_index = 1 if has_header else 0
        data = []

        for line in lines[start_index:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['0', '1'], ['1', '0']]:
                raise ValueError(f"Invalid data in file: {line}")
            data.append([int(values[0]), int(values[1])])

        return data
    
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self,data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails
        
        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                return 0, 0
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction
        
    class Analytics(Calculations):
        def predict_random(self, num_predictions):
            predictions = []
            for _ in range(num_predictions):
                prediction = randint(0, 1)
                predictions.append([prediction, 1 - prediction])
            return predictions
        
        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)
