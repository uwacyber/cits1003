# Lab 3: Computer Architecture: Users, files, processes

Date: 12/05/2021 Author: David Glance

### Learning Objectives

1. Explore various aspects of computer architecture such as processes, file systems, users and access control

### Technologies Covered

* Windows, MacOS, Linux
* Bash, PowerShell, Command Prompt

### Command Line

Operating systems offer a number of different ways of interacting with files, processes and other aspects of the system through the use of commands typed in a terminal window. These commands can even be added to files and run as scripts to perform more complicated actions.

On Windows, there is a program called the Command Prompt as well as a program called PowerShell, whilst on the Mac and Linux there is the Terminal program that runs various types of "shell" programs. Many of the commands in these systems are similar and so 

_**pwd**_ \(print working directory\) will print the current directory 

{% tabs %}
{% tab title="cmd.exe" %}
```bash
c:\Users\oztechmuse>pwd
c:\Users\oztechmuse

c:\Users\oztechmuse>
```
{% endtab %}

{% tab title="bash" %}
```bash
┌─[oztechmuse@parrot]─[~]
└──╼ $pwd
/home/oztechmuse
┌─[oztechmuse@parrot]─[~]
└──╼ $
```
{% endtab %}
{% endtabs %}

All operating systems have file systems that operate on the basis of a hierarchy of directories or folders. Users have a _**home directory**_ which in Windows is usually located in c:\Users, on the Mac it is /Users and on Linux it is in /home

Navigating around can be done using the **cd** \(change directory\) command with an argument that tells cd which directory you want to move to. Two special shortcuts are the "." \(single dot\) and ".." \(double dot\) that specify the current directory and the parent directory respectively.

{% tabs %}
{% tab title="cmd.exe" %}
```bash
c:\Users\oztechmuse>cd ..

c:\Users>
```
{% endtab %}

{% tab title="bash" %}
```bash
┌─[oztechmuse@parrot]─[~]
└──╼ $cd ..
┌─[oztechmuse@parrot]─[/home]
└──╼ $
```
{% endtab %}
{% endtabs %}

The ls \(list\) command \(dir in Windows cmd.exe\) will list the files in a directory. Without arguments, it will list the contents of the current directory, otherwise it will list the directory specified in the argument. Commands can take arguments but also options that control the way the command works including the output it produces. In the case of ls -al the options -al specify that we want to see all files and to display the results in a long listing format.

{% tabs %}
{% tab title="cmd.exe" %}
```bash
c:\>dir
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\

11/18/2019  09:06 AM    <DIR>          PerfLogs
01/26/2021  07:31 PM    <DIR>          Program Files
01/05/2021  08:20 PM    <DIR>          Program Files (x86)
07/16/2020  03:31 PM    <DIR>          Users
10/22/2020  03:03 PM    <DIR>          Windows
               2 File(s)         43,852 bytes
              12 Dir(s)  15,207,464,960 bytes free
              
```
{% endtab %}

{% tab title="bash" %}
```bash
┌─[oztechmuse@parrot]─[/]
└──╼ $ls -al
total 2097225
drwxr-xr-x   1 root root        292 Apr 24 21:25 .
drwxr-xr-x   1 root root        292 Apr 24 21:25 ..
lrwxrwxrwx   1 root root          7 Sep 12  2020 bin -> usr/bin
drwxr-xr-x   4 root root       1024 Apr 28 12:16 boot
drwxr-xr-x  19 root root       3380 Apr 28 12:06 dev
drwxr-xr-x   1 root root       6358 Apr 24 21:34 etc
drwxr-xr-x   1 root root         20 Sep 12  2020 home
lrwxrwxrwx   1 root root         37 Apr 24 21:25 initrd.img -> boot/initrd.img-5.10.0-6parrot1-amd64
lrwxrwxrwx   1 root root          7 Sep 12  2020 lib -> usr/lib
lrwxrwxrwx   1 root root          9 Sep 12  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root          9 Sep 12  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root         10 Sep 12  2020 libx32 -> usr/libx32
drwxr-xr-x   1 root root         22 Aug  8  2020 media
drwxr-xr-x   1 root root         16 Sep 17  2020 mnt
drwxr-xr-x   1 root root        674 Feb  4 12:18 opt
dr-xr-xr-x 296 root root          0 Apr 28 12:06 proc
drwxr-xr-x   1 root root        860 Apr 28 12:47 root
drwxr-xr-x  46 root root       1220 May 15 16:58 run
drwxr-xr-x   1 root root          0 May  6  2020 sandbox
lrwxrwxrwx   1 root root          8 Sep 12  2020 sbin -> usr/sbin
drwxr-xr-x   1 root root          8 Sep 12  2020 srv
-rw-------   1 root root 2147483648 Sep 12  2020 swapfile
dr-xr-xr-x  13 root root          0 Apr 28 12:06 sys
drwxrwxrwt   1 root root       1608 May 15 16:58 tmp
drwxr-xr-x   1 root root        122 Sep 12  2020 usr
drwxr-xr-x   1 root root        142 Dec 12 20:15 var

```
{% endtab %}
{% endtabs %}

There are a few differences between the information that is listed on the different platforms. In Bash, a file listing will give more information about who the owner of the file is and the permissions that are associated with the file. 

#### Creating, deleting, copying and moving a file

{% tabs %}
{% tab title="cmd.exe" %}
```bash
c:\Users\oztechmuse\test>echo "Test Content" > file.txt

c:\Users\oztechmuse\test>type file.txt
"Test Content"

c:\Users\oztechmuse\test>copy file.txt file2.txt
        1 file(s) copied.

c:\Users\oztechmuse\test>dir
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\Users\oztechmuse\test

05/16/2021  05:03 PM    <DIR>          .
05/16/2021  05:03 PM    <DIR>          ..
05/16/2021  05:02 PM                17 file.txt
05/16/2021  05:02 PM                17 file2.txt
               2 File(s)             34 bytes
               2 Dir(s)  15,902,515,200 bytes free

c:\Users\oztechmuse\test>del file2.txt

c:\Users\oztechmuse\test>dir
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\Users\oztechmuse\test

05/16/2021  05:03 PM    <DIR>          .
05/16/2021  05:03 PM    <DIR>          ..
05/16/2021  05:02 PM                17 file.txt
               1 File(s)             17 bytes
               2 Dir(s)  15,902,515,200 bytes free

c:\Users\oztechmuse\test>move file.txt file2.txt
        1 file(s) moved.

c:\Users\oztechmuse\test>dir
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\Users\oztechmuse\test

05/16/2021  05:03 PM    <DIR>          .
05/16/2021  05:03 PM    <DIR>          ..
05/16/2021  05:02 PM                17 file2.txt
               1 File(s)             17 bytes
               2 Dir(s)  15,902,515,200 bytes free

c:\Users\oztechmuse\test>
```
{% endtab %}

{% tab title="bash" %}
```bash
┌─[oztechmuse@parrot]─[~/test]
└──╼ $touch file.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ls
file.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $cp file.txt file2.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ls
file2.txt  file.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $rm file2.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ls
file.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $mv file.txt file2.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ls
file2.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $

```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you ever want help with a command, you can type _**help &lt;command&gt;**_ on Windows or _**man &lt;command&gt;**_ on Linux or Mac.
{% endhint %}

#### Finding files

Linux has a find command that can be used for finding files. The basic syntax is:

> _**find &lt;starting directory&gt; -name &lt;file to find&gt;**_

find will look in all sub-directories and report on any files that match the name provided

On Windows, it is slightly more complicated if we just use the command prompt:

```bash
c:\Users\oztechmuse\test>dir /s /b . | findstr /i file
c:\Users\oztechmuse\test\file2.txt
c:\Users\oztechmuse\test\subtest\file3.txt
```

Note that his is actually using 2 commands that are chained with the _**pipe**_ command **\|** What pipe does is takes the output from the command on the left of it and passes it as input to the command on the right. In this case, we do a _**dir**_ command that lists all of the files in the current directory and then search the output for text that matches the argument to the _**findstr**_ command.

### Hidden Files and other Attributes

In Linux, files that start with a period \(.\) are hidden from the directory listing command ls. To see them, you need to use the -a flag:

```bash
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ls  -l
total 0
-rw-r--r-- 1 oztechmuse oztechmuse 0 May 16 17:04 file.txt
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ls -al
total 0
drwxr-xr-x 1 oztechmuse oztechmuse   40 May 18 09:59 .
drwxr-xr-x 1 oztechmuse oztechmuse 1386 May 16 19:17 ..
-rw-r--r-- 1 oztechmuse oztechmuse    0 May 16 17:04 file.txt
-rw-r--r-- 1 oztechmuse oztechmuse    0 May 18 09:59 .hiddenfile

```

Linux has a limited set of specific attributes on a file that control how the file is accessed. One attribute for example is the Append Only attribute that only allows write operations on the file to append to it and not overwrite any existing content. Another attribute is Immutable which does not allow the file contents or metadata to change at all. You can list and change attributes on Linux using lsattr and chattr programs.

Windows' files have a wider range of attributes that determine characteristics and these can be managed using the **attrib** command.  Some of these attributes are:

* **Hidden** \(H\):  commands like dir and File Explorer do not show hidden files by default, unless asked to do so
* **System** \(S\): When set, indicates that the hosting file is a critical system file that is necessary for the computer to operate properly. Like hidden files, dir and File Explorer do not show these files by default
* **Directory** \(D\): The entry is a subdirectory, containing file and directory entries of its own.

We can illustrate how to change attributes as follows:

```bash
c:\Users\oztechmuse\attribfiles>echo "Hidden File" > hiddenfile.txt

c:\Users\oztechmuse\attribfiles>dir
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\Users\oztechmuse\attribfiles

05/18/2021  10:14 AM    <DIR>          .
05/18/2021  10:14 AM    <DIR>          ..
05/18/2021  10:14 AM                16 hiddenfile.txt
               1 File(s)             16 bytes
               2 Dir(s)  15,715,061,760 bytes free

c:\Users\oztechmuse\attribfiles>attrib +H hiddenfile.txt

c:\Users\oztechmuse\attribfiles>dir
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\Users\oztechmuse\attribfiles

05/18/2021  10:14 AM    <DIR>          .
05/18/2021  10:14 AM    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)  15,715,061,760 bytes free


c:\Users\oztechmuse\attribfiles>dir /A
 Volume in drive C has no label.
 Volume Serial Number is 54C8-8A2B

 Directory of c:\Users\oztechmuse\attribfiles

05/18/2021  10:14 AM    <DIR>          .
05/18/2021  10:14 AM    <DIR>          ..
05/18/2021  10:14 AM                16 hiddenfile.txt
               1 File(s)             16 bytes
               2 Dir(s)  15,715,061,760 bytes free
```

Here we create a file called hiddenfile.txt \(1\) which is visible when we do the dir command \(3\). We add the Hidden attribute using attrib +H \(15\) and now the file no longer shows up with a dir command \(17\). To see hidden files, we need to specify the /A switch on the dir command \(29\).

{% hint style="info" %}
Normally when using the GUI to show folders and files, it will keep hidden files and system files hidden as well as not showing file extensions. You can set the options in File Explorer to see all of these files.
{% endhint %}

### PowerShell

On Windows, there is a second environment called PowerShell that is closer to bash than the default command terminal. PowerShell commands can be aliased so that they seem similar to the commands already listed above. For example the PowerShell command \(called a cmdlet\) for cd \(change directory\) is actually **Set-Location**. But you can still use cd.

To get into PowerShell, you can either start the PowerShell window, or simply type powershell in the command prompt:

```bash
c:\Users\oztechmuse\test>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\oztechmuse\test> pwd

Path
----
C:\Users\oztechmuse\test


PS C:\Users\oztechmuse\test>
```

We will cover more PowerShell specific commands in the following exercise.

### Exercise

It will be easier if you do this exercise on Windows. However, it is  is possible to install PowerShell on Linux and Mac  \([https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-7.1](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-7.1)\).

We are going to download a file to our computer and so open a powershell window and create a directory called cits1003. Create another subdirectory called Lab2. cd into this directory and then use the command "Invoke-WebRequest" to download the file located at  "[https://github.com/uwacsp/opentrace/archive/refs/heads/master.zip](https://github.com/uwacsp/opentrace/archive/refs/heads/master.zip)" 

```bash
Invoke-WebRequest -Uri "https://github.com/uwacsp/opentrace/archive/refs/heads/master.zip" -OutFile "master.zip"
```

{% hint style="info" %}
Invoke-WebRequest is aliased as curl - a tool that can be used on Linux to download files
{% endhint %}

1. unzip the zip file using the command unzip
2. Rename the directory that is created to opentrace and delete the zip file
3. Use the command Get-ChildItem to search the opentrace directory for the file **AppDelegate.swift** \(you can find information on using this cmdlet here [https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/](https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/)\)
4. Using the PowerShell cmdlet Get-ChildItem, set the Hidden attribute on the AppDelegate.swift and check that it is not visible when using Get-ChildItem without any attribute arguments \(You will have to do an Internet search to find out how to do this\)

### Processes

There are a number of different ways of viewing the running processes on the system. From the command line, you can use the commands ps on Linux and tasklist on Windows. 

{% tabs %}
{% tab title="cmd.exe" %}
```bash
c:\Users\oztechmuse\test>tasklist

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0         16 K
smss.exe                       292 Services                   0        116 K
csrss.exe                      412 Services                   0      1,372 K
wininit.exe                    500 Services                   0          4 K
csrss.exe                      508 Console                    1    100,212 K
services.exe                   596 Services                   0      4,048 K
winlogon.exe                   604 Console                    1        604 K
lsass.exe                      644 Services                   0      8,800 K
svchost.exe                    772 Services                   0     14,736 K
fontdrvhost.exe                796 Services                   0         96 K
fontdrvhost.exe                804 Console                    1      2,612 K
svchost.exe                    880 Services                   0      7,736 K
dwm.exe                       1012 Console                    1     22,664 K
svchost.exe                    348 Services                   0     30,480 K
<SNIP...>
```
{% endtab %}

{% tab title="bash" %}
```bash
┌─[oztechmuse@parrot]─[~/test]
└──╼ $ps -f
UID          PID    PPID  C STIME TTY          TIME CMD
oztechm+   11876   11875  0 May15 pts/1    00:00:00 -bash
oztechm+  239127   11876  0 19:16 pts/1    00:00:00 bash
oztechm+  239185  239127  0 19:17 pts/1    00:00:00 ps -f
```
{% endtab %}
{% endtabs %}

The output is cut on the Windows output. The bash output for the program **ps** shows the parent process ID \(PPID\). The processes listed here are those bein run by the current user. This includes the command ps itself and as you can see, the parent PID of ps is the bash shell that we are currently running in. 

On Windows there are GUIs that provide a simpler and more detailed look at processes running on this machine. One program is called Process Hacker which shows the processes running on the machine as a hierarchy":

![Process Hacker Main Screen ](.gitbook/assets/screen-shot-2021-05-16-at-7.25.40-pm%20%281%29.png)

{% hint style="info" %}
You can install Process Hacker for Windows by downloading the latest setup file from here [https://github.com/processhacker/processhacker/releases](https://github.com/processhacker/processhacker/releases)  
{% endhint %}

From a user perspective, when looking at process information, we are interested in the amount of processing time \(CPU\) and memory the process is consuming. The other two measures that are also of interest from a security perspective are the Disk and Network usage.

There are other commands that allow you to manage processes from the command line. You can run a new process by simply typing the name of the program and hitting return. For example, if you run cmd, you will get a new command prompt within the same Window. If you have Process Hacker running, it will show a new cmd.exe running as a child of the cmd session your ran it from. 

You can type **exit** to terminate the new cmd session and return to the previous one. 

```bash
c:\Users\oztechmuse>cmd
Microsoft Windows [Version 10.0.16299.1508]
(c) 2017 Microsoft Corporation. All rights reserved.

c:\Users\oztechmuse>exit

c:\Users\oztechmuse>
```

You can launch programs using the **start** command which will start the cmd program but in a new window. 

```bash
c:\Users\oztechmuse>tasklist | findstr cmd
cmd.exe                      11140 Console                    1      2,872 K
cmd.exe                       4800 Console                    1      3,452 K

c:\Users\oztechmuse>start cmd

c:\Users\oztechmuse>tasklist | findstr cmd
cmd.exe                      11140 Console                    1      2,872 K
cmd.exe                       4800 Console                    1      3,352 K
cmd.exe                       1456 Console                    1      2,740 K
```

Here we are using the command tasklist and filtering the output to show only the cmd.exe processes. 

We can stop \(Kill\) the new process using the taskkill command

```bash
c:\Users\oztechmuse>taskkill /PID 1456
SUCCESS: Sent termination signal to the process with PID 1456.

c:\Users\oztechmuse>
```

In PowerShell, we can get more information about the process and we will explore this in the exercise 

### Exercise

Install and run Process Hacker. Spend some time familiarising yourself with the information provided.

  1. Find the process called System - what is its file path?

Start a cmd.exe window \(Command Prompt\) 

  2. How many new processes are running as a result?

Start PowerShell within the cmd.exe window and notice the new process appearing in Process Hacker 

Find the process id of the cmd.exe process that is the parent of the PowerShell process. We are going to retrieve all of the information we can from the process using the following PowerShell commands:

```bash
PS C:\Users\oztechmuse> $p = get-process -PID 4800
PS C:\Users\oztechmuse> $p | select-object *


Name                       : cmd
Id                         : 4800
PriorityClass              : Normal
FileVersion                : 10.0.16299.15 (WinBuild.160101.0800)
HandleCount                : 45
WorkingSet                 : 3211264
<SNIP...>
```

Note that the processes you will see in Process Hacker are those that you have authority to see as a normal user. You will get a great deal more information if you run Process Hacker as Administrator \(only possible on your own computer\).

### Users and Groups

Both Windows and Linux implement Role Based Access Control \(RBAC\) based on groups of users. On Windows 10, as the principle user of a PC, you will likely have Administrator access and so you will be part of a group called BUILTIN\Administrators. Windows does not let you perform actions as part of this role however and so will ask you for confirmation when you run an application as Administrator for example. 

You can view details of the users and groups on your machine by looking at Computer Management \(only if you have administrator access to the machine\). 

![Computer Management of Groups](.gitbook/assets/screen-shot-2021-05-19-at-11.56.25-am.png)

There are a variety of ways of getting user and group information using PowerShell:

* Get-LocalUser will list the users of the machine
* Get-LocalGroup will list the groups 
* Get-LocalGroupMember &lt;group name&gt; will list the members of a group

For information about the current logged on user you can use the command:

**whoami /all**

#### For Linux and Mac

You can use whoami to get the currently logged in user and the commands:

id &lt;user&gt; will list the groups the user is a member of

If you want to know all of the groups on the computer, you can list the contents of the file /etc/groups

```bash
0x4447734D4250:~$ cat /etc/group
##
# Group Database
# 
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:
nogroup:*:-1:
wheel:*:0:root
daemon:*:1:root
<SNIP...>
```

You can also list the passwd file which will list all of the users of the system

```bash
0x4447734D4250:~$ cat /etc/passwd
##
# User Database
# 
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
<SNIP...>
```

### File Permissions

#### Linux

All files on Linux have an user and a group that is assigned specific access to read \(r\), write \(w\) and execute  \(x\) the file. Looking at the access control list of a file, you can see that the permissions are specified for the user, group and other. We can do this using the tool getfacl

```bash
┌─[oztechmuse@parrot]─[~/test]
└──╼ $getfacl ./file2.txt 
# file: file2.txt
# owner: oztechmuse
# group: oztechmuse
user::rw-
group::r--
other::r--

```

We won't go into too much detail but this shows that the user has read and write access, the groupt and everyone else has just read access. The file is not marked as being executable and so there is no 'x' involved.

You can also see the permissions using the ls -al command on Mac and Linux

```bash
0x4447734D4250:~$ ls -al afile.txt
-rw-r--r--  1 dglance  staff  66 27 Aug  2020 afile.txt
```

Note that in this example, the group is "staff" whereas in the previous example it was "oztechmuse"

You can change permissions on files and directories using the chmod command. To mark a program as being executable for a user for example you can do:

```bash
0x4447734D4250:~$ ls -al afile.txt
-rw-r--r--  1 dglance  staff  66 27 Aug  2020 afile.txt
0x4447734D4250:~$ chmod u+x afile.txt
0x4447734D4250:~$ ls -al afile.txt
-rwxr--r--  1 dglance  staff  66 27 Aug  2020 afile.txt
```

#### Windows

We can use the PowerShell command Get-Acl to get the access  control list from a file on Windows

```bash
PS C:\Users\oztechmuse\test> get-acl master.zip | select *


PSPath                  : Microsoft.PowerShell.Core\FileSystem::C:\Users\oztechmuse\test\master.zip
PSParentPath            : Microsoft.PowerShell.Core\FileSystem::C:\Users\oztechmuse\test
PSChildName             : master.zip
PSDrive                 : C
PSProvider              : Microsoft.PowerShell.Core\FileSystem
CentralAccessPolicyId   :
CentralAccessPolicyName :
Path                    : Microsoft.PowerShell.Core\FileSystem::C:\Users\oztechmuse\test\master.zip
Owner                   : DESKTOP-IRRKDNQ\David Glance
Group                   : DESKTOP-IRRKDNQ\None
Access                  : {System.Security.AccessControl.FileSystemAccessRule, System.Security.AccessControl.FileSystemAccessRule, System.Security.AccessControl.FileSystemAccessRule}
Sddl                    : O:S-1-5-21-99674670-1004200984-2391121708-1000G:S-1-5-21-99674670-1004200984-2391121708-513D:(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;FA;;;S-1-5-21-99674670-1004200984
                          -2391121708-1000)
AccessToString          : NT AUTHORITY\SYSTEM Allow  FullControl
                          BUILTIN\Administrators Allow  FullControl
                          DESKTOP-IRRKDNQ\David Glance Allow  FullControl
AuditToString           :
AccessRightType         : System.Security.AccessControl.FileSystemRights
AccessRuleType          : System.Security.AccessControl.FileSystemAccessRule
AuditRuleType           : System.Security.AccessControl.FileSystemAuditRule
AreAccessRulesProtected : False
AreAuditRulesProtected  : False
AreAccessRulesCanonical : True
AreAuditRulesCanonical  : True
```

There is a great deal of information that is provided in the output of this, but essentially it will let you know which users and groups have access to the file. Note the difference betweeen Windows and Linux - multiple groups can be specified as having access to a Windows file or directory whereas on Linux you only specify one group.

Note that on Windows, you can right click on a file and view properties to see the permissions under the security tab. 

Changing permissions on a file in Windows is easiest through File Explorer. If you want to do it in PowerShell, you can do it as follows:

```bash
PS \test> $newacl = Get-Acl .\afile.txt
PS \test> $isProtected = $true
PS \test> $preserveInheritance = $true
PS \test> $newacl.SetAccessRuleProtection($isProtected, $preserveInheritance)
PS \test> Set-Acl .\afile.txt -AclObject $newacl
```



