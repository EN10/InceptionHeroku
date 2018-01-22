from flask import Flask, request
app = Flask(__name__)

import subprocess

@app.route('/')
def index():
    
    q = request.args.get('q')
    if q <> None:
        p = subprocess.Popen(['bash', 'run.sh', q], stdout=subprocess.PIPE)
        output, err = p.communicate()
        output = output.replace('\n','<br>')
    else:
        output = 'ERROR: No URL Given!'

    return output