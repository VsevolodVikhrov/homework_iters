def fibonacci_gen():
    prev_el = 0
    next_el = 1
    while True:
        yield prev_el
        prev_el, next_el = next_el, (next_el + prev_el)


for i in fibonacci_gen():
    print(i)
