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

```
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

```
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

## Case study: ACSC Guidelines for Cybersecurity Incidents

The Australian Cyber Security Center (ACSC) provides some guidelines for organizations of all levels (individuals, small business, corporate, government) on how to detect, manage, and report cybersecurity incidents.

Read through the following article and answer the questions below: [https://www.cyber.gov.au/acsc/view-all-content/advice/guidelines-cyber-security-incidents](https://www.cyber.gov.au/acsc/view-all-content/advice/guidelines-cyber-security-incidents)

### Question 4. Log it

System logs are an effective tool in detecting and investigating cyber security incidents. Which data source best fits the description: Logs that contain records of the requests made by both applications and users on a network.&#x20;

1. Domain Name System logs&#x20;
2. Email server logs&#x20;
3. Operating system event logs&#x20;
4. Security product logs&#x20;
5. Virtual Private Network and remote access logs&#x20;
6. Web proxy logs

{% hint style="info" %}
Submit the correct option as your flag (e.g., `CITS1003{`1`}` if option 1 is the correct answer).
{% endhint %}

### Question 5. Don't spill your data

A data spill is the accidental or deliberate exposure of data into an uncontrolled or unauthorized environment, or to unauthorized persons. The sequence of actions listed below form a timeline of response actions to a potential data spill. Which is the least sensible course of action given its position in the sequence:&#x20;

1. Identify: Recognise that a data spill has taken place.&#x20;
2. Contain: Determine the breadth of the data spill.&#x20;
3. Quantify: Determine the quantifiable loss and/or damages to the organization.&#x20;
4. Assess: Decide on the most appropriate course of action to address the data spill.&#x20;
5. Remediate: Remediate the data spill based on the course of action chosen.&#x20;
6. Prevent: Implement prevention measures to stop similar incidents from occurring in the future.

### Question 6. Not all security recommendations are great...

The Australian Government Information Security Manual provides recommendations and guidance for a wide range of cyber security matters. Organizations are encouraged to apply the recommended security controls where appropriate within their risk management frameworks. What is not a recommended security control for handling and containing intrusions?&#x20;

1. System owners are consulted before allowing intrusion activity to continue on a system for the purpose of collecting further data or evidence.&#x20;
2. Intrusion detection and prevention strategy is developed and implemented that includes at least network-based intrusion detection and prevention, procedures and resources for maintaining detection signatures, and procedures and resources for the analysis of event logs and real-time alerts&#x20;
3. To the extent possible, all intrusion remediation activities are conducted in a coordinated manner during the same planned outage.&#x20;
4. Legal advice is sought before allowing intrusion activity to continue on a system for the purpose of collecting further data or evidence.&#x20;
5. Following intrusion remediation activities, full network traffic is captured for at least seven days and analyzed to determine whether the adversary has been successfully removed from the system.
