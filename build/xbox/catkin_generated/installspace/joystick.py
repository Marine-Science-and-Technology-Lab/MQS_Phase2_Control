#!/usr/bin/env python2
import rospy
from cmd_msgs.msg import CMD #might need to make this
from sensor_msgs.msg import Joy

#This ROS node converts joystick inputs from an xbox controller
#into commands for the model quadski (mqs) robot

#Recieves joystick messages (subscribed to Joy topic)

#axis 0 steering marine
#axis 1 no input/output
#axis 2 reverse land
#axis 3 steering land
#axis 4 throttle marine
#axis 5 throttle land
#axis 6 no input/output
#axis 7 no input/output

#bt0 ESC on (sends HIGH until pressed again)
#bt1 bilge pump on (sends HIGH until pressed again)
#bt2 DAQ on  (sends HIGH until pressed again)
#bt3 wheel retraction (sends HIGH until postion recieved, next high reverese direction)
#bt4 cooling pump on (sends HIGH until pressed again)
#bt5 reverse bucket (must be held to operate)
#bt6 none
#bt7 none
#bt8 none

def callback(data):
   cmd=CMD()
   cmd.marine.str=4*data.axes[0]
   cmd.land.rev=4*data.axes[2]
   cmd.land.str=4*data.axes[3]
   cmd.marine.tht=4*data.axes[4]
   cmd.land.fwd=4*data.axes[5]
   cmd.op.esc=data.buttons[0]
   cmd.op.bp=data.buttons[1]
   cmd.op.daq=data.buttons[2]
   cmd.op.wrt=data.buttons[3]
   cmd.op.cp=data.buttons[4]
   cmd.op.revm=data.buttons[5]
   pub.publish(cmd)

def start():
    global pub
    #publishing to mqs/cmd to control mqs robot
    pub=rospy.Publisher('mqs/cmd',CMD)
    #subscirbes to joystick inputs on topic joy
    rospy.Subscriber("joy",Joy,callback)
    #starts the node
    rospy.init node('xbox')
    rospy.spin()


if name == '__main__':
    start()