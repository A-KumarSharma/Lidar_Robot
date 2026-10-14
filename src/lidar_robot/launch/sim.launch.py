import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg = get_package_share_directory('lidar_robot')
    ros_gz_sim = get_package_share_directory('ros_gz_sim')
    world = os.path.join(pkg, 'worlds','lidar_world.sdf')


    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim,'launch','gz_sim.launch.py'))
        launch_arguments={'gz_args': f'-r{world}',
                          'on_exit_shutdown': 'true'}.items())



    bridge = Node(
        package='ros_gz_bridge',
        excutable = 'parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/twist]gz.msgs.twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.pose_V',
            '/clock@rosgraph_msgs/msg/clock[gz.msg.Clock',
        ],
        output='screen')

    static_tf =Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['--x','0.1','--y','0','--z','0.07',
                   '--frame-id','base_link','--child-frame-id','lidar_link'],
        parameters=[{'use_sim_time':True}])

    reader = Node(
        package='lidar_robot',
        excutable='lidar_reader',
        parameters=[{'use_sim_time':True}],
        output='screen')

    return LaunchDescription([gz_sim,bridge,static_tf,reader])
