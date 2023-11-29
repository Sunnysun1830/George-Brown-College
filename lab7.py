""""
Task 1
    Given the following function
        def output(fruit, value):
            for val in range(value, -1, -1):
                print(fruit, val)

    Create a list of 3 fruits
    Create an empty list of threads
    Iterate through each fruit
        Create a new thread that calls on the function
            output
        with the args
            fruit = current value of fruit
            value = 10

    In another loop, START each thread

    Run this script at least 5 time.
    Write down your observations as a comment
"""
import threading


def output(fruit, value):
    for val in range(value, -1, -1):
        print(fruit, val)


def main():
    fruits = ["Golden Dragon Fruit", "Mango", "Orange"]
    threads = []

    for fruit in fruits:
        # arg is tuples
        thread = threading.Thread(target=output, args=(fruit, 10))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    for i in range(5):
        print(f'\n------ Run {i + 1} ------')
        main()
"""
in run some output are concurrent, multiple threads were running at the same time.
The order of fruits is not the same.
some number collapse 
"""