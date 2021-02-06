from celery import Celery
from .get_config import get_config

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

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
