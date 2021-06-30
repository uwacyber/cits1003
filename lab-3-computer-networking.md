# Lab 3 Computer Networking

Date: 12/05/2021 Author: David Glance

### Learning Objectives

1. Investigate the networking configuration of the computer and its local area network

### Technologies Covered

* Windows, MacOS, Linux
* Bash, PowerShell, Command Prompt
* nmap, PowerShell and Bash pingsweeps

### Network Interface

To communicate with a TCP/IP network, a computer uses a network interface. This may be connected to a fixed network via an ethernet cable or via a Wi-Fi network. From a TCP/IP perspective, there is little difference and the attributes of the interfaces are the same. The main attributes we are interested in are:

* **Interface Name**: usually **Mac**: en0, en, **Linux**: wlan0, eth0, **Windows**: Local Area Network Connection, Ethernet Adapter Ethernet0, etc.
* **IPv4 Address**: IP version 4 address e.g. 192.168.0.5
* Subnet Mask: 255.255.255.0
* **Default Gateway**: Usually the address of your router 192.168.0.1 
* **DNS Server**: Usually again, the address of your router or ISP DNS server

We can get these details using the command ipconfig on Windows and ifconfig and route on Linux and ifconfig and netstat on Mac

{% tabs %}
{% tab title="Windows" %}
```bash
PS C:\Users\oztechmuse\test> ipconfig

Windows IP Configuration


Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : uniwa.uwa.edu.au
   Link-local IPv6 Address . . . . . : fe80::3cfc:f569:4be1:6260%15
   IPv4 Address. . . . . . . . . . . : 192.168.114.3
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.114.1
   
```
{% endtab %}

{% tab title="Linux" %}
```bash
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ifconfig 
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.114.2  netmask 255.255.255.0  broadcast 192.168.114.255
        inet6 fe80::9118:dec7:b554:ab5c  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:74:41:cd  txqueuelen 1000  (Ethernet)
        RX packets 29958  bytes 24914501 (23.7 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 18684  bytes 2792921 (2.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 290802  bytes 82687161 (78.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 290802  bytes 82687161 (78.8 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        
┌─[✗]─[oztechmuse@parrot]─[~/test]
└──╼ $ip route
default via 192.168.114.1 dev eth0 proto dhcp metric 100 
192.168.114.0/24 dev eth0 proto kernel scope link src 192.168.114.2 metric 100 

```
{% endtab %}

{% tab title="Mac" %}
```
0x4447734D4250:~/Desktop/DevProjects/cits1003/Labs$ ifconfig en0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether f8:ff:c2:01:fa:e5 
	inet6 fe80::1cd9:f507:eb70:f809%en0 prefixlen 64 secured scopeid 0x6 
	inet 10.0.1.2 netmask 0xffffff00 broadcast 10.0.1.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
	
0x4447734D4250:~/Desktop/DevProjects/cits1003/Labs$ netstat -nr | grep default
default            10.0.1.1           UGScg          en0       
```
{% endtab %}
{% endtabs %}

For both Mac and Windows, the Graphical User Interface versions of network configuration are more convenient ways of getting this information however. 

Scanning the network

We are interested in finding out what other computers are on the network and we can do that using a tool called **nmap**.

{% hint style="info" %}
You can install nmap from [https://nmap.org/download.html](https://nmap.org/download.html)

For Windows, there is a Graphical User Interface version that you can install as well
{% endhint %}

nmap performs scans on computer networks to detect if other devices are connected. If it finds a host, it can also scan for open ports that indicate specific services that the computer is using. We are mainly interested in finding other hosts and so we will be limiting the scan to what is called a Ping Sweep. When you ping another computer on the network, it involves sending a TCP/IP packet to the computer to say "are you there" to which the other computer usually replies and says "yes".  Technically, a ping is an ICMP Echo Request to which the response is an ICMP Echo Reply. 

In the following example, our computer's IP address is 10.0.1.2 and the gateway \(the router\) is 10.0.1.1

```bash
0x4447734D4250:~/Desktop/DevProjects/cits1003/Labs$ ping -c 1 10.0.1.1
PING 10.0.1.1 (10.0.1.1): 56 data bytes
64 bytes from 10.0.1.1: icmp_seq=0 ttl=255 time=1.563 ms

--- 10.0.1.1 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 1.563/1.563/1.563/0.000 ms
```

Using the ping command to send 1 ping \(-c 1\), we get a reply which took 1.563 ms to send the message and then get the reply. This time is known as the round-trip time. 

nmap uses different ways of doing the same thing as a ping to determine if a computer is on the network. It isn't always reliable because sometimes computers are configured not to reply to pings, or a firewall will block them. 

If mobile devices such as an iPhone is connected to a network, it will stop responding to pings when it is not unlocked. Android phones do respond however.

We can use nmap to perform a ping scan 

```bash
0x4447734D4250:~/Desktop/DevProjects/cits1003/Labs$ nmap -sn 10.0.1.0/24 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-21 14:00 AWST
Nmap scan report for 10.0.1.1
Host is up (0.0086s latency).
Nmap scan report for 10.0.1.2
Host is up (0.00020s latency).
Nmap scan report for 10.0.1.5
Host is up (0.049s latency).
Nmap scan report for 10.0.1.7
Host is up (0.037s latency).
Nmap done: 256 IP addresses (4 hosts up) scanned in 13.55 seconds
```

On this network, we found 4 hosts:

* 10.0.1.1 \(the router\)
* 10.0.1.2 \(A Mac\)
* 10.0.1.5 \(An iPhone\)
* 10.0.1.7 \(A HomePod\)

nmap does have the ability to try and work out what operating system is running on a device that it detects but in the case of phones, it isn't very reliable. 

We can do a simple discovery program using PowerShell on Windows or Bash on Linux or Mac

{% tabs %}
{% tab title="Windows" %}
```bash
$Network = "192.168.114."

$HostEnd   = 10
$HostCount = 0
while ($HostCount -le $HostEnd) {
   $result = Test-Connection -computername $Network$HostCount -Quiet -count 1 
   if ($result -eq "True") 
   {
     Write-Host "$Network$HostCount found"
   }
   $HostCount++
}
```

We set three variables. $Network to represent the unchanging network part of the IP address and $HostCount that will start at the bottom of the range of hosts we want to scan and $HostEnd that is the last host that we want to scan. We loop from $HostCount to $HostEnd times \(5\). We use the Test-Connection cmdlet to ping the host 1 time and then check the result. If "True", we print that we have found the host.

{% hint style="info" %}
To run this code, copy it to a file called pingsweep.ps1 and change the parameters to match your network

To run, just type .\pingsweep.ps1
{% endhint %}
{% endtab %}

{% tab title="Bash" %}
```bash
#!/bin/bash
 host_is_up() {
   ping -c 1 -w 1 "${ip}" > /dev/null
 }
for i in {1..254}; do
   ip="10.0.1.${i}"
   if host_is_up "${ip}"; then
       echo "${ip}"
   fi
done
```

In this code, we enter a loop, incrementing the variable i during each iteration, from 1 to 254 \(5\). We use this number to create a new IP address using a network portion "10.0.1" and adding the variable _**i**_ as the host portion \(note that you could pass this portion in as an argument to the script\). The code then calls the host\_is\_up function \(2\) with the newly created IP address as an argument. The host\_is\_up function sends a ping \(-c 1\) and waits one second for a reply \(-w 1\) \(3\). This function will return a status code indicating whether the ping was successful, so we check for this code. If successful, we print IP address of the discovered host.

{% hint style="info" %}
To run, copy the code to a file pingsweep.sh and change the parameters to match your network

do chmod u+x pingsweep.sh

You can then run it as ./pingsweep.sh
{% endhint %}
{% endtab %}
{% endtabs %}

Exercise

1. Find out the IP address, Subnet Mask, Default Gateway and DNS of your computer
2. Install nmap and do a ping scan of the local network. Note that this won't work on Unifi - so you will only get your local machine if you are connected to that network.
3. Use the Powershell or Bash script to do the same scan and compare the results. 

