import json
from cm_timer import cm_timer_1
from print_result import print_result
from get_random import gen_random

path = "lab_python_fp//data_light.json"
with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(data):
    return sorted(set(job['job-name'].lower() for job in data))

@print_result
def f2(data):
    return list(filter(lambda x: x.startswith('программист'), data))

@print_result
def f3(data):
    return list(map(lambda x: x + ', с опытом Python', data))

@print_result
def f4(data):
    salaries = gen_random(len(data), 100000, 200001)
    return [f'{job}, зарплата {salary} руб.' for job, salary in zip(data, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))