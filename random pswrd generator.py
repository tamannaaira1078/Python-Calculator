letters = ["a", "b", "c", "d", "e", "f"]
numbers = ["1", "2", "3", "4", "5", "6"]
symbols = ["!", "@", "#", "$"]

import random
letter = random.choices(letters, k=3)
number = random.choices(numbers, k=2)
symbol = random.choice(symbols)
combine = letter + number + [symbol]
password = ''.join(combine)
print(f"{'Random Password'}:{password}")