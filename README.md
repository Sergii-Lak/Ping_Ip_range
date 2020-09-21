# Ping_Ip_range

Ping a large number of IP addresses in a few seconds.
The following modules are used: threading, subprocess, time (for the time measurement)


# USAGE:

- An important element is the variable "thread_max" - the number of threads.
It is 50 by default. But you can try increasing or decreasing the value to get faster results.

- You can also add two parameters: "- c", " 1" in the variable "ping_ip", like this:

<b>ping_ip = subprocess.call(["ping", "-n", "1", "-w", "1000", self.ip], stdout=subprocess.DEVNULL, shell=True)</b><br>

This increases the speed of getting results. In my case it's 20% - 30%. But you must have administrative privileges.

- There is also a time measurement using the decorator function:

<b>timer_decorator(func):</b><br>
    
