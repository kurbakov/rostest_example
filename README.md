# rostest_example

It is an example of the test infrastructure.

We have an example node, that is subscribed to the topic ```input``` and once something is posted, it adds 1 to the message and posts the result to the topic ```output```.

We have unit tests and a component test.

The tests can be executed with the following commands:

```
rostest src/ros_test/launch/component.test
rostest src/ros_test/launch/unit.test 
```
