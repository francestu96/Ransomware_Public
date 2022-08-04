# Ransomware
A fully working Ransomware infrastructure

# Disclaimer
<ins>**This project is for educational purpose only! Use it at your own risk!**</ins>

# Description
The project aims to spam a ranswomeare malware which encrypt all the computer files.

In order to infect a PC, the victim must execute a VBs script. How to fool them to execute it? With some Phishing technics.

First of all the victims receive an email from a trusted entity, i.e. the government.

The message contains an attachment which looks like a PDF, but instead it is a VBs script. At opening it will require admin rights, yet who will actually care about it?
Once the script has the needed permissions, it will encrypt your entire disk and will create a file with the istruction to recover them.

To make this, victims have to send cryptocurrency to a certian address and, throught the C&C server, ask the decryption key and the istruction to get their files back.
This repo includes all the components needed in order to make a successfull Ransomware attack.

It includes the **obfuscated malware**, the **anonymous tor website**, the **C&C server** and some utils for *email harvesting and spamming**.

# How to use it
## Backend folder 
It contains configurations and codes of the **tor website** and of the **C&C server**.
In **private folder** you find the Apache, tor and ngrok configurations to keep on your private server.
In **public folder** you find the web servers: the C&C and the anonymous tor website.

## MakeScript folder
In order to obfuscate the ransomware malware code, it needs to be splitted in different encriptions phases. 
Use **make-script.py** in order to execute them easly.

## Spam folder
It contains useful scripts to spam the malware via emails.
