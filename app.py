from flask import Flask
app = Flask(__name__)

import subprocess
p = subprocess.Popen(["python", "classify_image.py"], stdout=subprocess.PIPE)
output, err = p.communicate()
output = output.replace('\n','<br>')

@app.route('/')
def index():
	return output