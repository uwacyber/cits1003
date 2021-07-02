# Lab 5: Vulnerabilities

## What is a vulnerability?

In cybersecurity terms, a vulnerability is \(according to NIST\):

> "A weakness in an information system, system security procedures, internal controls or implementation that could be exploited by a threat source.”

That actually doesn't help us very much because just because a threat source might exploit a weakness, it might not have an impact on the organisation in any noticeable way. 

A complicating factor of vulnerabilities is the fact that they are a weakness in people as well as physical and electronic objects. For the most part, when we talk about vulnerabilities in the context of this lab, we will be talking about software vulnerabilities.

Vulnerabilities are usually quantified in some way using a range of different characteristics and severity. Once such scheme is the Common Vulnerability Scoring System \(CVSS Scores\) that provides a range of between 0-10 to represent the severity of the vulnerability. Vulnerabilities are identified by different organisations using their own identifiers but there is a standard one provided by the MITRE organisation called the Common Vulnerabilities and Exposures \(CVE\) identifier. For example, the CVE CVE-2017-00144 \([https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2017-0144](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2017-0144)\) relates to a vulnerability in Microsoft Windows file sharing protocols that was exploited by the WannaCry ransomware. This vulnerability was identified by Microsoft as MS17-010.

## How do we find vulnerabilities?

The complexity of vulnerabilities Vulnerabilities can be split into known and unknown types. For the known vulnerabilities, they will relate to a particular configuration or version of the software. If you know you have a particular version of Windows for example, there will be a list of known vulnerabilities that can be looked up in a vulnerability database. For this reason, finding vulnerabilities usually starts with understanding all of the software and systems that are running, especially the versions of the software and the way they have been configured and deployed. 

There are tools that will do automated scans of software, especially web servers. But what is a web server and what are the applications that they run?

## Web Applications

Websites are a collection of files that provide \(static\) formatting instructions as to a browser about how to layout content on a page. This comes in the form of HTML \(Hypertext Markup Language\), CSS \(Cascading Style Sheets\) and media files such as images. Dynamic behavior to add interactivity to a page in the browser can be added via JavaScript. JavaScript can also alter the formatting of a page by interacting with a rendered page's Document Object Model \(DOM\). The DOM is the way the browser organizes the HTML elements that control the formatting of the page.

A webpage can communicate with other programs running on servers by submitting data through the use of HTML forms, or by using communications technologies such as Web Sockets and Ajax \(Asynchronous JavaScript and XML\). This communication can be handled using a variety of different programming frameworks and web services including REST \(Representational State Transfer\), Python Django, Ruby on Rails and ASP.NET \(to name just a few of the many\).

Web services that are provided by applications running on servers typically interact with database technologies of some kind to handle the data used by the application. This will be either a relational database of some sort \(some examples of which are MySQL, PostgreSQL, Microsoft SQL Server, Oracle\) or what is called a NoSQL database \(for example, MongoDB, AWS Dynamo DB, Azure Cosmos DB\).

It is the interactivity of websites and applications that make them vulnerable to exploitation and give attackers the ability to execute commands on the remote machine, or view or alter files on that machine. Although there are many ways in which the interaction of browser, web applications, operating systems and databases can be exploited, we are going to focus on the top 10 most common types of vulnerabilities that are exploited by attackers.

## OWASP Top 10 Web Vulnerabilities

Whilst browsing a website, there are a number of specific types of vulnerabilities that you would be looking for. This starts with identifying the software being used for the site, the directory structure as outlined in the previous chapter, and then concentrating on the functionality of the site.

When looking for vulnerabilities, it is worth concentrating on the most common. The Open Web Application Security Project \(OWASP\) maintains a list of the top 10 most critical security risks to web applications. The latest list is:

1. Injection
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities \(XXE\)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting \(XSS\)
8. Insecure Deserialisation
9. Using Components with Known Vulnerabilities
10. Insufficient Logging and Monitoring

There are tools which will scan a web application automatically for these vulnerabilities with varying degrees of success. Some of these tools include OWASP ZAP, Burp Suite Professional, OpenVAS and Nessus to name a few. We will be doing the process manually however because it is important to understand the underlying mechanisms by which these vulnerabilities work, and also how they can be mitigated.

Exercise: Running a vulnerable web application OWASP Juice Shop

To run the website, use the Docker command:

```bash
docker run -d -p 3000:3000 bkimminich/juice-shop
```

This will start the website on the port 3000. You can access it using the URL http://127.0.0.1:3000 and should see the home page:

![OWASP Juice Shop Home Page](.gitbook/assets/screen-shot-2021-07-02-at-11.19.55-am.png)

Before we look at the site, we are going to install a program called OWASP ZAP that will perform an automated vulnerability scan on the site.

{% hint style="info" %}
Install OWASP ZAP for your platform from [https://www.zaproxy.org/download/](https://www.zaproxy.org/download/)
{% endhint %}

Open ZAP and configure the software to scan the Juice Shop website. In the top left hand corner, select "ATTACK Mode" in the dropdown. Select Automated Scan by clicking the button in the right hand window. Type in the URL of the Juice Shop http://127.0.0.1:3000 and then click "Attack".

The scan will take a while but you will notice that the Juice Shop has popped up green alerts announcing that you have solved two challenges!

![Juice Shop after scan](.gitbook/assets/screen-shot-2021-07-02-at-1.04.32-pm.png)

The first alert suggests that you have found a confidential document. If you go back to ZAP and expand the node http://127.0.0.1:3000 that is under the Sites listing on the left hand side, you will see a node in the tree that is called "ftp"

![](.gitbook/assets/screen-shot-2021-07-02-at-1.07.08-pm.png)

FTP is the File Transfer Protocol and is used to allow users to get files from a server i.e. an early version of DropBox or OneDrive. If you click on the FTP node, you will see a number of files including one called "acquisitions.md". Click on it and in the right hand window, select the &lt;-- Response tab button. You should be able to read the text of the file in the bottom window.

**FLAG: there is a flag in this file, grab it and enter it on CTFd**

Why is this a vulnerability? Well, for a start it didn't require usernames and passwords to access, in other words, it allowed anonymous access. Secondly, as mentioned previously, sensitive files should not be left on servers withouth encryption of any sort and even then, they should be made available only to the people who need to see it. So this is one of OWASP's Sensitive Data Exposure errors. 

## Second Error

The second error reported that there was a problem with Error Handling. This vulnerability occurs when the application does not handle errors correctly and the application returns extra information about the error and where it occurred. This can reveal a lot about the website and the code it is running to an attacker. 

To find this error, go back to ZAP and click on the Active Scan tab in the bottom window. Sort the output by Code with the sort order showing the largest codes at the top. look until you can find a code of 500 which is an Internal Server Error. Take the URL that caused this error and enter it into the browser. You should see something like this:

![Error information from URL http://127.0.0.1:3000/api/](.gitbook/assets/screen-shot-2021-07-02-at-4.44.49-pm.png)

The error information tells us that the application is a Node.JS application and that it is using the software Express, version 4.17.1 to run it. It also gives us information about the file structure of the application.

## Getting Admin Access

This vulnerability is something that as a professional penetration tester you would use other tools for or search for manually. It involves bypassing the authentication process on the app. Because it involves  a technique called SQL Injection, it is going to involve understanding SQL or Structured Query Language which is used to access databases. This is beyond the scope of this unit and so I will just show you how to do the bypass. If you are interested, you can read more about this technique which works on an alarmingly large number of sites and explains why Injection is the top vulnerability on OWASP's top ten list.

To do this, go to the Login page which is accessed from the Account menu in the top right hand of the home page of Juice Shop.

In the email field, enter:

```bash
' or 1=1 -- -
```

Enter anything into the password and hit the login button and presto you are logged in as the admin user!

So why did this work? 

Well, the code is taking the value of email and password and adding it to a statement like:

```sql
SELECT * FROM Users WHERE email = '' AND password = '' AND deletedAt IS NULL
```

It is looking for users in a table called Users where the email and password match and the user has not been deleted. The problem is the use of single quotes. If we enter an email with a single quote, it will close the first quote in the statement and add the OR statement which is always going to be true because 1 does equal 1. The characters -- - are how some databases specify that everything after these characters is a comment and should be ignored. So with our injection, we get a statement that looks like this:

```sql
SELECT * FROM Users WHERE email = '' or 1=1 -- - ' AND password = '' AND deletedAt IS NULL
```

So what this will do is return \*all\* the users from the Users table. It just so happens however that the first user in the table is the admin user admin@juice-sh.op and so that is the user we get logged in as. 

SQL injection is very powerful. In other circumstances, we can use a variety of techniques to read the entire database, which in a commercial website may include credit card information, usernames and passwords and other details.

**FLAG: Now that you are logged in, go to the user's detail page by clicking on the email address under the Account menu and grab the flag!**





