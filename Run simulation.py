# https://www.youtube.com/watch?v=LGqOH3sYmQA&t=355s
# heads in 50%, tails lose 40%
# first takes average of 20 trajectories, one toss a minute for 6 mins, then thousand trajectories, then million. shows upward trend
# then one trajectory, playing for 24 hours, then one week, still negative trend, fewer fluctuations, then 1 year. no fluctuations
# question: who is dominating the ensemble picture? look further

import pandas
import numpy
import random
import statistics
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

random.seed(1)
def flip_coin():
    toss = numpy.random.binomial(1,0.5)
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

first_trajectory = make_trajectory(60)


# fig, ax = plt.subplots()
# first_trajectory.plot()
# ax.set_xlabel("Number of flips")
# ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
# ax.set_title("One trajectory - 60 flips")
# fig.savefig('images/One trajectory - 60 flips.png')
#
# #now show 20 trajectories on same plat
#
# fig, ax = plt.subplots()
# first_trajectory.plot()
# for i in range(20):
#     make_trajectory(60).plot()
# ax.set_xlabel("Number of flips")
# ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
# ax.set_title("20 trajectories - 60 flips")
# fig.savefig('images/20 trajectories - 60 flips.png')
#
# #now show one trajectory for 24 hours, and one week
#
# fig, ax = plt.subplots()
# make_trajectory(60*24).plot()
# ax.set_yscale("log")
# ax.set_xlabel("Number of flips")
# ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:}'))
# ax.set_title("One trajectory - One week of flips")
# fig.savefig('images/One trajectory - One week of flips.png')
#
# #now one trajectory for 3 months (instead of a year) of flips
#
# fig, ax = plt.subplots()
# make_trajectory(60*24*90).plot()
# ax.set_yscale("log")
# ax.set_xlabel("Number of flips")
# ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:}'))
# ax.set_title("One trajectory - Three months of flips")
# fig.savefig('images/One trajectory - Three months of flips.png')
#



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

# #get the plot
# fig, ax = plt.subplots()
# thousand_trajectories = average_trajectories(20, 60)
# thousand_trajectories['average_trajectory'].plot()
# ax.set_xlabel("Number of flips")
# ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
# ax.set_title("1000 trajectories - 60 flips")
# fig.savefig('images/1000 trajectories - 60 flips.png')
#
# ##For a million trajectories, modify the code to just get the final amount, then look at the million final numbers.
# #note when y axis becomes log
#
# thousand_trajectories['average_trajectory'].to_csv('sims/100k trajectories, 60 flips, average.csv')
# thousand_trajectories['end_values'].to_csv('sims/100k trajectories, 60 flips, all end values.csv')

fig, ax = plt.subplots()
thousand_trajectories = average_trajectories(100000, 60)
thousand_trajectories['average_trajectory'].plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("100,000 trajectories - 60 flips")
fig.savefig('images/100,000 trajectories - 60 flips.png')


fig, ax = plt.subplots()
thousand_trajectories['end_values'].hist(grid=False, bins=50)
ax.set_yscale("log")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('{x:,.0f}'))
ax.xaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_xlabel("Dollars won")
ax.set_ylabel("Number of players")
ax.set_title("Histogram of 100,000 trajectories,  60 flips each")
fig.savefig('images/Histogram 100,000 trajectories - 60 flips.png')

#histogram for people that ended with more than $10,000
fig, ax = plt.subplots()
thousand_trajectories['end_values'][thousand_trajectories['end_values'] > 10000].hist(color="maroon",grid=False, bins=50)
ax.set_yscale("log")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('{x:,.0f}'))
ax.xaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_xlabel("Dollars won")
ax.set_ylabel("Number of players")
ax.set_title("Histogram of 100,000 trajectories, ended with more than $10,000,  60 flips each")
fig.savefig('images/Histogram 100,000 trajectories, ended with more than $10,000 - 60 flips.png')
sum(thousand_trajectories['end_values'] < 1)
#34,923 players have less than $1!

sum(thousand_trajectories['end_values'] < 10)
#55,161 less than $10

sum(thousand_trajectories['end_values'] < 100)
#81,767 people lose money

sum(thousand_trajectories['end_values'].between(100, 200))
#5,907 of the people that made money made less than $100

sum(thousand_trajectories['end_values'].between(200, 1000))
#4500 people made between 200 and 1000


thousand_trajectories['end_values'][thousand_trajectories['end_values'] > 10000]

thousand_trajectories['end_values'].nlargest(20)
#one person got almost 10 million, a few got 4 million, and a handful ended as millionares overall

max(thousand_trajectories['end_values'])/sum(thousand_trajectories['end_values'])
#richest person holds 5.9% of the wealth

sum(thousand_trajectories['end_values'].nlargest(10))/sum(thousand_trajectories['end_values'])
#richest 10 people hold 23% of wealth

sum(thousand_trajectories['end_values'].nlargest(100))/sum(thousand_trajectories['end_values'])
#richest hundred hold 55% of the wealth.

gdp_growth = (thousand_trajectories['average_trajectory'][60] - 100)/100
#gdp grew 1575% for the entire cohort. but how much of that is explained by the richest people?

gdp_growth_minus_richest = ((statistics.mean(thousand_trajectories['end_values'].nsmallest(99999)) - 100)/100)
#excluding richest man, gdp grew 1476% for the cohort.

(gdp_growth_minus_richest - gdp_growth)/gdp_growth
#meaning without the richest person, gdp growht would be 6% lower. but of course, all 99999 others would be unaffected

gdp_growth_minus_richest_10 = ((statistics.mean(thousand_trajectories['end_values'].nsmallest(99990)) - 100)/100)
(gdp_growth_minus_richest_10 - gdp_growth)/gdp_growth
#excluding the richest 10, gdp growth would be 24% lower. but of course, all 99990 others would be unaffected

gdp_growth_minus_richest_100 = ((statistics.mean(thousand_trajectories['end_values'].nsmallest(99900)) - 100)/100)
(gdp_growth_minus_richest_100 - gdp_growth)/gdp_growth
#excluding the richest 100, gdp growth would be 59% lower. but of course, all 99900 others would be unaffected

