# -*- coding: utf-8 -*-

from functions.my_model import load_predict

def find_tags(title=None, body=None):
    """Process the title and body provided
    Returns the proposed tags"""
    return load_predict(title + ' ' + body, 'python')