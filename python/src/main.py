import testmain as test
import random
for i in range(1, 100):
    arr = []
    for j in range(1000):
        arr.append(random.randint(0, i*1000)*random.randint(1, i*100))
    print(arr)
    test.main(arr)
    print("\n")
