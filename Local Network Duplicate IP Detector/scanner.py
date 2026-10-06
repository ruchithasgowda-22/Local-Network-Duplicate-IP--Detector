from scapy.all import ARP, Ether, srp
import time
def scan_network(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=False)[0]
    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices

def check_duplicate_ips(devices):
    ip_data = {}

    for device in devices:
        ip = device["ip"]
        mac = device["mac"]

        if ip not in ip_data:
            ip_data[ip] = []

        if mac not in ip_data[ip]:
            ip_data[ip].append(mac)

    conflicts = []

    for ip in ip_data:
        if len(ip_data[ip]) > 1:
            conflicts.append(ip)

    return conflicts


network = "172.20.10.0/28"
print("LOCAL NETWORK DUPLICATE IP DETECTOR")
print("=" * 40)
print("\nDiscovered Devices")
print("------------------")
devices = scan_network(network)

for device in devices:
    print("IP:", device["ip"], "MAC:", device["mac"])

print("\nDevices Found:", len(devices))

print("\nStarting 5-Scan Monitoring")
print("=" * 40)

total_conflicts = 0
last_devices = devices

for scan in range(1, 6):

    print("\nScan", scan)
    print("-" * 20)

    devices = scan_network(network)
    last_devices = devices

    for device in devices:
        print("IP:", device["ip"], "MAC:", device["mac"])

    conflicts = check_duplicate_ips(devices)

    if conflicts:
        print("Possible IP Conflict:", ", ".join(conflicts))
        total_conflicts += len(conflicts)
    else:
        print("No possible duplicate IP detected.")

    if scan < 5:
        print("Waiting 5 seconds...")
        time.sleep(5)

print("\n" + "=" * 40)
print("NETWORK MONITORING SUMMARY")
print("=" * 40)
print("Devices monitored :", len(last_devices))
print("Scans performed   : 5")
print("Conflicts detected:", total_conflicts)

if total_conflicts == 0:
    print("Network status    : STABLE")
else:
    print("Network status    : POSSIBLE IP CONFLICT")

print("=" * 40)
print("Monitoring completed.")