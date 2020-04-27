#Capture test scores
TestScore1 = int(input('Enter first test score: ' ))
TestScore2 = int(input('Enter second test score: ' ))
TestScore3 = int(input('Enter third test score: ' ))

#Average test scores
TestAverage = (TestScore1 + TestScore2 + TestScore3) / 3

#High Score
HighScore = 90

#Determine if Average is above high score
if TestAverage >= HighScore:
    print('Congradulations')
    print('That\'s a great score')
else:
    print('You\'re continueing to improve')