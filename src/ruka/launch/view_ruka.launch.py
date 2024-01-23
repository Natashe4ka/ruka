# import os
# import yaml

# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument
# from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution

# from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
# from ament_index_python.packages import get_package_share_directory


# def load_file(package_name, file_path):
#     package_path = get_package_share_directory(package_name)
#     absolute_file_path = os.path.join(package_path, file_path)

#     try:
#         with open(absolute_file_path, 'r') as file:
#             return file.read()
#     except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
#         return None

# def load_yaml(package_name, file_path):
#     package_path = get_package_share_directory(package_name)
#     absolute_file_path = os.path.join(package_path, file_path)

#     try:
#         with open(absolute_file_path, 'r') as file:
#             return yaml.safe_load(file)
#     except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
#         return None




# def generate_launch_description():
#     # Declare arguments


#     declared_arguments = []
#     declared_arguments.append(
#         DeclareLaunchArgument(
#             "gui",
#             default_value="true",
#             description="Start Rviz2 and Joint State Publisher gui automatically \
#         with this launch file.",
#         )
#     )
#     # Initialize Arguments
#     #gui = LaunchConfiguration("gui")

#     robot_description_content = Command(
#         [
#             PathJoinSubstitution([FindExecutable(name="xacro")]),
#             " ",
#             PathJoinSubstitution(
#                 [
#                     FindPackageShare("ruka"),
#                     "config",
#                     "ruka.urdf.xacro",
#                 ]
#             ),
#         ]
#     )
#     robot_description = {"robot_description": robot_description_content}

#     robot_description_semantic_config = load_file('ruka', 'config/ruka.srdf')
#     robot_description_semantic = {'robot_description_semantic' : robot_description_semantic_config}



#     rviz_config_file = PathJoinSubstitution(
#         [FindPackageShare("ruka"), "config", "moveit.rviz"]
#     )

#     joint_state_publisher_node = Node(
#         package="joint_state_publisher_gui",
#         executable="joint_state_publisher_gui",
#     )
#     robot_state_publisher_node = Node(
#         package="robot_state_publisher",
#         executable="robot_state_publisher",
#         output="both",
#         parameters=[robot_description],
#     )
#     rviz_node = Node(
#         package="rviz2",
#         executable="rviz2",
#         name="rviz2",
#         output="log",
#         arguments=["-d", rviz_config_file, robot_description_semantic],
        
#     )

#     nodes = [
#         joint_state_publisher_node,
#         robot_state_publisher_node,
#         rviz_node,
#     ]

#     return LaunchDescription(declared_arguments + nodes)





# from launch_ros.actions import Node
# from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
# from launch_ros.substitutions import FindPackageShare
# from launch.actions import RegisterEventHandler
# from launch.event_handlers import OnProcessExit
# from launch import LaunchDescription
# from moveit_configs_utils import MoveItConfigsBuilder
# from moveit_configs_utils.launches import generate_demo_launch


# def generate_launch_description():
#     moveit_config = MoveItConfigsBuilder("ruka", package_name="ruka").to_moveit_configs()
#     robot_description_content = Command(
#         [
#             PathJoinSubstitution([FindExecutable(name="xacro")]),
#             " ",
#             PathJoinSubstitution(
#                 [
#                     FindPackageShare("ruka"),
#                     "config",
#                     "ruka.urdf.xacro",
#                 ]
#             ),
#         ]
#     )
#     robot_description = {"robot_description": robot_description_content}

#     robot_controllers = PathJoinSubstitution(
#         [
#             FindPackageShare("ruka"),
#             "config",
#             "ros2_controllers.yaml",
#         ]
#     )

#     control_node = Node(
#         package="controller_manager",
#         executable="ros2_control_node",
#         parameters=[robot_description, robot_controllers],
#         # remappings=[
#         #     (
#         #         "/forward_position_controller/commands",
#         #         "/position_commands",
#         #     ),
#         # ],
#         output="both",
#     )

#     joint_state_broadcaster_spawner = Node(
#         package="controller_manager",
#         executable="spawner",
#         arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
#     )

#     robot_controller_spawner = Node(
#         package="controller_manager",
#         executable="spawner",
#         arguments=["ruka_arm_controller", "-c", "/controller_manager"],
#     )

#     # # Delay rviz start after `joint_state_broadcaster`
#     # delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
#     #     event_handler=OnProcessExit(
#     #         target_action=joint_state_broadcaster_spawner,
            
#     #     )
#     # )

#     # Delay start of robot_controller after `joint_state_broadcaster`
#     delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = RegisterEventHandler(
#         event_handler=OnProcessExit(
#             target_action=joint_state_broadcaster_spawner,
#             on_exit=[robot_controller_spawner],
#         )
#     )

#     q= generate_demo_launch(moveit_config)



#     return LaunchDescription([q , control_node, joint_state_broadcaster_spawner, robot_controller_spawner])


# import os
# import yaml
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument
# from launch.conditions import IfCondition
# from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
# from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare

# from ament_index_python.packages import get_package_share_directory

# def load_file(package_name, file_path):
#     package_path = get_package_share_directory(package_name)
#     absolute_file_path = os.path.join(package_path, file_path)

#     try:
#         with open(absolute_file_path, 'r') as file:
#             return file.read()
#     except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
#         return None

# def load_yaml(package_name, file_path):
#     package_path = get_package_share_directory(package_name)
#     absolute_file_path = os.path.join(package_path, file_path)

#     try:
#         with open(absolute_file_path, 'r') as file:
#             return yaml.safe_load(file)
#     except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
#         return None


# def generate_launch_description():
#     # Declare arguments

#     declared_arguments = []
#     declared_arguments.append(
#         DeclareLaunchArgument(
#             "gui",
#             default_value="true",
#             description="Start Rviz2 and Joint State Publisher gui automatically \
#         with this launch file.",
#         )
#     )
#     # Initialize Arguments
#     gui = LaunchConfiguration("gui")

#     # Get URDF via xacro
#     robot_description_content = Command(
#         [
#             PathJoinSubstitution([FindExecutable(name="xacro")]),
#             " ",
#             PathJoinSubstitution(
#                 [
#                     FindPackageShare("ruka"),
#                     "config",
#                     "ruka.urdf.xacro",
#                 ]
#             ),
#         ]
#     )
#     robot_description = {"robot_description": robot_description_content}

#     robot_description_semantic_config = load_file('ruka', 'config/ruka.srdf')
#     robot_description_semantic = {'robot_description_semantic' : robot_description_semantic_config}

#     rviz_config_file = PathJoinSubstitution(
#         [FindPackageShare("ruka"), "config", "view.rviz"]
#     )

#     joint_state_publisher_node = Node(
#         package="joint_state_publisher_gui",
#         executable="joint_state_publisher_gui",
#         condition=IfCondition(gui),
#     )

#     robot_state_publisher_node = Node(
#         package="robot_state_publisher",
#         executable="robot_state_publisher",
#         output="both",
#         parameters=[robot_description],
#     )
#     rviz_node = Node(
#         package="rviz2",
#         executable="rviz2",
#         name="rviz2",
#         output="log",
#         arguments=["-d", rviz_config_file],
#         parameters=[robot_description,
#                                  robot_description_semantic],
#         condition=IfCondition(gui),
#     )
#     #
#     nodes_to_start = [
#         joint_state_publisher_node,
#         robot_state_publisher_node,
#         rviz_node,
#     ]

#     return LaunchDescription(declared_arguments + nodes_to_start)

##################################################################################################################
##################################################################################################################

##################################################################################################################

##################################################################################################################
import os
import yaml
from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
def load_file(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path, 'r') as file:
            return file.read()
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        return None

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path, 'r') as file:
            return yaml.safe_load(file)
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        return None



def generate_launch_description():
    # Get URDF via xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("ruka"),
                    "config",
                    "ruka.urdf.xacro",
                ]
            ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}


    robot_description_semantic_config = load_file('ruka', 'config/ruka.srdf')
    robot_description_semantic = {'robot_description_semantic' : robot_description_semantic_config}
    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare("ruka"),
            "config",
            "ros2_controllers.yaml",
        ]
    )
    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("ruka"), "config", "moveit.rviz"]
    )

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, robot_controllers],
     
        output="both",
    )
    robot_state_pub_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description],
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
        parameters=[robot_description,
                                 robot_description_semantic],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["ruka_arm_controller", "-c", "/controller_manager"],
    )

    # Delay rviz start after `joint_state_broadcaster`
    delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[rviz_node],
        )
    )

    # Delay start of robot_controller after `joint_state_broadcaster`
    delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[robot_controller_spawner],
        )
    )

    nodes = [
        control_node,
        robot_state_pub_node,
        joint_state_broadcaster_spawner,
        delay_rviz_after_joint_state_broadcaster_spawner,
        delay_robot_controller_spawner_after_joint_state_broadcaster_spawner,
    ]

    return LaunchDescription(nodes)