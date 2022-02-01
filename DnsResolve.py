import dns
from dns import resolver,reversename


def Dns_Resolve(domain):

    records = ['A','AAAA','CNAME','DNAME','SOA','MX','TXT','PX','NS']

    for rec in records:
        try:
            answers = dns.resolver.resolve(domain, rec)
            for rdata in answers:
                print(rec, ':', rdata.to_text())
        except Exception as e:
            print(e)  # or pass


def Reverse_Dnslookup(IP):

    addr = reversename.from_address(IP)
    hostname = str(resolver.resolve(addr,"PTR")[0])
    print(hostname)


    
ch = int(input("1- Dns Resolve\n2- Reverse Dnslookup\n\n"))

if ch == 1:
    domain = str(input("Host Name: "))
    Dns_Resolve(domain)
    
if ch == 2:
    IP = str(input("IP Address: "))
    Reverse_Dnslookup(IP)