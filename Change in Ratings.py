YourRating = int(input("Enter your rating"))
OpponentRating = int(input("Enter your opponent's rating"))
Score = float(input("Enter your score"))
KFactor = int(input("Enter your K Factor"))
diff = OpponentRating-YourRating
k1 = (-0.00577)*diff
e = 2.712
ProbabilityFunction1 = 1/(1+(e**k1))
ProbabilityFunction0 = 1-ProbabilityFunction1
ProbabilityFunctionHalf = (ProbabilityFunction1-ProbabilityFunction0)/2
ChangeinRating1 = format(KFactor*ProbabilityFunction1, '.1f')
ChangeinRating0 = format(KFactor*ProbabilityFunction0, '.1f')
ChangeinRatinghalf = format(KFactor*ProbabilityFunctionHalf, '.1f')
if Score == 0:
        ChangeinRating0 = -float(ChangeinRating0)
        print(ChangeinRating0)
if Score == 1:
        print(ChangeinRating1)
if Score == 0.5:
    print(ChangeinRatinghalf)




