from flask import Flask, render_template, redirect, url_for, session, flash
from flask.helpers import url_for
from flask_socketio import SocketIO, join_room, leave_room
from forms import SignUpForm

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "this"

# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

socketio = SocketIO(app)

@app.route('/', methods=["POST", "GET"])
def login():

    form = SignUpForm()

    if(form.validate_on_submit()):

        client = {"username" : form.username.data, "room" : form.room.data}

        session["client"] = client

        return redirect(url_for("chat"))

    else:

        return render_template('login.html', isAutheticate = False, form = form)

@app.route('/chat', methods=["POST", "GET"])
def chat():
    
    if("client" in session):

        client = session["client"]

        if ("username" in client and "room" in client):

            data = {"username" : client["username"], "room" : client["room"]}

            return render_template('chat_room.html', data = data,isAutheticate = True)

    flash("Please sign up first!")
    
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("client", None)
    return redirect(url_for("login"))

@socketio.on('join')
def on_join(data):
    room = data["room"]
    join_room(room)
    socketio.emit('join_room_announcement', data, room = room)

@socketio.on('leave')
def on_join(data):
    room = data["room"]
    leave_room(room)
    socketio.emit('leave_room_announcement', data)

@socketio.on('message')
def handle_message(data):
    room = data["room"]
    socketio.emit('recieve_message',data, room = room)


if __name__ == '__main__':
    socketio.run(app, debug=True,port=5004)