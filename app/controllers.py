from flask import Blueprint, current_app
from factories.celery import create_celery
home = Blueprint('home_views', __name__)


@home.route('/')
def index():
    celery = create_celery(current_app)
    res = celery.send_task('tasks.simple_task', args=('-=-= TEST FROM VIEW =-=-', ))
    print res
    return
