# Introduction

How can we use coin flipping to see the flaw of GDP as a measure of a country's prosperity? 
This project was inspired by a [2011 presentation by physicist and Ergodicity Economics researcher Ole Peters at Goodenough College](https://www.youtube.com/watch?v=LGqOH3sYmQA&feature=youtu.be). 
In the presentation, Peters shows that randomly flipped coins to generate wealth can lead to a state where both of the following are true: 1) Given enough flips, any individual's wealth is guaranteed to fall to zero and 2) the wealth of the cohort of coin flippers increases steadily over time.
How could those two things both be true? Well, that's exactly the question I had as well. So I decided to replicate the simulation.

# Experiment and Results

The experiment goes like this: You start with $100 of wealth and flip a fair coin. If it lands heads, your wealth increases by 50%.
If tails, your wealth decreases by 40%. Just based on those numbers alone it would appear to be a favorable game. 
After one flip, you'll either have $150 or $60 with equal likelihood, for an expected value of $105. 
Similarly after two flips, you now stand to have either $225 with probability 1/4, $90 with probability 1/2, or $36 with probability 1/4, for an expected value of $110.25, which represents a 5% gain over your expected wealth from the previous round. So it does appear to be a wealth generating game. 
But now let's see what happens when we actually play, following the trajectory of one player flipping a coin once per minute for an hour: 
(I'll mostly mimic the sequence that Peters presents.)

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%2060%20flips.png' /></p>

We are not doing very well after an hour of flipping, though we did surpass $1,000 two separate times. 
Let's see what happens if we continue keep flipping for a week. 

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%20One%20week%20of%20flips.png' /></p>

Notice the y-axis needs to be converted to log scale. 
This is a continuation of the first hour of flipping, the portion of which is shown on the graph in green. Clearly, we are doing much worse now.
Let's see what happens after flipping for 3 months, continuing at the rate of one coinflip per minute:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%20Three%20months%20of%20flips.png' /></p>

Again, the first week of flips shown in green. I'm not sure how much closer to zero we could get. Now let's take a look at the total cohort of coin flippers that are doing the exact same thing. 
Since the flipping experiment went so poorly for us individually we might expect that it would be the same for the cohort. 
Again, here is our progress after flipping for one hour:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%2060%20flips.png' /></p>

Here are the trajectories of twenty other people who also threw a coin for an hour:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/20%20trajectories%20-%2060%20flips.png' /></p>

Not very easy to tell what's happening except that the experiment doesn't look to have gone too well for most of the 20, as most of the lines are near zero towards the end of the flipping. 
So let's look at a cohort of 1,000 people doing the same thing. We'll also average over the cohort, which will leave us with a single trajectory.

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/1000%20trajectories%20-%2060%20flips.png' /></p>

They are doing well! The wealth of the average of 1000 coin flippers looks to have shot up to over $2000 from the starting point of $100. But there is still a lot of noise. So let's see what a cohort of 100,000 people would look like:<sup>1</sup>

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/100%2C000%20trajectories%20-%2060%20flips.png' /></p>

Wow. Solid, stable growth with minimal noise. How could that be when we would expect each individual to lose money over time? Let's take a closer look at those 100,000 trajectories.<sup>2</sup>

Here is the distribution of the 100,000 trajectories, looking at the ending wealth amounts only since we don't really care what happens before 60 flips are completed:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/Histogram%20100%2C000%20trajectories%20-%2060%20flips.png' /></p>

Again, the axes are on a log scale or else the highest bar would completely dominate the rest. 
From here we can see immediately that people who ended with $0 (or close to $0) total almost the entire cohort of 100,000 people.
Because of the log scale it's difficult to see how much shorter than 100,000 the largest bar is.  

Examining the cohort directly reveals that, of the 100,000 people in the cohort:

* 81,767 ended with less than $100 - meaning they lost money overall.
* Of these, 55,161 ended with less than $10.
* And a whopping 34,923 ended with less than $1, many of them with zero (or close to).

Of course, we also want to look at the flippers that ended up making money:

* 5,907 people ended with more than $100 but less than $200.
* 4,560 ended up with more than $200 but less than $1,000.
* 6,245 people ended up with between $1,000 and $10,000.

That leaves about 1,581 people, or 1.6% of the overall cohort who ended up making over $10K. Now let's look at the distribution of just those folks.

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/Histogram%20100%2C000%20trajectories%2C%20ended%20with%20more%20than%20%2410%2C000%20-%2060%20flips.png' /></p>

It actually doesn't look too different than the previous histogram, and it tells us that the vast majority of the people that made over $10K are making not much more than that.
To round out the biggest winners of the experiment, the top twenty made between $1.5 million and $10 million, with the winner
of the game winning $9.9 million.

In terms of the total wealth of the cohort:

* The wealthiest person holds 5.9%
* The top 10 wealthiest people hold 23%
* And the top 100 wealthiest - representing 0.1% of people - hold 55% of the entire wealth of the cohort.

# Discussion

So what do the different ways we have to gauge the performance of this cohort tell us about the prosperity of the people after flipping coins for an hour? 
One of the most popular metrics is what we've already done, just taking a simple average. 
This is also how GDP is computed - as a simple average of everyone's income.
Looking at it this way, we can see that the average coin-flipper went from holding $100 at the start to $1,675 at the end. 
Using logarithmic growth rates, this represents 282% growth over the 1 hour of coin flipping. Our imaginary city people seem to be prosperous, fat, and happy.

However, using an alternative metric such as the Democratic Domestic Product, or DDP, we see a different picture. DDP is defined as:<sup>3</sup>

<p align="center"><img src="https://s0.wp.com/latex.php?latex=%5Ctext%7BDDP%7D%3D%5Cleft%28%5Cprod_i%5EN+x_i%5Cright%29%5E%7B1%2FN%7D&bg=ffffff&fg=000000&s=0&zoom=2" /></p>

Measuring the prosperity of the cohort this way, our group's starting DDP of $100 falls to just $4.2 after 60 flips. This is a 316% reduction in DDP. So not only is this result in the opposite direction of the previous result, the magnitude is larger.

How is this possible? As Peters notes, GDP gives equal weight to the dollar. More dollars in society means society is doing better, regardless of how those dollars are distributed before and after. DDP gives an equal weight to the person. Immediately it becomes clear why our peanut society tanked via the DDP but prospered with GDP, even though recall that the coin-flipping procedure mathematically increased the wealth of the average participant over time. This is because wealth in this context is not ergodic - the wealth gains measured when averaging over the ensemble do not reflect the gain in wealth to one person over time. In cases like these, measuring across ensembles versus across time can give very different results. 

I'm not making any statment about the prosperity of people today - all I've done is built a little toy and applied different metrics to it.
But, if our society were to ever turn into one resembling the toy city, with over 80% of people getting poorer over time, it's entirely possible that GDP wouldn't alert us to a decay of the majority. 

As a reward for getting to the end - the reason for the discrepancy in metrics when applied to the peanut city is because the logarithmic returns of the game are unfavorable to begin with. |log(0.6)| > |log(1.5)| 

Tweaking the payoffs to something like 1.6 and 0.7 would result in a different set of peanuts! Thank you for reading my piece. 

# Notes

1) Peters's final cohort consisted of a million people, but 100K gets the point across and makes the computations a bit more time friendly for my little old machine.

2) A little coding trick was employed to conserve memory, since for the 100,000 cohort I only care about each flipper's final wealth along with the average trajectory, and I certainly don't want to keep a data frame with 100,000 columns in working memory. Instead, I update the average trajectory iteratively as each flipper flips, weighting by 1/100,000, and I keep track of each final wealth value and store it separately.

3) See the second reference.

# References

1) https://www.youtube.com/watch?v=LGqOH3sYmQA&feature=youtu.be
2) https://ergodicityeconomics.com/2020/02/26/democratic-domestic-product/
