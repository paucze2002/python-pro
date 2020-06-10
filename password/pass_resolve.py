# by Paulina Czempiel
count = 0
file = open(r"possible_pass", "w")

for num in range(372002, 809992):
    number = str(num)
    prev_num = 0
    dec_num = False
    group = []
    for x in range(0, 6):
        letter = number[x]
        digit = int(letter)
        if prev_num == digit:
            if digit not in group:
                group.append(digit)
        if prev_num > digit:
            dec_num = True
            break
        prev_num = digit
    if not dec_num and len(group) == 2:
        print(number)
        file.write(number)
        file.write("\n")
        count += 1
print("There are " + str(count) + " possible numbers.")
file.write("There are " + str(count) + " possible numbers.")
