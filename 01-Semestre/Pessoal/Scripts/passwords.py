import string
import random
print('Password: ', ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range (8)))
