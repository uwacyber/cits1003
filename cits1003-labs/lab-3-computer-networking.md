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

## 1. Network Interface

To communicate with a TCP/IP network, a computer uses a network interface. This may be connected to a fixed network via an ethernet cable or via a Wi-Fi network. From a TCP/IP perspective, there is little difference and the attributes of the interfaces are the same. The main attributes we are interested in are:

* **Interface Name**: usually&#x20;
  * **Mac**: en0, en
  * **Linux**: wlan0, eth0
  * **Windows**: Local Area Network Connection, Ethernet Adapter Ethernet0, etc.
* **IPv4 Address**: IP version 4 address e.g. 192.168.0.5
* **Subnet Mask**: 255.255.255.0
* **Default Gateway**: Usually the address of your router e.g. 192.168.0.1
* **DNS Server**: Usually again, the address of your router or ISP DNS server

We can get these details using the command `ipconfig` on Windows and `ip addr` on Linux and Mac\*

\*you have to first install `iproute2mac` package as below.

```
brew install iproute2mac
```

{% hint style="warning" %}
If `brew` isn't installed on your machine, install it by running:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
{% endhint %}

{% hint style="danger" %}
If you get a warning like "warning: /opt/homebrew/bin is not in your PATH", run the following commands in the terminal:

`echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zprofile`

`eval $(/opt/homebrew/bin/brew shellenv)`
{% endhint %}

Then you should be able to see something like below (Mac will look similar to Linux).

{% tabs %}
{% tab title="Windows" %}
```bash
PS C:\> ipconfig

Windows IP Configuration


Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : uniwa.uwa.edu.au
   Link-local IPv6 Address . . . . . : fe80::3cfc:f569:4be1:6260%15
   IPv4 Address. . . . . . . . . . . : 192.168.114.3
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.114.1
   
```
{% endtab %}

{% tab title="Linux/Mac" %}
```bash
root@d99d71e2318a:/# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
8: eth0@if9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```
{% endtab %}
{% endtabs %}

For both Mac and Windows, the Graphical User Interface versions of network configuration are more convenient ways of getting this information however (but is not covered in this unit nor needed).

Start the docker container and run `ip addr`

```
sudo docker run -it --rm uwacyber/cits1003-labs:network 
```

```bash
root@d99d71e2318a:/# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
8: eth0@if9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```

We see that the container has 2 network interfaces (ignore the ones with `<NOARP>`). The first is the main ethernet interface with the outside world `eth0` **** (item 8). It has an address in a private IP address range. The second interface is called the loopback interface (item 1) and has what is called the home address `127.0.0.1`.

Alternatively, you can use a `route` command, where we will see the Gateway address is. A gateway is usually a router of some sort, if the machine is not communicating with other machines on the network, it will send its packets to the gateway for it to find where they need to go.

```bash
root@d99d71e2318a:/# route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         172.17.0.1      0.0.0.0         UG    0      0        0 eth0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 eth0
```

We can see that the gateway address is `172.17.0.1`.

Let us start another container and do an `ip addr`. You can do this by opening another terminal and using the same `docker run` command as above. &#x20;

```
sudo docker run -it --rm uwacyber/cits1003-labs:network
```

```bash
root@5434bfac0449:/# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
10: eth0@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```

This container has been given an IP address of `172.17.0.3`.

So our network looks like this:

![](<../.gitbook/assets/network1 (1).jpg>)

We can actually communicate between containers. To test this, use the ping command (example below is from the terminal with the address `172.17.0.2`):

```
ping -c 1 172.17.0.3
```

```bash
PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
64 bytes from 172.17.0.3: icmp_seq=1 ttl=64 time=0.715 ms

--- 172.17.0.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.715/0.715/0.715/0.000 ms
```

We will use ping below to scan the network but the way it works is to send a packet of a particular kind to the address and when received, the other host replies. Other than showing that there is a host responding at that address, you can also work out how far away it is because you get the round trip time (`rtt` at line 7) which in this case is 0.715 ms.

The networking picture looks simple enough, but what happens when we want to communicate with the machine that Docker is running on? Well, Docker has a special address for that which is `host.docker.internal.` Let us ping that:

{% hint style="info" %}
In Ubuntu VM, you should use `172.17.0.1` instead of `host.docker.internal`.
{% endhint %}

```bash
root@d99d71e2318a:/# ping -c 1 host.docker.internal
PING host.docker.internal (192.168.65.2) 56(84) bytes of data.
64 bytes from 192.168.65.2: icmp_seq=1 ttl=37 time=1.50 ms

--- host.docker.internal ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.496/1.496/1.496/0.000 ms
```

So this is on a different network (still a private one, however). Docker also has a `hostname` for the gateway on this network which is `gateway.docker.internal`**.**

So now our network looks like this:

![](../.gitbook/assets/network2.jpg)

It is actually a little more complicated than this but we will use another tool to explore the network.&#x20;

## 2. Scanning the network

We are interested in finding out what other computers are on the network and we can do that using a tool called `nmap`.

`nmap` performs scans on computer networks to detect if other devices are connected. If it finds a host, it can also scan for open ports that indicate specific services that the computer is using. We are mainly interested in finding other hosts and so we will be limiting the scan to what is called a Ping Sweep. When you ping another computer on the network, it involves sending a TCP/IP packet to the computer to say "are you there" to which the other computer usually replies and says "yes". Technically, a ping is an ICMP Echo Request to which the response is an ICMP Echo Reply (don't worry, you will learn more about these in the networks unit).

In the following example, our computer's IP address is `10.0.1.2` and the gateway (the router) is `10.0.1.1`

```bash
$ ping -c 1 10.0.1.1
PING 10.0.1.1 (10.0.1.1): 56 data bytes
64 bytes from 10.0.1.1: icmp_seq=0 ttl=255 time=1.563 ms

--- 10.0.1.1 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
rtt min/avg/max/stddev = 1.563/1.563/1.563/0.000 ms
```

Using the ping command to send 1 ping (`-c 1`), we get a reply which took 1.563 ms to send the message and then get the reply. This time is known as the round-trip time (`rtt`).

`nmap` uses different ways of doing the same thing as a ping to determine if a computer is on the network. It isn't always reliable because sometimes computers are configured not to reply to pings, or a firewall will block them.

If mobile devices such as an iPhone is connected to a network, it will stop responding to pings when it is not unlocked. Android phones (currently) do respond however (last checked Dec 2021).

Let us go back to our docker container and scan the network `192.168.65.0/24`\*. Just as a reminder, this notation means that we are going to check the computers with IP addresses that range from `192.168.65.0` - `192.168.65.255` (the `/24` means that the network part is `192.168.65` and so is fixed).

{% hint style="info" %}
Ubuntu VM users, scan `172.17.0.1` - `172.17.0.255`&#x20;
{% endhint %}

\*here, you should replace this address with the address you have found when pinging `host.docker.internal`.

To use `nmap` to perform a ping scan we use the following (note, this takes some time):

```
nmap -sn 192.168.65.0/24
```

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2022-02-02 02:55 UTC
Nmap scan report for 192.168.65.1
Host is up (0.0081s latency).
Nmap scan report for 192.168.65.2
Host is up (0.0036s latency).
Nmap scan report for 192.168.65.3
Host is up (0.000080s latency).
Nmap scan report for 192.168.65.4
Host is up (0.000087s latency).
Nmap scan report for 192.168.65.5
Host is up (0.00047s latency).
Nmap done: 256 IP addresses (5 hosts up) scanned in 45.40 seconds
```

On this network, we found 5 hosts (your result may vary depending on where you are scanning from):

* 192.168.65.1
* 192.168.65.2
* 192.168.65.3
* 192.168.65.4
* 192.168.65.5

`nmap` does have the ability to try and work out what operating system is running on a device and of course will discover services that are running as well. Before we look at that, let us try a different approach by using a script to discover hosts:

The following script is in a file `/root/pingsweep.sh`

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

```
./root/pingsweep.sh 192.168.65
```

```bash
192.168.65.1
192.168.65.2
192.168.65.3
192.168.65.4
192.168.65.5
```

## 3. Service discovery with `nmap`

Nmap uses a number of strategies to discover what services are running on a machine once it has discovered that it is actually available. Service discovery is done via a range of scripts that come with the `nmap` program. We can run them as follows (note, this takes a very long time!):

```
nmap -sC -sV 192.168.65.1-5
```

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2022-02-02 03:01 UTC
Nmap scan report for 192.168.65.1
Host is up (0.0044s latency).
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
|_Methods supported:CONNECTION
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
<--SNIP-->

Nmap scan report for 192.168.65.2
Host is up (0.0046s latency).
Not shown: 994 filtered ports
PORT     STATE SERVICE         VERSION
<--SNIP-->

Nmap scan report for 192.168.65.3
Host is up (0.0000040s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36985/udp   status
|   100024  1          38418/udp6  status
|   100024  1          38507/tcp   status
|_  100024  1          54161/tcp6  status

Nmap scan report for 192.168.65.4
Host is up (0.0000040s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36985/udp   status
|   100024  1          38418/udp6  status
|   100024  1          38507/tcp   status
|_  100024  1          54161/tcp6  status

Nmap scan report for 192.168.65.5
Host is up (0.000015s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE    VERSION
53/tcp open  tcpwrapped

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 5 IP addresses (5 hosts up) scanned in 250.21 seconds
```

We run `nmap` using the `-sC` (all scripts) and `-sV` (determine the versions of software providing the services discovered). We specified the hosts to scan as `192.168.65.1-5` to just look at the hosts we found before (replace the range as appropriate).

So what we have is (for this example):

* 192.168.65.1 running DNS (53) and an HTTP Proxy (3128)
* 192.168.65.2 this is the address for my PC (your output may vary)
* 192.168.65.3 RPC Services (111)
* 192.168.65.4 RPC Services (111)
* 192.168.65.5 DNS (53)

There are 2 DNS servers but we can tell which one is used by our Docker container by looking at the file where this is specified called `resolv.conf` located in the `/etc` directory.

```bash
root@04f7c0bbd066:/# cat /etc/resolv.conf
# DNS requests are forwarded to the host. DHCP DNS options are ignored.
nameserver 192.168.65.5
```

The other DNS service is paired with an HTTP proxy. This is a piece of software through which requests for external websites are made. From the Docker documentation, the host 192.168.65.1 is used to proxy requests to the Docker registry, the other 2 hosts, `192.168.65.2` and `.3` are used for internal purposes as well.

### Question 1. Scanning a remote access service

Now that we know the basics of using `nmap`, let us use it on a new host. Keep the network container running from above (or start it if you haven't got it running). In a new terminal, start the docker container:

```
sudo docker run -p 2222:2222 -it --rm uwacyber/cits1003-labs:cowrie
```

Back in the `network` container, do a ping scan of the `172.17.0.1-16` network and find what hosts are up. Run `nmap` against the IP of the second container you ran using all scripts and versions.

What is the service that you have found?

{% tabs %}
{% tab title="Hint?" %}
Hints are available on the next tabs.
{% endtab %}

{% tab title="Hint 1" %}
To scan for the hosts:

`$ nmap -sn 172.17.0.1-16`
{% endtab %}

{% tab title="Hint 2" %}
To scan with all scripts and versions of the specific target IP

`$ nmap -sC -sV 172.17.0.3`

If the IP address of the host you want to scan is different then use that address instead
{% endtab %}
{% endtabs %}

Try connecting to the service you found using the user root and no password. You will need to use a `ssh` command (try `ssh -help`), where you have to specify the port to be `2222`, and login as the `root`. Note, there is no password to login as root.

Once you have successfully logged on the machine as root, look at the file `/etc/passwd`

**Flag: Enter the flag from** `/etc/passwd`

{% hint style="info" %}
The cowrie container you started is actually a HoneyPot and logs everything that anyone does when interacting with it. Have a look at the output in the terminal where you ran it.

HoneyPots are deliberately left exploitable to attract potential attackers and watching what they do.
{% endhint %}

### Question 2. Understanding honeypot responses

Inspect the output (i.e. log) in the honeypot server terminal. You will see a list of actions taken on the server, whether it be itself or via the remote login user. You may be able to figure out by only reading the log what actions are taken on the honeypot server.

There are three types of keypairs generated by the honeypot server when an ssh connection is established for the very first time.

**Flag: Enter the three types of keypairs generated in order, separated by a comma no spaces (e.g., `CITS1003{type1,type2,type3}`).**

### Question **3**. Established crypto algorithms

When an ssh connection is initiated, the server negotiates the crypto algorithms to use for data exchange. For our honeypot server, both the incoming and outgoing crypto algorithms are the same.

**Flag: Enter the crypto algorithms (in order of appearance) used by the honeypot server to exchange data with the ssh connection. The algorithms are separated by a comma, no spaces (e.g., `CITS1003{algorithm1,algorithm2}`).**&#x20;

## **Case study: IP Spoofing in Django REST**

Recently, an IP spoofing vulnerability has been discovered in Django REST allowing attackers to circumvent the framework’s throttling feature, which is supposed to protect applications against mass requests.

Read through the following article and answer the questions below: [https://portswigger.net/daily-swig/ip-spoofing-bug-leaves-django-rest-applications-open-to-ddos-password-cracking-attacks](https://portswigger.net/daily-swig/ip-spoofing-bug-leaves-django-rest-applications-open-to-ddos-password-cracking-attacks)

### Question 4. what is IP spoofing?

1. An attack that fools the target computer and any intervening firewall into believing that messages from the intruder's computer are actually coming from an authorized user inside the organization's network.&#x20;
2. An attempt to clad or cover the internal processing (IP) lines with insulating material to shield the IP lines from excess heat or radiation. Illegally taping or listening in on telephone conversations.&#x20;
3. The prevention of denial-of-service attacks by routinely shuffling IP addresses on a subnetwork.&#x20;
4. Any malicious activity that disrupts a network through means of IP address table manipulation.

{% hint style="info" %}
Submit the correct option as your flag (e.g., `CITS1003{1}` if option 1 is the correct answer).
{% endhint %}

### Question 5. IP address range

Given the IP address 130.95.0.0/16, what is the IP address range of this specification?&#x20;

1. 130.0.0.0 - 130.255.255.255&#x20;
2. 130.95.0.0 - 130.95.0.255&#x20;
3. 130.95.0.0 - 130.95.0.0&#x20;
4. 130.95.0.0 - 130.95.255.255

### Question 6. IP Spoofing effect

The IP spoofing vulnerability found in Django is exploited by including a specific header in a web request. You can then submit an endless number of requests with the same client by simply changing the value of this header, bypassing rate limiting measures. Which is not an example of a malicious activity that can be performed due to this exploit?&#x20;

1. Brute forcing login credentials by sending as many web requests as needed.&#x20;
2. DDoS attacks by flooding the web server with requests.&#x20;
3. An attacker could use spoofed addresses to send seemingly legitimate requests to the server and analyze the server’s response to discover sensitive information, such as user credentials or server configurations.&#x20;
4. An application could have limits set on the number of password attempts a user can make before defense systems block the IP. An attacker can spoof the IP addresses of users behind network address translation (NAT) and flood the application server with requests to get their addresses blocked.
