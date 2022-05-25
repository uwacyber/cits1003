# Lab 1: Setting up your laptop

Walkthrough video:

Please NOTE, the walkthrough videos are for the guidance only, remember to use the lab materials provided in this labsheet, not from the walkthrough video!

**Docker and Bash 1-1** [https://www.youtube.com/watch?v=4vl4aUxo8Hk](https://www.youtube.com/watch?v=4vl4aUxo8Hk)

## Getting started

We will set up various software that will be used in the labs, with the main one being _**Docker Desktop**_. However, it is a good idea to create a folder specifically for organising the different week's labs.

There are three different ways to setup your lab environment:

1. Using VM (recommended, industry best practice).
2. Using your Host (could be dangerous, only for those of you who know what you are doing).
3. Using Cloud (e.g., Azure, Google Cloud, AWS etc.).

#### See below if you are planning to use VM.

![](../.gitbook/assets/1003\_vm\_route.png)

#### See below if you are planning to use Host.

![](../.gitbook/assets/1003\_host\_route.png)

If you are planning to use the cloud, see [section 2.2.](setting-up-your-laptop.md#2.2.-running-windows-10-on-azure)

## 1. Setting up a Virtual Machine (VM) to do labs

It is recommended to run the labs inside the VM for security (this adds another layer of protection, and as well as in an unlikely event where you break any configurations that could affect your host computer), especially for ones where we are handling live malware samples (e.g., labs 7 and 10). The malware samples are not capable of breaking out of docker containers to affect your host machine, but in general, it is a good idea to handle them inside a VM just in case you accidentally run them - this is also how it is done in the industry.

### 1.1. Windows/MacOS (non-M1)/Linux

There are many VM software you can use, such as VirtualBox, VMWare, etc. You can use any of those, but if you don't know where to start, you can start with [VirtualBox](https://www.virtualbox.org). If this isn't working for you, you could try [VMWare Workstation Player](https://www.vmware.com/au/products/workstation-player.html). Once you have installed the VirtualBox (or something equivalent), next we need to download the VM image we want to use. [Ubuntu ](https://ubuntu.com/download#download)or [Kali Linux](https://www.kali.org) are both good choices (download `iso` file or you will find a dedicated link that they provide for VM software). You can choose other lightweight versions like [Lubuntu](https://cdimage.ubuntu.com/lubuntu/releases/20.04/release/) if you prefer. When specifying the disk size, assign 20GB disk space. It won't fully occupy 20GB on your machine, as the size will dynamically adjust as you use it.

{% hint style="info" %}
FYI, I am using Lubuntu - 1CPU and 2GB RAM and albeit a bit slow, I have tested and ran all labs.

For the Ubuntu image, 2CPU and 4GB RAM is recommended.
{% endhint %}

For some labs, you would want to provide more RAM and CPU provided your computer has more RAM and CPU to work with. These can be done in the settings (but remember to shut down the VM to do this).

You might want to look up an installation guide online, such as this for Ubuntu: [https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview)

{% hint style="info" %}
Sometimes the VM will freeze. You might want to reset (Machine -> Reset) and it _usually_ fixes the issue. If not, you can try shutting down and restarting the VM. You may have to repeat this a few times. Some common solutions include:

* changing the graphics controller (trial and error)
* adding more RAM (don't need more than 2 CPU)
* adding more storage (20GB -> 30GB)
{% endhint %}

Once you have successfully installed and launched Ubuntu, it should bring up a GUI! It may ask you to update, which you should (improves user experience on VM). Once this is done, you can carry on with the labs as instructed.

Now, go to [`Section 3.1. Installing Docker Desktop`](setting-up-your-laptop.md#3.1.-installing-docker-on-ubuntu-on-your-vm)

### 1.2. M1 MacBook Users

Unfortunately, there are currently a limited number of options running VMs on M1 (Apple Silicon) MacBooks due to technical issues and challenges. Fortunately, There are a few options for you to choose from.

#### 1. VMWare has released a free version, please check here:

[https://blogs.vmware.com/teamfusion/2021/09/fusion-for-m1-public-tech-preview-now-available.html](https://blogs.vmware.com/teamfusion/2021/09/fusion-for-m1-public-tech-preview-now-available.html)

#### 2. UTM is also a possible VM solution:

[https://mac.getutm.app/](https://mac.getutm.app)

Virtualisation techniques are getting better as vendors are trying to address those issues, but it may still not work for the purpose of our labs. You will be safe to do most labs, but we highly recommend doing labs 7 and 10 with your friend or using a different laptop with VMs available if the above options are not working for you.

You are also recommended to install **Kali Linux**, as Ubuntu seems to be having issues that are not easily solvable currently.

Now, go to [`Section 3.1. Installing Docker Desktop`](setting-up-your-laptop.md#3.1.-installing-docker-on-ubuntu-on-your-vm)

## 2. Doing labs on your host machine

You can skip section 2 entirely if you have setup a VM to do the labs. But later if you decided to do some labs on your host machine, you can come back here and follow the instructions.

### 2.1. Windows

The first step is to install WSL2 on Windows. Open **administrator** PowerShell or Windows Command Prompt and type in:

```
wsl --install
```

Once complete, restart your machine.

To test this out, type `wsl` in the search bar and run the command prompt.

Now, go to [`Section 3.1. Installing Docker Desktop`](setting-up-your-laptop.md#3.1.-installing-docker-on-ubuntu-on-your-vm)

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

Now you can treat this cloud desktop as your host. If you selected a Windows VM, then go to [`Section 2.1. Windows`](setting-up-your-laptop.md#2.1.-windows-users-only-installing-windows-subsystem-for-linux-wsl), otherwise go to [`Section 3.1. Installing Docker Desktop`](setting-up-your-laptop.md#3.1.-installing-docker-on-ubuntu-on-your-vm)

### 2.3. Apple Mac M1 (Apple Silicon) Users: Enable Rosetta

Apple's computers are increasingly using the new M1 chip (ARM architecture) that uses a different instruction set than the Intel-based Macs (AMD architecture). Apple allows programs built for the Intel chip to run by using an emulator called Rosetta 2. If you have not already installed it, then:

1. Open a Terminal window
2. Type (paste) the command `/usr/sbin/softwareupdate --install-rosetta --agree-to-license`

Once this is done, you can proceed with installing and running Docker Desktop (below).

Whilst most of the Docker images in the labs can be run on the Apple M1, there may be warnings given about the platform (you may be able to avoid this warning by passing the argument `--platform linux/amd64`). We have created a multi-platform version for some images, which should be auto-selected when those images are used.

Now, go to [`Section 3.1. Installing Docker Desktop`](setting-up-your-laptop.md#3.1.-installing-docker-on-ubuntu-on-your-vm)

## 3. Installing and running Docker Desktop

We will be using a technology called _Docker Desktop_ to run different environments on your laptop. Unfortunately, this environment will not be available on the lab machines, so we will try and provide an alternative for people who want to use the lab machines. You will learn more about this in CITS2003, but for the sake of this unit, you do not need to understand how and why this works.

You can get a more comprehensive overview of what Docker is from here [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/). To summarise though, Docker allows you to "package and run an application in a loosely isolated environment called a container". Containers are a way of virtualizing an environment by using the native operating system's functionality to isolate application environments.

### 3.1. Installing Docker Desktop (Windows/Mac/Linux)

{% hint style="warning" %}
If you have installed a VM, install Docker Desktop inside your VM.
{% endhint %}

The process for installing Docker Desktop is straightforward and involves using the installer for the particular operating system you have (from the drop-down menu, select the appropriate OS):

{% embed url="https://www.docker.com/get-started" %}

#### 3.1.1. Another method for Ubuntu

You can also install docker on Ubuntu without the Docker Desktop. Run the following two lines (line by line) of code in your terminal and wait for it to install:

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

The full instruction can be found here: [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)

Now go to [`Section 3.2. Testing Docker`](setting-up-your-laptop.md#3.3-testing-docker)\`\`

### 3.2. Testing Docker

To test the environment, we will run a simple container that allows you to access a bash terminal. This allows you to enter commands that get executed within the container. You can only do what the container will let you do as it is a constrained environment.

To start with, make sure that your Docker Desktop application is running. Once it is, open a terminal window, PowerShell or Command prompt and run the following command (please note, the process may take a while on your machine).

{% hint style="warning" %}
All commands are treated as running from the VM. If running from the host, remove `sudo` at the beginning if it complains it cannot find `sudo`.
{% endhint %}

```
sudo docker pull uwacyber/cits1003-labs:bash
```

```
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

```
sudo docker run -it uwacyber/cits1003-labs:bash
```

Once the container is running, you can try the below command (first line only, second line is the output) in the terminal:

```
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

```
sudo docker run -it --rm uwacyber/cits1003-labs:bash
```

This will automatically remove the container so you don't have to go to GUI to do it (of course, nothing you do in this container will be saved).

If you saved the container (i.e., not using the `--rm` flag) and wants to restart that container that has stopped, first find the container ID you want to restart:

```
sudo docker ps -a
```

Next, restart the container:

```
sudo docker start -ai container_id
```

Here, the container ID is retrieved from the first column from the previous step (copy and paste).

Finally, once you have finished with a container, you can remove the container that was saved by:

```
sudo docker rm container_id
```

Remember that anything you have done in the container will be lost when you remove the container.

You can also delete the image downloaded from the Docker Desktop GUI, or from the command line find the image ID (column `IMAGE ID`):

```
sudo docker images
```

Delete the docker image:

```
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

## Case study: The World’s First Data Embassy

“Through its e-Estonia initiative, Estonia has built a digital society and developed the most technologically advanced government in the world. Practically every government service is paperless and performed electronically. As a result, Estonia is highly dependent on its information systems and the data stored on them. To protect its data, Estonia developed the concept of data embassies – servers outside the country that are legally under Estonian jurisdiction. The digital copies of key databases they store can be accessed in the event of a major data incident in the country, thereby protecting the digital lifeblood of this small Nordic country. Estonia is on its way to becoming a “country without borders”, and the data embassy is one of several Estonian programmes that blurs the lines of national borders and sovereign identity in a digital world.”

Read through the following article and answer the questions below: [https://www.oecd.org/gov/innovative-government/Estonia-case-study-UAE-report-2018.pdf](https://www.oecd.org/gov/innovative-government/Estonia-case-study-UAE-report-2018.pdf)

### Question 2. CIA

The ​​2007 wave of cyber attacks against Estonian government agencies, banks and media websites were in the form of Distributed Denial of Service (DDoS) attacks. These resulted in disruptions to the display of Estonian internet sites. This is primarily a violation of which aspect of cybersecurity?

* Confidentiality
* Integrity
* Availability
* Authentication
* Accountability

{% hint style="info" %}
Submit your flag with the correct answer (e.g., `CITS1003{Confidentiality}` if option 1 was the correct answer).
{% endhint %}

### Question 3. Authentication types

In Estonia, every citizen receives an electronic-ID in the form of an 11 digit personal identification number from the government. The ID is additionally issued with PIN codes enabling the person to use e-ID functionalities such as accessing state and private sector e-services. Primary electronic identification comes with a physical ID card, which is a mandatory identification document in Estonia. This form of identification can also be carried oute digitally, such as via mobile-ID. Additionally, during the application for obtaining this card, the applicant must be physically identified by Police and Border Guard officials at least once during the application process. Based on solely the above information, which type of authentication does this electronic-ID provide?

Note, the types are referred in the lecture slides.

* Type 1
* Type 2
* Type 3
* Type 4

{% hint style="info" %}
Submit your flag with the correct answer, replacing spaces with underscores (e.g., `CITS1003{Type_1}` if option 1 was the correct answer).
{% endhint %}

### Question 4. CIA returns

The article describes data centers in Estonia and Luxembourg and the associated challenges in keeping data in sync across them. One possible method could be providing object metadata by default for every object stored in the data center. This may include the entry date, content length, the last modified date and a hash of the content. Dissimilarities in metadata between data centers for the same object could help detect discrepancies. This measure would help maintain which aspect of cybersecurity?

* Confidentiality
* Integrity
* Availability
* Authorisation
* Non-repudiation
