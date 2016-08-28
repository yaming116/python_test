#!/usr/bin/evn python
# _*_ coding: utf-8 _*_

import os
import subprocess

__author__ = 'yaming116'

'dump apk permissions'

CMD = 'F:\\android-sdk\\build-tools\\23.0.3\\aapt dump permissions %s'

apks = []
try:
    files = os.listdir('apks./')
except Exception as  e:
    print('请在当前目录建立 apks 目录，并把apk文件放入当前目录')
finally:
    pass

for f in files :
    if f.endswith('.apk'):
        apks.append(os.path.join('apks', f))

permissions = ''

for a in apks:
    cmd = CMD % a;
    print(cmd)
    try:
        out = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except Exception as e:
        print('dump permissions error for %s ' % a)
    finally:
        pass

    if out is not None:
        permissions += out
        permissions += '============================================\r\n'

with open(os.path.join('permissions'), 'w') as f:
    f.write(permissions)