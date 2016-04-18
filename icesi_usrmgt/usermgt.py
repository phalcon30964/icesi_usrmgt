import json
import commands
from flask import Flask
app = Flask(__name__)

@app.route("/api/v1.0/usermgt/users")
def hello():

	ret = commands.getoutput("ls /home | sort")
	ret = ret.split("\n")
	ret = "{users:"+json.dumps(ret)+"}"
	return ret

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
