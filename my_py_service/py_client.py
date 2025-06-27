import sys
sys.path.append('/home/randolife/ros2_ws/install/my_py_service/lib/python3.8/site-packages')  # или актуальный путь

import rclpy
from rclpy.node import Node
from my_py_service.srv import PowerSum

class PowerSumClient(Node):
    def __init__(self):
        super().__init__('power_sum_client')
        self.client = self.create_client(PowerSum, 'power_sum')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Сервис не доступен, пытаемся подключиться...')
        self.req = PowerSum.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    node = PowerSumClient()

    if len(sys.argv) != 3:
        node.get_logger().error('Использование: ros2 run my_py_service py_client a b')
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    node.send_request(a, b)

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().error(f'Ошибка вызова сервиса: {e}')
            else:
                node.get_logger().info(f'Ответ сервиса: {response.c}')
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
