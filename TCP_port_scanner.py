import argparse
import socket

parser = argparse.ArgumentParser(description='Port scanner tcp')

parser.add_argument('-i', '--ip', help='IPv4 target', required=True)
parser.add_argument('-s', '--start', help='Starting port', type=int, required=True)
parser.add_argument('-e', '--end', help='Ending port', type=int, required=True)

args = parser.parse_args()

target = args.ip
start_port = args.start
end_port = args.end

open_ports = []

print('---------------------------------------------')
print('---------------- Scanning... ----------------')
print('---------------------------------------------')

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    try:
        print(f'Trying {port} port...')
        s.connect((target, port))
        print(f'Port {port} is open!!!')
        open_ports.append(str(port))
        banner = s.recv(1024)
        if banner:
            print(f'Service: {banner.decode("utf-8").strip()}')
        s.close()
    except:
        pass

print('---------------------------------------------')
print('------------- Scanner Complete --------------')
print('---------------------------------------------')
if open_ports:
    print(f'All open ports: {", ".join(open_ports)}')
else:
    print('No open port found')
