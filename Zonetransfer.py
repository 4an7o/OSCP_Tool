import sys
import dns as dns
import dns.resolver
import dns.zone


NS = dns.resolver.resolve(sys.argv[1], 'NS')
for nameserver in NS:
    print('NS:', nameserver.to_text())
    #ipval.to_text is the nameserver
    #find the host record on name server
    #print(nameserver.target)
    target=dns.resolver.resolve(nameserver.target,'A')
    for ip in target:
        print(str(ip))
        try:
            zone = dns.zone.from_xfr(dns.query.xfr(str(ip), sys.argv[1]))
            names = list(zone.nodes.keys())
            names.sort()
            for n in names:
                print(zone[n].to_text(n)) 
        except Exception as e:
            print( ip.to_text()+" refused zone transfer!")
            continue
    
    
