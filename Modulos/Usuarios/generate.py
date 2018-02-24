import string
import random

print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)))