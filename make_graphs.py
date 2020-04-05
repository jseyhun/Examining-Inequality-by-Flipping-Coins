import pandas
import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from run_simulation import make_trajectory

# Load data sets. Save them as pandas series so they're easier to work with.

one_trajectory = pandas.read_csv('data/One trajectory, 3 months of flips.csv', index_col=False, header=None)
one_trajectory = pandas.Series(one_trajectory[one_trajectory.columns[0]])

thousand_trajectories = pandas.read_csv('data/1000 trajectories, 60 flips, average.csv', index_col=False, header=None)
thousand_trajectories = pandas.Series(thousand_trajectories[thousand_trajectories.columns[0]])

all_trajects_average = pandas.read_csv('data/100k trajectories, 60 flips, average.csv', index_col=False, header=None)
all_trajects_average = pandas.Series(all_trajects_average[all_trajects_average.columns[0]])

all_trajects_end_vals = pandas.read_csv('data/100k trajectories, 60 flips, all end values.csv', index_col=False, header=None)
all_trajects_end_vals = pandas.Series(all_trajects_end_vals[all_trajects_end_vals.columns[0]])

# One trajectory - one hours of flips.

fig, ax = plt.subplots()
one_trajectory[0:61].plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("One trajectory - 60 flips")
fig.savefig('images/One trajectory - 60 flips.png')

# 20 trajectories - one hours of flips. On the same plot.

fig, ax = plt.subplots()
for i in range(20):
    make_trajectory(60).plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("20 trajectories - 60 flips")
fig.savefig('images/20 trajectories - 60 flips.png')



# Now show one trajectory for one week of flips. First, create a masking which will allow the green portion of the plot.

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


# Now do 1000 trajectories of 60 flips.

fig, ax = plt.subplots()
thousand_trajectories.plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("1000 trajectories - 60 flips")
fig.savefig('images/1000 trajectories - 60 flips.png')


# One trajectory for 3 months (instead of a year which Peters does) of flips. Add masking.

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


# 100,000 trajectories flipping 60 times.

fig, ax = plt.subplots()
all_trajects_average.plot()
ax.set_xlabel("Number of flips")
ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}'))
ax.set_title("100,000 trajectories - 60 flips")
fig.savefig('images/100,000 trajectories - 60 flips.png')

# Now make histograms. First, make the histogram of the 100,000 trajectory end values, and then of only the people that made more than $10,000.

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


