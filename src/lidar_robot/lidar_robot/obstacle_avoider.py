import rclpy 
from geometry_msgs.msg import Twist
from rclpy.node import Node 
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

from lidar_robot.lidar_utils import sector_min

class ObstacleAvoider(Node):

    def __init__(self):
        super().__init__("obstacle_avoider")
        self.declare_parameter('stop_distance',0.7)
        self.declare_parameter('forward_speed',0.3)
        self.declare_parameter('turn_speed',0.8)
        self.pub =self.create_publisher(Twist,'/cmd_vel',10)
        self.create_subcription(
            LaserScan,'/scan',self.on_scan,qos_profile_sensor_data
        )


    def on_scan(self,scan:LaserScan):
        stop = self.get_paramenter ("stop_distance").value
        fwd = self.get_paramenter('forward_speed').value
        turn = self.get_paramenter('turn_speed').value

        front = sector_min(scan,-30.0,30.0)
        left =sector_min(scan,30.0,90.0)
        right = sector_min(scan,-90.0,-30.0)

        cmd = Twist()
        if front < stop:
            cmd.angular.z = turn if left > right else -turn
        else:
            cmd.linear.x = fwd
        self.pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node.pub.publish(Twist())
        except Exception:
            pass
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == "__main__":
    main()
