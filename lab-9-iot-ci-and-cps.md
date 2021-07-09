# Lab 9: IoT CI & CPS

A challenge of dealing with IoT and Cyberphysical Systems in general is that the software runs on specific hardware rather than general purpose computers. Also, there are a number of different operating systems that these devices can use.  IoT are different from normal computers in that they have less resources like memory to operate with and usually are diskless. 

Having said that, a large number of consumer devices operate on a linux or linux-like system and so that makes analysis of these devices and even software emulation somewhat simpler. 

IoT have a history of poor security. One of the principle areas of concern, and one we will look at in this lab has been the use of hard-coded passwords for remote access to the devices and leaving access to those services open by default.

## Examining firmware 

In this exercise, we are going to be looking at the firmware from a Netgear Wireless Router the WNAP320 which was a consumer wireless router which went on sale in 2010 but was available for several years after that. Like all consumer router devices, it provides a web interface to administer the device. It also supports remote access using Telnet and SSH which are not enabled by default. The administration function is normally accessed by being on the local network or by using a direct cable to connect to the device. Some details of the device are provided here: [https://usermanual.wiki/Netgear/NetgearWnap320QuickReferenceGuide.33658341/html](https://usermanual.wiki/Netgear/NetgearWnap320QuickReferenceGuide.33658341/html)

The device ships with a default username of **admin** and a password of **password**. This is already a problem because a large number of users would leave the device configured with the defaults and never change them.

Let us start by using the docker container as follows

```bash
docker run -p 8000:8000 -it cybernemosyne/cits1003:iot 
```

Change directory to /opt/samples/WNAP320

In that directory is a ZIP file which is the firmware for the WNAP320 router \(alternatively, you can still download the firmware from Netgear http://www.downloads.netgear.com/files/GDC/WNAP320/WNAP320%20Firmware%20Version%202.0.3.zip\)

Let us unzip the file and see what it contains

```bash
> unzip WNAP320\ Firmware\ Version\ 2.0.3.zip 
Archive:  WNAP320 Firmware Version 2.0.3.zip
  inflating: ReleaseNotes_WNAP320_fw_2.0.3.HTML  
  inflating: WNAP320_V2.0.3_firmware.tar  
```

The file WNAPP320V2.0.3\_firmware.tar file is another archive file \(colloquially called a tarball\). We can extract this using the tar utility:

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

It turns out that there is a vulnerability in a number of these files that allows for remote command execution \(RCE\) that has the CVE CVE-2016-1555. The exploit code is listed on exploit-db here [https://www.exploit-db.com/exploits/45909](https://www.exploit-db.com/exploits/45909)

One of the affected files is boardDataWW.php and the specific code at fault is:

```php
		if (!empty($_REQUEST['macAddress']) && array_search($_REQUEST['reginfo'],Array('WW'=>'0','NA'=>'1'))!==false && ereg("[0-9a-fA-F]{12,12}",$_REQUEST['macAddress'],$regs)!==false) {
			//echo "test ".$_REQUEST['macAddress']." ".$_REQUEST['reginfo'];
			//exec("wr_mfg_data ".$_REQUEST['macAddress']." ".$_REQUEST['reginfo'],$dummy,$res);
			exec("wr_mfg_data -m ".$_REQUEST['macAddress']." -c ".$_REQUEST['reginfo'],$dummy,$res);
```

This code file is responsible for showing this page to capture a MAC address for the device:

![Screen handled by boardDataWW.php](.gitbook/assets/screen-shot-2021-07-09-at-2.26.16-pm.png)

When the user enters a MAC address and clicks the submit button, the code above checks that it has been sent a valid MAC address \(12 characters, alphanumeric\) and a region code, and then it passes that to a command line utility called wr\_mfg\_data. If the MAC address was f8ffc201fae5 and region code was 1, the command that would be executed would be:

```bash
wr_mfg_data -m f8ffc201fae5 -c 1
```

You will notice that there is no validation of the input to this command by the code. It just checks that the first 12 characters of the MAC address are alphanumeric. This means we can add data to the end of a valid MAC address and it will accept it. So if  we add a 

