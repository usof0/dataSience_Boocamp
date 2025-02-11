import timeit
from collections import Counter

def my_count_function(lst):
    counts = {}
    for number in lst:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts

def my_top(lst):
    counts_dict = my_count_function(lst)
    return sorted(counts_dict.items(), key=lambda item: item[1], reverse=True)[:10]

def collections_counter(lst):
    return dict(Counter(lst))

def collections_counter_top(lst):
    return dict(Counter(lst).most_common(10))

def main():
    setup = """
import random
from __main__ import my_count_function, my_top, collections_counter, collections_counter_top
random_list = [random.randint(0, 100) for i in range(1000000)]
"""
    time_of_my_func = timeit.timeit(
        setup=setup,
        stmt='my_count_function(random_list)',
        number=1
    )
    time_of_my_top_func = timeit.timeit(
        setup=setup,
        stmt='my_top(random_list)',
        number=1
    )
    time_of_counter = timeit.timeit(
        setup=setup,
        stmt='collections_counter(random_list)',
        number=1
    )
    time_of_counter_top = timeit.timeit(
        setup=setup,
        stmt='collections_counter_top(random_list)',
        number=1
    )

    print(f"my function: {time_of_my_func:.7f}")
    print(f"Counter: {time_of_counter:.7f}")
    print(f"my top: {time_of_my_top_func:.7f}")
    print(f"Counter's top: {time_of_counter_top:.7f}")


if __name__ == "__main__":
    main()
    