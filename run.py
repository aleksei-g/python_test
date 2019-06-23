from os import getenv

import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes
from task import QueueTask

DEFAULT_COUNT_WORKERS = 1
count_workers_env = getenv('COUNT_WORKERS', '')
COUNT_WORKERS = (
    int(count_workers_env)
    if count_workers_env.isdigit() and int(count_workers_env) > 0
    else DEFAULT_COUNT_WORKERS
)


async def queue_worker(queue):
    while True:
        task = await queue.get()
        await task['task'].run()
        queue.task_done(task)


async def start_background_queue(app):
    app['queue'] = QueueTask()
    app['queue_workers'] = [
        app.loop.create_task(queue_worker(app['queue']))
        for _ in range(COUNT_WORKERS)
    ]


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

setup_routes(app)

if __name__ == '__main__':
    app.on_startup.append(start_background_queue)
    web.run_app(app)
