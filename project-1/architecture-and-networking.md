# Architecture and Networking

## Flag 1: Getting in

We have recently been testing a new shared lab environment for all students to use! However, we had some serious security issues and we got hacked! Fortunately, we were able to revert to an older version and changed the SSH port so hackers cannot easily get in! We believe our systems are secure, but we have requested that you do a penetration test for us to make sure our systems are secure!

Hint: We can't scan the service and so we will try a few well-known variants: Try ports 22 \(they may be lying\), 2200, 2022 using ssh. The correct port will let you in immediately

You are given:

**Server**: cits3projtg2.cybernemosyne.xyz

**Username**: student

**Password**: cybernemosynecits1003

The flag is in the home directory **/home/student**.

## Flag 2: Finding the hidden creds

Wow you found the SSH port! Can you find anything else that you can use to compromise the user **jeff**? Alex left a note in `/home/jeff/read_me_jeff.txt` that said that he has hidden Jeff's new password in a file called `jeffs_creds.txt`. If you can find Jeff's new password, login as him to get your next flag!

Some useful commands for this challenge.

```text
find / <options> 2>/dev/null # Searches the entire file system based on the options you provide.
su <username> # Login as a different user
```

The flag is in the file called **flag2.txt** in `/home/jeff`.

## Flag 3: Insecure password manager

Well... maybe we shouldn't just leave our credentials lying around on our filesystem...

That is why David has been developing a new web based password manager! However, it is currently in development so it can only be reached locally on the server on port 1337 \(`http://127.0.0.1:1337/`\). For more information about how to use the beta password manager you should check David's note at `/home/alex/note_to_alex.txt`. Once you know the password for the password manager you can login using the `curl` command to send a POST request to succesfully login.

For an example:

```text
curl -X POST -d 'password=somepassword' http://127.0.0.1:1337
```

Can you access the password manager and retrieve the password for the user `alex`?

Login in as the user `alex` and you'll be able to find the flag in the file called **flag3.txt** in `/home/alex`.

## Flag 4: Pubkey shenanigans

Okay this is really bad, we believed that our password manager was secure so we put the credentials `alex` on the site. Now you have hacked into Alex's account and you can **steal David's private RSA key and use it to SSH into the server!** This is really really bad...

Can you SSH into David's account and retrieve the next flag?

When using public keys with the `ssh` command, you need to provide the `-i <filename>` option where `<filename>` is the name of the the private key file. You can also run the `ssh` command on the box, so you don't have to copy the private key to your own computer.

The flag is in the file called **flag4.txt** in `/home/david`.

## Flag 5: Hack the planet!

That is amazing that you were able to hack all of those accounts to reach David's account! We are actually extremely worried that you were able to get so far, especially since **david can run commands as the root user**. You can see what commands he can run using the command `sudo -l`, but we have recently clamped down on security and only allowed David to use the **text editor called vim** with `sudo`.

Can you use `vim` to hack the entire server?

You might find something useful on [GTFOBins](https://gtfobins.github.io/), which is a repository explaining privilege escalation techniques on Linux machines!

The flag is in a file in the `/root` folder.



