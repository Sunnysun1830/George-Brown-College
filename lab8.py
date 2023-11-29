# connect
import netmiko
net = netmiko.ConnectHandler(host="192.168.122.10", username="u1",
                             password="cisco", device_type="cisco_ios",
                             port=22, secret="cisco")

commands = ['enable', "config t", "username november password HelloWorld!",
            'end', "wr"]

output = net.send_config_set(commands)
# print(output)
print(output)
net.disconnect()