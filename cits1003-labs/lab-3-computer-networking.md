# Lab 4: Computer Networking

Walkthrough video:

**Networks 4-1** [https://www.youtube.com/watch?v=Tq6cKMcNavw](https://www.youtube.com/watch?v=Tq6cKMcNavw)

### Learning Objectives

1. Investigate the networking configuration of a docker container and its local area network
2. Understand some basics around network addresses, net masks, routing tables
3. Learn how to identify active hosts on a network and scan their ports

### Technologies Covered

* Windows, MacOS, Linux
* Bash
* Networking
* nmap, Bash pingsweeps



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

Start the docker container and run ifconfig

{% tabs %}
{% tab title="Windows/Apple Intel" %}
```bash
docker run -it  cybernemosyne/cits1003:network 
```
{% endtab %}

{% tab title="Apple Silicon" %}
```bash
docker run -it  cybernemosyne/cits1003:network-x
```
{% endtab %}
{% endtabs %}

```bash
/network$ docker run -it  cybernemosyne/cits1003:network 
root@3921e4d47009:/# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
        RX packets 6  bytes 516 (516.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

We see that the container has 2 network interfaces. The first is the main ethernet interface with the outside world **eth0**. It has an address in a private IP address range. The second interface is called the loopback interface and has what is called the home address **127.0.0.1**.

If we do a route command, we will see where the Gateway address is. A gateway is usually a router of some sort, if the machine is not communicating with other machines on the network, it will send its packets to the gateway for it to find where they need to go.

```bash
root@3921e4d47009:/# route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         172.17.0.1      0.0.0.0         UG    0      0        0 eth0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 eth0
```

We can see that the gateway address is 172.17.0.1.

Let us start another container and do an ifconfig.

```bash
root@b3f523e4a4b8:/# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.3  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:03  txqueuelen 0  (Ethernet)
        RX packets 81  bytes 45804 (45.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 74  bytes 4694 (4.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 10  bytes 1120 (1.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10  bytes 1120 (1.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

This container has been given an IP address of 172.17.0.3.

So our network looks like this:

![](<../.gitbook/assets/network1 (1).jpg>)

We can actually communicate between containers. To test this, use the ping command:

```bash
root@3921e4d47009:/# ping -c 1 172.17.0.3
PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
64 bytes from 172.17.0.3: icmp_seq=1 ttl=64 time=0.086 ms

--- 172.17.0.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.086/0.086/0.086/0.000 ms
```

We will use ping below to scan the network but the way it works is to send a packet of a particular kind to the address and when received, the other host replies. Other than showing that there is a host responding at that address, you can also work out how far away it is because you get the round trip time which in this case is 0.086 ms (a very short time).

The networking picture looks simple enouugh, but what happens when we want to communicate with the machine that Docker is running on? Well, Docker has a special address for that which is **host.docker.internal** Let us ping that:

```bash
root@3921e4d47009:/# ping -c 1 host.docker.internal
PING host.docker.internal (192.168.65.2) 56(84) bytes of data.
64 bytes from 192.168.65.2 (192.168.65.2): icmp_seq=1 ttl=37 time=0.246 ms

--- host.docker.internal ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.246/0.246/0.246/0.000 ms
```

So this is on a different network (still a private one however). Docker also has a hostname for the gateway on this network which is **gateway.docker.internal.**

So now our network looks like this:

![](../.gitbook/assets/network2.jpg)

It is actually a little more complicated than this but we will use another tool to explore the network.

### Question 1. Find the other network interfaces

On the docker container running under Docker Desktop, there are actually several network interfaces. Two we have mentioned above, find out what the other(s) are

**Flag: Enter the name of the interface that starts with a 't' when running Docker Desktop on a Mac or 's' when running Docker Desktop under Windows.**

## Scanning the network

We are interested in finding out what other computers are on the network and we can do that using a tool called **nmap**.

nmap performs scans on computer networks to detect if other devices are connected. If it finds a host, it can also scan for open ports that indicate specific services that the computer is using. We are mainly interested in finding other hosts and so we will be limiting the scan to what is called a Ping Sweep. When you ping another computer on the network, it involves sending a TCP/IP packet to the computer to say "are you there" to which the other computer usually replies and says "yes". Technically, a ping is an ICMP Echo Request to which the response is an ICMP Echo Reply.

In the following example, our computer's IP address is 10.0.1.2 and the gateway (the router) is 10.0.1.1

```bash
$ ping -c 1 10.0.1.1
PING 10.0.1.1 (10.0.1.1): 56 data bytes
64 bytes from 10.0.1.1: icmp_seq=0 ttl=255 time=1.563 ms

--- 10.0.1.1 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 1.563/1.563/1.563/0.000 ms
```

Using the ping command to send 1 ping (-c 1), we get a reply which took 1.563 ms to send the message and then get the reply. This time is known as the round-trip time.

nmap uses different ways of doing the same thing as a ping to determine if a computer is on the network. It isn't always reliable because sometimes computers are configured not to reply to pings, or a firewall will block them.

If mobile devices such as an iPhone is connected to a network, it will stop responding to pings when it is not unlocked. Android phones do respond however.

Let us go back to our docker container and scan the network 192.168.65.0/24 Just as a reminder, this notation means that we are going to check the computers with IP addresses that range from 192.168.65.0 - 192.168.65.255 (the /24 means that the network part is 192.168.65 and so is fixed)

To use nmap to perform a ping scan we use the following:

```bash
root@382158e39146:/# nmap -sn 192.168.65.0/24
Starting Nmap 7.80 ( https://nmap.org ) at 2021-07-14 11:38 UTC
Nmap scan report for 192.168.65.1
Host is up (0.00036s latency).
Nmap scan report for 192.168.65.2
Host is up (0.00039s latency).
Nmap scan report for 192.168.65.3
Host is up (0.000024s latency).
Nmap scan report for 192.168.65.4
Host is up (0.000024s latency).
Nmap scan report for 192.168.65.5
Host is up (0.00018s latency).
Nmap done: 256 IP addresses (5 hosts up) scanned in 34.63 seconds
root@3921e4d47009:/# 
```

On this network, we found 5 hosts:

* 192.168.65.1
* 192.168.65.2
* 192.168.65.3
* 192.168.65.4
* 192.168.65.5

nmap does have the ability to try and work out what operating system is running on a device and of course will discover services that are running as well. Before we look at that, let us try a different approach by using a script to discover hosts:

The following script is in a file /root/pingsweep.sh

```bash
#!/bin/bash
 host_is_up() {
   ping -c 1 -w 1 "${ip}" > /dev/null
 }
for i in {1..254}; do
   ip="$1.${i}"
   if host_is_up "${ip}"; then
       echo "${ip}"
   fi
done
```

Run the script by doing:

```bash
root@3921e4d47009:~# ./pingsweep.sh 192.168.65
192.168.65.1
192.168.65.2
192.168.65.3
192.168.65.4
192.168.65.5
```

## Service discovery with nmap

Nmap uses a number of strategies to discover what services are running on a machine once it has discovered that it is actually available. Service discovery is done via a range of scripts that come with the nmap program. We can run them as follows:

```bash
root@3921e4d47009:~# nmap -sC -sV 192.168.65.1-5 
Starting Nmap 7.80 ( https://nmap.org ) at 2021-07-15 01:19 UTC
Nmap scan report for 192.168.65.1
Host is up (0.00075s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE     VERSION
53/tcp   open  domain?
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
3128/tcp open  squid-http?
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.1 400 Bad Request
|     transfer-encoding: chunked
|     <html><head>
|     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
|     <title>ERROR: connection refused</title>
|     </head><body>
|     HTTP request must contain an absolute URI e.g. http://github.com/moby/vpnkit
|     <br>
|     <p>Server is <a href="https://github.com/moby/vpnkit">moby/vpnkit</a></p>
|     </body>
|_    </html>
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported: GET CONNECTION
<SNIP..>

Nmap scan report for 192.168.65.2
Host is up (0.00017s latency).
All 1000 scanned ports on 192.168.65.2 are closed

Nmap scan report for 192.168.65.3
Host is up (0.000016s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
111/tcp open  rpcbind 2-4 (RPC #100000)
<SNIP...>

Nmap scan report for 192.168.65.4
Host is up (0.000020s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
111/tcp open  rpcbind 2-4 (RPC #100000)
<SNIP...>

Nmap scan report for 192.168.65.5
Host is up (0.000024s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
53/tcp open  domain  (generic dns response: NOTIMP)
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
<SNIP...>
```

We run nmap using the -sC (all scripts) and -sV (determine the versions of software providing the services discovered). We specified the hosts to scan as 192.168.65.1-5 to just look at the hosts we found before.

So what we have is:

* 192.168.65.1 running DNS (53) and a HTTP Proxy (3128)
* 192.168.65.2 no ports open but we know that this is the address for our PC
* 192.168.65.3 RPC Services (111)
* 192.168.65.4 RPC Services (111)
* 192.168.65.5 DNS (53)

There are 2 DNS servers but we can tell which one is used by our Docker container by looking at the file where this is specified called resolv.conf

```bash
root@3921e4d47009:~# cat /etc/resolv.conf 
# DNS requests are forwarded to the host. DHCP DNS options are ignored.
nameserver 192.168.65.5
```

The other DNS service is paired with an HTTP proxy. This is a piece of software through which requests for external web sites are made. From the Docker documentation, the host 192.168.65.1 is used to proxy requests to the Docker registry, the other 2 hosts, 192.168.65.2 and .3 are used for internal purposes as well.

### Question 2. Scanning a remote access service

Now that we know the basics of using nmap, let us use it on a new host. Keep the network container running from above (or start it if you haven't got it running). In a new terminal, start the docker container:

{% tabs %}
{% tab title="Windows/Intel Mac" %}
```bash
 docker run -p 2222:2222 -it cybernemosyne/cits1003:cowrie
```
{% endtab %}

{% tab title="Apple Silicon" %}
```bash
 docker run -p 2222:2222 -it cybernemosyne/cits1003:cowrie-x
```
{% endtab %}
{% endtabs %}

Back in the network container, do a ping scan of the 172.17.0.1-16 network and find what hosts are up. Run nmap against the IP of the second container you ran using all scripts and versions.

What is the service that you have found?

{% tabs %}
{% tab title="Hint" %}
To scan for the hosts:

nmap -sn 172.17.0.1-16

To scan with all scripts and versions of the specific target IP

nmap -sC -sV 172.17.0.3

If the IP address of the host you want to scan is different then use that address
{% endtab %}
{% endtabs %}

Try connecting to the service you found using the user root and no password.

{% tabs %}
{% tab title="Hint" %}
To connect by ssh you use the command:

ssh -p 2222 root@172.17.0.3
{% endtab %}
{% endtabs %}

Once on the machine, look at the file /etc/passwd

**Flag: Enter the flag from /etc/passwd**

{% hint style="info" %}
The cowrie container you started is actually a HoneyPot and logs everything that anyone does when interacting with it. Have a look at the output in the terminal where you ran it.

HoneyPots are deliberately left exploitable to attract potential attackers and watching what they do.
{% endhint %}
