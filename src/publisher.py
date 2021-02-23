#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped 
import math

class talker():
    def __init__(self):
        
	rospy.init_node('publisher',anonymous=True)
	self.pub=rospy.Publisher('publisher_topic',PoseStamped,queue_size=10)
	self.rate = rospy.Rate(15) #15hz 
    def run(self):

        message=PoseStamped()
	self.rate = rospy.Rate(10)
	theta=0
	dt=0.1
	message.header.frame_id="map"
	
	while not rospy.is_shutdown():
	    theta=theta+dt
	    message.pose.position.x=math.cos(theta)
	    message.pose.position.y=math.sin(theta)
	    self.pub.publish(message)
	    self.rate.sleep()

if __name__ == '__main__':
	try:
            node=talker()
	    node.run()
	except rospy.ROSInterruptException:
	    pass
