#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String

pub = rospy.Publisher('/cmd_vel_sim', Twist, queue_size=10)

def talker(data):
    global twist
    twist.linear.x = data.linear.x
    twist.angular.z = data.angular.z
    # If the motor has reached its limit, publish a new command.
    pub.publish(twist)


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
        listener()
    except rospy.ROSInterruptException:
        pass
