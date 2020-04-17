import tqdm
import random
with open('passport_newgroup.txt', 'r') as f:
	data = f.read()

lines = data.splitlines()
for line in tqdm.tqdm(lines):
	if len(line) >20:
		idx = random.randint(10, 20)
		new_line = line[:idx]
		with open('new_passport.txt', 'a') as f:
			f.write(new_line)
			f.write('\n')