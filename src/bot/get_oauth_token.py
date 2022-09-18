# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, redirect
from requests import post

import sys
from urllib.parse import urlencode

# Идентификатор приложения
client_id = '39ae3c05ee564ee68e1837e22a88839a'
# Пароль приложения
client_secret = 'b5d672f23107421b845dfb579638d1f4'
# Адрес сервера Яндекс.OAuth
baseurl = 'https://oauth.yandex.ru/'

app = Flask(__name__)

@app.route('/')
def index():
    if request.args.get('code', False):
        # Если скрипт был вызван с указанием параметра "code" в URL,
        # то выполняется запрос на получение токена
        print(request.args)
        print(request.data)
        data = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'client_id': client_id,
            'client_secret': client_secret
        }
        data = urlencode(data)
        # Токен необходимо сохранить для использования в запросах к API Директа
        return jsonify(post(baseurl + "token", data).json())
    else:
        # Если скрипт был вызван без указания параметра "code",
        # то пользователь перенаправляется на страницу запроса доступа
        return redirect(baseurl + "authorize?response_type=code&client_id={}".format(client_id))