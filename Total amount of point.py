'''

Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4

'''



# using list comperhantions

def points(games):

    return sum(3 if x > y else 1 if x == y else 0 for x, y in (map(int, match.split(":")) for match in games))



def points(games):
    points_score = 0
    for match in games:
        x,y = map(int,match.split(":"))
        if x > y:
            points_score+=3
        if x == y:
            points_score+=1
        else: 
            points_score+=0
    return points_score            


print (points(["2:1", "2:3", "0:1"]))
