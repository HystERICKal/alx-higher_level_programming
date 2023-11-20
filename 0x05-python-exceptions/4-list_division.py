#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for v in range(list_length):
        try:
            divis_result = my_list_1[v] / my_list_2[v]
        except TypeError:
            print('wrong type')
            divis_result = 0
        except ZeroDivisionError:
            print('division by 0')
            divis_result = 0
        except IndexError:
            print('out of range')
            divis_result = 0
        finally:
            final_list.append(divis_result)
    return final_list
