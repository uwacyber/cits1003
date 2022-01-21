# Cryptography

## Flag 6: Mr Beep Boop Bot

_Beep boop_, my name is Mr Beep Boop Bot. I have a message for you, but I have only installed the minimal human language module. _So I just used a language more native to me and I hope that you can read it_.

{% file src="../.gitbook/assets/msg.txt" %}

## Flag 7: Decrypt XOR or fail

Can you decrypt the following message that was encrypted using the XOR operation with a key that is 1 byte long?

```text
KiA9OlhZWVoSHloIIjYRWRs2AlowNhpYMww2DCdaGy4QSFhYSEgU
```

## Flag 8: Train to Crack Station

I was on the train the other day going to **crack station** when this person came up to me and told me the MD5 hash of their password. "Why would you do something like this?" I asked him, but they just told me that their name was **John** and said "if I was the chosen one I would be able to get his password".

**Can you crack the hash below and get the password for John?**

```text
365d38c60c4e98ca5ca6dbc02d396e53
```

{% hint style="info" %}
If you can't get to the crack station - just try searching on the web using the hash.
{% endhint %}

## **Flag 9:** ECBrypted Image

On a late afternoon working hard as a NSA agent, you see an encrypted image sent between two suspected Kinder Surprise smugglers. After you inspect the communications further, you discover that the sender used AES encryption using the **ECB mode to encrypt the image**.

The original image was a **PPM file** and had a width and height of **1920 by 1080 pixels** respectively. However, you were unable to figure out what was the key used to encrypt the image.

**Can you still see the hidden message within the image?**

**Hint:**

Remember the lectures about ECB? But how do you view the image? A PPM file needs a header to be recognised. The specification for PPM is here [http://netpbm.sourceforge.net/doc/ppm.html](http://netpbm.sourceforge.net/doc/ppm.html)

To add a header to the file you can create a file with the header \(say, imgwithheader.ppm\) and then do:

```text
cat encrypted_image.bin >> imgwithheader.ppm
```

This will copy the contents of encrypted\_image.bin and concatenate \(add\) it to the file imgwithheader.ppm.

{% file src="../.gitbook/assets/encrypted\_image.bin" %}

## **Flag 10: Missing Letter**

Help I have forgotten the end of my encryption key and I cannot decrypt my data!

I know I used **AES-128** using **CBC mode** where the IV was `01020304050607080102030405060708` in **hexadecimal** and the key started off with `harperssecretke`. However. I still cannot decrypt my data below **in hexadecimal format**.

```text
375f9ad2bec3c930e5cd4b1d243e2ccf1d7a43f2c88f68cdd65cd01948de242caa6ec30ebea93c86b6deca3b247f7ca7
```

**Can you guess the AES key and decrypt the data?**

\*\*\*\*

