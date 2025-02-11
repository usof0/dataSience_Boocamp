import timeit

def loop(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails

def list_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

def main():
    setup = """
from __main__ import loop, list_comprehension
emails = [
    'john@gmail.com',
    'james@gmail.com',
    'alice@yahoo.com',
    'anna@live.com',
    'philipp@gmail.com'
] * 5
    """
    loop_time = timeit.timeit(setup=setup, stmt='loop(emails)', number=90_000_000)
    list_comprehension_time = timeit.timeit(setup=setup, stmt='list_comprehension(emails)', number=90_000_000)

    if list_comprehension_time <= loop_time:
        better = "list comprehension"
    else:
        better = "loop"

    times = sorted([loop_time, list_comprehension_time])

    print(f"it is better to use a {better}")
    print(f"{times[0]} vs {times[1]}")

if __name__ == "__main__":
    main()