# Eiker - Scanning Malicious Files in Linux Server

Coded by Ender Phan

Written by Python 

Operating System: Linux (All Linux Distribution)

Version 1.17

# Intro

The Eiker is created to help Linux Administrators / Cyber Security finding those malicious files which 
would make harm to their server such as Backdoor, Malware and so on with just few command lines.

# Usage: 

[-h] -D DIR [-d DAY] [-t TYPE]

optional arguments:

  -h, --help            show this help message and exit
  
  -D DIR, --dir DIR     Input Directory You Want To Scan
  
  -d DAY, --day DAY     You can choose what date you want to scan util today
  
  -t TYPE, --type TYPE  Chose file types you want to scan or blank if you want
                        to scan fully (e.g: .php, .html)
# Color levels

Red: high suspicion

Yellow: medium suspicion

White: low suspicion

# Example:
+ Scan entire Downloads directory at all time

$ python Eiker.py -D /home/ender/Downloads/
![Alt text](http://i.imgur.com/W3NZ4Bq.png)

+ Scan entire Downloads directory with the files modified since **10 days**

$ python Eiker.py -D /home/ender/Downloads/ -d 10
![Alt text](http://i.imgur.com/pAWROFA.png)

+ Scan entire Downloads directory at all time with file type is **.php**

$ python Eiker.py -D /home/ender/Downloads/ -t php
![Alt text](http://i.imgur.com/ctIPa7s.png)


