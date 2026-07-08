# Project1: Snake water gun
'''
snake = -1
water = 0
gun = 1
'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youDict = {"s": -1, "w": 0, "g": 1}
reverseDict = {-1: "Snake", 0: "Water", 1: "Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]} and computer choose {reverseDict[computer]}")


if you == computer:
    print("It's a tie")
elif (you == -1 and computer == 0) or (you == 0 and computer == 1) or (you == 1 and computer == -1):
    print("You win")            
else:    print("Computer wins")
