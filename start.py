#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random
def user_detail(firstname,secondname,password):
    new_user=User(firstname,secondname,password)
    return new_user
def add_user(new_user):
    '''
    Add new user to userlist
    '''
    User.add_user(new_user)
#credential operationn functions
def create_credential(name,username,passcode):
    credential=Credential(name,username,passcode)
    return credential

def add_credential(credential):
    '''
    Add credential to credential list
    '''
    Credential.add_credential(credential)
    
def delete_all():
    '''
    empty all list
    '''
    Credential.delete_all()
def delete_by_account_name(name):
    '''
    Delete by account name
    '''
    Credential.delete_by_account(name)
    
def find_by_username(name):
    
    return Credential.find_by_username(name)
def display_all():
    return Credential.display_all()

print('Welcome to may Valult')
print('__         __     ____     ._.    ._.  ._.   .____________.')
print('\ \       / /    / /\ \    | |    | |  | |   |____    ____|')
print(' \ \     / /    / /  \ \   | |    | |  | |        |  |')
print('  \ \   / /    / /====\ \  | |____| |  | |_____.  |  |')
print('   \_\./_/    /_/      \_\  \.______/   \______|  | _|')
print('Use the following short command to operate \n')
print('op -------- to open Vault')
print('cl -------- to close Vault')

operation=input('Select operation\n').lower()
if operation=='op':
    firstname=input("Enter first name\n").lower()
    secondname=input('Enter Second name\n').lower()
    password=input('Enter Your preffered password!\n')
    add_user(user_detail(firstname,secondname,password))
    
    print ('Dear '+firstname+' '+secondname+' Your system generated email is '+User.user_list[0].email+ '\n')
    print('Account created!!')
    print('<======================================================================>\n')
    print(User.user_list[0].email, User.user_list[0].password)
    passwordc=input("Confirm Your password!\n")
    while passwordc==User.user_list[0].password:
        
        print('<=====+++++++=============================++++++++++======================>\n')
        print('Use the following codes to manage you password!\n')
        print('add    -------------------------   Add credentials\n')
        print('del    -------------------------   Delete  credential\n')
        print('del-a  -------------------------   Delete all\n')
        print('date   -------------------------   To update name\n')
        print('sp     -------------------------   To show password for account\n')
        print('dc     -------------------------   display credential accounts\n')
        print('ex     -------------------------   Exit application\n')
        code=input('Enter operation code!\n').lower()
        if code=='add':
            name=input('Enter account name\n').lower()
            username=input('Enter username\n').lower().lower()
            print('Select option of password\n')
            print('gn ------------ Generate password\n')
            print('ep---------------- Enter your password\n')
            print('<=====================================================>')
            choice=input("Enter password mode\n")
            if choice=='ep':
                passcode=input("Enter choice password\n")
                add_credential(create_credential(name,username,passcode))
                
            elif choice=='gn':
                passcode=random.randint(00000,99999)
                #add to credential list
                add_credential(create_credential(name,username,passcode))
                
        elif code=='del':
            task=input('Enter account to delete\n').lower()
            delete_by_account_name(task)
            
        elif code=='del-a':
            task=input("Are you sure you to delete all credentials? Y/N\n").lower()
            if task=='y':
                if len(display_all())>0:
                 delete_all()
                 print("Done deleting!!")
                else:print("Nothing to delete")

        
        elif code=='sp':
            task=input('Enter account to view')
            if find_by_username(task):
                cred=find_by_username(task)
                print(cred.passcode)
        
        elif code=='dc':
            task=input("Credential to display\n").lower()
            if display_all():
               for credential in display_all():
                   print("Account name :"+credential.name+"\nAccount username :"+credential.username+"\nPassword :"+credential.passcode+ "\n")
            else:print("No credentials")
        elif code=="ex":
                break      
        else:print("Uknown Command")
 
elif operation=='cl':
    print('Exiting program....')
else:print("Unrecognised input!")