# pylint: disable=trailing-whitespace, disable=too-few-public-methods
"""
Class for works with csv
"""
import csv
import os
from os import listdir

class CsvWorker:
    """_summary_
    """
    def __init__(self):
        """
        Path for single docker:
        "app/modules/matrix_csv/2onX.csv"

        Path for compose:
        "./src/modules/matrix_csv/2onX.csv"
        """
        self.two_on_x = "./src/modules/matrix_csv/2onX.csv"
        self.three_on_x = "./src/modules/matrix_csv/2onX.csv"
    
    def _return_table_type(self, type_of_table: int):
        print(os.listdir())
        match type_of_table:
            case 0:
                return self.two_on_x
            case 1:
                return self.three_on_x

    def get_matrix(self, table_type: int, start_row: int):
        """Method for returning modules from csv

        Args:
            table_type (int): 0 = two on X, 1 three on x
            start_row (str): where table start in csv
        """
        items = []            
        
        with open(self._return_table_type(table_type), encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            # rows = [row for id, row in enumerate(csv_reader) if id in range(0, 10)]
            for row in (r for i, r in enumerate(csv_reader) if i in range(start_row,999)):
                if row == []:
                    break
                else:
                    items.append(row)
        return items
