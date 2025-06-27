from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    a_arg = DeclareLaunchArgument('a', default_value='2', description='First number')
    b_arg = DeclareLaunchArgument('b', default_value='3', description='Second number')

    py_server_node = Node(
        package='my_py_service',
        executable='py_server',
        name='power_sum_server',
    )

    py_client_node = Node(
        package='my_py_service',
        executable='py_client',
        name='power_sum_client',
        arguments=[
            LaunchConfiguration('a'),
            LaunchConfiguration('b')
        ],
    )

    return LaunchDescription([
        a_arg,
        b_arg,
        py_server_node,
        py_client_node,
    ])
