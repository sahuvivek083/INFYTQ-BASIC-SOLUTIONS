"""
Write a Python function which generates and returns a dictionary where the
keys are numbers between 1 and n (both inclusive) and the values are square
of keys.
Sample Input	Expected Output
10	            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
                 10: 100}
"""
def square_keys(num):
    new_dict={i :i*i for i in range(1,num+1)}
    return new_dict
num=10
print("new_dict=",square_keys(num))


