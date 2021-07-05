#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: blog.py
@time: 2021/7/5 0005 19:40
@desc:
'''
from flask import jsonify
from app.api import bp

@bp.route('blog', methods=['GET'])
def blog():
    return jsonify('blog_data!')