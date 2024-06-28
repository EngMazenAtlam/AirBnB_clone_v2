#!/usr/bin/python3
import os

ENV_VAR = {
            'hbnb_env' : os.getenv("HBNB_ENV"),
            'hbnb_usr' : os.getenv("HBNB_MYSQL_USER"),
            'hbnb_usr_pwd' : os.getenv("HBNB_MYSQL_PWD"),
            'hbnb_db' : os.getenv("HBNB_MYSQL_DB"),
            'hbnb_storage_type' : os.getenv("HBNB_TYPE_STORAGE"),
            'hbnb_host' : os.getenv('HBNB_MYSQL_HOST')
            }
