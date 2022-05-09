# pylint: disable=trailing-whitespace, disable=too-few-public-methods
"""
Class for works with csv
"""
import csv
import logging
import os


class CsvWorker:
    """_summary_
    """
    def __init__(self):
        self.two_on_x = "services/backend/src/matrix_csv/2onX.csv"
        self.three_on_x = "services/backend/src/matrix_csv/matrix_csv/3onX.csv"
        self.a_a = ""
    
    def _return_table_type(self, type_of_table: int):
        match type_of_table:
            case 0:
                return self.two_on_x
            case 1:
                return self.three_on_x
            
    
    def get_matrix(self, table_type: int):
        """Method for returning matrix from csv

        Args:
            table_type (int): 0 = two on X, 1 three on x
            start_row (str): where table start in csv
        """
        items = []            
        
        with open(self._return_table_type(table_type), encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                items.append(row)


a = CsvWorker()
a.get_matrix(0)