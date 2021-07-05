# Lab 8: Forensics

## **Memory Forensics**

This is adapted from [https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/README.md](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/README.md)

### \*\*\*\*

### **Challenge Description**



#### 

#### Memory dump analysis

We'll be analyzing the memory dump file \(challenge.raw\) using **Volatility 2.6** as it is best suited to our needs. All the labs in the repository can be solved using Volatility 2.

The very first thing that anyone needs to know before proceeding to forensic analysis of a memory dump is to determine the **profile** we are going to use.

The profile tells us the OS of the system or computer from which the dump was extracted. Volatility has a built-in plugin to help us determine the profile of the dump

Now, we'll be using the **imageinfo** plugin

`$ volatility -f Challenge.raw imageinfo`

[![Imageinfo](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/imageinfo.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/imageinfo.png)

Now as you can see, volatility provides a lot of suggestions as to which profile you should use. In some cases, all of the suggested profiles may not be correct. To help get over this barrier, you may use another plugin called **kdbgscan**. As far as this challenge is concerned, using kdbgscan isn't required.

Now as a forensic analyst, one of the most important things we would like to know from a system during analysis would be:

* Active processes
* Commands executed in the shell/terminal/Command prompt
* Hidden processes \(if any\) or Exited processes
* Browser History \(This is very much subjective to the scenario involved\)

And many more...

Now, to list the active or running processes, we use the help of the plugin **pslist**.

`volatility -f Challenge.raw --profile=Win7SP1x86 pslist`

[![pslist](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/pslist1.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/pslist1.png)

Executing this command gives us a list of processes which were running when the memory dump was taken. The output of the command gives a fully formatted view which includes the name, PID, PPID, Threads, Handles, start time etc..

Observing closely, we notice some processes which require some attention.

* cmd.exe
* DumpIt.exe
* explorer.exe

[![pslist-2](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/pslist2.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/pslist2.png)

* cmd.exe
  * This is the process responsible for the command prompt. Extracting the content from this process might give us the details as to what commands were executed in the system
* DumpIt.exe
  * This process was used by me to acquire the memory dump of the system.
* Explorer.exe
  * This process is the one which handles the File Explorer.

Now since we have seen that **cmd.exe** was running, let us try to see if there were any commands executed in the shell/terminal.

For this, we use the **cmdscan** plugin.

`volatility -f Challenge.raw --profile=Win7SP1x86 cmdscan`

[![cmdscan](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/cmdscan.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/cmdscan.png)

If you can see from the above image, a python file was executed. The executed command was `C:\Python27\python.exe C:\Users\hello\Desktop\demon.py.txt`

So our next step would be check if this python script sent any output to **stdout**. For this, we use the **consoles** plugin.

`volatility -f Challenge.raw --profile=Win7SP1x86 consoles`

[![consoles](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/consoles.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/consoles.png)

We see that a certain string `335d366f5d6031767631707f` has been written out to **stdout**. Now as one might observe, this is a **hex-encoded** string. Once we try to revert out the hex encoding, we get a gibberish text.

[![hex-revert](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/hexrevert.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/hexrevert.png)

Now if you remember, we tried to deduce some clues from the challenge description. The first one was something with the word "environment". Now there are certain system determined variables called **Environment variables**

To view the environment variables in a system, use the **envars** plugin. Going down the output, we see a strange variable by the name **Thanos** \(Ah! so maybe that's why it was provided in the description.\), the value of the variable is `xor and password`.

`volatility -f Challenge.raw --profile=Win7SP1x86 envars`

[![envars](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/envars.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/envars.png)

Now, we have 3 things in total:

* The gibberish text resulted from reverting the hex-encoded string
* Xor
* Password

Thinking for a while, makes us realise why the clue `xor` was provided. Let us try to attempt xor decoding on the gibberish text.

```text
a = "335d366f5d6031767631707f".decode("hex")

 for i in range(0, 255):
    b = ""
    for j in a:
        b = b + chr(ord(j) ^ i)
    print b
```

There are only 255 possibilities and if you see, the 3rd output is a suspicious text **1\_4m\_b3tt3r}**. That looks like part of the flag.

Well, the next part is `password`. Using volatility, we can extract the NTLM password hashes using the **hashdump** plugin.

`volatility -f Challenge.raw --profile=Win7SP1x86 hashdump`

[![hashdump](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/hashdump.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/hashdump.png)

Now the password hash we have to decrypt is `101da33f44e92c27835e64322d72e8b7`. We can use online NTLM hash cracking websites.

[![NTLM-cracker](https://github.com/stuxnet999/MemLabs/raw/master/Lab%200/Images/ntlm.png)](https://github.com/stuxnet999/MemLabs/blob/master/Lab%200/Images/ntlm.png)

Well there you go, we have the other half of the flag --&gt; **flag{you\_are\_good\_but**. Concatenating the 2 parts gives us the whole flag.

FLAG: **flag{you\_are\_good\_but1\_4m\_b3tt3r}**

I hope with the walkthrough provided for this simple CTF challenge, gives confidence and encourages you to try out the rest of the labs.

If you have any doubts/queries, feel free to reach out to me --&gt; [Contact me](https://github.com/stuxnet999/MemLabs#author)

