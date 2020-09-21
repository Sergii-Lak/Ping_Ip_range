import subprocess
import time
from threading import Thread


def timer_decorator(func):
    def wraper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(f"{round(end-start, 2)} seconds working!")
        return f

    return wraper


class RangeIP(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip

    def run(self):
        ping_ip = subprocess.call(["ping", "-n", "1", "-w", "1", self.ip], stdout=subprocess.DEVNULL,
                                  shell=True)
        # You can also add two parameters: "- c", " 1" like this:
        # ping_ip = subprocess.call(["ping", "-n", "1", "-c", "1", "-w", "1", self.ip], stdout=subprocess.DEVNULL, shell=True)
        # This increases the speed of getting results. In my case it's 20% - 30%
        # But you must have administrative privileges

        if ping_ip == 0:
            print(f"{self.ip} is UP")
        else:
            print(f"{self.ip} is DOWN")

    @timer_decorator  # This is a decorator for measuring execution of the script. You can delete this line
    def go(self):

        thread_max = 50

        list_ping_ip = []
        start_ip = 1
        end_ip = 254

        # Also, you can used this code for input request of range IP address
        # ---------------------------
        # start_ip = int(input("The number of start IP address for ping: "))
        # end_ip = int(input("The number of end IP address for ping: "))
        # ----------------------------

        for host in range(start_ip, end_ip + 1):
            ip = self.ip + str(host)
            ip_now = RangeIP(ip)
            list_ping_ip.append(ip_now)
            ip_now.start()

            wait = 0
            if len(list_ping_ip) > thread_max: wait = 1
            if host == end_ip: wait = len(list_ping_ip)

            for reap in range(wait):
                ping_ping = list_ping_ip[0]
                list_ping_ip = list_ping_ip[1:]
                ping_ping.join()


if __name__ == "__main__":
    R = RangeIP('8.8.8.')

    # Also, you can used this code in Range_IP:
    # -------------------------------------------
    # R = Range_IP(input("Host for range ping (example: '8.8.8.') : "))
    # -------------------------------------------

    R.go()