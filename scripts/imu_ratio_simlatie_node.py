#!/usr/bin/env python            
# license removed for brevity
import rospy          #importeer de rospy library
import math
from std_msgs.msg import String #importeer de string message om te gebruiken voor publishing
from geometry_msgs.msg import Twist

msg = """
Im running
"""
def imu_ratio():          
    pub = rospy.Publisher('fake_imu_ratio', String, queue_size=10)   
    rospy.init_node('imu_ratio_node', anonymous=True)      
    rate = rospy.Rate(10) # 10hz                       
    while not rospy.is_shutdown():                      
        ratio = 1
        for i in range(4):
          rate = rospy.Rate(10)
          while ratio > 0.9:
            		ratio = ratio - 0.01
			pub.publish(ratio)                            
            		rate.sleep() 
          rate = rospy.Rate(10)
          while ratio < 1.1:
            		ratio = ratio + 0.01
			pub.publish(ratio)                            
            		rate.sleep() 
        
if __name__ == '__main__':
    try:                                            
        imu_ratio()
    except rospy.ROSInterruptException:
        pass
