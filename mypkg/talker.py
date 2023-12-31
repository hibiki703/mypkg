import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

<<<<<<< HEAD
def cb(request, response):
    if request.name == "飯田響":
        response.age = 20 
    else:
        response.age = 255

    return response
 
rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
=======
class Talker():
    def __init__(self, nh):
        self.pub = nh.create_publisher(Int16, "countup", 10)
        self.n = 0
        nh.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
>>>>>>> lesson10
rclpy.spin(node)
