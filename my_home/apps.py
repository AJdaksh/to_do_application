import sys
from django.apps import AppConfig
from django.contrib.sessions.backends.db import SessionStore



class MyHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_home'
    def start():
        s=SessionStore
        s['page_id']='active'
        s.create  
        s=SessionStore(session_key=s.session_key)    
        return True
