from functions.addeqyes import *
import os
from time import sleep
from art import *
import argparse

parser = argparse.ArgumentParser(description="Check if the sum or difference of two numbers equals a given answer")
parser.add_argument("-a", "--addition", action="store_true", help="Use addition")
parser.add_argument("-s", "--subtraction", action="store_true", help="Use subtraction")

args = parser.parse_args()

os.system('cls' if os.name == 'nt' else 'clear')
if args.addition & args.subtraction:
    print("Error: please specify either --addition or --subtraction")
    exit()
elif args.subtraction:
    print('The Subtraction Checker')
    tprint("-", font="slant")
elif args.addition:
    print('The Addition Checker')
    tprint("+", font="slant")
else:
    print("Error: please specify either --addition or --subtraction")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

num = input("1st Number: ")
num2 = input("2nd Number: ")
awn = input("Answer: ")

if args.addition:
    print(addcheck(num, num2, awn))
else:
    print(subcheck(num, num2, awn))
sleep(1)