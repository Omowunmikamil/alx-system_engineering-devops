# 0x0D. Web stack debugging #0

### Background Context

The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Let’s start with a very simple example. My server must:

1. have a copy of the <i>/etc/passwd</i> file in <i>/tmp</i>
2. have a file named <p style= "color: red">/tmp/isworking</p> containing the string <p style= "color: red">OK</p>

Let’s pretend that without these 2 elements, my web application cannot work.
