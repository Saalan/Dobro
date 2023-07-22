#!/bin/bash
/var/www/dobro/venv/bin/python /var/www/dobro/bin/parsec_db2cfg.py >/dev/null 2>&1
/etc/iptables/iptables_rule.sh