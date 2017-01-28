# Eiker - Scanning Malicious Files in Linux Server

Coded by Ender Phan

Written by Python 

Oporating System: Linux (All Linux Distributions)

# Intro

The Eiker is created to help Linux Administrators / Cyber Security can easy to find those malicious files which 
would make harm to their server such as Backdoor, Malware and so on.

# Usage: 

[-h] -D DIR [-d DAY] [-t TYPE]

optional arguments:

  -h, --help            show this help message and exit
  
  -D DIR, --dir DIR     Input Directory You Want To Scan
  
  -d DAY, --day DAY     You can choose what date you want to scan util today
  
  -t TYPE, --type TYPE  Chose file types you want to scan or blank if you want
                        to scan fully (e.g: .php, .html)
                        
# Example:

$ python Eiker.py -D /home/ender/Downloads/
![Alt text](http://i.imgur.com/W3NZ4Bq.png)
    
