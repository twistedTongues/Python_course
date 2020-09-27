import re
import os
project_folder = os.path.abspath(".")
print(project_folder)
fp = open('/Users/•••••••/downloads/access.log.txt', 'r')
print('Loading...')
lines = 0
for line in fp:
    lines += 1
print('Loading...')
print("Number of requests: " + str(lines))
rp = '/Users/•••••••/downloads/access.log.txt'
with open(rp) as f:
    text = f.read()
    ip = re.findall(r"[0-9]+(?:\.[0-9]+){3}", text)
    ip_set = set(ip)
    print("Number of unique ip: " + str(len(ip_set)))
    brw_firefox = re.findall(r"Firefox", text)
    print("Number of requests from Firefox: " + str(len(brw_firefox)))
    brw_chrome = re.findall(r"Chrome", text)
    print("Number of requests from Chrome: " + str(len(brw_chrome)))
    brw_safari = re.findall(r"Safari", text)
    print("Number of requests from Safari: " + str(len(brw_safari)))
    brw_edge = re.findall(r"Edge", text)
    print("Number of requests from Edge: " + str(len(brw_edge)))
    brw_ie = re.findall(r"Internet Explorer", text)
    print("Number of requests from Internet Explorer: " + str(len(brw_ie)))
    brw_viv = re.findall(r"Vivaldi", text)
    print("Number of requests from Vivaldi: " + str(len(brw_viv)))
    brw_gnu = re.findall(r"GNU IceCat", text)
    print("Number of requests from GNU IceCat: " + str(len(brw_gnu)))
    brw_ya = re.findall(r"Yandex Browser", text)
    print("Number of requests from Yandex Browser: " + str(len(brw_ya)))
    brw_tor = re.findall(r"Tor", text)
    print("Number of requests from Tor: " + str(len(brw_tor)))
    brw_op = re.findall(r"Opera", text)
    print("Number of requests from Opera: " + str(len(brw_tor)))
