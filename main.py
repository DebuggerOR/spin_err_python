import threading

counter = 0
cycles = 10000


class Peterson:
    def __init__(self):
        self.flag = [0,0]
        self.turn = 0

    def lock(self, id):
        # say you want the lock
        self.flag[id] = 1
        # give other thread first
        self.turn = 1 - id
        # wait while other want and its his turn
        while self.flag[1 - id] == 1 and self.turn == 1 - id:
            "i am waiting"

    def unlock(self, id):
        # say you don't want lock
        self.flag[id] = 0


def thread_func(lock, id):
    for i in range(cycles):
        lock.lock(id)
        global counter
        counter += 1
        lock.unlock(id)


if __name__ == '__main__':
    plock = Peterson()

    t1 = threading.Thread(target=thread_func, args=(plock, 0))
    t1.start()

    t2 = threading.Thread(target=thread_func, args=(plock, 1))
    t2.start()

    t1.join()
    t2.join()

    print("counter equals to %d instead of %d" % (counter,2 * cycles))
