import os

from time import sleep
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from flask import Flask
app = Flask(__name__)

# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(2)
pool_executor = ProcessPoolExecutor(2)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'


@app.route('/jobs')
def run_jobs():
    """
    Note: this could be done the following way:
        * a list of jsons with arguments  for the pricer
        * submit pricer n-times
    """
    executor.submit(some_long_task2, 'hello', 123)
    executor.submit(some_long_task2, 'world', 456)
    return 'Two jobs was launched in background!'


def some_long_task1():
    print("Task #1 started!")
    sleep(10)
    print("Task #1 is done!")


def some_long_task2(arg1, arg2):
    print("Task #2 started with args: %s %s!" % (arg1, arg2))
    sleep(10)
    print("Task #2 is done!")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
