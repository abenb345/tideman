
candidate_size = int(input("Enter number of candidates: "))

candidates = []
for i in range(candidate_size):
    candidate = input(f"Enter candidate ({i+1} of {size}): ")
    candidates.append(candidate)

# x = candidates
# print(f"{x}")
voter_size = int(input("Enter number of voters: "))
rank = input("Rank these candidates in your desired order: ")
for i in range(voter_size):
    for j in range(candidate_size):
        ans = input(f"{j+1}: ")
