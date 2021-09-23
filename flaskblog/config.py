import os


class Config:
    SECRET_KEY = '70eff57c9ab5b5a860363e56df81f89a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'blogblog353@gmail.com'
    MAIL_PASSWORD = 'blog%353Blog%353#'
