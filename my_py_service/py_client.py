import rclpy
from rclpy.node import Node
from my_py_service.srv import PowerSum

class PowerSumClient(Node):
    def __init__(self):
        super().__init__('power_sum_client')
        self.declare_parameter('a', 0)
        self.declare_parameter('b', 0)

        self.a = self.get_parameter('a').get_parameter_value().integer_value
        self.b = self.get_parameter('b').get_parameter_value().integer_value

        self.client = self.create_client(PowerSum, 'power_sum')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.send_request()

    def send_request(self):
        request = PowerSum.Request()
        request.a = self.a
        request.b = self.b

        future = self.client.call_async(request)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Result: c = {response.c}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')
        finally:
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = PowerSumClient()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
