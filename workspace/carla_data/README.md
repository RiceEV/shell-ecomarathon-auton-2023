### Visualization of Image and Point Cloud Data

image_subscriber.py uses image subscriber to get images </br>
pointcloud_subscriber/cpp uses point cloud subscriber to get point clouds </br>

compile:
```
cd /path/carla_data
catkin_make
```

run (need to start ROS bridge first):
```
cd /path/carla_data
source devel/setup.bash
# visualize images in opencv
rosrun carla_data image_subscriber.py 
# visualize pointclouds in rviz
rosrun carla_data pointcloud_subscriber
```
