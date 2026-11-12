scores = [55, 72, 89, 90, 65, 78, 95, 60]
score = int(input("Enter your score: "))
count = 0
for i in range(len(scores)):
    if scores[i] == score:
        print("its index")
        break
    else:
        count += 1
        print("Score not found")
print(count)