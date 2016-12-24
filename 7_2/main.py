import re

with open("input.txt") as file:
    ips = file.read().splitlines()

counter = 0
aba = re.compile(r'(.)(.)(?!\2)\1(?=.*\[.*\2\1\2.*\])')
abaB = re.compile(r'\].*(.)(.)(?!\2)\1.*\[(?=.*\2\1\2.*)')

for ip in ips:
    match = aba.search(ip)
    matchReverse = abaB.search(ip[::-1])
    if match is not None or matchReverse is not None:
        counter += 1

print("Number of IPs with SSL support: " + str(counter))