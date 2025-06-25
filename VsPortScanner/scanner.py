import socket

def scan(ports, target) :
    print(f"Scanning ports of {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"(+) port {port} is open")
        except exception as ex:
            print(f"(-) error in scanning {port} port")
        finally:
            sock.close()

if __name__ == "__main__":
    target = input("Enter ip or target name : ")
    ports = range(1, 5000)
    scan(ports, target);
