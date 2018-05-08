#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String

goal_pos = 0;
pub = rospy.Publisher('/cmd_vel', Twist)

def talker(data):
    global goal_pos
    rospy.loginfo(rospy.get_name() + ': Current motor angle {0}'.format(data.current_pos))

    # If the motor has reached its limit, publish a new command.
    if fabs(goal_pos-data.current_pos) < 0.01:
        if goal_pos == 0:
            goal_pos = 3.141592
        else:
            goal_pos = 0

        str = "Time: {0} Moving motor to {1}" .format(rospy.get_time(), goal_pos)
        rospy.loginfo(str)
        pub.publish(Float64(goal_pos))


def listener():
    rospy.init_node('dxl_control', anonymous=True)
    rospy.Subscriber('/cmd_vel_sim', Twist, talker).
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
