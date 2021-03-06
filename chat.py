#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, emit


# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './Chat.html' )

def messageRecieved():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recieved event: ' + str( json ) )
  try:
    if json['data'] == "User Connected":
        socketio.emit( 'my response', {"message": u"One more user!", "user_name": "server"}, callback=messageRecieved )
    if  json['data'].split(" ")[-1] == "Disconnected":
        socketio.emit( 'my response', {"message": ' '.join(json['data'].split(" ")[:-1]) + u" left chat room" ,"user_name": "server"}, callback=messageRecieved )
  except:       
    socketio.emit( 'my response', json, callback=messageRecieved )

if __name__ == '__main__':
    socketio.run( app, debug = True )