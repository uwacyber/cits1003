# Lab 2: Cryptography

There is no walkthrough video for this lab, please talk to one of our facilitators (during the scheduled lab times) or discuss in the group chat if you need further assistance.

### Learning Objectives

1. Using CyberChef to explore encodings and encryption using operations and recipes
2. Understand different number representations such as binary and hexadecimal and character representations such as ASCII
3. Understand the use of shift ciphers, XOR and modern cryptography systems like AES and PGP

### Technologies Covered

* ASCII, Base64 encoding
* Binary, Hexadecimal
* CyberChef
* Caesar Cipher
* XOR encryption
* AES
* PGP

***

## 1. Ciphers

#### CyberChef

CyberChef is a website that has been developed by the UK GCHQ, a government cyber and security agency. It allows the simple chaining of a large number of different operations on inputs such as text to create an output. If we want to use the Caesar cipher to encode text for example, we can search for ROT13 in the operations, drag it into the Recipe window and simply type in the input window. The output will be transformed using the recipe automatically. In case you were wondering, ROT13 stands for rotate (Shift) by 13. The original Caesar cipher performed a shift of 3. Let's try this ourselves.

1. Go to CyberChef here [https://cyberchef.io/](https://cyberchef.io/)
2. Search for ROT13 and drag the operation to the Recipe window
3. Type "The quick brown fox" into the input window
4. Verify that the output is "Gur dhvpx oebja sbk"

![](../.gitbook/assets/cyberchef-rot13.png)

### Question 1. Unravelling Caesar

We can now try some "cryptanalysis" albeit using the unsophisticated approach of brute force. You have intercepted some encrypted text:

> Esp njmpcnspq td nzzvtyr fa l dezcx!

You suspect it has been encrypted using a Caesar cipher but you need to find out the shift number. How would you find out?

Remember that to decrypt a Caesar cipher, you need to use a shift that is 26 - shift number. For this question, leave the "Rotate lower case chars" and "Rotate upper case chars" selected (and no numbers are used).

Flag: Enter the plaintext

### Text encoding

#### ASCII Code

We are going to use CyberChef to explore how text is represented by the ASCII system. ASCII stands for the American Standard Code for Information Interchange. Each character is represented by a number between 0 - 254. So the letter 'a' is 97 and the letter 'z' is 122, etc. You can find the full chart here [http://www.asciitable.com/](https://www.asciitable.com).

To convert text to ASCII, we can use to "To Decimal" recipe under the Data format menu in CyberChef and then type the text "The quick brown fox". Your screen should look like this:

![](../.gitbook/assets/cyberchef1.png)

The ASCII in decimal is:

> 84 104 101 32 113 117 105 99 107 32 98 114 111 119 110 32 102 111 120

Remember that the space character is converted as well (to 32)

The binary representation of these numbers can be found using the "To Binary" operation:

Note: Normally ASCII is represented as Hexadecimal when programming

> 01010100 01101000 01100101 00100000 01110001 01110101 01101001 01100011 01101011 00100000 01100010 01110010 01101111 01110111 01101110 00100000 01100110 01101111 01111000

## 2. Encrypting with XOR (⊕)

We can pick a key to encrypt our text using the XOR operation. Remember that XOR works as follows:

0 ⊕ 0 = 0\
0 ⊕ 1 = 1\
1 ⊕ 0 = 1\
1 ⊕ 1 = 0

Let us take the binary from the previous example and XOR it with a key which is 1 byte long 00000001

To XOR the key against the binary for "The quick brown fox", we can repeat the key until it is the correct length (19 characters = 19 bytes)

> 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001 00000001

Try doing the XOR operation by hand and taking the binary output and converting it back to decimal and then to ASCII

There is an easier way of doing this of course, we can just use the XOR operation in CyberChef and take as the key the value 1. If you do this in CyberChef using "The quick brown fox", you will get

> Uid!pthbj!csnvo!gny

The exclamation marks are the result of the space character being XOR'd.

### Non-printable characters and Base64 encoding

Often the result of an XOR on ASCII characters will be non-printable characters. If we use the key 01111111 in binary or 127 in decimal, the output will be non-printable characters. You can see this by adding a second operation "To Decimal" to the recipe to see the actual ASCII decimal numbers. You will get

> 43 23 26 95 14 10 22 28 20 95 29 13 16 8 17 95 25 16 7

To handle this situation, we can encode the output into Base64 which is a binary-to-text encoding designed to carry binary data in text form.

If you replace the "To Decimal" operation with the "To Base64" operation in your recipe, you will get

> KxcaXw4KFhwUXx0NEAgRXxkQBw==

{% hint style="info" %}
Whenever you get text which ends in two "==" it is likely to be Base64 but remember that it doesn't always end this way.
{% endhint %}

To test that we are not making things up and that our encryption worked, we can take the Base64 string as an input and then create the recipe usng the operations:

1. From Base64
2. XOR with the key 127 in decimal

We should get our original input "The quick brown fox"

### Question 2. Brute forcing XOR

You are given the following Base64 encoded text

> KxgLAE4HCE4XARtOCgEASRpOBQABGU4aBgtOBQsXQk4dDwgLThoBTg8dHRsDC04HGkkdTgEAC04MFxoLTgIBAAlA

You don't know the key but you can assume it is one byte long and it uses XOR as the algorithm. You are going to try and brute force it to find the key.

Use the operation "_**XOR Brute Force**_" in CyberChef to find the key in Hexadecimal. What was the original message?

**Flag: Enter the plaintext**

## 3. Modern Ciphers

### AES

The Advanced Encryption Standard (AES) is the accepted standard block cipher that can use a variety of modes of operation. You can select AES Encrypt in CyberChef and input the text "Please keep this secret".

Enter the key in UTF8 format:

> specialsecretkey

For the IV (Initialisation Vector) in HEX, enter:

> 0102030405060708090a0b0c0d0e0f10

Select CBC Mode (leave the rest as is i.e., "Input = Raw" and "Output = Hex").

{% hint style="info" %}
AES IV length is 16 bytes. The key length is:

* 16 bytes = AES-128
* 24 bytes = AES-192
* 32 bytes = AES-256
{% endhint %}

{% hint style="info" %}
UTF8 is Unicode which expanded the number of bytes used to encode characters to 4 bytes (ASCII uses 1 byte). It is backwards compatible with ASCII but supports up to 1,112,064 characters and so supports Chinese and other languages.
{% endhint %}

The hex output of the encrypted text is:

> 0f1ee3bc7b64c9a266bb19aa3eb7e4a780bc1d201a444b3106d8e8ca4c7e7dc5

You can verify that you can decrypt this by adding the operation AES Decrypt to the recipe and using the same key and IV to decrypt.

An interesting thing to note is if you change a single character in the IV, you still get most of the output correct. Changing a single character in the key however will cause the decryption to fail.

### Question 3. Decrypting Snowden's message

You are given the following Base64 encoded text

> vqqjbybmIyq63sPvHyr1YjfX9c24qNVT56DXEyUmO/VxZAzc1wnA9jMljLURoDRvF6nhoUmi7H1Yd2xC30NMgfv/9y03Colw144ZVT3+5IyEdnvl3HR0wkgkkFxTs7eK

The key is _snowdenquotation_ and the IV is 0102030405060708090a0b0c0d0e0f10

What is the decrypted text?

**Flag: Enter the plaintext**

### PGP

Pretty Good Privacy (PGP) is an encryption program that uses _public-key cryptography_ to encrypt and digitally sign data. The following diagram illustrates how it works:

![How PGP works (From Wikipedia: https://en.wikipedia.org/wiki/Pretty\_Good\_Privacy)](../.gitbook/assets/1000px-pgp\_diagram.svg.png)

Note that we still use symmetric encryption to encrypt the main data because it is much faster than using the recipient's public key to encrypt.

#### Generating a Public/Private Keys

To start with, you will need to generate public and private keys which you can do in CyberChef using the "Generate PGP Key Pair" operation. It is a good idea to put in your name and email address because it will be incorporated into the public key. This way, when you send someone your public key, this information will automatically be available to them making it easier to add your key to a Keyring and retrieve it later.

Note that for the Key type, there are several options RSA of various key lengths and ECC. ECC is Elliptic Curve Cryptography and uses smaller keys than RSA. Since it is a newer protocol, it may not be as widely supported as RSA is.

Select RSA-1024 as the Key type and enter your name and email address into the fields provided. The output will be a private and public key. Select the text for the private key and copy it to a file called private.key and save it in a folder on your computer. Take all of the text starting and ending with the comment lines:

```
-----BEGIN PGP PRIVATE KEY BLOCK-----

-----END PGP PRIVATE KEY BLOCK-----
```

Do the same with the public key, saving it to a file called public.key.

We are now going to send an encrypted and digitally signed email to Edward Snowden. We have been given his public and private keys:

```
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: Keybase OpenPGP v2.1.15
Comment: https://keybase.io/crypto

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
Ch4=
=Vslj
-----END PGP PRIVATE KEY BLOCK-----

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: Keybase OpenPGP v2.1.15
Comment: https://keybase.io/crypto

xo0EYJ9LyQEEAJnHGn1GxD6mL6Rln4CGEpWtBujHKnEHyY86cSxNR+huurfFF3Kg
GI4rl2FdLEnwLuX/vuALwKcEKovHr5tOBXXZvK9Utwy/bS/4EsyfdurIO7GdF0xQ
0ynmnDnsj3p5iol1sMwvf84a0zJpjmCOQ1ShQh6Eyjg0I349QDA0DO9RABEBAAHN
LkVkd2FyZCBTbm93ZGVuIDxlZHdhcmQuc25vd2RlbkBwcm90b25tYWlsLmNvbT7C
swQTAQoAHgUCYJ9LyQIbLwMLCQcDFQoIAh4BAheAAxYCAQIZAQAKCRCJchAX4KHw
YTw1A/Y5rdcpoJdKXXi9AyO7Az6JSrF6P+KiZzCDMp8pVNXJggvdfqLAtbIkQA7b
SSi3IvkNrwBLvAJaF6voxPiA4oySy+i5oJyZ/s1KFn1NkH4nbpbgo+PmUjCw/fUk
Yk4ndsDG/G4v6dc1VnZ2/RyRdSlBOCmhu0VquWMj2OaW0zOmzo0EYJ9LyQEEANmm
hptKa4Dd9HNDlp4CijRpilKbhAuKr2YcbXNwu0tL9QkDYp2p6Ima9BZ6wG5diddr
A8600jcPyErIkQBpdgDlRcSEsMIdFO65BDEwhpDPjoqOa9JL3TomOi0JcxyN03tT
ayvvcCDhSc3Vm4wii1E9uzXhGavFTxkofjdtMk9ZABEBAAHCwIMEGAEKAA8FAmCf
S8kFCQ8JnAACGy4AqAkQiXIQF+Ch8GGdIAQZAQoABgUCYJ9LyQAKCRBHSh35lVcq
FaOhA/wLWCS8uKl35lmUE2IoG8yl/dSBzbDeeTTtGa3hIdn9zN37nSVN3liGTkxc
neB11htqKvc0krFQ7Nn+Hnj2qY9x8uhZxTRzz0SgGk+w55ND9P9qwrm423EFBuBm
r7xVuijMeHVC0Q8vNXiyltcGZryuriaUuFm3vsdXBj7OH2z7qAvKA/9huWSKav86
IgJihJlvyN5naBmOy+uSHPi7YQPWQqPvQ9PZnMUQ4/9YxhEXWQfkkddBOjbxs0/f
teZUypwhvFv8RBK2Cxf72Y+zHQ/Q1EFekS3V8+oYgqJa8QjxmvxHIzpLMwSb3xoG
ceoEEdKxxsXyZlZKuet6EZj8rczYo0uhT86NBGCfS8kBBACxeiZCh5dSnLn+2z/K
s76qeNp0VhIYwvjKu2hbhG8Knjzy022Hew2ibUp/Bgxkl7vGluFzTsSHkmm8Hltj
GI26OTCM8UzYbT41Uwd422w3eWaIdSsDaS050NVDVjGjbv8ZhtvXfaKC5VbyN5Lw
T3JzGTmMr0O5Wgl/PgiatHFwAQARAQABwsCDBBgBCgAPBQJgn0vJBQkDwmcAAhsu
AKgJEIlyEBfgofBhnSAEGQEKAAYFAmCfS8kACgkQ0Pyo6uNbTVEZ7AQAqZmkRT6U
EXa0+05Z3pTPU7WdUJjmiLDpEgOeuipWmXfdfB5aLvu0S4HCHrYVECluiZx+o8pI
Xu+DFr9VYV/2+wJZnhjqcfMehJNA49CwgGtrEx7r3ACSBRRq5qFEFdGbdzKjl3LW
w1kH7tT6VI7X3oDUOMDQBlgFFZkAQbjIg6Mh/QP/Xx/2pbUGaKRL6qX/t2wbehwQ
LI4YJGMLLL141nCwcaa/bxZBilR5Xwxdn1k8jWClvZYrV2ihnEFxL7kff2ofBXtr
vzKUgFL8xVB7zgRzfDNk8zRYXEm5gcpN7Wp74hCeswNgaZIEGZnMKa5P8y4U2OUb
Kwp5hrmJ5/y/ALOUCh4=
=BE7f
-----END PGP PUBLIC KEY BLOCK-----
```

{% hint style="info" %}
It is never a good idea to publicly share your private key.
{% endhint %}

Use the PGP Encrypt and Sign operation to encrypt the following text:

> This is a secret email

{% hint style="info" %}
When entering the keys, you must include the lines that specify the "BEGIN" and "END".
{% endhint %}

Remember that you need to use

1. Snowden's public key to encrypt the message
2. Your private key to sign the message

Take the output which should look something like this (similar, but not exactly as your private key differs from ours):

```
-----BEGIN PGP MESSAGE-----
Version: Keybase OpenPGP v2.1.15
Comment: https://keybase.io/crypto

wYwDR0od+ZVXKhUBA/0aapS0kDJoo8nppiFll/knSuKzNvZI1IpIiekNbf/4KVoq
SFdYmCvnbcAoj3DfGJUv1NQfi2FzromFgL0Df9/Na+HUPh53bsC+b3yrkx5Ivcgy
Ubb09R1fVloiwMWxTNou4tzRQPoNEqnjajt4jt0sfj7WOmpFZAvgHKShmzTYytLA
QAGtbCLVM/u5PhV38clp6tWoQLjkmOKkkOHZ4xxrrDCtTQbFuK/Ds1NOzGZTc8a0
aN4SUd1fpfgYl9DhthC8wM0eC5yChxZbUei31ESaETeHzucW1AISZNe7GkmeIIWU
+KLzue1AUxPqD1JHaqSxQnqw1pVtFbmg3Oqjx0OEo9C27EYka1bgd58Um5kPCaHm
dXFFTzneASjmx2WdLHFQJPwP0BqfFPv1AnAf2KAyALPNEIjavMR37LirVQZ/vd1Z
gHs+YvS9tMSqvTV+8P5U0Vzd2+z/xKBgbHRY2U0W+xToygE2SahWwxLbbdxAJ0kc
gI3IWf+gdgln7qQmK2KxjTw=
=xO3N
-----END PGP MESSAGE-----
```

And use the operation PGP Decrypt and Verify to make sure that you can check the signature and decrypt the message. Remember, to do this, you need:

1. Snowden's private key to decrypt the message
2. Your public key to verify the signature

And that is it, you can now send encrypted and digitally signed messages to your friends, colleagues and family!

{% hint style="info" %}
There are public servers where you can list your public key for others to use. You can also simply append it to your emails so that anyone wanting to send you encrypted messages can use that.
{% endhint %}

There are numerous command line and GUI-based software products that allow you to use PGP more easily. Some integrate with email clients as well.

### Question 4. Decrypt and verify another of Snowden's Messages

Let's say the following is your PGP private and public key pair.

```
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: Keybase OpenPGP v2.1.15
Comment: https://keybase.io/crypto

xcEYBGDdpbUBBAC8XmTQUTvFOCDJ60yeGmGfyw1cpXUKSVjNJXGcwTerOX7KVZMN
J+yP7jRUwnjUbFG5qTqMqLtzE3LG+0lOJKealgQUyrCHUE6ag0jtFZ61/+Bk+JVI
XVZH7Mig73OtsMtWSNxiXZwaFrFQZhdSyvraEGe9Hv1MB52ZYY0uKbvb7wARAQAB
AAP9GrV1rPX/uBibyZWkAPzzn7EuXVcWj9VTko7/G39oEc6utCjLF3/0MnpPkD8c
293Z/q3In/4iyg/VY/Joc/yNiQas9MIF2tgsmMZTb1tc5xaIar8JdOD3uqO7TPeU
eND/TmIgl7v3Qxgrt1gjRJwFOyOcfnrJalMW+psfZxeVtdUCAPJ17EKDtqFch7/B
z8Vqu+z020i8+GLSE5Bq4EsRObZCp4Lzfc+I4oZqzPd3RPrq3zW9o4vwG2WmNZlS
QCP7C3MCAMbjNEg+iGvZ9JmCd6qHhVYcuBSyVpsxjeV+Vm4LsKSCK666Uym6QmRo
oe7ZchjoGSKM1xq/XFbU5JXNJATghpUCAJlCQExmp3YEaqGYtDc5vKoDxFlwecgr
UCLu8nWLKTKZh3l+/h+MWrrJuhSsVm5ata6srBFYho2FjBS1IB9OCpynN80AwrQE
EwEKAB4FAmDdpbUCGy8DCwkHAxUKCAIeAQIXgAMWAgECGQEACgkQxGn2RENJ2gIA
fQP6AvKfY47YDv7TT9mElGWRdpyM9/40z9293u/3YuPXB1UljGK33M0UN8zEQabV
VPn5CrWC0lEWj/dae4grsyhj6HPxZgfoGX61Az2Tx5QJ7wjf8WdjS0smJauGv7Ej
4rNd7uC3oHTBW0FDduf1ZJA2LT1dhWZEHnL1iBHDn50Y1yPHwRgEYN2ltQEEALgv
Q/3WdnKux8i3ppnR+Z++xUfMA82qj0Bjm+UAu1KacoqhilYwXRhv3hfKZ9DkdPZX
sDvsh7K2bsdQj+nG89AWr6Eb3jrwOPyjb+ZH94GQcAAZpQU1CKOFiFAHjXia52nv
vNomk+RcmTd9B2cRwhPT+HsLvy2keH+5md2iQLU9ABEBAAEAA/4nH/c3+TIxG1qa
ExUDUNzPZ8VdgoN+UVBb06z+gODJ48AYHceWlnB4K+9IK3lRIO6Nk8P+fri2qFUw
5rajaN1Khvy4VpIAt5nFjCaKgEjhySr5nBwv1PWbpQgkdNe2a/3h59tcLVmPf8mu
C8pGO3L++cHFwbPoKYVVHHctsTbjGwIA26TP+aMjTgQj68GD5bCPm6fp+0sFoyoY
o7myundPFoBGtZMKAikt+MpEkaLBFDXjlv3VGmAkO3ij47PLVZS+EwIA1qvn/rAr
LdU9hsZEw0CzajUzWJVgfEN3t+TIS2HrVOYh+OyRhkJoLQGkCDF/3cR8uMuxLcs9
NB9bOlLuL5HpbwH9E1qTdRLga+SmvIisIq2GiwC3zns2WwBOw/PtcnSGvPAUL14R
9OJZBAA/L/eLGdSWknQyOu55BCAvMqJET2+F1KQ1wsCDBBgBCgAPBQJg3aW1BQkP
CZwAAhsuAKgJEMRp9kRDSdoCnSAEGQEKAAYFAmDdpbUACgkQduSnxbNIXxM0nwQA
pq8/BzYJOzX39KBcYHHVD3dKbO5Pmu3CRxAD2ASv6MkebvI6QW8As9uLEzDkEtzC
63sq4E4f4z5uubi2T2GxW4BikpVuSFLRijsizKY69RXfI9JZKMNXiA9M91+klDI9
9QZfE8UfSvF9vHC6IeXuiVYbHj6IAbyZBUDL9LONnF2ZKAQAiWJKi/cqIHKh8ovY
LJL9afSvbbJDHXpZpx896kiwQQVY66eVMhLnXEM8CC+W3VlmNJvGNCbKYWp5zPHE
fQFI1AVv11nXJL+EPYB1pTT/d6Y8byObbgBJ9X2lewQ4vguTTJYjrxMJ+NZvfdF7
kugjTYVzuDa7BvqGdDm7oT4UE3vHwRgEYN2ltQEEAMQ3CzB6ovyJmXHApgWkUL2D
J71Rp4nb0cwndpD4fpjGtADl2eQdxw0+t9W0qj5u/7Y/NCVNl9gHBkAjJ9bAeFrZ
8fQe5CW4EhSYnUVUQFaSS9cW60eW/8x1rBi+WnISfVUpUEjXi8HxVBt9FBma5Hqj
cCTabCnb4vG+8lfiemo7ABEBAAEAA/9aCxSEc9L150NWc1z8+9HdliGXfLBQ0GKv
uHBtyMt32r/iJZjfWVbuWhjM5nK14gRRIyIP+FK1XUveBQQURhE0eZubhERp7cnF
ncPimuDRQcjZ2C12/zRvLC/lRgE7bLeT06vVcoK9i+Ns//ryTLatWMksXSurhUid
NVLcxtVlGQIA8/4xdnNcOHYAcmLzqrIYqmFUiI+I5IgIOo8doi/xbm0wPyb5pzY4
UEfNJoYVuETqfO7AVzA7+iZ5Jc2BcHX7jQIAzd7yhbZE8nLGWDb/AyZgaJ4Mo2xO
0UlLx7KcQKckDkJpaLixoLVquZjZdtMLqN6EiTlLVL/eYbjoqx7plUOm5wIAjMz9
juz+NP6jyD92LKuOhoQFgHQMGQGBRpRSV8E+gpu/81JRVX8eju3mtv3qP7Cm9LaJ
RoJtEeQcQfp7POs/gae9wsCDBBgBCgAPBQJg3aW1BQkDwmcAAhsuAKgJEMRp9kRD
SdoCnSAEGQEKAAYFAmDdpbUACgkQGZ8AZxE5Vu4+qgQAtocBzDw2cww8dbn3kpZ8
567lePrGwpEKsUHlWvQhAHSjo3SLImwrQBZTp/EwMFPZpE8ABDsNNxZsy3n5PkrM
sud6nEYUZSza5tL7Gsy99r3bS1FEUWjvvM4LoTVNG2SnHdp+xRDxxjz1eG+4VnrF
l7XDaXv/8SGaCbYnjxvSe1Fi0AQAh27DnWMeC/6bkCvbLwbvSkdSdms6uBZgD7re
0uWN+OYkAzCTBnV0goRLXPYvJwpkbkOYkxzsIk6mnZCeuCWueheiulmrH1y3xtRM
aMwZU4IVkW327+yEhnqMCvG7Nnc7i3VXvjNlqjfGEmiI+3S6C5OYl22QdwPh9ID9
macf5Hk=
=Cjcr
-----END PGP PRIVATE KEY BLOCK-----

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: Keybase OpenPGP v2.1.15
Comment: https://keybase.io/crypto

xo0EYN2ltQEEALxeZNBRO8U4IMnrTJ4aYZ/LDVyldQpJWM0lcZzBN6s5fspVkw0n
7I/uNFTCeNRsUbmpOoyou3MTcsb7SU4kp5qWBBTKsIdQTpqDSO0VnrX/4GT4lUhd
VkfsyKDvc62wy1ZI3GJdnBoWsVBmF1LK+toQZ70e/UwHnZlhjS4pu9vvABEBAAHN
AMK0BBMBCgAeBQJg3aW1AhsvAwsJBwMVCggCHgECF4ADFgIBAhkBAAoJEMRp9kRD
SdoCAH0D+gLyn2OO2A7+00/ZhJRlkXacjPf+NM/dvd7v92Lj1wdVJYxit9zNFDfM
xEGm1VT5+Qq1gtJRFo/3WnuIK7MoY+hz8WYH6Bl+tQM9k8eUCe8I3/FnY0tLJiWr
hr+xI+KzXe7gt6B0wVtBQ3bn9WSQNi09XYVmRB5y9YgRw5+dGNcjzo0EYN2ltQEE
ALgvQ/3WdnKux8i3ppnR+Z++xUfMA82qj0Bjm+UAu1KacoqhilYwXRhv3hfKZ9Dk
dPZXsDvsh7K2bsdQj+nG89AWr6Eb3jrwOPyjb+ZH94GQcAAZpQU1CKOFiFAHjXia
52nvvNomk+RcmTd9B2cRwhPT+HsLvy2keH+5md2iQLU9ABEBAAHCwIMEGAEKAA8F
AmDdpbUFCQ8JnAACGy4AqAkQxGn2RENJ2gKdIAQZAQoABgUCYN2ltQAKCRB25KfF
s0hfEzSfBACmrz8HNgk7Nff0oFxgcdUPd0ps7k+a7cJHEAPYBK/oyR5u8jpBbwCz
24sTMOQS3MLreyrgTh/jPm65uLZPYbFbgGKSlW5IUtGKOyLMpjr1Fd8j0lkow1eI
D0z3X6SUMj31Bl8TxR9K8X28cLoh5e6JVhsePogBvJkFQMv0s42cXZkoBACJYkqL
9yogcqHyi9gskv1p9K9tskMdelmnHz3qSLBBBVjrp5UyEudcQzwIL5bdWWY0m8Y0
JsphannM8cR9AUjUBW/XWdckv4Q9gHWlNP93pjxvI5tuAEn1faV7BDi+C5NMliOv
Ewn41m990XuS6CNNhXO4NrsG+oZ0ObuhPhQTe86NBGDdpbUBBADENwsweqL8iZlx
wKYFpFC9gye9UaeJ29HMJ3aQ+H6YxrQA5dnkHccNPrfVtKo+bv+2PzQlTZfYBwZA
IyfWwHha2fH0HuQluBIUmJ1FVEBWkkvXFutHlv/MdawYvlpyEn1VKVBI14vB8VQb
fRQZmuR6o3Ak2mwp2+LxvvJX4npqOwARAQABwsCDBBgBCgAPBQJg3aW1BQkDwmcA
AhsuAKgJEMRp9kRDSdoCnSAEGQEKAAYFAmDdpbUACgkQGZ8AZxE5Vu4+qgQAtocB
zDw2cww8dbn3kpZ8567lePrGwpEKsUHlWvQhAHSjo3SLImwrQBZTp/EwMFPZpE8A
BDsNNxZsy3n5PkrMsud6nEYUZSza5tL7Gsy99r3bS1FEUWjvvM4LoTVNG2SnHdp+
xRDxxjz1eG+4VnrFl7XDaXv/8SGaCbYnjxvSe1Fi0AQAh27DnWMeC/6bkCvbLwbv
SkdSdms6uBZgD7re0uWN+OYkAzCTBnV0goRLXPYvJwpkbkOYkxzsIk6mnZCeuCWu
eheiulmrH1y3xtRMaMwZU4IVkW327+yEhnqMCvG7Nnc7i3VXvjNlqjfGEmiI+3S6
C5OYl22QdwPh9ID9macf5Hk=
=vGS8
-----END PGP PUBLIC KEY BLOCK-----
```

And you receive the following message from Edward Snowden.

```
-----BEGIN PGP MESSAGE-----
Version: Keybase OpenPGP v2.1.15
Comment: https://keybase.io/crypto

wYwDduSnxbNIXxMBA/0bycJqCVKY20AOHh8mY3ZUTT+BAUGgQsAEg3WKmhtenXmx
JtvG+sVeojA28QxA4fofcKrFTYosiIjeruEDyxxpJrGPZvkBwiaJXWw3EbAYS63O
lyGs0eGvowlSjkk3vnYRNUqbxW6qLbtOx4rju2KyYU/vw1YzqZ7f3ZMsEU5vcdLA
UAG/Gdk7XVIKdEBUQnQMN6wgUqCcAuz2C/WDE9NIPqvmvxpUrVDp5aKQxTjQEI/5
KxapysUNefTRkz5Wkjgh3YKl12sCFpK6Jr3fPpC2g2YkR5BpIQtmRwyM4fylx+3C
wkAN6BQxhM26/kH0jUg4U8AJNhVRa3KYqw3tFfFWdpL+LBEud2MH6rrr7+XtHAAd
NxSW3UcDhfW+YjWJcFT1PT84zDKERhrr8UgbK/veRVo19sNgdr9KRpF1YUGhEDD8
eCsm2dFDvuY7B0blwW+hZ5zhdb40VRgVBQFodgiPdQ4DejiqYQFoAVMgXAiHB+v7
rqvP4CHuDbkUDzCwm+LoL+A6ugcNPCQKIj/M1xnxGmds
=xYKa
-----END PGP MESSAGE-----
```

**FLAG: What is the secret message that he sent to you and was it really him?**

### **Question 5.** Crypto Mess

One of my friends sent me the following text and it looks horrible! They said they made it by combining multiple codes but I wasn't able to decode the message.

Can you retrieve the plaintext?

```
ZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgMGEgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTggMGEgZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTggZTIgYTAgYTQgZTIgYTAgYTQgZTIgYTAgODAgZTIgYTAgYTQgZTIgYTAgYTggZTIgYTAgYTg=
```

**Flag: Enter the plaintext**

## **Case study: Hashing vs. Encryption**

Encryption techniques protect data in motion. Hashing protects data at rest. Combining these strategies could, in theory, put a strong security boundary around critical assets. But both come with risks and benefits you should know about.

Read through the following article and answer the questions below:&#x20;

****[**https://www.okta.com/au/identity-101/hashing-vs-encryption/**](https://www.okta.com/au/identity-101/hashing-vs-encryption/)****

### Question 6. Encryption

Which of the following accurately describes the primary purpose of encryption? &#x20;

1.  Encryption aims to protect data at rest. &#x20;
2.  Encryption ensures the authenticity of data. &#x20;
3.  The main goal of encryption is to secure data during transport. &#x20;
4.  Encryption primarily involves the use of hashing algorithms. 

{% hint style="info" %}
Submit the correct option as your flag (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}

### Question 7. Salting
  
Regarding salting, which of the following is accurate? &#x20;

1.  Salting involves replacing characters in the original data with random numbers. &#x20;
2.  Salting is only effective when the same salt string is used for all data points. &#x20;
3.  Hashing with salting ensures that the original data can be easily recovered. &#x20;
4.  Salting is recommended to be different for each data point for enhanced protection.&#x20;


{% hint style="info" %}
Submit the correct option as your flag (e.g., CITS1003{1} if option 1 is the correct answer).
{% endhint %}
