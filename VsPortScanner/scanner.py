import socket

def scan(ports, target):
    try:
        ip = socket.gethostbyname(target)
        print(f"[i] Resolved {target} to {ip}!!! YEAHHH")
    except socket.gaierror:
        print("[-] Invalid hostname you cheater.")
        return

    print(f"[*] Scanning ports on {ip}...\n")
    
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"[+] Port {port} is OPEN, Lets Go!!")
            except Exception as ex:
                print(f"[-] Error scanning port {port}: {ex}, Oh NoOO")

def syn_scan(target, port):
    ip = IP(dst=target)
    syn = TCP(dport=port, flags="S")
    response = sr1(ip/syn, timeout=1, verbose=0)

    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:  # SYN-ACK
            print(f"[+] Port {port} is OPEN (SYN-ACK received). YEAHHH!!")
        elif response[TCP].flags == 0x14:  # RST-ACK
            print(f"[-] Port {port} is CLOSED (RST received), Oh nooo")
    else:
        print(f"[?] No response from port {port}")

if __name__ == "__main__":
    target = input("Enter IP or hostname: ").strip()
    if not target:
        print("[-] Nothing Entered. Ok Bye!!")
        exit()

    ports = range(1, 5000)
    scan(ports, target)
	 scan_type = input("Choose scan type (connect/syn): ").strip().lower()

    try:
        target_ip = socket.gethostbyname(target)
        print(f"[i] Resolved {target} to {target_ip}\n")
    except socket.gaierror:
        print("[-] Invalid hostname.")
        sys.exit()

    if scan_type == "connect":
        connect_scan(ports, target_ip)
    elif scan_type == "syn":
        run_syn_scan_range(target_ip, ports)
    else:
        print("[-] Invalid scan type. Use 'connect' or 'syn'.")

