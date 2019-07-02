#!/usr/bin/env python

import unittest
import rosunit

import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '../'))

from src.utils import add_one

PKG = 'ros_test'


class CaseB(unittest.TestCase):
    def test_runTestC(self):
        value = 0
        result = add_one(value)
        self.assertEqual(value+1, result)

    def test_runTestD(self):
        value = -0
        result = add_one(value)
        self.assertEqual(value+1, result)


if __name__ == '__main__':
    rosunit.unitrun('test_package', 'test_name', CaseB)
