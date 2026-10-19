number=input("Enter number of accounts that you want to create: ")
account_details=[]

def show_accounts():
    for index in range(len(account_details)):
        print(f"{account_details[index][0]:<20}|{account_details[index][1]:<20}|{account_details[index][4][3]:<20}")
    

def do_withdraw():
    user_account_no=int(input("Enter your account number:"))
    is_exist,index=validate(user_account_no)
    if(is_exist):
        withdraw_amount=int(input("Enter Withdraw amount"))
        current_balance=account_details[index][4][3]
        new_balance=current_balance - withdraw_amount
        account_details[index][4][3]=new_balance
        print(f"Account updated. Available balance:{new_balance}")
    else:
        print("Account Doesn't Exist. Please try again....")


def validate(user_account):
    for index in range(len(account_details)):
        if user_account in account_details[index]:
            return True,index
    return False,None
        

def do_deposit():
    user_account_no=int(input("Enter your account number:"))
    is_exist,index=validate(user_account_no)
    if(is_exist):
        deposit_amount=int(input("Enter deposite amount"))
        current_balance=account_details[index][4][3]
        new_balance=current_balance+ deposit_amount
        account_details[index][4][3]=new_balance
        print(f"Account updated. Available balance:{new_balance}")
    else:
        print("Account Doesn't Exist.Please try again....")
        

def create_account():
    for n in range(int(number)):
        print(f"-------Enter {n+1} account details------")
        personal_info=[]
        accountNo=int(input("Enter the account number:"))
        accountName=input("Enter Account Holder name")
        panNumber=input("Enter your PAN number:")
        dateofBirth=input("Enter your date of birth(DD-MM-YYYY)")
        emailId=input("Enter your email id:")
        contactNo=input("Enter your contact number:")
        address=input("Enter your address:")
        balance=int(input("Enter your balance:"))
        personal_info.append(emailId)
        personal_info.append(contactNo)
        personal_info.append(address)
        personal_info.append(balance)
        account_info=(accountNo,accountName,panNumber,dateofBirth,personal_info)
        account_details.append(account_info)
        print("*"*30)


create_account()

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Accounts")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        do_deposit()
    elif choice == 2:
        do_withdraw()
    elif choice == 3:
        print(f"{"ACCOUNT NO":<20}|{"NAME":<20}|{"BALANCE":<20}")
        show_accounts()
    else:
        break;




    
    

