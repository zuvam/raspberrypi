#!/usr/bin/env bash

exit

sudo apt-get update
sudo apt-get install hostapd isc-dhcp-server lshw

sudo cat >/etc/dhcp/dhcpd.conf <<EOC1
#
# Modified configuration file for ISC dhcpd for Debian
#
# The ddns-updates-style parameter controls whether or not the server will
# attempt to do a DNS update when a lease is confirmed. We default to the
# behavior of the version 2 packages ('none', since DHCP v2 didn't
# have support for DDNS.)
ddns-update-style none;

default-lease-time 600;
max-lease-time 7200;

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.
authoritative;

# Use this to send dhcp log messages to a different log file (you also
# have to hack syslog.conf to complete the redirection).
log-facility local7;

subnet 192.168.42.0 netmask 255.255.255.0 {
	range 192.168.42.10 192.168.42.50;
	option broadcast-address 192.168.42.255;
	option routers 192.168.42.1;
	default-lease-time 600;
	max-lease-time 7200;
	option domain-name "local";
	option domain-name-servers 8.8.8.8, 8.8.4.4;
}
EOC1

sudo cat >/etc/network/interfaces <<EOC2
auto lo
iface lo inet loopback

auto eth0
allow-hotplug eth0
iface eth0 inet manual

iface wlan0 inet static
  address 192.168.42.1
  netmask 255.255.255.0

# auto wlan0
# allow-hotplug wlan0
# iface wlan0 inet manual
# wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
EOC2

# sudo lshw -C network
# driver=rt2800usb
sudo cat >/etc/hostapd/hostapd.conf <<EOC3
interface=wlan0
driver=rtl8192cu
ssid=pi_borg
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=zuvaspiborg
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOC3

sudo cat >/etc/default/hostapd <<EOC4
# Defaults for hostapd initscript
#
# See /usr/share/doc/hostapd/README.Debian for information about alternative
# methods of managing hostapd.
#
# Uncomment and set DAEMON_CONF to the absolute path of a hostapd configuration
# file and hostapd will be started during system boot. An example configuration
# file can be found at /usr/share/doc/hostapd/examples/hostapd.conf.gz
#
DAEMON_CONF="/etc/hostapd/hostapd.conf"

# Additional daemon options to be appended to hostapd command:-
# 	-d   show more debug messages (-dd for even more)
# 	-K   include key data in debug messages
# 	-t   include timestamps in some debug messages
#
# Note that -B (daemon mode) and -P (pidfile) options are automatically
# configured by the init.d script and must not be added to DAEMON_OPTS.
#
#DAEMON_OPTS=""
EOC4

sudo cat>>/etc/sysctl.conf <<EOC5
# ipv4 router
net.ipv4.ip_forward=1
EOC5

sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

sudo cat>>/etc/network/interfaces <<EOC6

up iptables-restore < /etc/iptables.ipv4.nat
EOC6

wget http://adafruit-download.s3.amazonaws.com/adafruit_hostapd_14128.zip
unzip adafruit_hostapd_14128.zip
sudo mv /usr/sbin/hostapd /usr/sbin/hostapd.ORIG
sudo mv hostapd /usr/sbin


sudo service hostapd start
sudo service isc-dhcp-server start

sudo update-rc.d hostapd enable
sudo update-rc.d isc-dhcp-server enable

sudo mv /usr/share/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service ~/

sudo reboot