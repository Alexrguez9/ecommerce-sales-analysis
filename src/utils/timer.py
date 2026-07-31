import time

class Timer:
    def __init__(self):
        self.start = None

    def start_timer(self):
        self.start = time.time()

    def stop_timer(self):
        return time.time() - self.start