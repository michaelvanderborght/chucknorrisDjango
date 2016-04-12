from __future__ import unicode_literals

from django.apps import AppConfig


class ChucknorrisConfig(AppConfig):
    name = 'ChuckNorris'

    import redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    r.set("jokes","{'jokes',[{'joke':'bla'},{'joke':'bla2'}]}")
