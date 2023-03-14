import os

from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\q\xbfq\x97\xbf\t}\xec\x8c/\xcd\xb5V\x0e\x93\x81\xa0\xa9\xd0I=s\x17'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASEDIR, 'school-app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'uk']