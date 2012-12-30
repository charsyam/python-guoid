import socket, os
import time

if os.name != "nt":
    import fcntl
    import struct

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, 
                            struct.pack('256s', ifname[:15]))[20:24])

def get_local_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

def get_timestamp():
    now = int((time.time()) * 1000)
    return now

def til_next_millis(last):
    timestamp = get_timestamp()
    while (timestamp <= last):
        timestamp = get_timestamp()

    return timestamp

def guoid_hash(string):
    h = 0

    for s in string:
        h = ord(s) + h * 127

    return h

def guoid_hex(n):
    x = (n % 16)
    c = ""
    if (x < 10):
        c = x
    if (x == 10):
        c = "a"
    if (x == 11):
        c = "b"
    if (x == 12):
        c = "c"
    if (x == 13):
        c = "d"
    if (x == 14):
        c = "e"
    if (x == 15):
        c = "f"

    if (n - x != 0):
        return guoid_hex(n / 16) + str(c)
    else:
        return str(c)

