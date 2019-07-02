cmake_minimum_required(VERSION 2.8.3)
project(ros_test)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_add_nosetests(
    test/unit_tests1.py
    test/unit_tests2.py
    test/component_test.py
)
