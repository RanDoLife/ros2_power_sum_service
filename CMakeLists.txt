cmake_minimum_required(VERSION 3.5)
project(my_cpp_service)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rosidl_default_generators REQUIRED)   # для генерации srv
find_package(example_interfaces REQUIRED)

# Генерация интерфейсов для srv
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/PowerSum.srv"
)

# Экспортируем зависимости для генераторов
ament_export_dependencies(rosidl_default_runtime)

# Теперь находим пакеты, которые понадобятся для сборки нод
find_package(rosidl_default_runtime REQUIRED)

# Добавляем исполняемые файлы сервера и клиента
add_executable(server src/server.cpp)
ament_target_dependencies(server rclcpp)
rosidl_target_interfaces(server ${PROJECT_NAME} "rosidl_typesupport_cpp")

add_executable(client src/client.cpp)
ament_target_dependencies(client rclcpp)
rosidl_target_interfaces(client ${PROJECT_NAME} "rosidl_typesupport_cpp")

# Установка исполняемых файлов
install(TARGETS
  server
  client
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Устанавливаем launch-файлы
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
