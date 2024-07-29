# Lab 1: Setting up your laptop

## 1. The easiest way to set up VMs for labs START HERE FIRST!

What follows below is if you want to install VMWare and Kali basically from scratch. I have provided ready-made images however of ParrotOS and made download of VMWare for Mac and Windows available. So to install on Windows, just download VMWare Workstation and then the Intel version of the ParrotOS VM. For Mac, install VMWare Fusion Pro and if you have a new mac install the "arm" version of ParrotOS. If you have an old Intel-based Mac, then the Intel version - same as windows.

VMWare for Mac https://cits1003-vmware.s3.ap-southeast-2.amazonaws.com/VMware-Fusion-13.5.2-23775688_universal.dmg  
VMWare for Windows: https://cits1003-vmware.s3.ap-southeast-2.amazonaws.com/VMware-workstation-full-17.5.2-23775571.exe


VM for Mac with Apple Silicon: https://cits1003-vms.s3.ap-southeast-2.amazonaws.com/arm64/ParrotOS.vmwarevm.zip  
VM for Windows and Intel Mac: https://cits1003-vms.s3.ap-southeast-2.amazonaws.com/intel/ParrotOS.vmwarevm.zip

The username and password for the VMs is:


username: wsuser
password: ws1003admin


If you don't want to do this - then read all that follows:

**Walkthrough video**:

Please NOTE, the walkthrough videos are for the guidance only, remember to use the lab materials provided in this labsheet, not from the walkthrough video!

**Docker and Bash 1-1** [https://www.youtube.com/watch?v=4vl4aUxo8Hk](https://www.youtube.com/watch?v=4vl4aUxo8Hk)

## Getting started

We will set up various software that will be used in the labs, with the main one being _**Docker**_. However, it is a good idea to create a folder specifically for organising the different week's labs.

There are three different ways to setup your lab environment:

1. Using VM (recommended, industry best practice).
2. Using your Host (could be dangerous, only for those of you who know what you are doing).
3. Using Cloud (e.g., Azure, Google Cloud, AWS etc.).

#### See below if you are planning to use VM.

![](../.gitbook/assets/1003\_vm\_route.png)

#### See below if you are planning to use Host.

![](../.gitbook/assets/1003\_host\_route.png)

If you are planning to use the cloud, see [section 2.2](lab-1-setting-up-your-laptop.md#id-2.2.-cloud-desktop).

## 1. Setting up a Virtual Machine (VM) to do labs

A VM is a piece of software that allows you to emulate or virtualise an operating system such as Windows or a distribution of GNU/Linux. It is recommended to run the labs inside a VM for security (this adds another layer of protection, and as well as in an unlikely event where you break any configurations that could affect your host computer), especially for ones where we are handling live malware samples (e.g., labs 7 and 10). The malware samples are not capable of breaking out of docker containers to affect your host machine, but in general, it is a good idea to handle them inside a VM just in case you accidentally run them - this is also how it is done in the industry.

For the labs, you will work in an Linux based operating system inside of a VM. Operating systems are often distributed as installer images (`iso` file format) which will need to be manually installed, or pre-built VM images which can be directly imported into a VM without installation. Since VM images do not require installation, we will use this where possible.

Please refer to [section 1.1](lab-1-setting-up-your-laptop.md#id-1.1.-windows-macos-non-m1-linux) or [1.2](lab-1-setting-up-your-laptop.md#id-1.2.-m1-m2-etc.-macbook-users) for specific set up instructions for your system.

### 1.1. Windows/MacOS (non-M1)/Linux

There are many VM software you can use, such as VirtualBox, VMWare, etc. You can use any of those, but if you don't know where to start, you can start with [VirtualBox](https://www.virtualbox.org). If this isn't working for you, you could try [VMWare Workstation Player](https://www.vmware.com/au/products/workstation-player.html).

Once you have installed the VirtualBox (or something equivalent), we need to download the VM image we want to use. [Kali Linux](https://www.kali.org) (preferred) or [Ubuntu](https://ubuntu.com/download#download) are both good choices. You can choose other lightweight versions like [Lubuntu](https://cdimage.ubuntu.com/lubuntu/releases/20.04/release/) if you prefer.

For Kali Linux, you can directly download the VM image for VirtualBox [here](https://cdimage.kali.org/kali-2023.4/kali-linux-2023.4-virtualbox-amd64.7z) or VMWare [here](https://cdimage.kali.org/kali-2023.4/kali-linux-2023.4-vmware-amd64.7z). A `.7z` file will start downloading. This type of file (short for 7zip) is a file archive format which allows multiple files and directories to be compressed into a single archive file. The Kali Linux VM image will be inside the 7zip archive we are downloading. Once the 7zip archive is downloaded, you will need to extract the VM image. On Windows, you might need to install the [7-zip software](https://www.7-zip.org/download.html) to perform the extraction.

Now, you will need to import the VM image into your VM.

**The username and password for the pre-built Kali VM image is both `kali`.**

{% hint style="info" %}
When specifying the disk size, assign 30GB disk space. It won't fully occupy 30GB on your machine, as the size will dynamically adjust as you use it.

FYI, I tested using Lubuntu - 1CPU and 2GB RAM and albeit a bit slow, I have successfully ran all labs.

For the Kali or Ubuntu image, 2CPU and 4GB RAM is recommended.
{% endhint %}

For some labs, you would want to provide more RAM and CPU provided your computer has more RAM and CPU to work with. These can be done in the settings (but remember to shut down the VM to do this).

{% hint style="info" %}
Sometimes the VM will freeze. You might want to reset (Machine -> Reset) and it _usually_ fixes the issue. If not, you can try shutting down and restarting the VM. You may have to repeat this a few times. Some common solutions include:

* changing the graphics controller (trial and error)
* adding more RAM (don't need more than 2 CPU)
* adding more storage (20GB -> 30GB)
{% endhint %}

Once you have imported a pre-built Linux VM image or manually installed a Linux distribution onto your VM, you can carry on with the labs as instructed.

Now, go to [`Section 3.1. Installing Docker`](lab-1-setting-up-your-laptop.md#id-3.1.-installing-docker-windows-mac-linux)

### 1.2. M1/M2 etc. MacBook Users

For M1/B2 Macs, you will need to use the VM UTM. You can download it here: [https://mac.getutm.app/](https://mac.getutm.app)

The Kali VM on UTM runs all labs as intended, so this should work for you for this unit.

The Apple Silicon laptops have fundamentally different CPU architecture which causes some issues, but for the purpose of this unit, it will just be fine.

You are also recommended to install **Kali Linux**, but you can use other generic OSes such as Ubuntu. You can find useful instructions for creating a Kali VM in UTM here:

[https://mac.getutm.app/gallery/kali-2023](https://mac.getutm.app/gallery/kali-2023)

{% hint style="info" %}
If you have a black screen when installing Kali, please go to settings and "+ New..." in Devices, and add Serial. Then start the VM, you can install using the Serial (terminal). Once the installation is finished, you can remove the Serial device.

If you have a blue screen after installing Kali, please go to settings -> Display -> Emulated Display Card, and select any non-GUI options (e.g., virtio-ramfd).
{% endhint %}

Now, go to [`Section 3.1. Installing Docker`](lab-1-setting-up-your-laptop.md#id-3.1.-installing-docker-windows-mac-linux)

## 2. Doing labs on your host machine

You can skip section 2 entirely if you have setup a VM to do the labs. But later if you decided to do some labs on your host machine, you can come back here and follow the instructions.

Please note, this is NOT the recommended way of setting it up, but it might be useful if your laptop is not sufficiently powered to run VMs.

### 2.1. Windows

The first step is to install WSL2 on Windows. Open **administrator** PowerShell or Windows Command Prompt and type in:

```
wsl --install
```

Once complete, restart your machine.

To test this out, type `wsl` in the search bar and run the command prompt.

Now, go to [`Section 3.1. Installing Docker`](lab-1-setting-up-your-laptop.md#id-3.1.-installing-docker-windows-mac-linux)

### 2.2. Cloud desktop

If you are unable to get your laptop/PC working, another option is to run Windows 10 on a Virtual Machine on Azure. However, if we are going to use a cloud (i.e., Azure), then you can install Ubuntu on it instead of putting on a Windows image and setting up WSL and docker. Nevertheless, to do this, you will need a student account created on https://portal.azure.com/.

{% hint style="info" %}
Alternate cloud providers include Google Cloud, Amazon AWS etc.
{% endhint %}

You can create a VM using Windows 10 Pro 21 H1 and pick a Standard\_D2s\_V3 machine. Use all of the default settings but select Australia as the region to run it in (if you are located internationally, pick a region close to you).

Once created, you can connect to the machine via remote desktop and then configure the machine as above.

{% hint style="warning" %}
Although you have credit when creating a student account, be careful with the machine and stop it running by using the console when you are not using it - that way you will not be charged for the time you are not using it.
{% endhint %}

Now you can treat this cloud desktop as your host. If you selected a Windows VM, then go to [`Section 2.1. Windows`](lab-1-setting-up-your-laptop.md#id-2.1.-windows), otherwise go to [`Section 3.1. Installing Docker`](lab-1-setting-up-your-laptop.md#id-3.1.-installing-docker-windows-mac-linux)

### 2.3. Apple Mac M1 (Apple Silicon) Users: Enable Rosetta

Apple's computers are increasingly using the new M1 chip (ARM architecture) that uses a different instruction set than the Intel-based Macs (AMD architecture). Apple allows programs built for the Intel chip to run by using an emulator called Rosetta 2. If you have not already installed it, then:

1. Open a Terminal window
2. Type (paste) the command `/usr/sbin/softwareupdate --install-rosetta --agree-to-license`

Once this is done, you can proceed with installing and running Docker (below).

Whilst most of the Docker images in the labs can be run on the Apple M1, there may be warnings given about the platform (you may be able to avoid this warning by passing the argument `--platform linux/amd64`). We have created a multi-platform version for some images, which should be auto-selected when those images are used.

Now, go to [`Section 3.1. Installing Docker`](lab-1-setting-up-your-laptop.md#id-3.1.-installing-docker-windows-mac-linux)

## 3. Installing and running Docker

We will be using a technology called _Docker_ to run different environments on your laptop. Unfortunately, this environment will not be available on the lab machines, so you will have to bring your own device. For the sake of this unit, you do not need to understand how and why this works.

You can get more comprehensive overview of what Docker is from here [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/). To summarise though, Docker allows you to "package and run an application in a loosely isolated environment called a container". Containers are a way of virtualizing an environment by using the native operating system's functionality to isolate application environments.

### 3.1. Installing Docker (Windows/Mac/Linux)

{% hint style="warning" %}
If you have installed a VM, install Docker inside your VM.
{% endhint %}

Docker on Kali and Ubuntu linux can be installed by running the following commands:

```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable docker --now
```

An official guide for getting started with Docker can be found below:

{% embed url="https://www.docker.com/get-started" %}

Now go to [`Section 3.2. Testing Docker`](lab-1-setting-up-your-laptop.md#id-3.2.-testing-docker)

### 3.2. Testing Docker

To test the environment, we will run a simple container that allows you to access a bash terminal. This allows you to enter commands that get executed within the container. You can only do what the container will let you do as it is a constrained environment.

To start with, make sure that your Docker Desktop application is running. Once it is, open a terminal window, PowerShell or Command prompt and run the following command (please note, the process may take a while on your machine).

{% hint style="warning" %}
All commands are treated as running from the VM. If running from the host, remove `sudo` at the beginning if it complains it cannot find `sudo`.
{% endhint %}

```bash
sudo docker pull uwacyber/cits1003-labs:bash
```

```bash
bash: Pulling from uwacyber/cits1003-labs
a31c7b29f4ad: Pull complete
56dc59d71033: Pull complete
2bfc36697d0c: Pull complete
9f3f7e1eed32: Pull complete
6f99373aa497: Pull complete
2bd679cc1668: Pull complete
312a9631755e: Pull complete
Digest: sha256:3aa1540adfa7a7bdd8e0955845e24372d2a7a28d5a9aa45f957abc9714a29aa2
Status: Downloaded newer image for uwacyber/cits1003-labs:bash
docker.io/uwacyber/cits1003-labs:bash
```

```bash
sudo docker run -it uwacyber/cits1003-labs:bash
```

Once the container is running, you can try the below command (first line only after the `#`, second line is the expected output) in the terminal:

```bash
root@9215e663eb9d:/# whoami
root
```

The `docker pull` command downloads the docker image to your machine. The image contains all of the files and configurations needed to run the container. You run a container using the `docker run` command as shown above.

In the case of the bash container, to stop it, you simply type `exit`. Other containers can be stopped using the `docker stop` command from another terminal. To do this, you need to provide the Container ID which you can do as follows:

```bash
0x4447734D4250:~$ sudo docker ps -a
CONTAINER ID   IMAGE                         COMMAND       CREATED         STATUS         PORTS     NAMES
45fe3a838ef0   uwacyber/cits1003-labs:bash   "/bin/bash"   3 minutes ago   Up 3 minutes             hungry_hodgkin
0x4447734D4250:~$ docker stop 45fe3a838ef0
45fe3a838ef0
```

By simply quitting with command `exit`, it saves the container. If you wish to remove the container automatically when you finish the session, add the `--rm` flag (this will be added in the examples by default):

```bash
sudo docker run -it --rm uwacyber/cits1003-labs:bash
```

This will automatically remove the container so you don't have to go to GUI to do it (of course, nothing you do in this container will be saved).

If you saved the container (i.e., not using the `--rm` flag) and wants to restart that container that has stopped, first find the container ID you want to restart:

```bash
sudo docker ps -a
```

Next, restart the container:

```bash
sudo docker start -ai container_id
```

Here, the container ID is retrieved from the first column from the previous step (copy and paste).

Finally, once you have finished with a container, you can remove the container that was saved by:

```bash
sudo docker rm container_id
```

Remember that anything you have done in the container will be lost when you remove the container.

You can also delete the image downloaded from the Docker Desktop GUI, or from the command line find the image ID (column `IMAGE ID`):

```bash
sudo docker image ls
```

Delete the docker image:

```bash
sudo docker rmi image_id
```

We will be using containers in the various labs and so you will learn more about using Docker and how containers work generally as we proceed.

### Question 1. Find your first flag

Go back to the bash docker container. There is a file called flag.txt hidden somewhere. Can you find it?

{% tabs %}
{% tab title="" %}
Click on the Hint tab to reveal the solution
{% endtab %}

{% tab title="Hint" %}
{% hint style="info" %}
To find the file, we will first go to the home directory of the user root by using the

> cd /root

command. This will change the current directory to /root

Once there, we can list the contents of that directory by using the **ls** command (don't worry about the meaning of "-al" flag for now)

> ls -al

There will be a file called flag.txt in the directory. We can view the contents of the file by using the **cat** command:

> cat flag.txt
{% endhint %}
{% endtab %}
{% endtabs %}

**Flag: Submit the flag on the CTF server that you just found!**

## Case study: Mainstream cyber attacks: data breach

A data breach is an incident in which sensitive, protected, or confidential information is accessed, disclosed, or stolen without authorization. This can include personal information such as names, addresses, and Social Security numbers, as well as financial information such as credit card numbers and bank account information.

Data breaches can occur in various ways, such as hacking into a computer system, stealing physical devices containing data, or social engineering techniques like phishing emails or phone calls. The consequences of a data breach can be severe, including financial loss, damage to reputation, and potential legal liability.

Read through the following article and answer the questions below: [https://webo.digital/blog/optus-medibank-data-breaches-cyber-security](https://webo.digital/blog/optus-medibank-data-breaches-cyber-security)

### Question 2. CIA

Which aspect of cybersecurity do the cyber attacks primarily violate?

1. Confidentiality
2. Integrity
3. Availability
4. Authentication
5. Non-repudiation

{% hint style="info" %}
Submit your flag with the correct answer (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}

### Question 3. How was Optus compromised?

Which is the reason given by third-parties about how Optus was compromised?

1. Advanced Persistent Threat (APT) attacks
2. Scams such as spam text messages, phishing emails, etc.
3. Lack of authentication and authorization
4. None of the above

{% hint style="info" %}
Submit your flag with the correct answer (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}

### Question 4. Mitigation

What should be done to safeguard businesses from data breaches?

1. Implement, monitor and update customized IT policies and protocols
2. Enforce mandatory multi-factor authentication
3. Encrypt user data in an end-to-end way
4. All of the above

{% hint style="info" %}
Submit your flag with the correct answer (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}
