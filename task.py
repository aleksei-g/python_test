import asyncio

from datetime import datetime


class Task:
    def __init__(self, n, d, n1, interval):
        self.n = n
        self.d = d
        self.n1 = n1
        self.interval = interval
        self.current_value = 0

    async def run(self):
        for step in range(1, self.n):
            await asyncio.sleep(self.interval)
            self.current_value = self.n1 + self.d * step


class QueueTask(asyncio.Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._running_task = []

    def _get(self):
        task = {
            'task': super()._get(),
            'start_time': datetime.now(),
        }
        self._running_task.append(task)
        return task

    def task_done(self, task):
        super().task_done()
        if task in self._running_task:
            self._running_task.remove(task)

    def get_running_tasks(self):
        tasks = [dict(task, num=num)
                 for num, task in enumerate(self._running_task, 1)]
        return tasks

    def get_pending_tasks(self):
        tasks = [{
            'num': num,
            'task': task
        } for num, task in enumerate(self._queue, 1)]
        return tasks
