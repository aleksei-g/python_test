from views import tasks_list, new_task


def setup_routes(app):
    app.router.add_get('/', tasks_list, name='tasks_list')
    app.router.add_get('/tasks/new', new_task, name='new_task')
    app.router.add_post('/tasks/new', new_task, name='new_task')
