# Lab 1: Setting up your laptop

Throughout this unit, we will use various software and the two most important being **Linux** and **Docker**. In this lab, we need to set up both.

## 1. Setting Up a Linux-based Virtual-Machine Environment

**Linux** is an operating system (OS) as Windows and MacOS. Because many modern software tools are built specifically for Linux, it is the preferred environment for professionals. Therefore, we use Linux in this unit. [Kali Linux](https://www.kali.org) is recommended as it is tailored to a cybersecurity context. You may also use other distributions, such as Ubuntu, if you are  comfortable with them. Please note that if you choose a different distribution, you are expected to manage the installation and tool configuration on your own.

A **Virtual Machine (VM)** is a piece of software that allows you to virtualize an OS different from the one you are currently running. For example, your current OS is Windows 11 and your virtualized one is Kali Linux. 

In Sections 1.1–1.3, we provide step-by-step guidance for setting up a Kali Linux VM. If you are using Windows, see [Section 1.1](lab-1-setting-up-your-laptop.md#id-1.1-windows). If you are using MacOS on an M-series chip (e.g., M1/M2/M3), see [Section 1.2](lab-1-setting-up-your-laptop.md#id-1.2-macos-apple-silicon). If you are using macOS on an Intel/AMD chip, see [Section 1.3](lab-1-setting-up-your-laptop.md#id-1.3-macos-intel-amd). If you are using Linux, you can skip ahead to [Section 2](lab-1-setting-up-your-laptop.md#id-2.-learning-the-kali-linux-bash-terminal). If you encounter any issues, ask a lab facilitator for assistance.

Before you begin, make sure your computer has at least 20 GiB of free disk space and 8 GiB of RAM. Running virtualized environments is resource-intensive. If your computer does not meet these hardware requirements, you may encounter unexpected issues.

### 1.1 Windows

For Windows, it is recommended that you use **WSL2** (Windows Subsystem for Linux) to run Linux. WSL2 allows Linux applications to run alongside Windows applications seamlessly. Your computer should be running Windows 10 (version 1903 or later) or above to support WSL2. The steps below provide a walkthrough of the setup. After finishing this subsection, go to [Section 2](lab-1-setting-up-your-laptop.md#id-2.-learning-the-kali-linux-bash-terminal).

#### Step 1: Install/Enable WSL2

Open the `Start Menu` from your Windows, enter `powershell`, and launch it. Alternatively, press `Win + R`, type `powershell`, and press Enter.

First, run the following command to ensure the system is set to use WSL2 by default:

```powershell
wsl --set-default-version 2
```

If the command above fails (or if WSL is not installed/enabled), run the command below to install/enable WSL components. Restart if prompted, then continue.

```powershell
wsl --install --no-distribution
```

#### Step 2: Install Kali Linux

You can install it directly via PowerShell:

```powershell
wsl --install kali-linux
```

Once installed, open your `Start Menu`, search for Kali Linux if it does not start automatically, and click to open it. It will take a moment to initialize and then ask you to set a username and password. An example output (for reference only) is shown below:

```text
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
Enter new UNIX username: kali
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
```

Please set the username and password to `kali` and note them down. When you type passwords, characters will not appear. This is a standard security feature. Once you see a command prompt like `kali@your-computer:~$`, this is your Kali Linux bash terminal, showing your terminal environment is ready. If you want to use the Kali bash terminal again after closing the powershell, again open your `Start Menu`, search for Kali Linux, and click to launch it.

If you are using the bash terminal for the first time, it is recommended that you walk through [Section 2](lab-1-setting-up-your-laptop.md#id-2.-learning-the-kali-linux-bash-terminal) before proceeding to the next step.

#### Step 3: Install Kali Desktop GUI

A Kali desktop environment can provide a more "native" OS experience (similar to Windows). To enable Kali desktop, run the following commands in your Kali Linux bash terminal (to help you with the installation, watch this video starting at 5:15: [https://www.youtube.com/watch?v=UXyS-xofGNM](https://www.youtube.com/watch?v=UXyS-xofGNM).

```bash
sudo apt update
sudo apt install -y kali-win-kex
```

This involves downloading a large number of Linux packages, thus taking a while. During installation, you may be asked to choose a keyboard layout and press `Enter` to use the default one.

After the installation, run the following command to start the desktop:

```bash
kex --win -s
```

After running the command, you will be prompted to set a password. This is only for the local connection between Windows and Kali Desktop, so you can use a simple password (e.g., `123`). When asked if you want a view-only password, type `n` and press `Enter`.

A desktop window will appear shortly. You can now use Kali as if it were a native GUI operating system. To exit, press `F8` and select `Disconnect` from the popup menu. In the future, type `kex --win -s` in your Kali bash terminal to relaunch the GUI.

Note that the Kali Desktop running via WSL2 may sometimes be unstable, as this is not a true standalone desktop environment. You may see occasional error pop-ups. In such cases, press `F8`, close the Desktop and relaunch a new one from the terminal.

### 1.2 MacOS (Apple Silicon)

For MacOS with Apple Silicon (e.g., M1/M2/M3 Chips), you should use **UTM** to run Linux. The steps below provide a walkthrough of the setup. After finishing this subsection, go to [Section 2](lab-1-setting-up-your-laptop.md#id-2.-learning-the-kali-linux-bash-terminal).

#### Step 1: Download/Install UTM

From your MacOS browser, open the UTM website [here](https://mac.getutm.app/) and click the `Download` button. Your browser will start downloading a UTM installer file (usually a `.dmg` file). Once finished, locate the downloaded file in your `Downloads` folder. Double-click the downloaded `.dmg` file to open it. 

After opening the `.dmg`, a `Finder` window will appear showing the UTM app icon, and an `Applications` folder shortcut. Drag the UTM app icon into the `Applications` folder icon. This copies UTM into `/Applications`. Wait a few seconds until the copy finishes and then right-click the installer disk image to eject it.

After the installation, Go to `/Applications`, find UTM, and double-click it. If MacOS says "UTM can't be opened because it is from an unidentified developer", go to `System Settings` and then `Privacy & Security`, scroll down, click `Open Anyway`, and then confirm. Or if it simply asks for confirmation, click `Open`.

When UTM launches successfully, you should see the UTM main window, which confirms UTM is installed.

#### Step 2: Install Kali Desktop GUI

Once the UTM application is installed, you need to download a Kali Linux image specifically pre-configured for UTM. Specifically, open the [UTM Gallery](https://mac.getutm.app/gallery/kali-2023), and click the `Download` button. You will be redirected to [archive.org](https://archive.org/details/kali-linux-2023-arm64-utm), where the VM file is hosted. On the webpage, you have to create an Internet Archive account in order to download the file. After you complete the registration steps and sign in to [archive.org](https://archive.org/details/kali-linux-2023-arm64-utm) again, you will be able to locate the `DOWNLOAD OPTIONS` on the right-hand side of the page, and see multiple formats such as `TORRENT` and `ZIP`.

You click `ZIP` for downloading. The ZIP file is approximately 4.5 GiB, so the download may take some time depending on your network. After the download completes, double-click the downloaded .zip file. MacOS will automatically extract it into a folder in the same location. After extraction, look for a file ending with `.utm` (e.g., `Kali Linux 2023.utm`). This `.utm` file is the VM bundle. Simply double-click this `.utm` file, and UTM should open it automatically and the Kali VM will appear in the left sidebar of the UTM window.

Finally, click the `Play/Run` button (▶) on the sidebar, and wait for the VM to boot. Once boot completes, you should see the Kali Linux desktop environment. When you log into the environment for the first time, note that both **the username and password for the pre-built Kali VM image are `kali`.**

### 1.3 MacOS (Intel/AMD)

For older MacOS using Intel or AMD processors, it is recommended that you use **VirtualBox** to run Linux. Download VirtualBox for macOS [here](https://download.virtualbox.org/virtualbox/7.2.6/VirtualBox-7.2.6-172322-OSX.dmg). After finishing this subsection, go to [Section 2](lab-1-setting-up-your-laptop.md#id-2.-learning-the-kali-linux-bash-terminal).

Once VirtualBox is installed, you need to download a pre-configured Kali Linux VM image [here](https://cdimage.kali.org/kali-2025.4/kali-linux-2025.4-virtualbox-amd64.7z). Alternatively, you can download it from the [official Kali website](https://www.kali.org/get-kali/#kali-virtual-machines).

The download will be a `.7z` file. This is a compressed archive (similar to a `.zip` file), so you must extract this archive first.

After the extraction, open VirtualBox. From the top menu, click `Machine → Open`. In the file picker, navigate to the extracted folder, select the `.vbox` file and click `Open`. After that, you should see a new VM entry (e.g., Kali Linux) in the VirtualBox left panel. Click that VM entry and click `Start` to boot the VM. After booting, you should see the Kali Linux desktop and its login screen.

Still, **the username and password for the pre-built Kali VM image are both `kali`.**

Note that the above installation instructions were written two years ago. Since we currently do not have a MacOS machine with Intel/AMD chips available, we have not tested these steps recently. If you encounter any issues, please contact the lab facilitators for help.

{% hint style="info" %}
If you have a black screen when installing Kali, please go to `settings` and `"+ New..." in Devices`, and add `Serial`. Then start the VM, you can install using the Serial (terminal). Once the installation is finished, you can remove the Serial device.

If you have a blue screen after installing Kali, please go to `settings -> Display -> Emulated Display Card`, and select any non-GUI options (e.g., virtio-ramfd).
{% endhint %}

## 2. Learning the Kali Linux Bash Terminal

Since you have set up your Linux environment, you need to know some basic commands via a **bash terminal**. In Linux, the terminal is a text-based interface for interacting with the system by typing commands. While graphical interfaces are user-friendly, the terminal offers direct control of the system and you will use the terminal throughout this unit. Please watch this video to practice basic Linux commands: [https://www.youtube.com/watch?v=J2zquYPJbWY](https://www.youtube.com/watch?v=J2zquYPJbWY)

For a quick reference of frequently used commands such as `ls`, `cd`, and `mkdir`, you can refer to this [Linux Command Line Cheatsheet](https://hep.ph.liv.ac.uk/twiki/pub/Computing/AccountRegistration/linux-command-line.pdf). If you want to know how a specific command works, you can search the [Linux Manual Pages](https://man7.org/linux/man-pages/index.html). Alternatively, you can also access the Linux Manual Pages within the terminal by typing `man` followed by the command (e.g., `man ls`). 

## 3. Installing and Running Docker

Docker is a tool that allows you to run software inside containers. A container is a small, self-contained environment that includes everything a piece of software needs to function, such as libraries, configuration files, and dependencies. This method removes the need to install different programs and dependencies manually while also keeping the container environment separate from your system. For a more comprehensive deep-dive, you can visit the [official Docker documentation](https://docs.docker.com/get-started/overview/).

In this unit, we use Docker to simplify lab setups. All the tools required for future labs are pre-packaged into individual Docker images. To run these images and set up your lab environments, you must have Docker installed within your Linux system.

Before you start, it is recommended that you watch the following walkthrough video for the guidance only:

**Docker and Bash 1-1** [https://www.youtube.com/watch?v=4vl4aUxo8Hk](https://www.youtube.com/watch?v=4vl4aUxo8Hk)


### 3.1. Installing Docker

{% hint style="warning" %}
You must install Docker specifically inside the Linux OS you set up in the previous section. Do not attempt to use "Docker Desktop" for Windows or macOS, as our lab environments are designed to run strictly within your Linux terminal.
{% endhint %}

To install Docker on Kali Linux, open your terminal and run the following commands:

```bash
sudo apt update
sudo apt install -y docker.io
```

An official guide for getting started with Docker can be found below:

{% embed url="https://www.docker.com/get-started" %}

### 3.2. Testing Docker

To test the environment, we will run a simple container that allows you to access a bash terminal. This allows you to enter commands that get executed within the container. You can only do what the container will let you do as it is a constrained environment.

To start with, from your Linux bash terminal, run the following command (please note, the process may take a while).

```bash
sudo docker pull uwacyber/cits1003-labs:bash
```

Example output (for reference only) is shown below:

```text
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

Run the following command:

```bash
sudo docker run -it uwacyber/cits1003-labs:bash
```

Once the container is running, you can try the below command (right after the `#`) in the terminal:

```bash
root@9215e663eb9d:/# whoami
```

Example output (for reference only) is shown below:

```text
root
```

The `docker pull` command downloads the docker image to your machine. The image contains all of the files and configurations needed to run the container. You run a container using the `docker run` command as shown above.

In the case of the bash container, to stop it, you simply type `exit`. Other containers can be stopped using the `docker stop` command from another terminal. To do this, you need to provide the Container ID which you can do as follows:

```bash
0x4447734D4250:~$ sudo docker ps -a
```

Example output (for reference only) is shown below:

```text
CONTAINER ID   IMAGE                         COMMAND       CREATED         STATUS         PORTS     NAMES
45fe3a838ef0   uwacyber/cits1003-labs:bash   "/bin/bash"   3 minutes ago   Up 3 minutes             hungry_hodgkin
```

```bash
0x4447734D4250:~$ docker stop 45fe3a838ef0
```

Example output (for reference only) is shown below:

```text
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
