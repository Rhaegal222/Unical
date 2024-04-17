import random

n = 1200
matrice = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
  for j in range(n):
    matrice[i][j] = random.randint(0, 1)

with open("input.txt", "w") as f:
  for i in range(n):
    f.write("".join(str(x) for x in matrice[i]))
    f.write("\n")
