#include <memory>
#include <cmath>
#include "rclcpp/rclcpp.hpp"
#include "my_cpp_service/srv/power_sum.hpp"

using PowerSum = my_cpp_service::srv::PowerSum;
using std::placeholders::_1;
using std::placeholders::_2;

class PowerSumServer : public rclcpp::Node
{
public:
  PowerSumServer() : Node("power_sum_server")
  {
    service_ = this->create_service<PowerSum>(
      "power_sum",
      std::bind(&PowerSumServer::handle_service, this, _1, _2));
    RCLCPP_INFO(this->get_logger(), "Service server ready.");
  }

private:
  void handle_service(
    const std::shared_ptr<PowerSum::Request> request,
    std::shared_ptr<PowerSum::Response> response)
  {
    int64_t a = request->a;
    int64_t b = request->b;
    int64_t c = static_cast<int64_t>(std::pow(2, a)) + static_cast<int64_t>(std::pow(3, b));
    response->c = c;

    RCLCPP_INFO(this->get_logger(), "Received a=%ld, b=%ld. Returning c=2^a + 3^b = %ld", a, b, c);
  }

  rclcpp::Service<PowerSum>::SharedPtr service_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<PowerSumServer>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
