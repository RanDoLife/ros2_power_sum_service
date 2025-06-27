#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_py_service.srv import PowerSum
import math

class PowerSumService(Node):
    def __init__(self):
        super().__init__('power_sum_server')
        self.srv = self.create_service(PowerSum, 'power_sum', self.compute_callback)
        self.get_logger().info('Service server ready.')

    def compute_callback(self, request, response):
        a = request.a
        b = request.b
        response.c = int(math.pow(2, a) + math.pow(3, b))
        self.get_logger().info(f'Received a={a}, b={b}. Returning c={response.c}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = PowerSumService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
