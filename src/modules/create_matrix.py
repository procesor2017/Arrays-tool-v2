# pylint: disable=pointless-string-statement
"""
Class for getting together csv and user input
"""
from . import csv_worker

# User payload test [{"0":"a","1":"aa","2":"aaa"},{"0":"b","1":"bb","2":"bbb"}] -> [[a,aa,aaa],[b,bb,bbb]] -> 2 rows and 3 columns
# [{"0":"a","1":"aa","2":"aaa","3":"aaaa","4":"aaaaa"},{"0":"b","1":"bb","2":"bbb","3":"bbbb","4":"bbbbb"},{"4":"ccccc"},{"4":"ddddd"}]

json = [{"0":"a","1":"aa","2":"aaa"},{"0":"b","1":"bb","2":"bbb"}]

def create_orto(table_type, start_row, user_input):
    """_summary_

    Args:
        table_type (_type_): 0 = two on x, 1 three on x
        start_row (_type_): where table start in csv
        user_input (_type_): table which user send me
    """
    csv = csv_worker.CsvWorker()
    load_arr = csv.get_matrix(table_type, start_row)
    # print(load_arr)
    # # [['0', '0', '0'], ['0', '1', '1'], ['1', '0', '1'], ['1', '1', '0']]
    # [['0', '0', '1', '1', '2'], ['0', '1', '0', '1', '1'], ['0', '1', '1', '0', '3'], ['1', '0', '0', '1', '3'], ['1', '0', '1', '0', '1'], ['1', '1', '0', '0', '2'], ['1', '1', '1', '1', '0']]
    print(load_arr)

    w, h = len(load_arr[0]), len(load_arr)

    matrix = [[0 for x in range(w)] for y in range(h)]
    x= 0
    y=0
    for i in load_arr:
        for j in i:
            try:
                matrix[x][y] = user_input[int(j)][str(y)] # user_input[int(j)][str(y)] # První mi z load_arr načte na jakém řádku je ta daná hodnota
            except:
                matrix[x][y] = None
            y+=1
            
        y =0
        x +=1
    return matrix

def get_matrix_type(user_input: list):
    """I need get dict with data where 2^4 4^1 are {2: 4, 4: 1}

    Args:
        user_input (list): _description_
    """
    number_of_row = len(user_input)
    number_of_col = len(user_input[0])
    
    value_list = []
    
    for i in range(0, number_of_col):
        number_of_value = 0
        for j in range(0, number_of_row):
            try:
                if user_input[j][str(i)] is not None:
                    number_of_value += 1
            except KeyError as e:
                pass
        value_list.append(number_of_value)
    
    n_number = {}

    for i in value_list:
        n_number[i] = value_list.count(i)

    return n_number
        

def choose_and_return_matrix(user_input: list):
    
    table_type = list(get_matrix_type(user_input).items())
    
    print(table_type) # {2: 4, 4: 1}
    
    if len(table_type) <= 1:
        """
        Table which have 2 different n_var in row
        2^3 ; 4^5 ; 3^4; 2^11 
        """
        if table_type[0][0] <= 2 and table_type[0][1] <=3:
            return create_orto(0,1, user_input)  # 2^3
        elif table_type[0][0] <= 2 and table_type[0][1] <=11:
            return create_orto(0,17, user_input)  # 2^11 
        elif table_type[0][0] <= 3 and table_type[0][1] <=4:
            return create_orto(1,1, user_input)  # 3^4
        elif table_type[0][0] <= 4 and table_type[0][1] <=5:
            return create_orto(2,1, user_input)  # 4^5
        elif table_type[0][0] <= 5 and table_type[0][1] <=6:
            return create_orto(3,1, user_input)  # 5^6
    elif len(table_type) <= 2:
        """
        Table which have 2 different n_var in row
        2^4 4^1 ; 2^4 3^1 ; 2^8 8^1
        """
        if table_type[0][0] <= 2 and table_type[0][1] <=2:
            if table_type[1][0] <= 6 and table_type[1][1] <=1:
                return create_orto(0,45, user_input)                # 2^2 6^1
            elif table_type[1][0] <= 10 and table_type[1][1] <=1:
                return create_orto(0,173, user_input)               # 2^2 10^1

        elif table_type[0][0] <= 2 and table_type[0][1] <=4:
            if table_type[1][0] <= 3 and table_type[1][1] <=1:
                return create_orto(0,31, user_input)                # 2^4 3^1
            elif table_type[1][0] <= 4 and table_type[1][1] <=1:
                return create_orto(0,7, user_input)                 # 2^4 4^1
        
        elif table_type[0][0] <= 2 and table_type[0][1] <=8:
            if table_type[1][0] <= 5 and table_type[1][1] <=1:
                return create_orto(0,151, user_input)               # 2^8 5^1
            elif table_type[1][0] <= 8 and table_type[1][1] <=1:
                return create_orto(0,59, user_input)                # 2^8 8^1

        elif table_type[0][0] <= 3 and table_type[0][1] <=6:
            if table_type[1][0] <= 6 and table_type[1][1] <=1:
                return create_orto(1,12, user_input)                # 3^6 6^1

        elif table_type[0][0] <= 3 and table_type[0][1] <=9:
            if table_type[1][0] <= 9 and table_type[1][1] <=1:
                return create_orto(1,32, user_input)                # 3^9 9^1

        elif table_type[0][0] <= 4 and table_type[0][1] <=8:
            if table_type[1][0] <= 8 and table_type[1][1] <=1:
                return create_orto(2,19, user_input)                # 4^8 8^1   


    elif len(table_type) <= 3:
        """ More than 2 """
        if table_type[0][0] <= 2 and table_type[0][1] <=3:
            if table_type[1][0] <= 3 and table_type[1][1] <=2:
                if table_type[2][0] <= 6 and table_type[2][1] <=3:
                    return create_orto(0,233, user_input)           # 2^3 3^2 6^3 
        elif table_type[0][0] <= 2 and table_type[0][1] <=4:
            if table_type[1][0] <= 3 and table_type[1][1] <=1:
                if table_type[2][0] <= 6 and table_type[2][1] <=3:
                    return create_orto(0,195, user_input)           # 2^4 3^1 6^3 

    elif len(table_type) <= 4:
        """More Than 3"""
        if table_type[0][0] <= 2 and table_type[0][1] <=5:
            if table_type[1][0] <= 3 and table_type[1][1] <=3:
                if table_type[2][0] <= 4 and table_type[2][1] <=1:
                    if table_type[2][0] <= 6 and table_type[2][1] <=7:
                        return create_orto(0,77, user_input)        # 2^5 3^3 4^1 6^7      
    else:
        pass



# choose_and_return_matrix([{"0":"a","1":"aa","2":"aaa","3":"aaaa","4":"aaaaa"},{"0":"b","1":"bb","2":"bbb","3":"bbbb","4":"bbbbb"},{"4":"ccccc"},{"4":"ddddd"}])