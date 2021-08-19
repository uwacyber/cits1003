# Forensics

## Introduction

These exercises require Wireshark. You can install this on your computer or you can run it from docker:

```bash
 docker run -v /yourfolder:/opt/share -p 3000:3000 linuxserver/wireshark
```

Replace /yourfolder with a path to a directory or folder on your machine. This will allow you to share data with Wireshark. Once the container is running, you can run it from your browser by going to http://127.0.0.1:3000

## Flag 1**7**: Who is that?

**All the forensic challenges use the captured.pcapng that you can download from Task 1!**

Help our Windows server is under attack! Well we think we are but not 100% sure...

The reason why we think that we are being attacked is because we noticed thousands of network packets being sent to and from our server. Can you analyse our network packet dump and find if we have been compromised?

The first task that you will need to do is identify the IP address of the suspicious user. To support the claim that the IP address is being used for a malicious purpose, use [AbuseIPDB](https://www.abuseipdb.com/) to retrieve the **country** where the IP address originates from. The flag will be in the format below in all lower case and no spaces:

**`<COUNTRY>:<IP ADDRESS>`**

For an example:

**`australia:120.123.69.5`**

We will use **wireshark** to examine the capture file `captured.pcapng` that has the data from the network dump.

Once you have loaded the `captured.pcapng` file, look at the **statistics** for **IPv4** \(there is a statistics button on the top bar\). The suspicious user has the highest count of packets being captured, besides the host which has the IP address of 10.0.0.4.

{% file src="../.gitbook/assets/forensic\_challenges.zip" %}

## Flag 18: Wow Such Bad Creds

**All the forensic challenges use the captured.pcapng that you can download from Task 1!**

Once you have identified the malicious actor, you can filter the traffic by using the display filter `ip.addr == <IP address>` \(eg. `ip.addr == 120.123.69.5`\).

You can see in the filtered packet capture that they first used a _port scanner_ then a _web fuzzer_ to scan the server. A _web fuzzer_ is a tool that brute forces a tonne of web requests to a website to establish a map of valid URL paths on the website and _potentially find vulnerable sections_. However, this means that the packet dump would start with **a lot of unnecessary data**. Keep this in mind while you are analysing the packets and finding evidence of what the adversary did.

**Our next task is to figure out how the adversary was able to login to the website with the URI path of `/secure`.**

To help with your analysis you can filter for just web requests \(HTTP\) by using the `http` display filter. For an example `ip.addr == 120.123.69.5 && http` will only display the web requests to and from the IP address `120.123.69.5`.

**Can you find the username and password that the adversary used to login?**

You answer needs to be in the format `<username>:<password>`. For an example if the was username `david` and the password `12345` your answer would be `david:12345`.

## Flag 19: That File Does Not Look Safe

**All the forensic challenges use the captured.pcapng that you can download from Task 1!**

The malicious actor was able to upload a malicious **PHP** file to the website and used a Local File Inclusion vulnerability to start executing commands on the server.

**What was the name of the PHP file that the hacker uploaded?**

## Flag 20: That Exe Looks Terrifying

**All the forensic challenges use the captured.pcapng that you can download from Task 1!**

It is speculated that the PHP file that was discovered in Task 3 was used to upload and execute some malware on the Windows server.

**What was the name of the executable that was uploaded onto the server?**

Your answer would be something like `something.exe`.

## Flag 21: A Present From The Hacker

**All the forensic challenges use the captured.pcapng that you can download from Task 1!**

It turns out that that malware the hacker uploaded was a **bind shell**. Bind shells open a port on a victims computer that enables the attacker to connect and start executing terminal commands on, without the inconveniences of using a PHP file.

Since we are dealing with a bind shell now, you'll want to remove the `http` display filter in wireshark and replace it with `tcp`.

It is speculated that the hacker left a message on the Windows Server.

**What was the file and message that the hacker left on the server?**

Your answer needs to be in the format of `<MESSAGE>:<FILE>` for an example `HACK THE PLANET:C:\message.txt`.



