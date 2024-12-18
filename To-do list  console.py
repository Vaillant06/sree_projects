#To-Do list console
import datetime
from dataclasses import field

users={1001:["SREENATH","sree@130806",[["pygame","13-12-2024","pending"],["physics","16-12-2024","pending"]]],1002:["ARTHI","arthi@160906",[]]}
user_id=1001

def add_user():
    global users,user_id
    info=[]
    user_id += 1
    print("WELCOME NEW USER")
    user_name = input("Enter the username: ")
    user_password = input("Enter a strong six digit password to secure your data: ")
    found_special = False
    found_digit = False
    special_characters = ["@", "#", "$"]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(user_password) < 6:
        print("\033[91mProvide a strong password of at least 6 characters!\033[0m")
        return users,user_id
    else:
        for char in user_password:
            if char in special_characters:
                found_special = True
            if char in num:
                found_digit = True
        if found_special and found_digit:
            info.append(user_name)
            info.append(user_password)
            info.append([])
            users[user_id] = info
            print(f"Your user_id is {user_id}")
            print("\033[92mNew user has been added successfully!\033[0m\n")
        else:
            print( "\033[91mProvide a strong password containing at least one special character (@, #, $) and one digit!\033[0m")
    return users,user_id



def login():
    global users
    print("-"*30)
    print("DISPLAY USER TO-DO LIST")
    print("-"*30)
    temp_id=int(input("Enter the user_id: "))
    found=False
    for key,values in users.items():
        if temp_id==key:
            found=True
            print(f"WELCOME {values[0]}")
            temp_pw=input("Enter the password: ")
            if temp_pw==values[1]:
                print(f"User {values[0]} has been logged in successfully!")
                print("-"*30)
                print(f"TO-DO LIST OF THE USER {values[0]}")
                print("-"*30)
                if not values[2]:
                    print("No to do list assigned")
                for i in range((len(values[2]))):
                    if values[2][i][2]=="pending":
                        print(f"\033[91m{values[2][i]}\033[0m")
                    else:
                        print(f"\033[92m{values[2][i]}\033[0m")
            else:
                print("\033[91mWrong password!\033[0m")
    if not found:
        print("\033[91mUser ID not found!\033[0m")



def add_to_do_list():
    global users
    print("-" * 30)
    print('ADD TASKS SECTION')
    print("-" * 30)
    to_do_list=[]
    temp_id = int(input("Enter the user_id: "))
    found=False
    for key, values in users.items():
        if temp_id == key:
            found=True
            print(f"Welcome {values[0]}")
            temp_pw = input("Enter the password: ")
            if temp_pw == values[1]:
                print(f"User {values[0]} has been logged in successfully!")
                add_task=input("Enter a task to add: ")
                date=input("Enter the due date(DD-MM-YYYY): ")
                due_date=datetime.datetime.strptime(date, "%d-%m-%Y").date()
                actual_date=due_date.strftime("%d-%m-%Y")
                status=input("Enter the current status of the task: ")
                to_do_list.append(add_task)
                to_do_list.append(actual_date)
                to_do_list.append(status)
                values[2].append(to_do_list)
                break
            else:
                print("Wrong password!")
    if not found:
        print("\033[91mUser ID not found!\033[0m")
    return users



def update_to_do_list():
    global users
    print("-"*30)
    print("UPDATE TO-DO LIST SECTION")
    print("-"*30)
    temp_id = int(input("Enter the user_id: "))
    found=False
    for key, values in users.items():
        if temp_id == key:
            found=True
            print(f"Welcome {values[0]}")
            temp_pw = input("Enter the password: ")
            if temp_pw == values[1]:
                print(f"User {values[0]} has been logged in successfully!")
                print(f"To-Do list of the user {values[0]}")
                for i in range((len(values[2]))):
                    print(f"{i+1}.{values[2][i]}")
                num=int(input("Enter the task number to update: "))
                f=False
                for i in range(len(values[2])):
                    if num==i+1:
                        found=True
                        f = True
                        change=input("Enter the field to change(Name/date/status): ").lower()
                        if change=="name":
                            print(f"Old name: {values[2][i][0]}")
                            new_name=input("Enter the new name for the task: ")
                            if values[2][i][0]==new_name:
                                print("There is no change in the name of the task.")
                            else:
                                values[2][i][0]=new_name
                                print(f"Task name has been updated to {values[2][i][0]} successfully!")
                            break
                        elif change=="date":
                            print(f"Old date: {values[2][i][1]}")
                            new_date = input("Enter the new date for the task: ")
                            if values[2][i][1]==new_date:
                                print("There is no change in the name of the task.")
                            else:
                                values[2][i][1]=new_date
                                print(f"Task name has been updated to {values[2][i][1]} successfully!")
                            break
                        elif change=="status":
                            print(f"Old status: {values[2][i][2]}")
                            new_status = input("Enter the updated status for the task: ")
                            if values[2][i][2]==new_status:
                                print("There is no change in the name of the task.")
                            else:
                                values[2][i][2]=new_status
                                print(f"Task name has been updated to {values[2][i][2]} successfully!")
                            break
                    if f:
                        print("\033[91mEnter the correct field!\033[0m")
            else:
                print("\033[91mWrong password!\033[0m")
    if not found:
        print("\033[91mUser ID not found!\033[0m")
    return users

