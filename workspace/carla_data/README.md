### Visualization of Image and Point Cloud Data

image_subscriber.py uses image subscriber to get images </br>
pointcloud_subscriber/cpp uses point cloud subscriber to get point clouds </br>

Compile:
```
cd /path/carla_data
catkin_make
```

Run (need to start ROS bridge first):
```
cd /path/carla_data
source devel/setup.bash
# Visualize images in opencv
rosrun carla_data image_subscriber.py 
# Visualize pointclouds in rviz
rosrun carla_data pointcloud_subscriber
# Open rviz
rviz
```
