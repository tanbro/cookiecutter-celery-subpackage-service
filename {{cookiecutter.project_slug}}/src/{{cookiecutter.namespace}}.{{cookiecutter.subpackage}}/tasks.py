from .app import app

@app.task
def hello(s):
    return 'Hello, {}!'.format(s)
