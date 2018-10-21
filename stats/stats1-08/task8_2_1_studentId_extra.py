#!/usr/bin/env python3

"""
Question:  the probability of rolling a double six  within twenty-four rolls of 
    a pair of dice?

1. The probability of rolling a six with both dice is 1/36 on the first roll.

2. The probability of not rolling a double six on the first roll is
    1- (1/36) = 35/36
    
Therefore, the probability of not rolling a double six 24 consecutive times
   is (35/36)^24 ~ 0.51; then, the probability of rolling a double six is 
   1 - (35/36)^24, about 0.49.

Submit your simulation result

"""
# %% Modules and Libraries
import random

# %% author
__author__ = "Kousuke Tsuchiya"
__studentId__ = "s1f101700158"

# %%
def check_rolling_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == dice2 and dice1 == 6 and dice2 == 6:
        return True
    return False
def checkPascal(numTrials): 
    count = 0
    for i in range(numTrials):
        for j in range(24):
            if check_rolling_dice():
                count += 1
                break
    return count / numTrials 

numTrials = 10000
prob = checkPascal(numTrials)
print('{} Trials, Probability of winning ={}'.format(numTrials, prob))
