import random


class testGenerator:
    def __init__(self) -> None:
        self.generatedTest = []

    def small_number_test_generator(self, i):
        for j in range(i):
            self.generatedTest.append(random.randint(0, i * 10) * random.randint(1, i * 10))

    def get_test(self):
        return self.generatedTest

    def negative_number_test_generator(self, i):
        for j in range(i):
            self.generatedTest.append(
                random.randint(0, i * 10) * random.randint(1, i * 10) * (random.randint(0, 1) * 2 - 1))

    def large_number_test_generator(self, i):
        for j in range(i):
            self.generatedTest.append(random.randint(0, i * 1000) * random.randint(1, i * 100))

    def large_number_and_negative_number_test_generator(self, i):
        for j in range(i):
            self.generatedTest.append(
                random.randint(0, i * 1000) * random.randint(1, i * 100) * (random.randint(0, 1) * 2 - 1))

    def sorted_number_test_generator(self, i):
        for j in range(i):
            self.generatedTest.append(j)

    def reversed_number_test_generator(self, i):
        for j in range(i):
            self.generatedTest.append(i - j)

    def duplicated_number_test_generator(self, i):
        random_number = random.randint(1, i )
        for j in range(random_number):
            self.generatedTest.append(j)
        for j in range(random_number, i):
            self.generatedTest.append(random.randint(0, i * 10))

    def duplicated_negative_number_test_generator(self, i):
        random_number = random.randint(1, i )
        for j in range(random_number):
            self.generatedTest.append(j)
        for j in range(random_number, i):
            self.generatedTest.append(random.randint(0, i * 10) * (random.randint(0, 1) * 2 - 1))
