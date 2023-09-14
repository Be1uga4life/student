from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import datetime
from pathlib import Path
import string
import random
import sys
import os

app = Flask(__name__)
app.secret_key = '8HBlop91yup&p;lu1jghahp()*;'

@app.route("/")
def index():
    return render_template('ticketing.md')

@app.route("/create_ticket", methods=['POST'])
def create_ticket():
    subject = request.form['a']
    message = request.form['b']

    now = datetime.now()
    time = now.strftime("%H:%M:%S")

    hash = random.getrandbits(5)

    letters = string.ascii_lowercase
    uniq = ''.join(random.choice(letters) for i in range(10))

    path = "/home/eroxyi/vscode/student/templates/tickets/ticket_{}".format(uniq)

    touch_command = "touch {}".format(path)
    os.system(touch_command)

    subject_command = "awk 'BEGIN {print \"" + subject + "\"}' > " + path
    os.system(subject_command)

    os.system("awk 'BEGIN {print \"" + "+==============================================================+" + "\"}' >> " + path)

    message_command = "awk 'BEGIN {print \"" + message + "\"}' >> " + path
    os.system(message_command)

    log_message = '[date: {}] [ticket: {}] [subject: {}] [message: {}]'.format(time, "ticket_"+uniq, subject, message)
    f = open("/var/log/ccgt.log", "a")
    f.write(log_message + "\n")

    return redirect(url_for('index'))

if __name__ == '__main__':
    if Path('/var/log/ccgt.log').is_file():
        app.run(host = '0.0.0.0', port = 4201)
    else:
        sys.exit("no log file found, please create before running again")
