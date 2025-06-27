#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "my_cpp_service/srv/power_sum.hpp"

using namespace std::chrono_literals;

class PowerSumClient : public rclcpp::Node
{
public:
  PowerSumClient() : Node("power_sum_client")
  {
    this->declare_parameter<int64_t>("a", 0);
    this->declare_parameter<int64_t>("b", 0);

    int64_t a = this->get_parameter("a").as_int();
    int64_t b = this->get_parameter("b").as_int();

    client_ = this->create_client<my_cpp_service::srv::PowerSum>("power_sum");

    while (!client_->wait_for_service(1s)) {
      if (!rclcpp::ok()) {
        RCLCPP_ERROR(this->get_logger(), "Client interrupted while waiting for service.");
        return;
      }
      RCLCPP_INFO(this->get_logger(), "Waiting for service to appear...");
    }

    auto request = std::make_shared<my_cpp_service::srv::PowerSum::Request>();
    request->a = a;
    request->b = b;

    auto result_future = client_->async_send_request(request,
      std::bind(&PowerSumClient::response_callback, this, std::placeholders::_1));
  }

private:
  void response_callback(rclcpp::Client<my_cpp_service::srv::PowerSum>::SharedFuture future)
  {
    auto response = future.get();
    RCLCPP_INFO(this->get_logger(), "Result: c = %ld", response->c);
    rclcpp::shutdown();
  }

  rclcpp::Client<my_cpp_service::srv::PowerSum>::SharedPtr client_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<PowerSumClient>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
