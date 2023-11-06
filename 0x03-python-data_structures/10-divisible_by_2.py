#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Tru_Fals_list = []
    if my_list:
        for list_item in my_list:
            if list_item % 2 == 0:
                Tru_Fals_list.append(True)
            else:
                Tru_Fals_list.append(False)
        return Tru_Fals_list
