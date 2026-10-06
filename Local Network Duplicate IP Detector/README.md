# Local Network Duplicate IP Detector with Conflict Alerts

## About the Project

Local Network Duplicate IP Detector with Conflict Alerts is a Computer Networks Mini Project to detect the possible duplicate IP address in a Local Network.

This system will search the local network and retrieve the available IP and MAC address details, compare them and alert you if an IP address is found which is likely to be a duplicate.

## Technologies Used

- Python
- Scapy
- Tkinter
This protocol is used to determine the address of a server.
The local network scan is done using the Ethernet protocol.Local network scan is based on Ethernet protocol.

## Main Features

- Scans the configured local network
- Discovers active devices
- Collects IP and MAC addresses
- Checks for possible duplicate IP addresses
- Shows found devices in a graphical user interface
Displays the number of scans and conflicts.
- Issues warning if there is a potential IP conflict
- Gives a steady state if no possible conflict is identified
- Can monitor a network repeatedly

## Network Configuration

The range used for the network in the current implementation is:

`172.20.10.0/28`

## How It Works

The system detects the range of local networks configured.
Using scapy, make a ARP request.
3. Request sent as an Ethernet broadcast.
4. Active devices respond with the information of their IP and MAC address.
5. The information detected is stored in the system.
6. IP address is matched with MAC address.
7. If the same IP address has multiple different mac addresses, then it is reported as an IP conflict.
The Tkinter graphical interface will be used to display the result.

## Project Files

The graphical user interface and scan results/alerts are provided by:
scanner.py - ARP Network Scanning and Duplicate IP Detection.

## Expected Result

If there is no match for any duplicate IP address found, the system will show:

`Status: STABLE`

If a potential duplicate IP is found, the following message will appear:

In that case the status will be `Status: POSSIBLE IP CONFLICT`.

## Project

Computer Networks (24CS503)

Malnad College of Engineering, Hassan