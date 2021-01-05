# -*- coding: utf-8 -*-

import os
import socket
import sys

import yaml  # pip3 install pyyaml

if 'python' in sys.executable:
    abs_path = lambda file: os.path.abspath(os.path.join(os.path.dirname(__file__), file))
else:
    abs_path = lambda file: os.path.abspath(os.path.join(os.path.dirname(sys.executable), file))
    # mac 上打包后 __file__ 指定的是用户根路径，非当执行文件路径

config = yaml.full_load(open(abs_path('config.yaml'), encoding='utf8'))


def get_host_ip():
    """
    获取本机的IP
    """
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        if s:
            s.close()

    return ip


IP = get_host_ip()
