from wtforms import Form, IntegerField, FloatField


class TaskForm(Form):
    n = IntegerField('Количество элементов', description='integer')
    d = FloatField(
        'Дельта между элементами последовательности',
        description='float',
    )
    n1 = FloatField('Стартовое значение', description='float')
    interval = FloatField(
        'Интервал в секундах между итерациями',
        description='float',
    )
