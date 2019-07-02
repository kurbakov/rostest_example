#!/usr/bin/env python

import unittest
import rosunit

import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '../'))

from src.utils import add_one

PKG = 'ros_test'


class CaseA(unittest.TestCase):
    def test_runTestA(self):
        value = -1
        result = add_one(value)
        self.assertEqual(value+1, result)

    def test_runTestB(self):
        value = 999
        result = add_one(value)
        self.assertEqual(value+1, result)


if __name__ == '__main__':
    rosunit.unitrun('test_package', 'test_name', CaseA)
