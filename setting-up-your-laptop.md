# Setting up your laptop

We will set up various software that will be used in the labs, the principle one being Docker Desktop. However, it is a good idea to create a folder specifically for organising the different week's labs. 

## Windows users: Installing Windows Subsystem for Linux 

This is a necessary step for the unit and also for running Docker Desktop. There are instructions for this on the web e.g. here: [https://andrewlock.net/installing-docker-desktop-for-windows/](https://andrewlock.net/installing-docker-desktop-for-windows/)

To get started, you need to launch a command prompt in Administrator mode. Search for cmd and then right click on the command prompt and select run as Administrator.

![Running Command Prompt as Administrator](.gitbook/assets/screen-shot-2021-06-30-at-10.12.47-am.png)

Then enter the following commands:

> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart 
>
> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Now type powershell to get a powershell prompt and continue with the commands:

> Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart
>
> wsl --set-default-version 2

From the Windows Store, search for and install: Ubuntu 20.04

After this, restart windows. 

To test this out, type wsl in the search bar and run the command prompt. 

## Installing and running Docker Desktop

We will be using a technology called Docker Desktop to run different environments on your laptop. Unfortunately, this environment will not be available on the lab machines and so we will try and provide an alternative for people who want to use the lab machines. 

You can get a more comprehensive overview of what Docker is from here [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/). To summarise though, Docker allows you to "package and run an application in a loosely isolated environment called a container". Containers are a way of virtualizing an environment by using the native operating system's functionality to isolate application environments.

The process for installing Docker Desktop is straightforward and involves using the installer for the particular laptop you have:

{% embed url="https://www.docker.com/get-started" %}

To test the environment, we will run a simple container that allows you to access a terminal.

First of all, make sure that your Docker Desktop application is running. Once it is, open a terminal window, PowerShell or Command prompt:

{% tabs %}
{% tab title="Windows" %}

{% endtab %}

{% tab title="Mac OSX" %}
```bash
MyComputer:~$ docker pull cybernemosyne/cits1003:powershell
Digest: sha256:691832551b79cd93e5592b54d234b89d23b253336934677e311e64eefc8b958b
Status: Image is up to date for cybernemosyne/cits1003:powershell
cybernemosyne/cits1003:powershell

0x4447734D4250:~$ docker run -it cybernemosyne/cits1003:powershell
PowerShell 7.1.3
Copyright (c) Microsoft Corporation.

https://aka.ms/powershell
Type 'help' to get help.

PS /> ls
bin  boot  dev	etc  home  lib	lib32  lib64  libx32  media  mnt  opt  proc  root  run	sbin  srv  sys	tmp  usr  var
```
{% endtab %}
{% endtabs %}

The _**docker pull**_ command downloads the docker image to your machine. The image contains all of the files and configurations needed to run the container. You run a container using the _**docker run**_ command as shown above. 

In the case of the PowerShell container, to stop it, you simply type _**exit**_. Other containers can be stopped using the _**docker stop**_ command.

Once you have finished with a container, you can remove the image that was downloaded using either the Docker Desktop GUI or by using the _**docker rm**_ command. Remember that anything you have done in the container will be lost when you remove the container. 

We will be using containers in the various labs and so you will learn more about using Docker and how containers work generally as we proceed. 

## Exercise: Find your first flag

Go back to the powershell docker container. There is a file called flag.txt hidden somewhere. Can you find it? 

&lt;details&gt;

&lt;summary&gt;You may not have learned the commands to navigate in the shell so to find the flag: Click to expand!&lt;/summary&gt;

cd /root

ls

cat flag.txt

&lt;/details&gt;




