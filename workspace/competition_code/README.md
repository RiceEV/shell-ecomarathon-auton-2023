Example Project
===============

This contains a simple ROS catkin package meant to demonstrate the pipeline for
testing and getting results for Shell Eco-marathon simulation projects.

Requirements
------------

The software requires [Ubuntu Linux 20.04](https://ubuntu.com/download/desktop) and
[ROS Noetic](http://wiki.ros.org/noetic) to build and run.

Important considerations:
* Project submissions are compiled in a fresh Ubuntu Linux 20.04 / ROS Noetic
  environment.
* Any software dependencies must be defined properly in the
  [catkin package manifest](http://wiki.ros.org/catkin/package.xml) and will be
  installed at build time by [rosdep](http://wiki.ros.org/rosdep).
* All ROS packages must [install](http://wiki.ros.org/catkin/CMakeLists.txt#Optional_Step:_Specifying_Installable_Targets)
  themselves when built; the source code will not be present in the simulation
  environment, only installed targets.
* All project submissions **must** have a package named `shell_simulation` with a
  launch file named `shell_simulation.launch` that requires no parameters or arguments
  in order to run; this is used as the entry point for launching the project.
* Uploaded projects *must* be named `project.zip` and contain only the source
  code of ROS packages.
* The simulation will automatically end after either all goals have been reached
or after it has been running for 10 minutes.

The map and goal points will be revealed before the start of the competition.

Usage
-----

The following ROS topics are available within the simulation:


```
Published topics:
  * /carla/ego_vehicle/collision [carla_msgs/CarlaCollisionEvent]
  * /carla/ego_vehicle/depth_middle/image [sensor_msgs/Image]
  * /carla/ego_vehicle/depth_middle/camera_info [sensor_msgs/CameraInfo]
  * /carla/ego_vehicle/gnss [sensor_msgs/NavSatFix]
  * /carla/ego_vehicle/imu [sensor_msgs/Imu]
  * /carla/ego_vehicle/lane_invasion [carla_msgs/CarlaLaneInvasionEvent]
  * /carla/ego_vehicle/odometry [nav_msgs/Odometry]
  * /carla/ego_vehicle/speedometer [std_msgs/Float32]
  * /carla/ego_vehicle/rgb_front [sensor_imgs/Image]
  * /carla/ego_vehicle/vehicle_status [carla_msgs/CarlaEgoVehicleStatus]
  * /carla/ego_vehicle/vlp16_1 [sensor_msgs/PointCloud2]
  * /clock [rosgraph_msgs/Clock]
  * /rosout [rosgraph_msgs/Log] 5 publishers
  * /rosout_agg [rosgraph_msgs/Log]
  * /tf [tf2_msgs/TFMessage]

  These topics have data from sensors that can be used to observe the environment:
  * /carla/ego_vehicle/depth_middle/image [sensor_msgs/Image]
  * /carla/ego_vehicle/depth_middle/camera_info [sensor_msgs/CameraInfo]
  * /carla/ego_vehicle/gnss [sensor_msgs/NavSatFix]
  * /carla/ego_vehicle/lane_invasion [carla_msgs/CarlaLaneInvasionEvent]
  * /carla/ego_vehicle/imu [sensor_msgs/Imu]
  * /carla/ego_vehicle/odometry [nav_msgs/Odometry]
  * /carla/ego_vehicle/vlp16_1 [sensor_msgs/PointCloud2]
```

And messages can be published to this topic to control the vehicle:

```
  *  /brake_command [std_msgs/Float64]
  Valid values range from 0.0 (no brake) to 1.0 (full brake)
  *  /gear_command [std_msgs/String]
  Valid values are "forward" or "reverse"
  *  /handbrake_command [std_msgs/Bool]
  If set to "true", throttle will be ignored
  *  /steering_command [std_msgs/Float64]
  Valid values range from -1.0 (full left) to 1.0 (full right)
  *  /throttle_command [std_msgs/Float64]
  Valid values range from 0.0 (no throttle) to 1.0 (full throttle)
```
