import socket       # Socket-Bibliothek wird verwendet, um Netzwerkkommunikation zu ermöglichen Referenz: https://docs.python.org/3/library/socket.html
import termcolor    # Termcolor-Bibliothek wird verwendet, um farbigen Text in der Konsole anzuzeigen


# Definieren der Funktion scan(targets, ports), die für das Scannen einer IP-Adresse und einer bestimmten Anzahl von Ports verantwortlich ist.
# Die Funktion verwendet eine for-Schleife, um die scan_port-Funktion für jeden Port im angegebenen Bereich aufzurufen.
def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

        
# Die Funktion scan_port nimmt eine IP-Adresse und einen Port als Parameter, 
# versucht eine Verbindung herzustellen und gibt den Port-Status aus
def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.connect((ipadress, port))
        print("[+] Port offen " + str(port))
        sock.close()
    except:
        pass

# Benutzereingabe für IP-Adressen und Anzahl der zu scannenden Ports
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Wieviele Ports willst du scannen?  "))

# Wenn mehrere IP-Adressen eingegeben wurden, werden alle nacheinander gescannt, 
# ansonsten wird das einzelne Ziel gescannt
if ',' in targets:
        print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
        for ip_addr in targets.split(',')
                scan(ip_addr.strip(' '),ports)
else: 
        scan(targets,ports)


