#!/usr/bin/env python


# Owned
__author__ = "Matthew De Schepper"
__email__ = "matthew.deschepper@student.kdg.be"
__status__ = "Dev"


"""
oefening met verschillende functies:
1 IP weergave (LAN en/of WAN, eth0 en of wlan0)
2 Password generator
3 system update en upgrade (linux)
4 Software installatie (linux) vb.: Apache, MariaDB, PHP,
5 system info weergave
6 netwerk en/of poortscanner
7 gpio pin weergave en hun status
8 Een functie die je zelf bedenkt en in het concept past.
"""

import sys
sys.path.insert(1, 'Hostname_IP.py')
sys.path.insert(2, 'Password_Generator.py')

from Hostname_IP import Hostname_IP
import Password_Generator


print("""Geef het nummer van de functie die je wilt gebruiken
    1 IP weergave (LAN en/of WAN, eth0 en of wlan0/)
    2 Password generator
    3 system update en upgrade (linux)
    4 Software installatie (linux) vb.: Apache, MariaDB, PHP,
    5 system info weergave
    6 netwerk en/of poortscanner
    7 gpio pin weergave en hun status
    8 Een functie die je zelf bedenkt en in het concept past.""")
functieAntwoord = input()
if functieAntwoord == "1":
    Hostname_IP()
elif functieAntwoord == "2":
    Password_Generator()
