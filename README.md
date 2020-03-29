# Introduction

How can we see the flaw of GDP as a measure of a country's prosperity by flipping coins? 
This project was inspired by a [2011 presentation by physicist Ole Peters at Goodenough College](https://www.youtube.com/watch?v=LGqOH3sYmQA&feature=youtu.be). 
In the presentation, Peters shows that randomly flipped coins to generate wealth can lead to a state where both of the following are true: 1) Given enough flips, any individual's wealth is guaranteed to fall to zero and 2) the wealth of the cohort of coin flippers increases steadily over time.
How could those two things both be true? Well, that's exactly the question I had as well. So I decided to replicate the simulation.

# Results

The experiment goes like this: You start with $100 of wealth and flip a fair coin. If it lands heads, your wealth increases by 50%.
If tails, you wealth descreases by 40%. Just based on those numbers alone it would appear to be a favorable game. 
After one flip, you'll either have $150 or $60 with equal likelihood, for an expected value of $105. 
Similarly after two flips, you now stand to have either $225 with probability 1/4, $90 with probability 1/2, or $36 with probability 1/4, for an expected value of $110.25, which represents a 5% gain over your expected wealth from the previous round. 
But now let's see what happens when we play the game, following the trajectory of one player flipping a coin once per minute for an hour: 
(I'll mostly mimic the sequence that Peters presents.)

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%2060%20flips.png' /></p>

We are not doing very well after an hour of flipping, though we did surpass $1,000 two separate times. 
Let's see what happens if we continue keep flipping for a week. 

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%20One%20week%20of%20flips.png' /></p>

Notice the y-axis needs to be converted to log scale. 
This is a continuation of the first hour of flipping, the portion of which is shown on the graph in green. Clearly, we are doing much worse now.
Let's see what happens after flipping for 3 months, continuing at the rate of one coinflip per minute:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%20Three%20months%20of%20flips.png' /></p>

Again, the first week of flips shown in green. I'm not sure how much closer to zero we could get. Now let's take a look at the the cohort of coin flippers that are doing the exact same thing. 
Since the flipping experiment went so poorly for us individually we might expect that it would be the same for the cohort. 
Again, here is our progress after flipping for one hour:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%2060%20flips.png' /></p>

Here are the trajectories of twenty other people who also threw a coin for an hour:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/20%20trajectories%20-%2060%20flips.png' /></p>

Not very easy to tell what's happening, so let's look at a cohort of 1,000 people doing the same thing:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/1000%20trajectories%20-%2060%20flips.png' /></p>

They are doing well! But there is still a lot of noise. So let's see what a cohort of 100,000 people would look like:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/100%2C000%20trajectories%20-%2060%20flips.png' /></p>

Wow. Solid, stable growth with minimal noise. How could that be when we would expect each individual to lose money over time? Let's take a closer look at those 100,000 trajectories.

# Discussion

Let's take a look at the distribution of the 100,000 trajectories, looking at the ending wealth amounts only since we don't really care what happens before 60 flips are completed:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/Histogram%20100%2C000%20trajectories%20-%2060%20flips.png' /></p>

Again, the axes are on a log scale or else the highest bar would completely dominate the rest. 
From here we can see immediately that people who ended with $0 (or close to $0) total almost the entire cohort of 100,000 people.
Because of the log scale it's difficult to see how much shorter than 100,000 the largest bar is. 
Examining the cohort directly reveals that, of the 100,000 people in the cohort:

* 81,767 ended with less than $100.
* Of these, 55,161 ended with less than $10.
* And a whopping 34,923 ended with less than $1, many of them with zero (or close to).

Of course, we also want to look at the flippers that ended up making money:

* 5,907 people ended with more than $100 but less than $200.
* 4,500 ended up with more than $200 but less than $1000.



