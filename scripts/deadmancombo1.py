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
	
def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def safety():
    	global twist
    	# Initial movement
	key = getKey()
	x = 0
	if key == 'k':
		x = 0
	elif key == 'j':
		x = 1
    	twist = Twist()
	twist.linear.x = 1*x; twist.linear.y = 0; twist.linear.z = 0;
    	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    	pub.publish(twist)
    	rospy.spin()


if __name__ == '__main__':
    	settings = termios.tcgetattr(sys.stdin)
	pub = rospy.Publisher('cmd_vel_safety', Twist, queue_size = 1)
	rospy.init_node('safety_deadman', anonymous=True)
	try:
		print msg
        	safety()
		
   	except rospy.ROSInterruptException:
        	pass
