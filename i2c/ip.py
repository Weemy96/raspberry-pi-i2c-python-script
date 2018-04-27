import socket
import psutil

def find_ip_form_interface(family=socket.AF_INET):
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface!='lo', snic.address)

def get_ip():
    ipv4s = list(find_ip_form_interface())
    for r in range(len(ipv4s)):
        network_interface=ipv4s[r][0]
        if (network_interface == True):
            ip = ipv4s[r][1]
            break
        else:
            ip="Not Connection"
    return str(ip)

#print get_ip()

