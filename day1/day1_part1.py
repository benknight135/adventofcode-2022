'''
Find the Elf carrying the most Calories.
How many total Calories is that Elf carrying?
'''

# Read the input data
input_filename = "day1_input.txt"
with open(input_filename) as input_file:
    input_data = input_file.readlines()

# Find the total calories of the elf carrying the most calories
elf_cal_total = 0
largest_cal = 0
for line in input_data:
    if "\n" == line:  # new line means data group is finished
        if elf_cal_total >= largest_cal:
            largest_cal = elf_cal_total
        elf_cal_total = 0
        continue
    elf_cal_total += int(line)

print(largest_cal)
