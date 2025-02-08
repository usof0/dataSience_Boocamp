from random import randint
import logging
import requests
# import json
from config import TEL_CHAT_ID, TEL_WEBHOOK_URL

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        logging.info(f"Initializing Research with file: {file_path}")
        self.data = self.file_reader(self.has_header())
        self.Analytics = self.Analytics(self.data)

    def has_header(self):
        logging.info("Checking if file has a header")
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline()
            if first_line.strip().split(',') == ['head', 'tail']:
                return True
            else:
                return False
        except FileNotFoundError:
            logging.error(f"File {self.file_path} does not exist")
            raise FileNotFoundError(f"File {self.file_path} does not exist")
        
    def file_reader(self, has_header=True):
        logging.info(f"Reading file {self.file_path} with header={has_header}")
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        if len(lines) < 1:
            logging.error("File is empty")
            raise ValueError("File is empty.")
        
        start_index = 1 if has_header else 0
        data = []

        for line in lines[start_index:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['0', '1'], ['1', '0']]:
                logging.error(f"Invalid data in file: {line}")
                raise ValueError(f"Invalid data in file: {line}")
            data.append([int(values[0]), int(values[1])])

        logging.info(f"Successfully read {len(data)} observations from file")
        return data
    
    def send_telegram_message(self, message):
        logging.info("Sending message to Telegram")
        payload = {
            "chat_id" : TEL_CHAT_ID,
            "text" : message
        }
        try:
            response = requests.post(TEL_WEBHOOK_URL, json=payload)
            response.raise_for_status()
            logging.info("Message sent successfully to Telegram")
        except Exception as e:
            logging.error(f"Failed to send message to Telegram: {e}")
    
    class Calculations:
        def __init__(self, data):
            logging.info("Initializing Calculations")
            self.data = data

        def counts(self,data):
            logging.info("Calculating counts of heads and tails")
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails
        
        def fractions(self, heads, tails):
            logging.info("Calculating fractions of heads and tails")
            total = heads + tails
            if total == 0:
                return 0, 0
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction
        
    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)
            logging.info("Initializing Analytics")

        def predict_random(self, num_predictions):
            logging.info(f"Generating {num_predictions} random predictions")
            predictions = []
            for _ in range(num_predictions):
                prediction = randint(0, 1)
                predictions.append([prediction, 1 - prediction])
            return predictions
        
        def predict_last(self):
            logging.info("Retrieving the last observation")
            return self.data[-1]

        def save_file(self, data, file_path):
            logging.info(f"Saving data to {file_path}")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)
