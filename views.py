import aiohttp_jinja2
from aiohttp import web

from forms import TaskForm
from task import Task


@aiohttp_jinja2.template('index.html')
async def tasks_list(request):
    running_tasks = request.app['queue'].get_running_tasks()
    pending_tasks = request.app['queue'].get_pending_tasks()
    return {
        'request': request,
        'running_tasks': running_tasks,
        'pending_tasks': pending_tasks,
    }


@aiohttp_jinja2.template('new_task_form.html')
async def new_task(request):
    if request.method == 'POST':
        payload = await request.post()
        task_form = TaskForm(payload)
        if task_form.validate():
            task = Task(
                n=task_form.n.data,
                d=task_form.d.data,
                n1=task_form.n1.data,
                interval=task_form.interval.data,
            )
            await request.app['queue'].put(task)
            raise web.HTTPFound(request.app.router['tasks_list'].url_for())
    else:
        task_form = TaskForm()
    return {'request': request, 'form': task_form}
