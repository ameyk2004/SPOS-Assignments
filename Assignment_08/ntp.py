import ntplib
from time import time,ctime

def get_ntp_time(ntp_server = "time.google.com"):
    client = ntplib.NTPClient()
    response = client.request(ntp_server,version=3)
    ntp_time = response.tx_time
    local_time = time()
    offset = response.offset
    print(f"NTP Server Time: {ctime(ntp_time)}")
    print(f"Local System Time: {ctime(local_time)}")
    print(f"Clock Offset: {offset:.6f} seconds")

    return ntp_time, offset

def main():
    ntp_time, offset = get_ntp_time()
    print(f"Adjusting local time by {offset:.6f} seconds (for simulation)")

main()

# NTP PROTOCOL
# NETWORK LAYER PROTOCOL