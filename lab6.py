import time
import paramiko


class Connector:
    def __init__(self, host, user, pwd, port=22):
        self.__host = host
        self.__user = user
        self.__pwd = pwd
        self.__port = port

        self.__ssh_client = paramiko.SSHClient()
        self.__ssh_client.set_missing_host_key_policy((paramiko.AutoAddPolicy()))
        self.__ssh_client.connect(hostname=host, username=user, password=pwd, port=port)

        self.__shell = self.__ssh_client.invoke_shell()

    def __del__(self):  # destructor, called when class is no longer in used
        self.__ssh_client.close()  # close SSH

    # lab6 week9
    def send_shell_command(self, command, user_input=None):
        # shell instance variable
        self.__shell.send(command + "\n")
        time.sleep(1)
        response = self.__shell.recv(10000)
        decode = response.decode()

        # user input if length is greater than 0
        if user_input and len(user_input) > 0:
            self.__shell.send(user_input + '\n')
            time.sleep(1)
            response = self.__shell.recv(10000)
            decode += response.decode()

        return decode

    def send_exec_command(self, command):
        # SSH Client instance variable
        stdin, stdout, stderr = self.__ssh_client.exec_command(command + "\n")
        time.sleep(1)
        return stdout.read().decode()


admin = Connector(
    host="192.168.122.1",
    user="student",
    pwd="student")

send_command1 = admin.send_shell_command("whoami", user_input="ls")
print(send_command1)
print("_" * 20)
