import pandas
import numpy
import statistics
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

#load datasets. Save them as pandas series so they're easier to work with

one_trajectory = pandas.read_csv('data/One trajectory, 3 months of flips.csv', index_col=False, header=None)
one_trajectory = pandas.Series(one_trajectory[one_trajectory.columns[0]])

thousand_trajectories = pandas.read_csv('data/1000 trajectories, 60 flips, average.csv', index_col=False, header=None)
thousand_trajectories = pandas.Series(thousand_trajectories[thousand_trajectories.columns[0]])

all_trajects_average = pandas.read_csv('data/100k trajectories, 60 flips, average.csv', index_col=False, header=None)
all_trajects_average = pandas.Series(all_trajects_average[all_trajects_average.columns[0]])

all_trajects_end_vals = pandas.read_csv('data/100k trajectories, 60 flips, all end values.csv', index_col=False, header=None)
all_trajects_end_vals = pandas.Series(all_trajects_end_vals[all_trajects_end_vals.columns[0]])

#do one hour of flips.

fig, ax = plt.subplots()
one_trajectory[0:61].plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("One trajectory - 60 flips")
fig.savefig('images/One trajectory - 60 flips.png')

#now show 20 trajectories on same plat

# fig, ax = plt.subplots()
# first_trajectory.plot()
# for i in range(20):
#     make_trajectory(60).plot()
# ax.set_xlabel("Number of flips")
# ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
# ax.set_title("20 trajectories - 60 flips")
# fig.savefig('images/20 trajectories - 60 flips.png')

#now show one trajectory for 24 hours, and one week. need masking first
masking = numpy.append(numpy.repeat(0, 61), numpy.repeat(1, len(one_trajectory) - 61))
masked_array = numpy.ma.array(one_trajectory, mask=masking)

fig, ax = plt.subplots()
one_trajectory[0:(60*24*7+1)].plot()
plt.plot(masked_array, color="lime", linewidth="2")
ax.set_yscale("log")
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:.2}'))
ax.set_title("One trajectory - One week of flips")
fig.savefig('images/One trajectory - One week of flips.png')


#get the plot
fig, ax = plt.subplots()
thousand_trajectories.plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("1000 trajectories - 60 flips")
fig.savefig('images/1000 trajectories - 60 flips.png')


# now one trajectory for 3 months (instead of a year) of flips. add mask
masking = numpy.append(numpy.repeat(0, (60*24*7 + 1)), numpy.repeat(1, len(one_trajectory) - (60*24*7 + 1)))
masked_array = numpy.ma.array(one_trajectory, mask=masking)

fig, ax = plt.subplots()
one_trajectory.plot()
plt.plot(masked_array, color="lime", linewidth="2")
ax.set_yscale("log")
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:}'))
ax.set_title("One trajectory - Three months of flips")
fig.savefig('images/One trajectory - Three months of flips.png')


# For a million trajectories, modify the code to just get the final amount, then look at the million final numbers.
# #note when y axis becomes log


fig, ax = plt.subplots()
all_trajects_average.plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("100,000 trajectories - 60 flips")
fig.savefig('images/100,000 trajectories - 60 flips.png')


fig, ax = plt.subplots()
(all_trajects_end_vals/1000000).hist(grid=False, bins=200)
ax.set_yscale("log")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('{x:,.0f}'))
ax.xaxis.set_major_locator(tick.MultipleLocator(1))
ax.xaxis.set_major_formatter(tick.IndexFormatter(['$0', '$1M', '$2M', '$3M', '$4M', '$5M', '$6M', '$7M', '$8M', '$9M', '$10M']))
ax.set_xlabel("Dollars won")
ax.set_ylabel("Number of players")
ax.set_title("Histogram of 100,000 trajectories,  60 flips each")
fig.savefig('images/Histogram 100,000 trajectories - 60 flips.png')

#histogram for people that ended with more than $10,000
fig, ax = plt.subplots()
(all_trajects_end_vals[all_trajects_end_vals > 10000]/1000000).hist(color="maroon",grid=False, bins=200)
ax.set_yscale("log")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('{x:,.0f}'))
ax.xaxis.set_major_locator(tick.MultipleLocator(1))
ax.xaxis.set_major_formatter(tick.IndexFormatter(['$0', '$1M', '$2M', '$3M', '$4M', '$5M', '$6M', '$7M', '$8M', '$9M', '$10M']))
ax.set_xlabel("Dollars won")
ax.set_ylabel("Number of players")
ax.set_title("Histogram of 100,000 trajectories, ended with more than $10,000\n60 flips each")
fig.savefig('images/Histogram 100,000 trajectories, ended with more than $10,000 - 60 flips.png')
sum(all_trajects_end_vals < 1)
#34,923 players have less than $1!

sum(all_trajects_end_vals < 10)
#55,161 less than $10

sum(all_trajects_end_vals < 100)
#81,767 people lose money

sum(all_trajects_end_vals.between(100, 200))
#5,907 of the people that made money made less than $100

sum(all_trajects_end_vals.between(200, 1000))
#4500 people made between 200 and 1000


all_trajects_end_vals[all_trajects_end_vals > 10000]

all_trajects_end_vals.nlargest(20)
#one person got almost 10 million, a few got 4 million, and a handful ended as millionares overall

max(all_trajects_end_vals)/sum(all_trajects_end_vals)
#richest person holds 5.9% of the wealth

sum(all_trajects_end_vals.nlargest(10))/sum(all_trajects_end_vals)
#richest 10 people hold 23% of wealth

sum(all_trajects_end_vals.nlargest(100))/sum(all_trajects_end_vals)
#richest hundred hold 55% of the wealth.

gdp_growth = (all_trajects_average[60] - 100)/100
#gdp grew 1575% for the entire cohort. but how much of that is explained by the richest people?

gdp_growth_minus_richest = ((statistics.mean(all_trajects_end_vals.nsmallest(99999)) - 100)/100)
#excluding richest man, gdp grew 1476% for the cohort.

(gdp_growth_minus_richest - gdp_growth)/gdp_growth
#meaning without the richest person, gdp growht would be 6% lower. but of course, all 99999 others would be unaffected

gdp_growth_minus_richest_10 = ((statistics.mean(all_trajects_end_vals.nsmallest(99990)) - 100)/100)
(gdp_growth_minus_richest_10 - gdp_growth)/gdp_growth
#excluding the richest 10, gdp growth would be 24% lower. but of course, all 99990 others would be unaffected

gdp_growth_minus_richest_100 = ((statistics.mean(all_trajects_end_vals.nsmallest(99900)) - 100)/100)
(gdp_growth_minus_richest_100 - gdp_growth)/gdp_growth
#excluding the richest 100, gdp growth would be 59% lower. but of course, all 99900 others would be unaffected
