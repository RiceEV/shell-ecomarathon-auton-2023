## Workspace for Code
1. carla_data: a visualization for carla image and point cloud data in ros


## ROS Commands to Access Topics
- rostopic list: lists all ros topics
- rostopic echo [topic]: prints out the topic

## How to get the ego vehicle driving in ROS
- Run CARLA
- Run carla-ros-bridge with ego vehicle
- Run source ~/carla-ros-bridge/catkin_ws/devel/setup.bash
    - This will let ROS recognize the ego vehicle message types
- Run the following command:
    - rostopic pub /carla/ego_vehicle/vehicle_control_cmd carla_msgs/CarlaEgoVehicleControl "{throttle: 1.0, steer: 1.0}" -r 10
- This should make the car do donuts! You can also do more advanced control things.
