#!/usr/bin/env python            
# license removed for brevity
#git pulll test
import rospy          #importeer de rospy library
import math
from std_msgs.msg import String #importeer de string message om te gebruiken voor publishing
from geometry_msgs.msg import Twist


def imu_ratio():          
    pub = rospy.Publisher('fake_imu_ratio', Twist, queue_size=10)   
    rospy.init_node('imu_ratio_node', anonymous=True)      
    rate = rospy.Rate(10) # 10hz                       
    while not rospy.is_shutdown():                      
        ratio = 1
        for i in range(4):
          rate = rospy.Rate(10)
          while ratio > 0.9:
            		ratio = ratio - 0.01
            		twist = Twist()
	   		twist.linear.x = ratio; twist.linear.y = 0; twist.linear.z = 0;
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
			pub.publish(twist)                            
            		rate.sleep() 
          rate = rospy.Rate(10)
          while ratio < 1.1:
            		ratio = ratio + 0.01
            		twist = Twist()
			twist.linear.x = ratio; twist.linear.y = 0; twist.linear.z = 0;
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0;
			pub.publish(twist)                            
            		rate.sleep() 
        
if __name__ == '__main__':
    try:                                            
        imu_ratio()
    except rospy.ROSInterruptException:
        pass
