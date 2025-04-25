
#Prompt user to enter number of candidates
candidate_size = int(input("Enter number of candidates: "))

#dclare arrays and hashes to store voters choice and ranks as candidates from most to least favorite
ranks = []
array = []

pairs = {}
pair = {}

#array to store all candidates
candidates = []

#Make each user enters the candidates 
for i in range(candidate_size):
    candidate = input(f"Enter candidate ({i+1} of {candidate_size}): ")
    candidates.append(candidate)

x = candidates
#Print all candidates names 
print(f"{x}")

#ask user number of voters and how each one of them voted
voter_size = int(input("Enter number of voters: "))
print("Rank these candidates in your desired order: ")
for i in range(voter_size):
    print("\n")
    for j in range(candidate_size):
        ans = input(f"{j+1}: ")
        array.push(ans)

#Rest below is to be reviewed soon

name = input("Enter name: ")
for i in range(len(candidates)):
    if name == candidates[i]:
        # ranks[rank] = i
        print("yes")


for i in range(len(candidates)):
    for j in range(i+1,len(candidates),1):
        preferences[ranks[i]][ranks[j]] += 1


for i in range(len(candidates)):
    for j in range(len(candidates)):
        if preferences[i][j] > preferences[j][i]:
            count+=1
            pair["winner"] = i
            pair["loser"] = j

for i in range(count):
    for j in range(i+1,len(candidates),1):
        preferences[ranks[i]][ranks[j]] += 1
# for i in range(len(candidates)):
#     for j in range(i+1,len(candidates),1):
#         if preferences[i][j] > preferences[j][i]:
#             count+=1
