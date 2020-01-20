customer_details = [{
    "Email": "omoloja.kazeem@gmail.com",
    "Password": "123456",
    "Balance":120
},{
    "Email": "omoloja.kaz@gmail.com",
    "Password": "Olute",
    "Balance":100.0
}]


def initialize():
    option = input("""
    Press 1: Create Account
    Press 2: Transaction >
    """)
    if option == '1':
        create_account()
    elif option == '2':
        perform_transaction()
    else:
        print("I don't Understand")
        create_account()

def create_account():
    print("""To create an Account, you would need an 
    1. email/Unique identity
    2. Password
    """)
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    if email not in customer_details:
        if '@' and '.' in email:
            customer_details.append({'Email':email})
            customer_details.append({'Password':password})
            customer_details.append({'Balance':0.0})
            print("User Added Successfully")
        else:
            print("Email not in the correct Format")
            
    else:
        print("User already Exist")
    
def perform_transaction():
    
    user_email = input("Enter your Email: ")
    user_pass = input("Enter your Password: ")
    for data in customer_details:
        if user_email in data['Email']:
            if data['Password'] == user_pass:
                option = input("""
            Press 1: check balance
            Press 2: deposit
            Press 3: withdraw
            Press 4: transfer
            """)
                if option == '1':
                    print(f'Your Account Balance is: {data["Balance"]}')
                elif option == '2':
                    deposit = int(input("How much do you want to deposit?: "))
                    data['Balance'] += deposit
                elif option == '3':
                    withdrawal = int(input("How much do you want to Withdraw?: "))
                    data['Balance'] -= withdrawal
                elif option == '4':
                    transfer = int(input("How much do you want to Transfer?: "))
                    data['Balance'] -= transfer
            else:
                print("Can't Find User")
        
initialize()
global option
