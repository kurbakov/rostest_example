#!/usr/bin/env python

import unittest
import rosunit

import rospy
from std_msgs.msg import Int32

PKG = 'ros_test'


INPUT = 100
EXPECTED = 101


class CaseB(unittest.TestCase):
    def callback(self, data):
        self.assertEqual(EXPECTED, data)

    def test_runTestC(self):
        rospy.init_node('test', anonymous=False)
        rospy.Subscriber('output', Int32, self.callback)

        pub = rospy.Publisher('input', Int32, queue_size=10)
        pub.publish(INPUT)


if __name__ == '__main__':
    rosunit.unitrun(PKG, 'test_name', CaseB)
