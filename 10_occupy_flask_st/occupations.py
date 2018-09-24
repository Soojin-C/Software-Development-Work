# Choidhury -- Soojin Choi and Raunak Chowdhury
# Softdev1 pd8
# K#06: StI/O: Divine your Destiny!
# 2018-09-13

from random import random

entries = open('./data/occupations.csv', 'r')
entries = entries.read()

entries = entries.split('\n')

# Delete the title and last column
title = entries.pop(0).split(',')
total = entries.pop(-2).split(',')
total_percentage = float(total[1]) #we need the total percentage for later


#split each entry into a list based on commas
for entry_index in range(len(entries)):
    if entries[entry_index] == '':
        entries.pop(entry_index)
    elif entries[entry_index].count(',') > 1:
        entries[entry_index] = entries[entry_index].split('",')
    else:
        entries[entry_index] = entries[entry_index].split(',')

#print(entries)

# build a dictionary
occupations = {}
for entry in entries:
    occupations[entry[0]] = float(entry[1])

#print(occupations)

def random_average():
    '''
    bar is the interval of the total that the weighted percentage holds for each occupation.
    randvalue is a random float value from the interval [0,99.8).


    Looping through the keys, you get the value attached to them, the percentage that get added to the bar. This is used to check the next interval that the percent is out of the total.
    If the randvalue falls in this interval, then the key (the occupation) gets returned.
    Otherwise, it continues looping until the correct interval is found. Since the randvalue is < 99.8, the interval will be found before the loop terminates.
    '''

    # generate random number
    bar = 0
    randvalue = random() * total_percentage #total_percentage is 99.8, not 100!
    keys = list(occupations.keys())
    #print(occupations.values())
    for key in keys:
        value = occupations[key]
        bar += value
        if (randvalue <= bar):
            #print(key, occupations[key])
            return key #This will always return because the randvalue is in the interval [0,99.8)

#print(entries)

if __name__ == '__main__':
    # Run 100 tests for good measure and see if it's the same
    num_times = 0
    for time in range(100):
        #print(type(random_average()))
        if random_average().count('Education, training and library') > 0:
            num_times+= 1
    #print(occupations[6.1])
    print('Number of times "Education, training and library" popped up: {}'.format(num_times))
    # The number of times hovers around 3-11 after numerous tests, which is very accurate for a 6.1% chance
