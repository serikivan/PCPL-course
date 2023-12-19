from contextlib import contextmanager
import time

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        elapsed = time.time() - self.start
        print(f"Прошло: {elapsed}")

#with cm_timer_1():
    #time.sleep(5.5)
   

@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"Прошло: {elapsed}")

#with cm_timer_2():
    #time.sleep(5.5)