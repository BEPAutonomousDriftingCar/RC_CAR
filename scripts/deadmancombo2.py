#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy
import math

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Bool

msg = """
Reading from the keyboard  and Publishing to Twist!
"""

def talker(data):
   	global twist
    	twist = Twist()
	twist.linear.x = data.linear.x*bool
    	twist.angular.z = data.angular.z*bool
    	pub.publish(twist)
	

def safety():
	global bool
	bool = Bool()
    	bool = data
	return bool
    	# If the motor has reached its limit, publish a new command.

def listener():
    	global twist
   	rospy.Subscriber('/cmd_vel_sim', Twist, talker)
	rospy.Subscriber('/cmd_vel_safety', Twist, safety)
   	 # Initial movement.
    	twist = Twist()
    	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
   	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
   	pub.publish(twist)
    	rospy.spin()


if __name__ == '__main__':
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('deadman', anonymous=True)
	try:
		print msg
        	listener()
		
   	except rospy.ROSInterruptException:
        	pass
