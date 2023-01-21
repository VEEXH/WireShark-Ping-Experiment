# WireShark-Ping-Experiment
## Wireshark Automation in Network Failure

This Python program is designed to automate Wireshark packet captures in the event of network failure. It uses the `ping` command to check the reachability of a specific host (8.8.8.8 in this example) and starts a Wireshark packet capture on a specified interface (eth0 in this example) if the host is not reachable. The captured packets are saved to a file named `capture.pcap` and the capture stops when the network comes back up.

## Prerequisites
- Wireshark should be installed on the machine on which you are running the program.
- Python 3 should be installed on the machine on which you are running the program.
- The user running the program should have permission to run Wireshark.
- You should have the python library `subprocess` installed, if not you can install it by running `pip install subprocess`

## Configuration
- You can modify the hostname to ping in the `check_network` function to any hostname or IP address that you want to use as a marker for network failure.
- You can modify the interface to capture in the `start_capture` function to any interface that you want to capture.
- You can modify the filename in the `start_capture` function to any name you want to give to the captured file.

## Output
- The program will continuously check the network status and start the packet capture if the network fails.
- The captured packets will be saved to a file named `capture.pcap` in the same directory where the program is run.

# Warning 
- Running Wireshark on a production environment without testing it in a lab environment is not recommended.
- Make sure you understand the impact of this program before running it.
- This is just an example and it might not work as is.
- You may have to adjust the path of the wireshark executable depending on your setup.

## How To Run
Run the program using the command `python <filename.py>`
The program will start running and check the network status continuously, It will start the packet capture if the network fails and stop it when the network comes back up.
