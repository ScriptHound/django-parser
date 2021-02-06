from celery import Celery
from .get_config import get_config
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djparser.settings')
django.setup()
CONF = get_config()
USER = CONF['USER']
NAME = CONF['NAME']
HOST = CONF['HOST']
PORT = CONF['PORT']
PASSWD = CONF['PASSWORD']

app = Celery('main',
             broker='redis://127.0.0.1:6379',
             backend=f'db+postgresql://{USER}:{PASSWD}@{HOST}:{PORT}/{NAME}'
             )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
