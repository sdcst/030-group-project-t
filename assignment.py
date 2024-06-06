#!python3

import math




def title():
    print("\nGreetings and welcome to my calculator.\nThis program is written by Kevin Hu,\nScroll down for more information.")
       

title()

def print_welcome():
    welcome_art = """
__        __   _                                      
\\ \\      / /__| | ___ ___  _ __ ___   ___    
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\          
  \\ V  V /  __/ | (_| (_) | | | | | |  __/             
   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|
 """
    print(welcome_art)

print_welcome()
 


def instructions():
    print("\nThis program will calculate: \nThe volume of a sphere \nThe surface area of sphere \nConverting Between Fahrenheit and Celsius\nConverting Between Celsius and Fahrenheit\nProvincial Sales Tax")

instructions()
import math
a = str(input("\nSay v to calculate the volume of a sphere\nSay s to calculate surface area of a sphere\nSay f for Fahrenheit to Celsius conversion\nSay c for the Celsius to Farenheit conversion\nSay t for the PST calculator\nSay exit if you want to stop the program.\n"))

def voas():
        if a == "v" or a=="V":
            radius = float(input("please enter the radius\n"))
            volume = (4/3) * math.pi * (radius ** 3)
            roundedvolume = round(volume,2)
            print(f"The volume of the sphere is {roundedvolume}")

voas()

def saos():
    if a == "s" or a == "S":
            r = float(input("Please enter the radius\n"))
            sa = 4 * math.pi * (r ** 2)
            roundedsa =round(sa,2)
            print(f"The surface area of the sphere is {roundedsa}")

saos()

def ftoc():
    if a == "f" or a=="F":
        fahrenheit = int(input("Please enter the fahrenheit so I convert it into celsius\n"))
        celsius1 = (fahrenheit - 32) * 5/9
        roundedc =round(celsius1,2)
        print(f"The temperature in celsius is {roundedc} degrees")

ftoc()

def ctof():
    if a=="c" or a=="C":
        celsius = int(input("please enter the celsius so I can convert it into fahrenheit\n"))
        fahrenheit1 = (celsius * 9/5) + 32
        roundedf =round(fahrenheit1,2)
        print(f"The temperature in fahrenheit is {roundedf} degrees")

ctof()

def pst():
    if a == "t" or a=="T":
        price = float(input("Enter your total price\n"))
        pstrate = float(input("Enter the amount of provincial tax rate you have to pay as a decimal\n"))
        pstamount = price * pstrate
        roundedpstamount = round(pstamount,2)
        print(f"The total tax you have to pay is ${roundedpstamount}")
    else:
        print("That's invalid.. rerun the program and try again")
        exit()

pst()

def stop():
    if a == "exit" or a=="Exit" or a=="eXit" or a=="exIt" or a== "exiT" or a=="EXIT":
        print("Bye!")
        exit()

stop()

def again():
    calc_again = input('Do you want to use the calculator again? Type y for Yes and n for No\n')
    if calc_again == 'Y' or calc_again=="y":
        a
    elif calc_again == 'N' or calc_again =="n":
            print('Bye!')
    else:
        print("That is invalid.. Rerun the program and try again")

again()