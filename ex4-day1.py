#!/usr/bin/env python
ip_adr = raw_input("Enter IP address:")
octets = ip_adr.split(".")
print "{:<12} {:<12} {:<12} {:<12}".format(octets[0],octets[1],octets[2],octets[3])
