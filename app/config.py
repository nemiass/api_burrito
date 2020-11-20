from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
# MYSQL connection
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'burrito'

mysql = MySQL()
mysql.init_app(app)
app.secret_key = 'mysecretkey'
