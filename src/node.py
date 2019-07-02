#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

from utils import add_one


class Node:
    def __init__(self):
        self.throttling_publisher = rospy.Publisher('output', Int32, queue_size=10)

    def callback(self, data):
        result = add_one(data)
        self.throttling_publisher.publish(result)

    def run(self):
        rospy.init_node('node', anonymous=False)
        rospy.Subscriber('input', Int32, self.callback)
        rospy.spin()


if __name__ == '__main__':
    package = Node()
    package.run()