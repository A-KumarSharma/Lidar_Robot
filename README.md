# lidar_robot (ROS 2 Jazzy + Gazebo Harmonic, Python)
# Explaination
I developed a LiDAR-based mobile robot simulation using ROS 2 Jazzy and Gazebo Harmonic.

The main objective of this project was to simulate a robot that can detect obstacles and navigate its surroundings.

I used Gazebo to create the robot simulation and integrated a LiDAR sensor to collect distance measurements from the environment.

I used ROS 2 topics for communication between different components. The LiDAR publishes sensor data on the `/scan` topic, and I developed a Python-based obstacle avoidance node that processes this data and publishes velocity commands through `/cmd_vel`.

I also implemented keyboard-based teleoperation for manual robot control and used RViz2 to visualize the LiDAR data.

Through this project, I gained practical experience with ROS 2, sensor integration, robot simulation, Python programming, and autonomous obstacle avoidance.

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
