#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: April 5, 2022
# This program asks the user for their age
# then if check if are older than 25 and
# younger than 40 years of age and tell them if
# they can date or not


def main():
    # ask users for their age
    string_age = input("Enter your age ")

    # check for type of input 
    try:
        integer_age = int(string_age)
        print("")
        # check user age and display the message
        if (integer_age > 25) and (integer_age < 40):
            print("You can date the grandchild.")
        if (integer_age > 40):
            print("You are too old to date the grandchild.")
        if(integer_age < 25):
            print("You are too young to date the grandchild.")

    # check for type of input 
    except Exception:
        print("")
        print( "input is not a integer.")

if __name__ == "__main__":
    main()
