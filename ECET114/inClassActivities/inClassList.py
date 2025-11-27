#Elvis Nguyen
#In Class List

scores = [0]*6
total = 0

for i in range(len(scores)):
    scores[i] = float(input("Enter the score: "))

print(scores)

for i in range(len(scores)):
    total += scores[i]

print(f"Total: {total}")

high = max(scores)
low = min(scores)

print(f"avg: {total/len(scores):.2f}, min: {low}, max: {high}")