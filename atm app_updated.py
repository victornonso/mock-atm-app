import random
import deposit_withdrawals_class

database ={}

def generateNewAccount():

    return random.randrange(1111111111,9999999999)

def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("enter password \n")

    newAccountNumber = generateNewAccount()

    database[newAccountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % newAccountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for newAccountNumber,personalInfo in database.items():
        if(newAccountNumber == accountNumberFromUser):
            if(personalInfo[3] == password):
                bankOperation(personalInfo)
                user = personalInfo
        # else : print ('account number or pin!')

def withdrawalOperation():
    print("withdrawal")


def depositOperation():
    print("Deposit Operations")

def logout():
    login()

newUser = deposit_withdrawals_class.Transactions("user", 0)


def bankOperation(user):
    print('These are the available options:')
    print('1. Cash Deposit')
    print('2. Withdrawal')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:\n'))

    if(selectedOption == 1):   
        new_deposit = newUser.deposit(5000, "first deposit")
        print (new_deposit)
        print("************************************")
        bankOperation(user)
    elif(selectedOption == 2):
        new_drawings = newUser.withdraw(2000, "first withdrawal")
        print (new_drawings)
        print("************************************")
        bankOperation(user)
    elif(selectedOption == 3):
        complaint = input("please what issues are you having with our services \n")
        return (complaint)
    elif(selectedOption == 4):
        exit()
    else:
        print('Invalid Option selected, please try again')

print("Welcome, what would you like to do?")
print ("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    login()
elif(actionSelect == 2):
    register()


          


    
        






























