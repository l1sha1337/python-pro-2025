file = open("weather.txt", "r")
line = file.readline()
count = 0
while len(line) != 0:
    print(line.strip())
    if int(line) > 0:
        count = count + 1
    line = file.readline()

print(count, "дня с температурой больше ноля")

