
import random

bingo = []

'''def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()'''

import random

def generate_random_numbers():
    return random.sample(range(1, 91), 8)

def check_and_replace_duplicates(numbers):
    while len(numbers) != len(set(numbers)):
        numbers = generate_random_numbers()
    return numbers

def create_bingo_grid():
    numbers = check_and_replace_duplicates(generate_random_numbers())
    numbers.sort()
    return [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BINGO", numbers[4]],
        [numbers[5], numbers[6], numbers[7]],
    ]

def pretty_print(bingo_grid):
    for row in bingo_grid:
        print(' '.join(f'{str(num):<3}' for num in row))

bingo_grid = create_bingo_grid()
pretty_print(bingo_grid)