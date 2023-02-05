# Virtual Shell Eco-Marathon Autonomous Competition 2023
This is the codebase for the Rice Electric Vehicle autonomous subteam for the
virtual shell eco-marathon autonomous competition.

## Project Structure
- workspace
    - This folder contains all of the runnable code

- environment
    - This folder contains all of the environment setup info you'll need!
    
    
## Install and Setup carla-ros-bridge

1. Clone https://github.com/carla-simulator/ros-bridge into /home
2. Go to https://carla.readthedocs.io/projects/ros-bridge/en/latest/ros_installation_ros1/
3. Follow the "source repository" instructions
	- Create a catkin workspce: mkdir -p ~/carla-ros-bridge/catkin_ws/src
	- Clone the ROS Bridge repository and submodules: 
		cd ~/carla-ros-bridge
    		git clone --recurse-submodules https://github.com/carla-simulator/ros-bridge.git catkin_ws/src/ros-bridge
    	- Set up the ROS environment according to the ROS version you have installed (noetic in our case): 
    		source /opt/ros/noetic/setup.bash
    	- Install the required ros-dependencies:
    		cd catkin_ws
    		rosdep update
    		rosdep install --from-paths src --ignore-src -r
    	- Build the ROS bridge:
    		catkin_make
4. Run the ROS bridge
	- Go to the carla root folder: cd /opt/carla-simulator
	- ./CarlaUE4.sh
	- Add the correct CARLA modules to your Python path:
		export CARLA_ROOT=/opt/carla-simulator
		export PYTHONPATH=$PYTHONPATH:$CARLA_ROOT/PythonAPI/carla/dist/carla-0.9.13-py3.7-linux-x86_64.egg:$CARLA_ROOT/PythonAPI/carla
	- Add the source path for the ROS bridge workspace according to the installation method of the ROS bridge. This should be done in every terminal each time you want to run the ROS bridge:
		source ~/carla-ros-bridge/catkin_ws/devel/setup.bash
	- Start the ROS bridge. Use any of the different launch files available to check the installation:
    ```
    # Option 1: start the ros bridge
    roslaunch carla_ros_bridge carla_ros_bridge.launch

    # Option 2: start the ros bridge together with an example ego vehicle
    roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch
    ```
    
# CARLA Rendering options
- https://carla.readthedocs.io/en/latest/adv_rendering_options/#rendering-options
- Graphics Quality
	- Epic mode by default: ./CarlaUE4.sh -quality-level=Epic
	- Low mode (we are going to use this one): ./CarlaUE4.sh -quality-level=Low
- No-rendering mode
	- To disable and enable rendering via the command line, run the following commands:
		- cd /opt/carla-simulator/PythonAPI/util && python3 config.py --no-rendering
		- cd PythonAPI/util && python3 config.py --rendering
- Off-screen mode
	- ./CarlaUE4.sh -RenderOffScreen
