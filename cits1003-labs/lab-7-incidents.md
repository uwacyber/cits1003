# Lab 7: Incidents

{% hint style="danger" %}
This lab will be using live malware samples. Although the samples we use are not capable of breaking out of docker containers, it is best to minimize the risk by doing this lab within a virtual machine (VM), such as using VirtualBox with Ubuntu. Please check the [Setup VM for Labs](setting-up-your-laptop.md#1.-setting-up-virtual-machine-vm-to-do-labs) section to do this. If you are doing the lab directly from your host machine, you should delete the container once you have finished the lab to remove all malware samples - otherwise your antivirus software may not be happy and throw a tantrum. You can automatically delete the container by adding `--rm` flag when running the container.
{% endhint %}

Walkthrough video:

**Incidents 7-1** [https://www.youtube.com/watch?v=SiGKMrr-qdY](https://www.youtube.com/watch?v=SiGKMrr-qdY)

## Intro to cybersecurity incidents

There are a number of specific definitions of a cybersecurity incident:

* Any event that has compromised confidentiality, integrity or availability of an organisation’s assets
* From a VERIS perspective, an incident is the result of an Actor, taking some Action, on an Asset, resulting in the Attributes of an incident, i.e., how it was affected. In this case, the action exploits a vulnerability in the asset
* An incident is when there is actual loss or imminent threat of loss. Otherwise, it is an Event
  * e.g., you fell on the ground and hurt yourself - an incident
  * e.g., a leaf fell on the ground - an event
* One of the popularly used Standard for incident handling is NIST SP800-61. It defines an incident as: “A computer security incident is a violation or imminent threat of violation of computer security policies, acceptable use policies, or standard security practices”

What most organisations take this to mean in practice is that they have discovered unauthorised access or use of an organisations' assets. From a legal perspective, even accessing a machine without permission is potentially a crime. Of course, the cybersecurity incident becomes much worse if the access then leads to the theft or corruption of data.

An incident can be detected in a number of ways. The organisation may be alerted through the use of Intrusion Detection Systems/Intrusion Protection Systems (IDS/IPS) or through the use of a SIEM (Security Information and Event Management) system which is supplied with data from log files from network equipment and computers. An anti-malware software system might raise the alarm or a user may notice erratic behaviour on their computer (e.g., a virus modifying/corrupting files).

However, it is also possible that attacks go unnoticed for extended periods of time. The _**dwell time**_, the time between an attack and it becoming noticed, is globally on average around 24 days. Once the attack is noticed however, an incident management process is started and is handled through an incident response team.

## Handling an Incident

![NIST Incident Response Lifecycle](../.gitbook/assets/incidentlifecycle.png)

In this lab, we are going to concentrate on the detection and analysis part of the lifecycle. We are going to start with a range of observations that will give us potential indicators of compromise (IOCs) and techniques and procedures and we will eventually identify the specific group that carried out the attack.

## 1. Using Yara to identify Malware

Yara ([https://github.com/VirusTotal/yara](https://github.com/VirusTotal/yara)) is a tool that uses a set of configurable rules to identify and classify malware. Of course, your anti-malware software installed on desktops will try and identify any malware it finds and there are also online tools that will try and identify malware that is uploaded to them like [https://www.virustotal.com/gui/](https://www.virustotal.com/gui/). However, there are situations where malware is not found, or machines and storage devices need to be searched to check if malware is present on them.

Yara tries to match text and binary from the malware it analyses. Before we start matching malware, let us try and write a rule that will match the text "hello, world!".

To start, run the docker container:

```bash
sudo docker run -it --rm uwacyber/cits1003-labs:incident
```

Change directory to `/opt/malware/test`. This directory has a subdirectory `./files` which has two files in it. One called `bye.txt` which contains the text `"bye bye"` and another file called `hello.txt` that has the text "`hello, world!"`

We are going to create a Yara rules file which you can edit on the machine using the editor `vi`. If you haven't used `vi` before, don't worry, the steps are provided for you to use it.

{% hint style="info" %}
if `vi` is missing, install it:&#x20;

`sudo apt-get update; sudo apt-get install -y vim`
{% endhint %}

Start editing the file by typing

```bash
vi hello_world.yar
```

To start editing, type `i` for insert mode. Then type the following rule:

```bash
rule hello_world
{
	strings:
	   $hello = "hello, world!"
	condition:
	   $hello
}
```

{% hint style="info" %}
If you are on Windows, you can copy the above text, then right-click in the PowerShell to paste.
{% endhint %}

Once you have finished typing, hit the Escape key `esc` which puts you into command mode (you should not see `INSERT` at the bottom of the editor) and then type `:wq` (short for write and quit) which will save the file and quit `vi`.

Before we run the rule, let us go through what it is actually doing. The variable `$hello` is set to the value of the text (the string) `"hello, world!"`. The condition simply says check if that string is in the file and if it is, the condition is satisfied and Yara reports a match. Let us run yara with this rules file in the directory `/opt/malware/test` as follows:

```bash
root@ccaeedcb7816:/opt/malware/test# yara hello_world.yar ./files 
hello_world ./files/hello.txt 
```

We have run yara and told it to search the subdirectory `./files` and it has found a match in the file `hello.txt`.

Of course, Yara rules can get much more complicated but the principle is the same. Once you have found a piece of malware, you can write rules that will match that malware because of the text and binary data it contains. You can also find other malware that is related to another malware in some way because it has reused some code for example.

## 2. Recognising Malware Samples

{% hint style="danger" %}
WARNING: The malware you are analysing is real and so \*do not\* try and remove it from the container or run it.
{% endhint %}

### Malware Sample 1

Change directory into `/opt/malware/malware_sample1`. You need to first unzip the malware file `malware1.zip`.&#x20;

```bash
unzip malware1.zip
```

You will be prompted to enter a password, which you can type in `infected` - this is the industry best practice to always have malware sample(s) encrypted with the password `infected`.

Now, run yara using the rules file against the malware. It should identify it with a name. Once you have found out the name of the malware, investigate the web to find out the following about the malware:

1. What is the name of the malware?
2. Which APT group is thought to be responsible for the malware?
3. Which country did this malware target in 2014?

{% hint style="info" %}
Once finished with the malware sample, delete it:

`rm malware1`
{% endhint %}

### **Question 1. Find the malware1 hash**

**FLAG: Get the MD5 hash of the file malware 1 and enter that in as a hash.**

{% hint style="info" %}
Actually, you could have just taken the hash of the file and done a Google search to find the name of the malware as it is in itself an IOC - but that doesn't work in the real world because the hash will change if a single byte is changed in the file and so it is very fragile.
{% endhint %}

### Malware Sample 2

Change directory into `/opt/malware/malware_sample2`, decrypt the `malware2.zip` and run yara using the rules file against the malware. It should identify it with a name. Once you have found out the name of the malware, investigate the web to find out the following about the malware:

1. What is the name of the malware?
2. What is the name of the group thought to be responsible for the malware?
3. Roughly how many computers were infected?

{% hint style="info" %}
Don't forget to delete the malware sample once finished:

`rm malware2`
{% endhint %}

### Question 2. Find the malware2 hash

**FLAG: Get the MD5 hash of the file malware 2 and enter that in as a hash.**

### Network log analysis

Malware often communicates with a command and control centre (C2 server) to send data and receive commands. The IP addresses and domain names used by malware are also IOCs. Of course, amongst IOCs, IP addresses and domains are relatively easy to change (and is indeed the case).

There is a (small) network log that you can see in the directory `/opt/malware/malware_conn`. The important bits of information from the log are the two IP addresses. The first IP address is the source IP address which in this case is a single machine. That is followed by a port number. The second IP address is the destination followed by the port that is being connected to.

Examine the log and find any IP addresses that look suspicious and check if indeed it is an IOC related to either of the two malware samples you have already identified. You should be able to:

1. Identify the IP address(es) that are associated with IOCs
2. Identify the malware that the IP address(es) belong to

### Question 3. Identify the APT Group

**FLAG: Enter the APT Group Name associated with the IP address(es) (note, spaces are converted with underscores e.g.,** `hello world` **->** `hello_world`**).**

{% hint style="info" %}
You can search through the file manually and see if you can spot anything but to make things easier you can use the following commands:

```bash
cat malware.log | awk -F ' ' '{print $3," ", $5, " ", $6}' | sort -u
```

The `awk` command will chunk each line based on text separated by spaces (`-F ' '`) and then print the source IP address, the destination IP address and the destination port. The `sort -u` command will sort the output and remove duplicates.

The other thing to remember is that the address range `192.168.0.0` to `192.168.255.255` is non-routable across the Internet (i.e. it is a private IP address range meant for internal networks).
{% endhint %}

## Case study: Cyber Security Incident Reporting in Australia

Reporting a cyber security incident helps to contain the spread of the attack and prevent further damage. By reporting the incident, affected systems can be disconnected from the network and steps can be taken to minimize the impact of the attack.
The Security of Critical Infrastructure Act 2018 provides for mandatory cyber incident reporting for critical infrastructure assets. Critical infrastructure owners and operators are required to report a cyber security incident to the Australian Cyber Security Centre (ACSC). 

Read through the following article and answer the questions below: [https://www.cisc.gov.au/critical-infrastructure-centre-subsite/Files/cyber-security-incident-reporting.pdf](https://www.cisc.gov.au/critical-infrastructure-centre-subsite/Files/cyber-security-incident-reporting.pdf)

### Question 4. What is a cyber security incident?

Which of the following best describes a cyber security incident?&#x20;

1. Unauthorized access and malware infections are prevented by installing firewalls and antivirus software.&#x20;
2. Software fuzzing and software vulnerabilities discovery.&#x20;
3. Unauthorised modification of the integrity of computer data.&#x20;
4. Software and network disaster recovery plan development.


{% hint style="info" %}
Submit the correct option as your flag (e.g., `CITS1003{`1`}` if option 1 is the correct answer).
{% endhint %}

### Question 5. When do I need to report?

If a security researcher observes that a cyber security incident has occurred, or is occurring, AND the incident has had, or is having, a significant impact on the availability of individual or company asset, the research must notify the ACSC in a short time.&#x20;

Which of the following is true about time length?&#x20;

1. Verbal notification within 72 hours plus another written record within 48 hours (critical incident)&#x20;
2. Verbal notification within 12 hours plus another written record within 48 hours (non-critical incident)&#x20;
3. Verbal notification within 12 hours plus another written record within 84 hours (critical incident)&#x20;
4. Verbal notification within 48 hours plus another written record within 72 hours (non-critical incident)


### Question 6. What doesnot a cyber security incident affect?

In the article’s provided example, which of the following is unlikely to be impacted by a cyber security incident?&#x20;

1. A cyber security incident might impact a bank’s internal network.&#x20;
2. A cyber security incident might expose a bank’s sensitive information.&#x20;
3. A cyber security incident might compromise a bank’s electronic devices.&#x20;
4. A cyber security incident might affect the provision of banking services. 

