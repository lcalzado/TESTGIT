#Importing libreries
import re
import ipaddress

#Defining Variables
pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b' #Regular expresion to identify an Ip addresses on any string.

data = '''Forti777SVC01-2 (2) # show 
config system dhcp server
    edit 160
        set default-gateway 152.165.208.1
        set netmask 152.165.208.20
        set interface "810AN2-INT1"
        config ip-range
            edit 1
                set start-ip 152.166.208.2
                set end-ip 152.166.215.254
            next
        end
        set shared-subnet enable
        set relay-agent 152.167.208.1
        set dns-server1 152.167.208.73
    next
end
Forti777SVC01-2 (2) #
'''

ips = re.findall(pattern, data)
filtro1 = ips[0]
filtro2 = ips[1]
filtro3 = ips[2]
filtro4 = ips[3]
filtro5 = ips[4]
filtro6 = ips[5]

ip1 = ipaddress.IPv4Address(filtro1)
ip2 = ipaddress.IPv4Address(filtro2)
ip3 = ipaddress.IPv4Address(filtro3)
ip4 = ipaddress.IPv4Address(filtro4)
ip5 = ipaddress.IPv4Address(filtro5)
ip6 = ipaddress.IPv4Address(filtro6)

cantidad_ips = int(ip2) - int(ip1) + 1
cantidad_ips2 = int(ip4) - int(ip3) + 1
cantidad_ips3 = int(ip6) - int(ip5) + 1

print(cantidad_ips)
print(cantidad_ips2)
print(cantidad_ips3)
