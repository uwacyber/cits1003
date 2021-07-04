# Lab 7: Incidents

There are a number of specific definitions of a cybersecurity incident:

* Any event that has compromised confidentiality, integrity or availability of an organisation’s assets 
* From a VERIS perspective, an incident is the result of an Actor, taking some Action, on an Asset, resulting in the Attributes of an incident, i.e., how it was affected. In this case, the action exploits a vulnerability in the asset 
* An incident is when there is actual loss or imminent threat of loss. Otherwise, it is an Event 
* Standard for incident handling is NIST SP800-61 it defines an incident as: “A computer security incident is a violation or imminent threat of violation of computer security policies, acceptable use policies, or standard security practices”

What most organisations take this to mean in practice is that they have discovered unauthorised access or use of an organisations's assets. From a legal perspective, even accessing a machine without permission is potentially a crime. Of course, the cybersecurity incident becomes much worse if the access then leads to the theft or corruption of data.

An incident can be detected in a number of ways. The organisation may be alerted through the use of Intrusion Detection Systems/Intrusion Protection Systems \(IDS/IPS\) or through the use of a SIEM \(Security Information and Event Management\) system which is supplied with data from log files from network equipment and computers. An anti-malware software system might raise the alarm or a user may notice erratic behaviour on their computer. 

However, it is also possible that attacks go unnoticed for extended periods of time. The _**dwell time**_, the time between an attack and it becoming noticed, is globally around 24 days. Once the attack is noticed however, an incident management process is started and is handled through an incident response team.

## Handling an Incident

![NIST Incident Response Lifecycle](.gitbook/assets/incidentlifecycle.png)

In this lab, we are going to concentrate on the detection and analysis part of the lifecycle. We are going to start with a range of observations that will give us potential indicators of compromise \(IOCs\) and techniques and procedures and we will eventually identify the specific group that carried out the attack. 

## Using Yara to identify Malware

Yara is a tools that uses a set of configurable rules to identify and classify malware. Of course, your antimalware software installed on desktops will try and identify any malware it finds and there are also online tools that will try and identify malware that is uploaded to them like [https://www.virustotal.com/gui/](https://www.virustotal.com/gui/). However, there are situations where malware is found, or machines and storage devices need to be searched to check if malware is present on them.

Yara tries to match text and binary from the malware it analyses. Before we start matching malware, 

```bash
rule hello_world
{
	strings:
	   $hello = "hello, world!"
	condition:
	   $hello
}
```

\*\*\* During this process, it is important to think about the problem as a detective would think about a crime. What were the motivations of the attacker and do they normally attack this type of target? What is their mode of operation, i.e. what tactics, techniques and procedures do they normally adopt. With respect to the latter, we will be using the MITRE ATT&CK \([https://attack.mitre.org/](https://attack.mitre.org/)\) framework to identify the groups involved.





