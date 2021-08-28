"""Write a python function to add 'ing' at the end of a given string and return the new string.
If the given string already ends with 'ing' then add 'ly'.
If the length of the given string is less than 3, leave it unchanged.
sleep	sleeping
amazing	amazingly
is	is"""

def add_string(str1):
    # start writing your code here
    if len(str1) >= 3:
        if str1.endswith("ing"):
            str1 = str1 + "ly"

        else:
            if not str1.endswith("ly") and str1 not in ["the"]:
                str1 = str1 + "ing"

    return str1

str1=input()
print(add_string(str1))
