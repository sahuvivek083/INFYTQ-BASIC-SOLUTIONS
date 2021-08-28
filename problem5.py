"""
Write a python function which accepts a sentence and finds the number of
letters and digits in the sentence.
It should return a list in which the first value should be letter count and
second value should be digit count.
Ignore the spaces or any other special character in the sentence.

Sample Input	Expected Output
Infosys 123	[7,3]
ABCEFG	[6,0]
"""
def num_letters_digits(sentence):
    import re
    alpha_list=re.findall("[A-Z]", sentence,re.I)
    digit_list=re.findall("\d",sentence)

    result=[len(alpha_list),len(digit_list)]
    return result
sentence="Infosys 123"
print(num_letters_digits(sentence))



