import rclpy
from rclpy.node import Node
from my_py_service.srv import PowerSum

class PowerSumServer(Node):
    def __init__(self):
        super().__init__('power_sum_server')
        self.srv = self.create_service(PowerSum, 'power_sum', self.calculate_callback)

    def calculate_callback(self, request, response):
        a = request.a
        b = request.b
        # Вычисляем c = 2^a + 3^b
        response.c = pow(2, a) + pow(3, b)
        self.get_logger().info(f'Incoming request: a={a}, b={b} -> c={response.c}')
        return response

def main(args=None):
    rclpy.init(args=args)
    server = PowerSumServer()
    rclpy.spin(server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
