#!  /home/vedantsagwaldebain/.local/share/pipx/venvs/scapy/bin/python

from scapy.all import * 

def function(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:
        print(f"ping received from {pkt[IP].src}")
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
        data = b"https://google.com"

        reply  = ip / icmp / data
        send(reply, verbose = False)
        print(f"Sent custom ICMP reply to {pkt[IP].src}")

print("Listening for ICMP Echo Requests...")
sniff(filter="icmp", prn=function)
