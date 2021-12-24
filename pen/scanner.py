import nmap

scanner = nmap.PortScanner()

print(
    "Welcome, is a NMAP automation tool"
)
print(
    "<------------------------------------------------------------------------>"
)


ip_addr = input(
    "Enter IP Address :- "
)

print(
    "The IP you entered is :-", ip_addr
)
type(ip_addr)

resp = input(
    "\nPlease enter the type of scan you want to run :-\n1. SYN ACK Scan\n2. UDP SCAN\n3. Comprehensive Scan\n\nRun scan :- "
)

print(
    "You have selected option :-", resp
)

if resp == "1":
    print(
        "\nNMAP version ", scanner.nmap_version()
    )

    print(
        "\n"
    )

    scanner.scan(
        ip_addr,
        '1-1024',
        '-v -sS'
    )

    print(
        scanner.scaninfo()
    )

    print(
        "IP status :-", scanner[ip_addr].state()
    )

    print(
        scanner[ip_addr].all_protocols()
    )

    print(
        "Open ports :-", scanner[ip_addr]
    )



if resp == "2":
    print(
        "\nNMAP version ", scanner.nmap_version()
    )

    print(
        "\n"
    )

    scanner.scan(
        ip_addr,
        '1-1024',
        '-v -sU'
    )

    print(
        scanner.scaninfo()
    )

    print(
        "IP status :-", scanner[ip_addr].state()
    )

    print(
        scanner[ip_addr].all_protocols()
    )

    print(
        "Open ports :-", scanner[ip_addr]['udp'].keys()
    )



if resp == "3":
    print(
        "\nNMAP version ", scanner.nmap_version()
    )

    print(
        "\n"
    )

    scanner.scan(
        ip_addr,
        '1-1024',
        '-v -sS -sV -sC -A -O'
    )

    print(
        scanner.scaninfo()
    )

    print(
        "IP status :-", scanner[ip_addr].state()
    )

    print(
        scanner[ip_addr].all_protocols()
    )

    print(
        "Open ports :-", scanner[ip_addr]
    )
