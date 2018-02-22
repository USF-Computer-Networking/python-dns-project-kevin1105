""" 
project1.py
Name : Kevin Kim
- Finds DNS address of domain name
- Finds the hostname of an IP address (REVERSE DNS)
- usage: python ./project1.py -a google.com
- usage: python ./project1.py -i 198.27.250.181 or 8.8.4.4
- usage: python ./project1.py -m google.com
"""

import argparse
import dns.resolver
import dns.name

def manipulateName(domainName):
    n = dns.name.from_text(domainName)
    print n.labels

def DNS(type, domainName):
    if type == "A":
        print("  Address")
    if type == "PTR":
        print("     IP")
    print("************")
    dnsresolver = dns.resolver.Resolver()
    query = dnsresolver.query(domainName, type)
    for rdata in query:
        print(rdata)

def main():
    arg = argparse.ArgumentParser()
    arg.add_argument('-a', '--address', default=False, help="Finds address of DNS records")
    arg.add_argument('-i', '--ptr', default=False, help="Finds the hostname of IP address")
    arg.add_argument('-m', '--output', default=False, help="Manipulates domain name")
    args = arg.parse_args()
    try:
        if args.address is not False:
            DNS("A", args.address)
        elif args.ptr is not False:
            DNS("PTR", '.'.join(reversed(args.ptr.split("."))) + ".in-addr.arpa")
        elif args.output is not False:
            manipulateName(args.output)
        else:
            arg.print_help()
    except:
        print("Search failed")
        
if __name__ == '__main__':
    main()
