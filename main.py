#         -*- coding:utf-8 -*-        #
#  Copyright (c) 2019 - 2039 XueQian  #
#         version_added:: 2.0.0         #
import os
import time
from flask import *

app = Flask(__name__)
list_ = []


def mkdir(path):
    # path = path[:-len('\\' + path.split('\\')[-1])]
    # 当时还没学三元，将就一下吧
    # 判断结果
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def zy():
    try:
        if (request.method == 'POST'):
            p = '.\\' + request.json.get('path')
            print(p)
            list_.append({'name':p, 'time': time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time()))})
            mkdir(p[:-len(p.split('\\')[-1])])
            open(p, 'wb').write(eval(request.json.get('file')))
            return 'OK'
        p = os.path.abspath('./file').replace('\\', '/')
        return f"file://{p}"
    except Exception as e:
        print(e)
        return 'False'


@app.route('/c/<name>')
def _room(name):
    return jsonify(eval(name))


if __name__ == '__main__':
    print(" * Run's time: " + time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time())))
    app.run(host='192.168.3.10', port=2232, debug=False)

# host='192.168.3.10'
