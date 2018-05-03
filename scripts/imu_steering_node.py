#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

mgs = """
IM RUNNING



"""

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('controller', anonymous=True)
    rospy.Subscriber('fake_imu_ratio', Twist, callback)
    pub = rospy.Publisher('test_cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown(): 		
	pub.publish(data)                            
        rate.sleep() 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
		
if __name__ == '__main__':
    try:
	listener()
	
    except rospy.ROSInterruptException:
        pass
