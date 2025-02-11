import timeit
import sys
from functools import reduce

def loop_function(num):
    total = 0
    for i in range(1, num + 1):
        total += i**2
    return total

def reduce_function(num):
    return reduce(lambda res, i: res + i**2, range(1, num + 1), 0)

def main():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: python3 benchmark.py <function> <number_of_calls> <number_for_sum>")
        
        func = sys.argv[1]
        num_of_calls = int(sys.argv[2])
        num_for_sum = int(sys.argv[3])
        if func == "loop":
            stmt = f'loop_function({num_for_sum})'
        elif func == "reduce":
            stmt = f'reduce_function({num_for_sum})'
        else:
            raise ValueError("Invalid function name")
        
        run_time = timeit.timeit(stmt=stmt, globals=globals(), number=num_of_calls)
        
        print(run_time)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    