#!/usr/bin/env python               
# license removed for brevity
import rospy                    #importeer de rospy library
from std_msgs.msg import String #importeer de string message om te gebruiken voor publishing
from geometry_msgs.msg import Twist

def talker_test():          
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)        #Node is publishing naar de chatter2 topic, message type string
    rospy.init_node('talker_test', anonymous=True)     #Naam van de node is talker_test en wordt door anonymous een string achter geplakt     
    rate = rospy.Rate(10) # 10hz                        #Datarate per seconde
    while not rospy.is_shutdown():                        #Doe dingen als het niet uit staat
        hello_str = "Anand is er niet op tijdstip %s" % rospy.get_time()        #De string
        rospy.loginfo(hello_str)                        #Log de string
        pub.publish(hello_str)                              #Publish de string naar de topic chatter2
        rate.sleep()                                          #Slaap/pauseer om te zorgen dat de gewenste datarate wordt bereikt
                                                    #standaard code, gewoon doen
if __name__ == '__main__':
    try:                                            #loop door talker_test() als er niets ander gebeurt
        talker_test()
    except rospy.ROSInterruptException:
        pass
