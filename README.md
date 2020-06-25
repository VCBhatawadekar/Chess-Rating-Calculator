# Chess-Rating-Calculator

Elo ratings are used in many competitive games where player having higher rating is considered to have higher probablity of winning.
These ratings of players are updated time to time. This Elo rating is used to approximate strength of player.

A basic implementation of algorithms to calculate variation in Elo ratings is carried out in this project.
The algorithm is constructed on basic knowledge of probability. The probabilty of any probable result that is,
1. win 2.loss 3.draw can be calculated by ratings of the two players as follows,

Let,
  Rating of Player 1 = R1
  Rating of Player 1 = R2
  Probability of Player 1 winning = P(W)
  Probability of Player 1 losing  = P(L)
  Probability of Player 1 drawing = P(D)
  
Now,
  P(W) = 1/(1+(k1^k2(R2-R1)))
  P(L) = 1 - P(W) 
  P(D) = 0.5(P(W))-P(L))
  
The constant used in above formula k1,k2 were selected according such that k1 = Euler's Number. This can be further Simplified by taking k1 = 10 and k2 = 1/400.
There are infinite number of pairs of k1,k2 that satisfy the requirements. Once probabilities are calculated change in ratings is proportional to them.
Here, I have used Kfactor variable to simulate the K factor known as development factor. This can be thought of as a proportionality constant. 
After some analysis it was found that it has 
  limiting condition = 0.92Kfactor ( for decisive game )
  limiting condition = 0.42Kfactor ( for non-decisive game )
Note: One cannot have change in rating greater that limiting condition.  

  
