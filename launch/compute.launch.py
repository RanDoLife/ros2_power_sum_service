from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('a', default_value='2', description='First number a'),
        DeclareLaunchArgument('b', default_value='3', description='Second number b'),

        Node(
            package='my_py_service',
            executable='py_server',
            name='server',
            output='screen'
        ),

        Node(
            package='my_py_service',
            executable='py_client',
            name='client',
            output='screen',
            parameters=[{
                'a': LaunchConfiguration('a'),
                'b': LaunchConfiguration('b'),
            }]
        ),
    ])
