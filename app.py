from flask import Flask, request
app = Flask(__name__)

import subprocess

@app.route('/')
def index():
    q = request.args.get('q')

    subprocess.call(["curl", q, ">", "image.jpg"])
    p = subprocess.Popen(["python", "classify_image.py", "--image_file", "image.jpg"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    output = output.replace('\n','<br>')

    return output