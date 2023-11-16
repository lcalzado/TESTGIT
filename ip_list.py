#Importing libreries
import re

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
print(ips)