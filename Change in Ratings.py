#import math
YourRating = int(input("Enter your rating "))
OpponentRating = int(input("Enter your opponent's rating "))
Score = float(input("Enter your score "))
KFactor = int(input("Enter your K Factor "))
diff = OpponentRating-YourRating
k1 = (-1/400)*diff
ProbabilityFunction1 = 1/(1+(10**k1))
ProbabilityFunction0 = 1-ProbabilityFunction1
ProbabilityFunctionHalf = (ProbabilityFunction1-ProbabilityFunction0)/2
ChangeinRating1 = format(KFactor*ProbabilityFunction1, '.1f')
ChangeinRating0 = format(KFactor*ProbabilityFunction0, '.1f')
ChangeinRatinghalf = format(KFactor*ProbabilityFunctionHalf, '.1f')
if Score == 0:
        ChangeinRating0 = -float(ChangeinRating0)
        if float(ChangeinRating0)<-0.92*KFactor:
                print(format(-0.92*KFactor, '.1f'))
        else:
                print(ChangeinRating0)
if Score == 1:
        if float(ChangeinRating1)>0.92*KFactor:
                print(format(0.92*KFactor, '.1f'))
        else:
                print(ChangeinRating1)
if Score == 0.5:
        if diff<0:
                if float(ChangeinRatinghalf)<(0.42*KFactor*-1):
                        print(-0.42*KFactor)
                else:
                        print(ChangeinRatinghalf)
        elif diff>0:
                if float(ChangeinRatinghalf)>(0.42*KFactor):
                        print(0.42*KFactor)
                else:
                        print(ChangeinRatinghalf)
        else:
                print(ChangeinRatinghalf)