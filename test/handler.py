# -*- coding: utf-8 -*-
import json
import os
import sys

# 以下の行を追加
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'vendor'))

from PIL import Image


def hello(event, context):
    img = Image.open('lena_std.tif', 'r')
    resize_img = img.resize((100, 100))
    status = resize_img.save('/tmp/resize_img.jpg', 'JPEG', quality=100, optimize=True)
    return status
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    # """
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }
    # """
