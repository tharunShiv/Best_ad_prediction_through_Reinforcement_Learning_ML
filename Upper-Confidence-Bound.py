# Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# refer the algorithm
# Implementing UCB
import math
N = 10000 # number of rounds (row )
d = 10 # number of ads ( bandits )
ads_selected = []  # list of all the diff ads selected at each round 
# ^ it will be a vector consisting of N = 10000 number of lists, containing the ads selected at each round

numbers_of_selections = [0] * d
# numbers_of_selections is the number of times ad i was
# selected until n rounds 
sums_of_rewards = [0] * d 
# sum_of_rewards is the sums of rewards of each
# version of the ad i
total_reward = 0
for n in range(0, N):  # since we have to compute for every round
    ad = 0 # since it is diff at each round
    max_upper_bound = 0  # since it will be diff at each round
    for i in range(0, d): # for 10 ads
        if (numbers_of_selections[i] > 0): 
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            # log(n+1) because indexes start from 0 in python
            # because python considers the first round as 1
            # but here it is 0
            upper_bound = average_reward + delta_i
        else:
            # this is applied for the initial first 10 rounds
            # because we are not gonna apply any strategy for the first 10 rounds
            upper_bound = 1e400 # this is 10 power 400
            # why?
            # we will get n=0 for round 0
            # n=1 round=1
            # and so on for other rounds
        if upper_bound > max_upper_bound: # to find the max upperbound
            max_upper_bound = upper_bound
            ad = i
    # we are still at the round n
    # we are appending the ad selected in this round n        
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad] # we are
    # getting the value of whether the ad is clicked or not from the 
    # real dataset
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward 
    total_reward = total_reward + reward

# Visualising the results
# to plot how many times each ad was selected
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
