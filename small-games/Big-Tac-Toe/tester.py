from game import TicTacToe as TTT


class Test:
    """
        TYPES:
        * test: [a function that checks to see if a condition of its parameter(s) is true.
                 throws an appropriate error if this is not the case]
        * test_list: [(each element): a dictionary that contains the test [test], 
                      the input [input], its expected value [expected], and an error message [message] to 
                      print should the test not work]
    """

    def __init__(self):
        self.test_list = []

    def add_test(self, test, input, expected, message):
        # precondition: msg MUST be a string
        self.test_list.append(
            {"test": test, "input": input, "expected": expected, "message": message})

    def __add__(self, test_class2):
        # precondition: test_class2 MUST be of class type Test
        return self.test_list + test_class2.test_list


def run_tests(test_list):
    test_count = 0
    for test_container in test_list:
        test = test_container[0]
        input = test_container[1]
        expected = test_container[2]
        message = test_container[3]
        try:
            assert test(input) == expected
        except:
            print("Error occurred on test", test_count, message)
        test_count += 1
    print("all done")


move_invariant_tests = []

if __name__ == "__main__":
    run_tests
