#! /usr/bin/evn python

import rospy

rospy.init_node('print_info')
print 'INFORMATION: All essential nodes are now running. You can connect simulink to the car via two ways: /cmd_vel or /cmd_vel_sim (use second if you want emercency button). Start rc_car dm_init.py for emercency button'
rospy.spin()
