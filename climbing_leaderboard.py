'''
Alice is playing an arcade game and wants to climb to the top of the leaderboard. Can you help her track her ranking as she beats each level? The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
For example, four players have the scores , , , and . Those players will have ranks , , , and , respectively.

When Alice starts playing, there are already  people on the leaderboard. The score of each player  is denoted by . Alice plays for  levels, and we denote her total score after passing each level  as . After completing each level, Alice wants to know her current rank.

You are given an array, , of decreasing leaderboard scores, and another array, , of Alice's cumulative scores for each level of the game. You must print  integers. The  integer should indicate the current rank of alice after passing the  level.

Input Format

The first line contains an integer, , denoting the number of players already on the leaderboard.
The next line contains  space-separated integers describing the respective values of .
The next line contains an integer, , denoting the number of levels Alice beats.
The last line contains  space-separated integers describing the respective values of .

Constraints

 for
 for
The existing leaderboard, , is in descending order.
Alice's scores are cumulative, so  is in ascending order.
Subtask

For  of the maximum score:

Output Format

Print  integers. The  integer should indicate the rank of alice after passing the  level.

Sample Input 0

7
100 100 50 40 40 20 10
4
5 25 50 120
Sample Output 0

6
4
2
1
Explanation 0

Alice starts playing with  players already on the leaderboard, which looks like this:

image

After Alice finishes level , her score is  and her ranking is :

image

After Alice finishes level , her score is  and her ranking is :

image

After Alice finishes level , her score is  and her ranking is tied with Caroline at :

image

After Alice finishes level , her score is  and her ranking is :

image
'''
# Keep previous score
# Keep current ranking from previous score
# Update ranking when score doesn't match by 1
# Stop loop when alice score greater than or equal to value
def binary_search(scores,aliceScore,low,high,rankings):
    middle = (high-low)/2 + low
    if aliceScore == scores[middle] or middle==low:
        return middle
    elif aliceScore > scores[middle]:
        return binary_search(scores, aliceScore, low, middle, rankings)
    elif aliceScore < scores[middle]:
        return binary_search(scores, aliceScore, middle, high, rankings)
n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))

# Precalculate rankings
rankings = []
currentRanking = 1
prevScore = scores[0]
for i in range(0,n):
    currentScore = scores[i]
    if prevScore > currentScore:
        currentRanking += 1
    prevScore = currentScore
    rankings.append(currentRanking)
for i in range(0,m):
    aliceScore = alice[i]
    index = binary_search(scores, aliceScore, 0, n, rankings)
    if aliceScore >= scores[index]:
        print rankings[index]
    else:
        print rankings[index]+1

