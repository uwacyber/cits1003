# Part 1 - Linux and Networking (<font color="red">Bad</font>)
## Penguin OS Part 1: For the FTP
### Step1 
**"nmap -Pn 34.166.68.59": Used "nmap" command to scan the IP address to find the port running FTP server which was "2121/tcp open ccproxy-ftp" i.e the port number was 2121.**

### Step2
**"ftp 34.166.68.59 -p 2121": Used ftp command to connect to the IP address and used "anonymous" as the user name to login.** 

### Step3
**Using "ls" found a txt file called "note-to-flipper-pals.txt" and used "GET" command to download it onto my system.**


#### Flag Found In the Downloaded file
```bash
UWA{fTpLipP3r5}
```
<div style="page-break-after: always;"></div>

# Part 1 - Linux and Networking (<font color="red">Average</font>)
## Penguin OS Part 1: For the FTP
### Step 1
I employed "nmap" to scan available ports: **nmap -sC -sV -Pn 34.116.68.59**, where "-sC" enables Nmap default script scanning; "-sV" instructs Nmap to perform version detection against the target services; "-Pn" tells Nmap not to perform host discovery. Based on the output, FTP server operates on port 2121.

### Step 2
I connected to the server via "anonymous login", which does not require a specific username and password: **ftp 34.116.68.59 -p 2121**. 

### Step 3
I utilised the "ls" command to list visible files and found a file titled **note-to-flipper-pals.txt**. The result is:

**-r-xr-xr-x 1 0        0             152 Apr 09 10:05 note-to-flipper-pals.txt**
**226 Directory send OK.**

### Step 4
I used the command "get" to enable the downloading of files from the FTP server to my local machine: **get note-to-flipper-pals.txt**.

### Step 5
I entered the "exit" command, which disconnects from the FTP server. 

### Step 6
The file "note-to-flipper-pals.txt" is downloaded into the directory where I initiated the FTP session. I examined its contents via "cat": **cat note-to-flipper-pals.txt**.

The result is: **Hello all of my flipper friends! If you want to access my Penguin OS, you will need to SSH with the following credentials.**
**penguinusr:UWA{fTpLipP3r5}**

#### Flag Found
```
UWA{fTpLipP3r5}
```

<div style="page-break-after: always;"></div>


# Part 1 - Linux and Networking (<font color="red">Excellent</font>)
## Penguin OS Part 1: For the FTP
### Step 1: Determining the FTP Server's Port
As the FTP server's port has been altered, identifying the port it operates on became a priority. To accomplish this, I employed `nmap`, a tool for port scanning.

#### Command:
```bash
nmap -sC -sV -Pn 34.116.68.59
```
#### Explanation of Flags:
- `-sC`: Enables `nmap` default script scanning.
- `-sV`: Instructs `nmap` to perform version detection against the target services.
- `-Pn`: Tells `nmap` not to perform host discovery.

#### Result:
```bash
Nmap scan report for 59.68.116.34.bc.googleusercontent.com (34.116.68.59)
PORT      STATE  SERVICE  VERSION
2121/tcp  open ftp      vsftpd 3.0.5 # [1]
2222/tcp  open ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
```

### Step 2: Connecting to the FTP Server
In Step 1, FTP server operates on port 2121 [1], I connected to it via `anonymous login`, which refers to a special type of login where a user logs in without a specific username and password. 

#### Command:
```bash
ftp 34.116.68.59 -p 2121
```

#### Result:
```bash
Connected to 34.116.68.59.
220 (vsFTPd 3.0.5)
Name (34.116.68.59:laptop): ftp # user is 'ftp'
331 Please specify the password.
Password: # the password I used was 'ftp', same as the username
230 Login successful.
```

### Step 3: Listing Available Files
I utilised the `ls` [1] command to list visible files and found a file titled `note-to-flipper-pals.txt`. Here's the breakdown of what I discovered:

#### Command:
```bash
ftp> ls # [1]
```

#### Result:
```bash
-r-xr-xr-x 1 0        0             152 Apr 09 10:05 note-to-flipper-pals.txt
226 Directory send OK.
```

### Step 4: Retrieving the File
I used the command `get` to enable the downloading of files from the FTP server to my local machine. Here's how I used the `get` command to retrieve the file `note-to-flipper-pals.txt`:

#### Command:
```bash
ftp> get note-to-flipper-pals.txt
```

### Step 5: Exiting the FTP Session
I entered the `exit` command, which disconnects from the FTP server. 

### Step 6: Examining File Contents
The file `note-to-flipper-pals.txt` is downloaded into the directory where I initiated the FTP session. I examined its contents via `cat`. 

#### Command:
```bash
cat note-to-flipper-pals.txt
```

#### Result:
```bash
Hello all of my flipper friends!

If you want to access my Penguin OS, you will need to SSH with the following credentials.
penguinusr:UWA{fTpLipP3r5}
```
The provided credentials for SSH access are:

**Username**: `penguinusr`
**Password**: `UWA{fTpLipP3r5}`

These credentials would grant access to the Penguin OS, indicating a potential pathway for further exploration or analysis.

#### Flag Found
```
UWA{fTpLipP3r5}
```