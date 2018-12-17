SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Itzler.666@localhost/flask-order"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SERVER_PORT = 5000
AUTH_COOKIE_NAME = "flask-order"

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]