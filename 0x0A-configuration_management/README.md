# 0x0A. Configuration management

![4i8il3B](https://github.com/Omowunmijuin/alx-system_engineering-devops/assets/109985883/a433ad06-e397-4bc4-a412-dd416bb29b85)

## Background Context
When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

### There were 2 pieces of bad news:
1. When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
2. The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

>>INSTALL puppet
1. $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
2. $ apt-get install -y ruby-augeas
3. $ apt-get install -y ruby-shadow
4. $ apt-get install -y puppet

>>INSTALL puppet-lint
1. $ gem install puppet-lint

>>AUTHOR
0. NAME:   Omowunmi kamiludeen
1. MAIL:   balikiskamil@gmail.com
