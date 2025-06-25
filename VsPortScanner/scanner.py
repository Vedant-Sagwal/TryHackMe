import socket

def scan(ports, target):
    try:
        ip = socket.gethostbyname(target)
        print(f"[i] Resolved {target} to {ip}")
    except socket.gaierror:
        print("[-] Invalid hostname.")
        return

    print(f"[*] Scanning ports on {ip}...\n")
    
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"[+] Port {port} is OPEN")
            except Exception as ex:
                print(f"[-] Error scanning port {port}: {ex}")

if __name__ == "__main__":
    target = input("Enter IP or hostname: ").strip()
    if not target:
        print("[-] No target entered. Exiting.")
        exit()

    ports = range(1, 5000)
    scan(ports, target)

