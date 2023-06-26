# 0x0C. Web server

## <p align="center">![alt text](https://github.com/Dikachis/alx-system_engineering-devops/blob/main/image_devops/Web_server.png?raw=true)</p>

**Web Server:**
Do not mix up web server and server.

A web server is a software that delivers web pages. A server is an actual computer.

But you might hear people referring to a web server using the word server. (Check out the server concept page to learn more about this.)

As mentioned above, a server is a physical machine, an actual computer, but in the Cloud era that could also be a virtual computer, generally called a VM ([Virtual Machine](https://en.wikipedia.org/wiki/Virtual_machine)) or [container](https://www.cio.com/article/247005/what-are-containers-and-why-do-you-need-them.html).

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:
=================================
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command (if using sandbox).

** A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb). **

![82VsYEC](https://github.com/Omowunmijuin/alx-system_engineering-devops/assets/109985883/8fc523b7-65f7-4a4f-a415-b277feed9a33)

#### Tips: to test your answer Bash script, feel free to reproduce the checker environment:

- start a Ubuntu 16.04 sandbox
- run your script on it
- see how it behaves

**Read:**
	- [Wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server)
	- [Web server](https://www.techtarget.com/whatis/definition/Web-server)
	- [What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)

>>
to run puppet file: ``sudo puppet apply filename.pp``
to run puppet file: ``sudo puppet apply 7-puppet_install_nginx_web_server.pp``
