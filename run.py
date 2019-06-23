import argparse
from os import getenv

import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes
from task import QueueTask


COUNT_WORKERS_CHOISES = range(1, 6)
DEFAULT_COUNT_WORKERS = 1
count_workers_env = getenv('COUNT_WORKERS', DEFAULT_COUNT_WORKERS)
parser = argparse.ArgumentParser(description='PERX Python test')
try:
    parser.add_argument(
        '--count_workers',
        default=int(count_workers_env),
        type=int,
        choices=COUNT_WORKERS_CHOISES,
        help='Number of queue workers.'
    )
    args = parser.parse_args()
    COUNT_WORKERS = args.count_workers
    if COUNT_WORKERS not in COUNT_WORKERS_CHOISES:
        raise ValueError
except ValueError:
    raise ValueError(
        'Environment variable "COUNT_WORKERS" must be an integer from interval:'
        ' {}'.format(', '.join([str(x) for x in COUNT_WORKERS_CHOISES])))


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
