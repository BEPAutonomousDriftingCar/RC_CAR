#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy
import math

from geometry_msgs.msg import Twist
from std_msgs.msg import String

import sys, select, termios, tty
msg = """
Reading from the keyboard  and Publishing to Twist!
"""

def talker(data):
   	global twist
    	twist = Twist()
	twist.linear.x = data.linear.x
    	twist.angular.z = data.angular.z
    	pub.publish(twist)
	
def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def safety():
	global twist
	twist = Twist()
    	twist.linear.x = 0
    	twist.angular.z = 0
    	# If the motor has reached its limit, publish a new command.
    	pub.publish(twist)

def listener():
    global twist
	key = getKey()
	while key != 'k':
		rospy.Subscriber('/cmd_vel_sim', Twist, talker)
    # Initial movement.
    twist = Twist()
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    pub.publish(twist)
    rospy.spin()


if __name__ == '__main__':
    	settings = termios.tcgetattr(sys.stdin)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('deadman', anonymous=True)
	try:
		print msg
        	listener()
   	except rospy.ROSInterruptException:
        	pass


