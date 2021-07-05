#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: __init__.py.py
@time: 2021/7/5 0005 19:36
@desc:
'''
from flask import Blueprint

bp = Blueprint('api', __name__)

# # 写在最后是为了防止循环导入，blog.py文件也会导入 bp
from app.api import blog
