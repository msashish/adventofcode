import os
import sys


class CommonTools:
    records = []

    def get_input_data(self, mod_name):
        module_name = os.path.basename(mod_name).split('.')[0]
        with open(f"inputs/data_{module_name}.txt", 'r') as f:
            for row in f:
                self.records.append(row[:-1])
        return self.records
