from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    a_arg = DeclareLaunchArgument('a', default_value='2', description='First number a')
    b_arg = DeclareLaunchArgument('b', default_value='3', description='Second number b')

    a = LaunchConfiguration('a')
    b = LaunchConfiguration('b')

    server_node = Node(
        package='my_cpp_service',
        executable='server',
        output='screen'
    )

    client_node = Node(
        package='my_cpp_service',
        executable='client',
        output='screen',
        parameters=[{'a': a, 'b': b}]  # <- Вот это передаёт параметры клиенту
    )

    return LaunchDescription([
        a_arg,
        b_arg,
        server_node,
        client_node
    ])
