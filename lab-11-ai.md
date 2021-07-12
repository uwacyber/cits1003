# Lab 10: AI

Artificial Intelligence is a collection of technologies that allows computers to simulate human intelligence. Its applicability in cybersecurity involves all aspects of AI, including natural language processing, speech recognition, expert systems, robotics and vision. Fundamental to  these types of AI is machine learning, a technology that uses an approach to learning that tries and mimics the way nerve cells work in the brain. 

 One area of active research in machine learning is the use of adversarial images. This is where slight changes in the image causes machine learning systems to incorrectly classify objects within the image. So for example, a panda is wrongly recognised as a gibbon. The changes to the image can be imperceptible to a human and so this type of attack could be used to alter a radiological image and change a negative diagnosis of cancer to a positive one in a system that is automatically screening for cancer. 

Adversarial attacks could become increasingly common as we come to rely on machine learning systems to automate processes and decisions. This has made the field of research into defences against this type of attack important. 

In the area of malware recognition, malware can adopt tactics to prevent recognition by taking an adversarial approach. 

To see how this works, we can use a program that uses what is called a non-targetted black box approach to adversarial images. 

Start the docker container as follows:

```bash
/ai/share$ docker run -v /projects/share:/opt/adverserial/share -it cybernemosyne/cits1003:ai 
root@453e8234c9fd:/# 
```

The -v flag will allow you to share a local directory with the container which we are going to use to get image files. So use a local directory with nothing in it.

Once on the docker container, go to the directory /opt/adversarial/share. From there, run the exploit.py program. This program will take a normal image of a Labrador and create adversarial versions of the image. If you are interested in the details, the program comes for a toolkit called Foolbox \([https://github.com/bethgelab/foolbox](https://github.com/bethgelab/foolbox)\). 

To run the script we do so as follows:

```bash
root@3432bc8b6c77:/opt/adversarial/share# python ../exploit.py ../lab_og.jpg 
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
Processing image: prediction: Saluki confidence: 13.087703287601471
Saving Epsilon = 0.100
Processing image: prediction: Weimaraner confidence: 14.949022233486176
Saving Epsilon = 0.150
Processing image: prediction: Weimaraner confidence: 16.211819648742676
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

**Flag: Enter the name of the dog type that Wolfram recognises when the "Epsilon = 0.150.jpg" file is uploaded.**

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
/opt/ember# python scripts/classify_binaries.py -m ./dataset/ember_model_2018.txt malware 
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
root@3432bc8b6c77:/opt/ember# python scripts/classify_binaries.py -m ./dataset/ember_model_2018.txt git.exe 
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

**Flag: Enter the full classification probability for the malware you found above**

It is possible to create adversarial versions of malware that are designed to evade classification by machine learning detection techniques, however that is beyond the scope of this practical. 

If you are interested in what Lief can tell you about the binary, you can use it as follows:

```bash
>>> import lief
>>> binary = lief.parse("malware")
Unable to find the section associated with BOUND_IMPORT

>>> print(binary)
"key" of the var key should be equal to 'Translation' ()
Dos Header
==========
Magic:                        5a4d
Used Bytes In The LastPage:   90
File Size In Pages:           3
Number Of Relocation:         0
Header Size In Paragraphs:    4
Minimum Extra Paragraphs:     0
Maximum Extra Paragraphs:     ffff
Initial Relative SS:          0
Initial SP:                   b8
Checksum:                     0
Initial IP:                   0
Initial Relative CS:          0
Address Of Relocation Table:  40
Overlay Number:               0
OEM id:                       0
OEM info:                     0
Address Of New Exe Header:    b8

Rich Header
===========
Key: 8acd8739
  - ID: 0xd000 Build ID: 0x1fe9 Count: 1
  - ID: 0x9000 Build ID: 0x1f69 Count: 6
  - ID: 0xe000 Build ID: 0x1c83 Count: 1

<SNIP...>
```

There is a great deal of content that follows.

