f = open("scores.txt", "r")
lines = f.readlines()
f.close()

scores = []
for line in lines:
    scores.append(int(line))

print("Games played:", len(scores))
print("Best:", min(scores))
print("Average:", sum(scores) / len(scores))