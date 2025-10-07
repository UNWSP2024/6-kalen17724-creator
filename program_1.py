
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random 
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    dice_one = random.randint (1, 6)
    dice_two = random.randint (1, 6)
    # Sum 2 numbers
    total = dice_one + dice_two 
    print (sum)
    # return sum to calling function
    return total 
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main(): 
    total_sum = 0 
    for i in range(100):
        roll=randDice()
        total_sum += roll 
        print(f"ROll {i+1}:{roll}")
    average = total_sum / 100
    print(f"Average of 100 rolls: {average}")

main()
