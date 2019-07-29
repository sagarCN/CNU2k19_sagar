from flask import Flask, render_template
import flask
import redis
import os


app = Flask(__name__)
app.debug = True

bind_port = os.environ['BIND_PORT']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
user = os.environ['USERNAME']


db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT) 


@app.route("/")
def index():
	if db.exists("3"):
		db.mset({"1":int(db.get("2"))})
		db.mset({"2":int(db.get("3"))})
		db.mset({"3":int(db.get("1")) + int(db.get("2"))})
	elif db.exists("2"):
		db.mset({"3":int(db.get("1")) + int(db.get("2"))})
	elif db.exists("1"):
		db.mset({"2":1})
		return "Hello % s Reloaded %d number of times" % (user, int(db.get("2")))
	else:
		db.mset({"1":1})
		return "Hello % s Reloaded %d number of times" % (user, int(db.get("1")))

	return "Hello % s Reloaded %d number of times" % (user, int(db.get("3")))


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')