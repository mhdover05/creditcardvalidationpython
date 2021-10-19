accountNumber = input("enter an account number")
def accountValidation(string):
    i = 0
    n = len(string)
    s = len(string)
    validationCode = 0
    while(n>0):
        if ((i+1)%5):
            if(string[i].isnumeric()):
                validationCode = 1
            else:
                validationCode = 0
                return validationCode
        else:
            if(string[i]==" "):
                print(" ")
        i=i+1
        n=n-1
    return validationCode
code = accountValidation(accountNumber)
if(code==1):
    accountView = "**** **** **** " +accountNumber[-4] +accountNumber[-3] +accountNumber[-2] +accountNumber[-1]
else:
    print("Enter a valid account number")
print(accountView)
