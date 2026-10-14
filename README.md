# lidar_robot (ROS 2 Jazzy + Gazebo Harmonic, Python)

## Install
    sudo apt install ros-jazzy-ros-gz ros-jazzy-teleop-twist-keyboard

## Build
    mkdir -p ~/ros2_ws/src && cp -r lidar_robot ~/ros2_ws/src/
    cd ~/ros2_ws && colcon build --packages-select lidar_robot
    source install/setup.bash

## Run
    ros2 launch lidar_robot sim.launch.py     # Gazebo + bridge + lidar_reader


## Demo Video


https://github.com/user-attachments/assets/cecedd5c-fe6a-40d2-afb0-71be04ecaee5




## cmds

Drive it (new terminal, source the workspace):
    ros2 run teleop_twist_keyboard teleop_twist_keyboard

Or autonomous obstacle avoidance:
    ros2 run lidar_robot obstacle_avoider --ros-args -p use_sim_time:=true

Visualize: `rviz2` -> Fixed Frame `odom` -> Add -> LaserScan, topic `/scan`
(QoS Reliability: Best Effort).

## Topics
/cmd_vel (ROS->Gz) | /odom, /scan, /tf, /clock (Gz->ROS)

## Troubleshooting
No /scan data on a VM / no GPU: `export LIBGL_ALWAYS_SOFTWARE=1` before launching.
