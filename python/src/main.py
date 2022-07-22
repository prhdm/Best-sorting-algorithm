import src.test.testAlgorithm as test
from src.test import testGennerator


def main():
    test_with_sorted_numbers()
    test_with_reversed_numbers()
    test_with_duplicated_numbers()
    test_with_duplicated_negative_numbers()


def test_for_small_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.small_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("small_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("small_numbers")


def test_with_negative_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.negative_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("negative_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("negative_numbers")


def test_with_large_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.large_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("large_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("large_numbers")

def test_with_large_numbers_and_negative_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.large_number_and_negative_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("large_numbers_and_negative_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("large_numbers_and_negative_numbers")

def test_with_sorted_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.sorted_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("sorted_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("sorted_numbers")


def test_with_reversed_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.reversed_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("reversed_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("reversed_numbers")


def test_with_duplicated_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.duplicated_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("duplicated_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("duplicated_numbers")

def test_with_duplicated_negative_numbers():
    test_algorithm = test.Test()
    test_generator = testGennerator.testGenerator()
    for i in range(1, 100):
        test_generator.duplicated_negative_number_test_generator(i)
        arr = test_generator.get_test()
        test_algorithm.set_arr(arr)
        test_algorithm.test("duplicated_negative_numbers")
    print("Number of correct: " + str(test_algorithm.get_number_of_correct()))
    test_algorithm.plot_results("duplicated_negative_numbers")


if __name__ == '__main__':
    main()
