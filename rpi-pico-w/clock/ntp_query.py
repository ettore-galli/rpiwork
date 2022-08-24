# Query NTP server for time
#
# Freely inpired by (i.e. shamelessly copied from):
# https://www.mattcrampton.com/blog/query_an_ntp_ser
#
# Reference for reading buffer:
# https://www.sciencedirect.com/topics/computer-science/network-time-protocol


from socket import AF_INET, SOCK_DGRAM

import socket
import struct, time


def get_ntp_time(host="pool.ntp.org", port=123, buf=1024, gmt_offset_h=0):

    addr = socket.getaddrinfo(host, port, 0, SOCK_DGRAM)[0][-1]

    msg = "\x1b" + 47 * "\0"

    # reference time (in seconds since 1900-01-0
    TIME1970 = 2208988800  # 1970-01-01 00:00:00

    # connect to server
    client = socket.socket(AF_INET, SOCK_DGRAM)
    client.connect(addr)

    client.sendto(msg.encode("utf-8"), addr)

    msg, address = client.recvfrom(buf)

    t = struct.unpack("!40bI4b", msg)[40]

    t -= TIME1970

    return time.gmtime(t + gmt_offset_h * 3600)
