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

def listener1():
    	global dm
	global twist
   	rospy.Subscriber('/dm_init', Twist, talker2)
    	rospy.Subscriber('/cmd_vel_sim', Twist, talker1)
    	# Initial movement.
    	#twist = Twist()
    	#twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    	#twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    	#pub.publish(twist)
    	rospy.spin()
	
def talker1(data):
    	global dm
	global twist
    	twist = Twist()
    	#twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    	#twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    	twist.linear.x = data.linear.x * dm 
    	twist.angular.z = data.angular.z * dm
    	pub.publish(twist)
	
def talker2(data):
    	global dm
	dm = data.linear.x
	twist = Twist()
	twist.linear.x = dm 
    	pub.publish(twist)
    	return dm
	
if __name__ == '__main__':
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('deadman', anonymous=True)
	try:
		print msg
        	listener1()
		
   	except rospy.ROSInterruptException:
        	pass
