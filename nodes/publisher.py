#!/usr/bin/env python3  
import rospy
from std_msgs.msg import String

rospy.init_node('publisher')
rate = rospy.Rate(rospy.get_param('~rate', 10))
pub = rospy.Publisher('/message', String, queue_size=10)
message = rospy.get_param('~message', 'pub2')


while not rospy.is_shutdown():
    pub.publish(message)
    rate.sleep()