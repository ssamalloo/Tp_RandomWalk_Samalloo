#!/usr/bin/env python3

import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
import time

class carrer:
        def __init__(self):
                rospy.init_node('carrer', anonymous=True)
                self.pub = rospy.Publisher('square_point', PoseStamped, queue_size=10)
                self.rate = rospy.Rate(15)
                self.message = PoseStamped()
                self.length=5
                self.state=None
                self.message.pose.position.x = 0
                self.message.pose.position.y = 0
                self.message.header.frame_id='map'

                self._running = True

                rospy.Subscriber('button_state', Bool, self.sub_callback)

        def sub_callback(self, data):
                self.state = data.data

        def run(self):
                while not rospy.is_shutdown():
                        while(self.state == True):
                                if(self.message.pose.position.x == 0 & self.message.pose.position.y == 0):
                                        while ((self.message.pose.position.y != self.length) & self.state == True):
                                                self.message.pose.position.y += 1
                                                self.pub.publish(self.message)
                                                self.rate.sleep()

                                        while ((self.message.pose.position.x != self.length) & self.state == True):
                                                self.message.pose.position.x += 1
                                                self.pub.publish(self.message)
                                                self.rate.sleep()

                                if(self.message.pose.position.x == self.length & self.message.pose.position.y == self.length):
                                        while ((self.message.pose.position.y != 0) & self.state == True):
                                                self.message.pose.position.y -= 1
                                                self.pub.publish(self.message)
                                                self.rate.sleep()


                                        while ((self.message.pose.position.x != 0) & self.state == True):
                                                self.message.pose.position.x -= 1
                                                self.pub.publish(self.message)
                                                self.rate.sleep()


if __name__ == '__main__':
    try:
        node=carrer()
        node.run()
    except rospy.ROSInterruptException:
        pass

