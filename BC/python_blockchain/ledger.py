import pandas as pd
from datetime import datetime

class Ledger:
    def __init__(self):
        self.records = []

    def add_record(self, timestamp, data_type):
        record = {'Timestamp': timestamp, 'Data Type': data_type}
        self.records.append(record)

    def save_to_excel(self, filename="ledger.xlsx"):
        df = pd.DataFrame(self.records)
        df.to_excel(filename, index=False)

    def get_ledger(self):
        return self.records
