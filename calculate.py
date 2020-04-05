import pandas
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

### Calculate various statistics. May not use all of them in the write-up.

sum(all_trajects_end_vals < 1)
# 34,923 players have less than $1!

sum(all_trajects_end_vals < 10)
# 55,161 ended with less than $10.

sum(all_trajects_end_vals < 100)
# 81,767 people lose money overall.

sum(all_trajects_end_vals.between(100, 200))
# 5,907 of the people that made money made less than $100.

sum(all_trajects_end_vals.between(200, 1000))
# 4,560 people made between 200 and 1000.

sum(all_trajects_end_vals.between(1000, 10000))
# 6,425 made between 1000 and 100000

all_trajects_end_vals.nlargest(20)
# One person got almost 10 million, a few got 4 million, and a handful ended as millionares overall.

max(all_trajects_end_vals)/sum(all_trajects_end_vals)
# Richest person holds 5.9% of the wealth.

sum(all_trajects_end_vals.nlargest(10))/sum(all_trajects_end_vals)
# Richest 10 people hold 23% of wealth.

sum(all_trajects_end_vals.nlargest(100))/sum(all_trajects_end_vals)
# Richest hundred hold 55% of the wealth.

gdp_growth = (all_trajects_average[60] - 100)/100
# Gdp grew 1575% for the entire cohort. but how much of that is explained by the richest people?

gdp_growth_minus_richest = ((statistics.mean(all_trajects_end_vals.nsmallest(99999)) - 100)/100)
# Excluding richest man, gdp grew 1476% for the cohort.

(gdp_growth_minus_richest - gdp_growth)/gdp_growth
# Meaning without the richest person, gdp growth would be 6% lower. but of course, all 99999 others would be unaffected.

gdp_growth_minus_richest_10 = ((statistics.mean(all_trajects_end_vals.nsmallest(99990)) - 100)/100)
(gdp_growth_minus_richest_10 - gdp_growth)/gdp_growth
# Excluding the richest 10, gdp growth would be 24% lower. but of course, all 99990 others would be unaffected.

gdp_growth_minus_richest_100 = ((statistics.mean(all_trajects_end_vals.nsmallest(99900)) - 100)/100)
(gdp_growth_minus_richest_100 - gdp_growth)/gdp_growth
# Excluding the richest 100, gdp growth would be 59% lower. but of course, all 99900 others would be unaffected.



### Calculate GDP growth using logarithmic growth rates from Peters.

# Get GDP and DDP calculation functions.

def calculate_gdp(data):
    n = len(data)
    return sum(data)/n


def calculate_ddp(data):
    n = len(data)
    log_ddp = (1/n)*sum([math.log(x) for x in data])
    return math.exp(log_ddp)


gdp_g = math.log(calculate_gdp(all_trajects_end_vals) / 100)
#282% GDP growth in 1 hour.

math.log(calculate_gdp(all_trajects_end_vals.nsmallest(99999)) / 100)
#276% GDP growth if excluding the richest person.

math.log(calculate_gdp(all_trajects_end_vals.nsmallest(99990)) / 100)
#256% growth excluding the richest 10.

math.log(calculate_gdp(all_trajects_end_vals.nsmallest(99900)) / 100)
#206% growth if excluding the richest 100.


ddp_g = math.log(calculate_ddp(all_trajects_end_vals)) - math.log(100)
#-316% growth. So a higher magnitude and in the opposite direction as the GDP metric. Society has decayed.