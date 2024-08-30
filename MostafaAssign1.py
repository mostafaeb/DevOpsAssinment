import subprocess
import sys
import re

def get_packet_loss(ip):
    try:
        # Execute the ping command
        output = subprocess.check_output(["ping", "-c", "4", ip], universal_newlines=True)

        # Extract packet loss using regex
        packet_loss = re.search(r'(\d+)% packet loss', output)

        if packet_loss:
            return int(packet_loss.group(1))
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def main(ips):
    for ip in ips:
        loss = get_packet_loss(ip)
        if loss is not None:
            print(f"For the IP address {ip}, the rate of packet loss is: {loss}%")
        else:
            print(f"For the IP address {ip}, the Destination Host/Net is Unreachable! or we have packet loss.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Enter the IP address(es) like: \"python3 script.py 1.1.1.1 ...\"")
    else:
        main(sys.argv[1:])
