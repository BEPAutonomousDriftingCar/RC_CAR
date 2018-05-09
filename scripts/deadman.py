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

pub = rospy.Publisher('/cmd_vel_sim', Twist, queue_size=1)

def talker(data):
    global twist
    twist.linear.x = data.linear.x
    twist.angular.z = data.angular.z
    # If the motor has reached its limit, publish a new command.
    pub.publish(twist)

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def listener():
    global twist
    rospy.init_node('deadman', anonymous=True)
    rospy.Subscriber('/cmd_vel', Twist, talker)
    # Initial movement.
    twist = Twist()
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0;
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
    pub.publish(twist)
    rospy.spin()


if __name__ == '__main__':
    try:
        key = getKey()
        if key == "k":
            listener()
    except rospy.ROSInterruptException:
        pass
    finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		pub.publish(twist)

    	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

