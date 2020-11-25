import sys
import math

n = int(input())
m = int(input())
dict_voters = dict()
voters_vote = dict()
final_votes = {"Yes" : 0, "No" : 0}

for i in range(n):
    person_name, nb_vote = input().split()
    nb_vote = int(nb_vote)
    dict_voters[person_name] = nb_vote
    voters_vote[person_name] = []
    
for i in range(m):
    voter_name, vote_value = input().split()
    
    if voter_name in dict_voters.keys():
        voters_vote[voter_name].append(vote_value)
        
for voter, votes_value in voters_vote.items():
    if len(votes_value) <= dict_voters[voter]:
        for vote in votes_value:
            if vote in ["Yes", "No"]:
                final_votes[vote] += 1

print(final_votes["Yes"], final_votes["No"])