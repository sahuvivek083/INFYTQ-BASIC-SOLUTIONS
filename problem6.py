"""
Write a python function which accepts a list of numbers
and returns true, if 1, 2, 3 appears in sequence in the list.
Otherwise, it should return false.

Sample Input	Expected Output
[1, 1, 2, 3, 1]	True
[1, 1, 2, 4, 3]	False
"""
def list_num(list):
    list= str(list).replace(" ", "")
    if "1,2,3" in list:
        return True
    else:
        return False
list=[1,1,2,3,1]
print(list_num(list))