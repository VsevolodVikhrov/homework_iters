import datetime
import time
from typing import Union


def random_gen(bound: Union[int, bool] = False):
    counter = 0
    data = []
    while not bound or counter <= bound:
        start = datetime.datetime.now().microsecond
        now1 = datetime.datetime.now().microsecond
        now2 = datetime.datetime.now().microsecond
        end = datetime.datetime.now().microsecond
        try:
            operations = {
                0: now1 + end + now2 * start,
                1: start + end - now1 * now2,
                2: start * end / now2 % now1,
                3: start - now1 / end * now2,
                4: start * now1 // now2 + end,
                5: start / now2 * end % now1,
                6: start // now2 + now1 - end,
                7: end + start * now1 - now2,
                8: end / start + now2 + now1,
                9: end + now1 + start // now2
            }
            choose_index = str(start * now1 - now2 + end)
            choose_index = int(choose_index[0])
            result = int(operations[choose_index])
            if result < 0:
                result *= -1
            if result % 10000 >= 0:
                result = int(str(result)[:4])
            if not data:
                data.append(result)
            time.sleep(0.01)
            if result not in data and ((data[counter] / result) > 1.05 or (data[counter] / result) < 0.95):
                data.append(result)
                yield result
                counter += 1
        except ZeroDivisionError:
            pass


count_of_numbers = int(input("Input zero for endless loop or number for set count of rands: "))
for i in random_gen(count_of_numbers):
    print(i)





