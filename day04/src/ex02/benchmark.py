import timeit
import sys

def loop(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails

def list_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

def list_map(emails):
    return list(map(lambda email: email if email.endswith('@gmail.com') else None, emails))

def list_filter(emails):
    return list(filter(lambda email: email.endswith('@gmail.com'), emails))

def main():
    setup = """
from __main__ import loop, list_comprehension, list_map, list_filter
emails = [
    'john@gmail.com',
    'james@gmail.com',
    'alice@yahoo.com',
    'anna@live.com',
    'philipp@gmail.com'
] * 5
    """
    try:
        if len(sys.argv) != 3:
            raise ValueError("Usage: python3 benchmark.py <function> <number_of_calls>")
        
        func = sys.argv[1]
        num_of_calls = int(sys.argv[2])

        if func == "loop":
            stmt = 'loop(emails)'
        elif func == "list_comprehension":
            stmt = 'list_comprehension(emails)'
        elif func == "map":
            stmt = 'list_map(emails)'
        elif func == "filter":
            stmt = 'list_filter(emails)'
        else:
            raise ValueError("Invalid function name")
        
        run_time = timeit.timeit(setup=setup, stmt=stmt, number=num_of_calls)
        
        print(run_time)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()