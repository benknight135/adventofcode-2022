'''
Find the top three Elves carrying the most Calories.
How many Calories are those Elves carrying in total?
'''

# Read the input data
input_filename = "day1_input.txt"
with open(input_filename) as input_file:
    input_data = input_file.readlines()

# Find the calorie totals
elf_cal_total = 0
elf_totals = []
for line in input_data:
    if "\n" == line:
        elf_totals.append(elf_cal_total)
        elf_cal_total = 0
        continue
    elf_cal_total += int(line)

# Find the top 3 calories and sum them
elf_totals.sort(reverse=True)
top_3_sum = sum(elf_totals[0:3])
print(top_3_sum)
