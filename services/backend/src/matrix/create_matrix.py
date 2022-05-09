"""
Class for getting together csv and user input
"""
from yaml import load
import csv_worker

# User payload test [{"0":"a","1":"aa","2":"aaa"},{"0":"b","1":"bb","2":"bbb"}] -> [[a,aa,aaa],[b,bb,bbb]] -> 2 rows and 3 columns

json = [{"a", "aa", "aaa"}, {"b","bb","bbb"}]

def create_orto(user_input):
    orto_arr = []
    
    csv = csv_worker.CsvWorker()
    load_arr = csv.get_matrix(0,1)
    # print(load_arr)  # [['0', '0', '0'], ['0', '1', '1'], ['1', '0', '1'], ['1', '1', '0']]
    
    row = 0
    for i in load_arr:
        new_row = []
        val = 0
        for j in i:
            value = user_input[row]
            val +=1
        
        row+=1
    
    
create_orto(json)