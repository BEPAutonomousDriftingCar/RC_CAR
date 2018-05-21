#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy
import math

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Bool

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
    	global bool
    	# Initial movement
	key = getKey()
	x = 0
	if key == 'k':
		x = 0
	elif key == 'j':
		x = 1
    	bool = Bool()
	bool = x
    	pub.publish(bool)
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
