import socketio
import json
from utils.timer_door import Timer
from utils.devices_control import close_door,open_door
from utils.constant import SERVER_DEVICE_CTR_ADDR

#Create socket for door control server connection
sio   = socketio.Client()


#Timer for door control
timer = Timer(2,close_door)
timer.start()

@sio.event
def connect():
    print('Connection to door server established')
    msg = "5"
    sio.emit("doorMessage",msg)

@sio.event
def open_door_msg(msg):
    print('Open the door message : ', msg)
    if msg['open_door'] == "yes":
      open_door()
      timer.reset()

@sio.event
def close_door_msg():
    print('Close the door message')
    close_door()
    timer.reset()

@sio.event
def disconnect():
    print('Disconnected from door control server')

if __name__ == '__main__':
    print("Door-Control-Server is connected")
    sio.connect(SERVER_DEVICE_CTR_ADDR)
    sio.wait()
