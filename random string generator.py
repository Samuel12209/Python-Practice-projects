import random
import string

abc = list(string.ascii_lowercase)
abc = "".join(abc)

string = ""

for i in range(50):
    letter = (random.choice(abc))
    string += letter

print(string)
print("Done")