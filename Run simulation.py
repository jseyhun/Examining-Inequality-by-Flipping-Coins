# https://www.youtube.com/watch?v=LGqOH3sYmQA&t=355s
# heads in 50%, tails lose 40%
# first takes average of 20 trajectories, one toss a minute for 6 mins, then thousand trajectories, then million. shows upward trend
# then one trajectory, playing for 24 hours, then one week, still negative trend, fewer fluctuations, then 1 year. no fluctuations
# question: who is dominating the ensemble picture? look further

import pandas
import numpy
import random

random.seed(1)
def flip_coin():
    toss = numpy.random.binomial(1, 0.5)
    if toss == 1:
        return 1.5
    if toss == 0:
        return 0.6

def make_trajectory(n_flips):
    t = pandas.Series([], dtype="float64")
    t[0] = 100.0
    for i in range(1, n_flips + 1):
        t[i] = t[i-1]*flip_coin()
    return t

one_trajectory = make_trajectory(60*24*90)
one_trajectory.to_csv('data/One trajectory, 3 months of flips.csv', index=False, header=False)

#now average 1000 trajectories
#I am not going to store a dataframe of 1000 (or however many trajectories). Will just do it one at a time

def average_trajectories(n_trajectories, num_flips):

#initialize first trajectory. call it p to stand for previous trajectory.

    p = make_trajectory(num_flips)


#initialize series which will hold the end value of each trajectory

    end_values = pandas.Series([], dtype="float64")
    end_values[0] = p[num_flips]

    p[1:(num_flips + 2)] = p[1:(num_flips + 2)] / n_trajectories #because the p series is just 1 part of the series which will averaged

#now as I make subsequent trajectories, I want to add the results of each flip (weighted by 1/1000) to the corresponding
#flip of the previous trajectory. After 1000 trajectories, this will have been mathematically equivalent to ripping 1000 trajectories in a
#data frame and averaging. Except this will use much less memory since we'll only need 2 trajectories in storage at a time.

    def make_traj_and_average_to_previous(n_flips, prev_trajectory, num_trajectories):
        t = pandas.Series([], dtype="float64")
        t[0] = 100.0
        for i in range(1, n_flips + 1):
            t[i] = t[i - 1] * flip_coin()
            prev_trajectory[i] = prev_trajectory[i] + (t[i] / num_trajectories)
        return {'prev_trajectory': prev_trajectory, 'end_value': t[i]}

#now I have the first of my thousand trajectories, and a function that will make a new trajectory and average it with the first trajectory.
#so just repeat 1000 times

    for i in range(1, n_trajectories):
        if i % 100 == 0:
            print(i)
        q = make_traj_and_average_to_previous(num_flips, p, n_trajectories)
        end_values[i] = q['end_value']
        p = q['prev_trajectory']

    return {'average_trajectory': p, 'end_values': end_values}

thousand_trajectories = average_trajectories(1000, 60)
thousand_trajectories['average_trajectory'].to_csv('data/1000 trajectories, 60 flips, average.csv', index=False)

all_trajectories = average_trajectories(100000, 60)
all_trajectories['average_trajectory'].to_csv('data/100k trajectories, 60 flips, average.csv', index=False)
all_trajectories['end_values'].to_csv('data/100k trajectories, 60 flips, all end values.csv', index=False)
