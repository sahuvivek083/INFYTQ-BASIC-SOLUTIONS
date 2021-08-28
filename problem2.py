"""
Write a python function which accepts a string containing a pattern of brackets
and returns true if the pattern of brackets is correct. Otherwise it returns false.
The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.

Sample Input	Expected Output
)()((()())	False
()((())())	True
"""
def bracket(input_str):
    if input_str.count("(") == input_str.count(")") and input_str.startswith("(") and input_str.endswith(")"):
        return True
    else:
        return False

input_str1=')()((()())'
input_str2='()((())())'
print(bracket(input_str1))
print(bracket(input_str2))
