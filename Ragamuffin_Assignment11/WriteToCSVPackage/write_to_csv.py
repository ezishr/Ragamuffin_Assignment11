# write_to_csv.py

import csv

class Write_To_CSV:
    def __init__(self, path, data, header):
        self.path = path
        self.data = data
        self.header = header

    def write_to_csv_path(self):
        with open(self.path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(self.header)
            writer.writerows(self.data)