### Visualization of Image and Point Cloud Data

image_subscriber.py uses image subscriber to get images </br>
pointcloud_subscriber/cpp uses point cloud subscriber to get point clouds </br>

compile:
```
cd /path/carla_data
catkin_make
```

run:
```
cd /path/carla_data
source devel/setup.bash
rosrun carla_data image_subscriber.py
rosrun carla_data pointcloud_subcriber
```
