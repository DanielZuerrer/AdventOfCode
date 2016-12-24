import re

with open("input.txt") as file:
    ips = file.read().splitlines()

counter = 0
abba = re.compile(r'(.)(.)\2(?!\2)\1(?![^[]*\])')
bracketsAbba = re.compile(r'(.)(.)\2(?!\2)\1(?=[^[]*\])')
for ip in ips:
    match = abba.search(ip)
    inBrackets = bracketsAbba.search(ip)
    if match is not None and inBrackets is None:
        counter += 1

print("Number of IPs with TLS support: " + str(counter))