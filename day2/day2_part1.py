'''
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A),
and you should choose Paper (Y).
This ends in a win for you with a score of 8 (2 because
you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B),
and you should choose Rock (X).
This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors,
giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide,
you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything
goes exactly according to your strategy guide?
'''

# Read the input data
input_filename = "day2_input.txt"
with open(input_filename) as input_file:
    input_data = input_file.readlines()
