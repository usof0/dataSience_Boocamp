import timeit

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

def main():
    setup = """
from __main__ import loop, list_comprehension, list_map
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
    map_time = timeit.timeit(setup=setup, stmt='list_map(emails)', number=90_000_000)

    min_time = min(loop_time, list_comprehension_time, map_time)

    if min_time == list_comprehension_time:
        better = "list comprehension"
    elif min_time == map_time:
        better = "loop"
    else:
        better = "map"

    times = sorted([loop_time, list_comprehension_time, map_time])

    print(f"it is better to use a {better}")
    print(f"{times[0]} vs {times[1]} vs {times[2]}")

if __name__ == "__main__":
    main()