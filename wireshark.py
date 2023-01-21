import os
import subprocess
import time

def check_network():
    # Use the ping command to check if a specific host is reachable
    hostname = "8.8.8.8"
    response = os.system("ping -c 1 " + hostname)

    # Check the response code
    if response == 0:
        print(hostname, 'is up!')
        return True
    else:
        print(hostname, 'is down!')
        return False

def start_capture():
    # Start a Wireshark packet capture
    interface = "eth0"
    filename = "capture.pcap"
    capture = subprocess.Popen(["wireshark", "-i", interface, "-w", filename])
    print("Starting packet capture on interface", interface)
    return capture

def stop_capture(capture):
    # Stop the Wireshark packet capture
    capture.kill()
    print("Packet capture stopped")

def main():
    # Continuously check the network status
    while True:
        network_status = check_network()
        if not network_status:
            capture = start_capture()
            # Wait for network to come back up
            while not check_network():
                time.sleep(5)
            stop_capture(capture)

if __name__ == "__main__":
    main()
