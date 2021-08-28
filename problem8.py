"""
Write a python function which accepts a list of strings containing details of
deposits and withdrawals made in a bank account and returns the net amount in
the account.
Suppose the following input is supplied to the function
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.

Sample Input	                    Expected Output
["D:300","D:200","W:200","D:100"]	400
["D:350","W:100","W:500","D:1000"]	750
"""
def net_amount(string):
    amount=0
    for data in string:
        tr_type=data.split(":")[0]
        #print(tr_type)
        tr_amt=int(data.split(":")[1])
        #print(tr_amt)
        if tr_type=="D":
            amount +=tr_amt
        if tr_type=="W":
            amount -=tr_amt

    return amount
string=["D:300","D:200","W:200","D:100"]
print("Acc_balance:",net_amount(string))
