import queue
import threading
import time
import sys
from threading import Lock, Event

sys.set_int_max_str_digits(1000000)

lock = Lock()

def create_matrix_and_calculate(size, value, times):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    multiplyer = matrix

    for i in range(size):
        for j in range(size):
            matrix[i][j] = value ** (i + j)

    for i in range(size):
        for j in range(size):
            counter = 0
            for k in range(size):
                counter += matrix[i][k] * multiplyer[k][j]
            matrix[i][j] = counter

    return sum(sum(row) for row in matrix)


class Producer(threading.Thread):
    def __init__(self, task_queue, stop_event, max_tasks):
        super().__init__()
        self.task_queue = task_queue
        self.stop_event = stop_event
        self.max_tasks = max_tasks

    def run(self):
        for task_id in range(1, self.max_tasks + 1):
            task = (task_id + 1, 2, 3)
            self.task_queue.put(task)
            print(f"Producer added task {task_id}: {task}\n")
            time.sleep(1)

        self.stop_event.set()


class Consumer(threading.Thread):
    def __init__(self, task_queue, stop_event):
        super().__init__(daemon=True)
        self.task_queue = task_queue
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            try:
                task = self.task_queue.get(timeout=1)
                size, value, times = task

                result = create_matrix_and_calculate(size, value, times)
                with lock:
                    print(f"Consumer processed task: {task}, result: {result}\n")

                self.task_queue.task_done()
            except queue.Empty:
                continue

        # Обрабатываем оставшиеся задачи после сигнала о завершении
        while not self.task_queue.empty():
            task = self.task_queue.get()
            size, value, times = task

            result = create_matrix_and_calculate(size, value, times)
            with lock:
                print(f"Consumer processed task: {task}, result: {result}")

            self.task_queue.task_done()


if __name__ == "__main__":
    max_tasks = 10
    task_queue = queue.Queue()
    stop_event = Event()
    producer = Producer(task_queue, stop_event, max_tasks)
    num_consumers = 4

    consumers = [Consumer(task_queue, stop_event) for _ in range(num_consumers)]

    producer.start()
    for consumer in consumers:
        consumer.start()

    # Ожидание завершения работы потоков
    producer.join()
    for consumer in consumers:
        consumer.join()

    print("All tasks done!")