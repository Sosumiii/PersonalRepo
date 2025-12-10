scoreFile = open("test_scores.csv", "r")
lines = scoreFile.readlines()
scoreFile.close()

for line in lines:
    tokens = line.split(",")
    total = 0

    for token in tokens:
        total += float(token)

    print(f"The total for this row of scores is {total}")
    print(f"The average score for this row is {total/len(tokens)}\n")