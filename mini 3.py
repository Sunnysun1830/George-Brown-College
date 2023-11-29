import time
import paramiko
import datetime     # module work with dates and times


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
        self.__ssh_client.close()   # close SSH

    def send_shell_command(self, command):
        # shell instance variable
        self.__shell.send(command + "\n")
        time.sleep(1)
        response = self.__shell.recv(10000)
        decode = response.decode()
        return decode

    def send_exec_command(self, command, save_command=False):
        # SSH Client instance variable
        stdin, stdout, stderr = self.__ssh_client.exec_command(command + "\n")
        time.sleep(1)
        decode = stdout.read().decode()

        # mini3
        if save_command:
            current_time = datetime.datetime.now()
            # The name of the text file should be “command_DD_MONTH_YYYY-24HHOUR_MINUTE.txt”
            filename = f"{command}_{current_time.strftime('%d_%B_%Y-%H%M')}.txt"
            # d day with 2 digit
            # B full month name
            # Y year with 4 digit
            # H in 24-hour format with 2 digit
            # M minutes with 2 digit

            with open(filename, 'w') as file:
                file.write(decode)

            return decode


admin = Connector(
    host="192.168.122.1",
    user="student",
    pwd="student")

send_command1 = admin.send_shell_command("whoami")
print(send_command1)
print("_" * 20)
send_command2 = admin.send_exec_command("ls", save_command=True)
print(send_command2)
print("_" * 20)