#!/bin/bash
# script add iptables rule for PARSEC.app
echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50000 -j DNAT --to-destination 54.196.56.234  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50001 -j DNAT --to-destination 3.82.118.224   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50002 -j DNAT --to-destination 34.192.234.161 :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50003 -j DNAT --to-destination 34.225.150.153 :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50004 -j DNAT --to-destination 3.211.4.80     :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50005 -j DNAT --to-destination 18.209.3.173   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50006 -j DNAT --to-destination 54.156.171.75  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50007 -j DNAT --to-destination 54.156.206.140 :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50008 -j DNAT --to-destination 34.198.18.15   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50009 -j DNAT --to-destination 54.172.6.82    :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50010 -j DNAT --to-destination 52.72.34.199   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50011 -j DNAT --to-destination 34.225.179.58  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50012 -j DNAT --to-destination 3.225.67.142   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50013 -j DNAT --to-destination 34.192.57.180  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50014 -j DNAT --to-destination 107.20.12.118  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50015 -j DNAT --to-destination 54.145.246.46  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50016 -j DNAT --to-destination 52.21.55.64    :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50017 -j DNAT --to-destination 52.202.22.234  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50018 -j DNAT --to-destination 52.70.60.249   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50019 -j DNAT --to-destination 54.197.251.63  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50020 -j DNAT --to-destination 18.210.116.105 :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50021 -j DNAT --to-destination 18.205.230.75  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50022 -j DNAT --to-destination 52.70.151.38   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50023 -j DNAT --to-destination 34.194.73.148  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50024 -j DNAT --to-destination 3.225.68.46    :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50025 -j DNAT --to-destination 3.231.64.208   :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50026 -j DNAT --to-destination 52.72.178.249  :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50027 -j DNAT --to-destination 54.225.204.226 :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50028 -j DNAT --to-destination 3.221.88.61    :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50029 -j DNAT --to-destination 52.3.134.67    :443  	# kessel-ws.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50100 -j DNAT --to-destination 188.114.99.234 :443  	# kessel-api.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50101 -j DNAT --to-destination 188.114.98.234 :443  	# kessel-api.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50110 -j DNAT --to-destination 104.18.0.181   :443  	# builds.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50111 -j DNAT --to-destination 104.18.1.181   :443  	# builds.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50120 -j DNAT --to-destination 104.19.143.75  :443  	# builds.parsecgaming.com
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50121 -j DNAT --to-destination 104.19.140.75  :443  	# builds.parsecgaming.com
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50122 -j DNAT --to-destination 104.19.128.76  :443  	# builds.parsecgaming.com
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50123 -j DNAT --to-destination 104.19.142.75  :443  	# builds.parsecgaming.com
iptables -t nat -A PREROUTING -d 65.21.243.37 -p tcp --dport 50124 -j DNAT --to-destination 104.19.141.75  :443  	# builds.parsecgaming.com
iptables -t nat -A PREROUTING -d 65.21.243.37 -p udp --dport 50000 -j DNAT --to-destination 35.169.37.243  :3478 	# stun.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p udp --dport 50001 -j DNAT --to-destination 52.86.26.213   :3478 	# stun.parsec.app
iptables -t nat -A PREROUTING -d 65.21.243.37 -p udp --dport 50002 -j DNAT --to-destination 3.228.228.84   :3478 	# stun.parsec.app

iptables -t nat -A POSTROUTING -d 54.196.56.234   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 3.82.118.224    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 34.192.234.161  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 34.225.150.153  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 3.211.4.80      -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 18.209.3.173    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 54.156.171.75   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 54.156.206.140  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 34.198.18.15    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 54.172.6.82     -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.72.34.199    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 34.225.179.58   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 3.225.67.142    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 34.192.57.180   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 107.20.12.118   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 54.145.246.46   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.21.55.64     -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.202.22.234   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.70.60.249    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 54.197.251.63   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 18.210.116.105  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 18.205.230.75   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.70.151.38    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 34.194.73.148   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 3.225.68.46     -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 3.231.64.208    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.72.178.249   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 54.225.204.226  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 3.221.88.61     -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 52.3.134.67     -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-ws.parsec.app
iptables -t nat -A POSTROUTING -d 188.114.99.234  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-api.parsec.app
iptables -t nat -A POSTROUTING -d 188.114.98.234  -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# kessel-api.parsec.app
iptables -t nat -A POSTROUTING -d 104.18.0.181    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsec.app
iptables -t nat -A POSTROUTING -d 104.18.1.181    -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsec.app
iptables -t nat -A POSTROUTING -d 104.19.143.75   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsecgaming.com
iptables -t nat -A POSTROUTING -d 104.19.140.75   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsecgaming.com
iptables -t nat -A POSTROUTING -d 104.19.128.76   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsecgaming.com
iptables -t nat -A POSTROUTING -d 104.19.142.75   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsecgaming.com
iptables -t nat -A POSTROUTING -d 104.19.141.75   -p tcp --dport 443   -j SNAT --to-source 65.21.243.37:443  	# builds.parsecgaming.com
iptables -t nat -A POSTROUTING -d 35.169.37.243   -p udp --dport 3478  -j SNAT --to-source 65.21.243.37:3478 	# stun.parsec.app
iptables -t nat -A POSTROUTING -d 52.86.26.213    -p udp --dport 3478  -j SNAT --to-source 65.21.243.37:3478 	# stun.parsec.app
iptables -t nat -A POSTROUTING -d 3.228.228.84    -p udp --dport 3478  -j SNAT --to-source 65.21.243.37:3478 	# stun.parsec.app
