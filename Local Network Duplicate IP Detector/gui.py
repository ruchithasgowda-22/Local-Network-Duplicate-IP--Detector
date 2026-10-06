import tkinter as tk
from tkinter import ttk, messagebox
from scanner import scan_network, check_duplicate_ips
window = tk.Tk()
window.title("Local Network Duplicate IP Detector")
window.geometry("700x600")
tk.Label(
    window,
    text="LOCAL NETWORK DUPLICATE IP DETECTOR",
    font=("Arial", 16, "bold")
).pack(pady=15)
tk.Label(
    window,
    text="Network: 172.20.10.0/28"
).pack()
info = tk.Frame(window)
info.pack(pady=15)

devices_label = tk.Label(info, text="Devices Found: 0")
devices_label.grid(row=0, column=0, padx=20)

scans_label = tk.Label(info, text="Scans: 0")
scans_label.grid(row=0, column=1, padx=20)

conflicts_label = tk.Label(info, text="Conflicts: 0")
conflicts_label.grid(row=0, column=2, padx=20)
status = tk.Label(
    window,
    text="Status: READY",
    font=("Arial", 12, "bold")
)
status.pack(pady=5)
table = ttk.Treeview(
    window,
    columns=("IP", "MAC"),
    show="headings",
    height=8
)
table.heading("IP", text="IP Address")
table.heading("MAC", text="MAC Address")
table.column("IP", width=220)
table.column("MAC", width=350)
table.pack(pady=15)

scan_count = 0
def scan():
    global scan_count
    scan_count += 1
    devices = scan_network("172.20.10.0/28")
    conflicts = check_duplicate_ips(devices)

    for row in table.get_children():
        table.delete(row)

    for device in devices:
        table.insert(
            "",
            "end",
            values=(device["ip"], device["mac"])
        )

    devices_label.config(
        text="Devices Found: " + str(len(devices))
    )
    scans_label.config(
        text="Scans: " + str(scan_count)
    )
    conflicts_label.config(
        text="Conflicts: " + str(len(conflicts))
    )

    if conflicts:
        status.config(text="Status: POSSIBLE IP CONFLICT")
        messagebox.showwarning(
            "IP Conflict",
            "Possible IP Conflict Detected!"
        )
    else:
        status.config(text="Status: STABLE")
def clear():
    global scan_count
    scan_count = 0
    for row in table.get_children():
        table.delete(row)
    devices_label.config(text="Devices Found: 0")
    scans_label.config(text="Scans: 0")
    conflicts_label.config(text="Conflicts: 0")
    status.config(text="Status: READY")
tk.Button(
    window,
    text="START SCAN",
    command=scan,
    padx=20,
    pady=8
).pack(pady=5)
tk.Button(
    window,
    text="CLEAR",
    command=clear,
    padx=30,
    pady=5
).pack()
window.mainloop()