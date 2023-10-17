# break will step out of the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')

print()
# continue will just skip the current iteration but continue the loop
for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')