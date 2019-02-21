from celery import Celery
app=Celery('hello', broker='amqp://guest@localhost//')

@app.task()
def hell():
    return 'hello world'


hell()