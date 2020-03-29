# Introduction

How can we see the flaw of GDP as a measure of a country's prosperity by flipping coins? 
This project was inspired by a [2011 presentation by physicist Ole Peters at Goodenough College](https://www.youtube.com/watch?v=LGqOH3sYmQA&feature=youtu.be). 
In the presentation, Peters shows that randomly flipped coins to generate wealth can lead to a state where both of the following are true: 1) Given enough flips, any individual's wealth is guaranteed to fall to zero and 2) the wealth of the cohort of coin flippers increases steadily over time.
How could those two things both be true? Well, that's exactly the question I had as well. So I decided to replicate the simulation.

# Results

The experiment goes like this: You start with $100 and flip a fair coin. If it lands heads, your wealth increases by 50%.
If tails, you wealth descreases by 40%. Just based on those numbers alone it would appear to be a favorable game. 
After one flip, you'll either have $150 or $60 with equal likelihood, for an expected value of $105. 
Similarly after two flips, you now stand to have either $225 with probability 1/4, $90 with probability 1/2, or $36 with probability 1/4, for an expected value of $110.25, which represents a 5% gain over your expected wealth from the previous round. 
But now let's see what happens when we play the game, following the trajectory of one player flipping a coin once per minute for an hour: 
(I'll mostly mimic the sequence that Peters presents.)

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%2060%20flips.png' /></p>

We are not doing very well after an hour of flipping, though we did surpass $1,000 two separate times. 
Let's see what happens if we continue keep flipping for a week. 

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%20One%20week%20of%20flips.png' /></p>

This is a continuation of the first hour of flipping, the portion of which is shown on the graph in green. Clearly, doing worse now.
Let's see what happens after flipping for 3 months, continuing at the rate of one coinflip per minute:

<p align="center"><img src='https://github.com/jseyhun/Examining-Inequality-by-Flipping-Coins/blob/master/images/One%20trajectory%20-%20Three%20months%20of%20flips.png' /></p>

I'm not sure how much closer to zero we could get. Now let's take a look at the the cohort of coin flippers
