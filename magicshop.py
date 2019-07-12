__author__ = 'GitHub:Air-Zhuang'

from app import create_app
import platform

app=create_app()

if __name__ == '__main__':
    if (platform.system() == 'Linux'):
        app.run(host='172.19.91.71', port=8999, debug=app.config['DEBUG'])
    else:
        app.run(host='127.0.0.1', debug=app.config['DEBUG'])
