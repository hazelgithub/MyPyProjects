class SigFigSuspension():
    def __init__(self,account,status):
        self.account = account
        self.status  = status

    def sigfigsusp(self):
        if self.status == ('A' or 'a'):
            return ('Account is Active' )
        else :
            return ('Account is not Active ')

Acct_Num = input("Account Number- > ")
Status   = input("Enter Status -> ")

#print(int(Acct_Num))


if isinstance(Acct_Num,int) == True :
    sigfigsuspension = SigFigSuspension(Acct_Num,Status)
    print(sigfigsuspension.sigfigsusp())
else :
    print("It is not Numerical  ")

list1 = [1,2,3,4,5],[6,7,8,9,10]
print(list1)
print((list1[0][1]))
