import random
with open('numbers.txt','w') as f:
    f.writelines('{}\n'.format(random.randint(-1000000,1000000)) for _ in range(50000))

