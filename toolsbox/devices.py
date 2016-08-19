#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import subprocess
import os
import os.path
import logging
from toolsbox.platform_tools import get_device_product

__author__ = 'yaming'

''


ANDROID_HOME = 'ANDROID_HOME'
COMMAND_ADB_DEVICES = '%s devices'
COMMAND_ADB_PRODUCT = '%s -s %s shell getprop ro.product.model'

android_home = None
adb_path = None


def check_env():
    global android_home
    android_home = os.getenv(ANDROID_HOME)
    logging.info('android home is %s' % android_home)
    if android_home:
        return True
    return False


def build_adb_path():
    global adb_path
    if android_home:
        adb_path = os.path.join(android_home, 'platform-tools', 'adb')
    else:
        logging.error('android home not found')
        raise ValueError('ANDROID_HOME not found')


def get_connect_devices():
    global adb_path
    command = COMMAND_ADB_DEVICES % adb_path
    devices = []
    try:
        output = subprocess.check_output(command, shell=True).decode("utf-8")
        logging.info('adb devices:  %s' % output)
    except Exception as e:
        logging.info(e)
        pass

    lines = output.splitlines()
    for line in lines[1:-1]:
        d = line.split('\t')[0]
        devices.append(d)

    logging.info('devices : %s' % devices)
    return devices


def build_product_devices():
    devices_list = get_connect_devices()
    device_dict = {}
    for device_id in  devices_list:
        command = COMMAND_ADB_PRODUCT % (adb_path, device_id)
        logging.info('COMMAND_ADB_PRODUCT : %s' % command)
        try:
            output = subprocess.check_output(command, shell=True).decode("utf-8")
        except Exception as e:
            logging.error(e)

        p = output.split('\r')[0]
        device_dict.update({get_device_product(p): device_id})

    return device_dict

if __name__ == '__main__':
    print(check_env())
    build_adb_path()
    print(adb_path)
    print(build_product_devices())
    pass
