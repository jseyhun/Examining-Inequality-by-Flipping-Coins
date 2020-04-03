#Load data
import pandas
import numpy
import math

#https://ergodicityeconomics.com/2020/02/26/democratic-domestic-product/

one_trajectory = pandas.read_csv('data/One trajectory, 3 months of flips.csv', index_col=False, header=None)
one_trajectory = pandas.Series(one_trajectory[one_trajectory.columns[0]])

thousand_trajectories = pandas.read_csv('data/1000 trajectories, 60 flips, average.csv', index_col=False, header=None)
thousand_trajectories = pandas.Series(thousand_trajectories[thousand_trajectories.columns[0]])

all_trajects_average = pandas.read_csv('data/100k trajectories, 60 flips, average.csv', index_col=False, header=None)
all_trajects_average = pandas.Series(all_trajects_average[all_trajects_average.columns[0]])

all_trajects_end_vals = pandas.read_csv('data/100k trajectories, 60 flips, all end values.csv', index_col=False, header=None)
all_trajects_end_vals = pandas.Series(all_trajects_end_vals[all_trajects_end_vals.columns[0]])

#calculate GDP growth using logarithmic growth rates from Peters

def calculate_gdp(data):
    n = len(data)
    return sum(data)/n


def calculate_ddp(data):
    n = len(data)
    log_ddp = (1/n)*sum([math.log(x) for x in data])
    return math.exp(log_ddp)


gdp_g = math.log(calculate_gdp(all_trajects_end_vals) / 100)
#282% gdp growth in 1 hour

math.log(calculate_gdp(all_trajects_end_vals.nsmallest(99999)) / 100)
#276% gdp growth if excluding the richest person

math.log(calculate_gdp(all_trajects_end_vals.nsmallest(99990)) / 100)
#256% growth excluding the richest 10

math.log(calculate_gdp(all_trajects_end_vals.nsmallest(99900)) / 100)
#206% growth if excluding the richest 100

calculate_ddp(all_trajects_end_vals)

ddp_g = math.log(calculate_ddp(all_trajects_end_vals)) - math.log(100)
#-316% growth. so a higher magnitude and in the opposite direction as the previous metric. society has decayed.