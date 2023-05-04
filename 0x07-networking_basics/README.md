			0x07. Networking basics #0
			DevOps		Network

Resources

Read or watch->
- OSI model: https://en.wikipedia.org/wiki/OSI_model
- Different types of network: https://www.lifewire.com/lans-wans-and-other-area-networks-817376
- LAN network: https://en.wikipedia.org/wiki/Local_area_network
- WAN network: https://en.wikipedia.org/wiki/Wide_area_network
- Internet: https://en.wikipedia.org/wiki/Internet
- MAC address: https://whatismyipaddress.com/mac-address
- What is an IP address: https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/
- Private and public address: https://www.iplocation.net/public-vs-private-ip-address
- IPv4 and IPv6: https://www.webopedia.com/insights/ipv6-ipv4-difference/
- Localhost: https://en.wikipedia.org/wiki/Localhost
- TCP and UDP: https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/
- TCP/UDP ports List: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
- What is ping /ICMP: https://en.wikipedia.org/wiki/Ping_%28networking_utility%29
- Positional parameters: https://wiki.bash-hackers.org/scripting/posparams

man or help:
* netstat
* ping

Learning Objctives ->
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

OSI Model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:
- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.
![OSI Model](https://user-images.githubusercontent.com/109985883/236348440-e59ecf61-93e4-4c84-b9dd-9c478716aabc.png)
In this project we will mainly focus on:
- The Transport layer and especially TCP/UDP
- On the Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.
![OSI Model concrete description](https://user-images.githubusercontent.com/109985883/236348483-8594e934-c00b-4357-8a79-d0f589cd3e80.jpg)
* What it is OSI Model
* How many layers it has
* How it is organized

What is a LAN
![LAN Connection](https://user-images.githubusercontent.com/109985883/236348580-f1d227c2-ca1b-4c3b-84da-49884680cc12.jpg)
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.
- Typical usage
- Typical geographical size

What is a WAN
* Typical usage
* Typical geographical size

What is the Internet
![Internet](https://user-images.githubusercontent.com/109985883/236348607-fb42b277-4d70-4f39-9526-6065b6944e5e.gif)
The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.
- What is an IP address
- What are the 2 types of IP address
- What is localhost
- What is a subnet
- Why IPv6 was created

TCP/UDP
![UDP TCP](https://user-images.githubusercontent.com/109985883/236348706-89a5959d-0cb9-4b1f-9797-6c39f4463786.jpg)
Let’s fill the empty parts in the drawing above.
* What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
* What is the main difference between TCP and UDP
* What is a port
* Memorize SSH, HTTP and HTTPS port numbers
* What tool/protocol is often used to check if a device is connected to a network

Requirements->

General:
- Allowed editors: vi, vim, emacs
- All your Bash script files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass shellcheck without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

More Info:
The second line of all your Bash scripts should be a comment explaining what is the script doing

For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:

What is the most important position in a software company?
1. Project manager
2. Backend developer
3. System administrator
