
import ntplib
from time import time, ctime
def get_ntp_time(ntp_server):
    client = ntplib.NTPClient()
    response = client.request(ntp_server, version=3)
    ntp_time = response.tx_time
    local_time = time()
    offset = response.offset

    print(f"NTP TIME : {ctime(ntp_time)}")
    print(f"LOCAL TIME : {ctime(local_time)}")
    print(f"OFFSET TIME : {offset:.06f}")


def main():
    get_ntp_time('time.google.com')

main()