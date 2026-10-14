import math 
import rclpy 
from rclpy.node import Node 
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan 

from lidar_robot.lidar_utils import sector_min 

class LidarReader(Node):
    def __init__ (self):
        super().__init__('lidar_robot')
        self.create_subscription(
            LaserScan, '/scan', self.on_scan, qos_profile_sensor_data
        )

    def on_scan(self, scan: LaserScan):
        valid =[r for r in scan.ranges
                if math.isfinite(r) and scan.range_min <= r <= scan.range_max]
        closest=min(valid) if valid else math.inf
        front = sector_min(scan,-20.0,20.0)
        left = sector_min(scan,60.0,-60.0)
        right = sector_min(scan,-120.0 , -60.0)
        self.get_logger().info(
        f'{len(scan.ranges)} rays | closest={closest:.2f} m |'
        f'front={front:.2f} left={left:.2f} right={right:.2f}',
        throttle_duration_sec=1.0)


def main(args=None):
    rclpy.init(args=args)
    node = LidarReader()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
