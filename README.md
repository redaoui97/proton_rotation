# proton_rotation
Unga bunga script to run a command while rotating public ip using protonvpn-cli

### Introduction

A simple python script based on protonvpn that changes your public ip. Useful to circumvent some rate-limit restrictions.

### Installation
Install the Protonvpn cli : ```sudo apt-get install protonvpn-cli```

Install python requirements : ```pip3 install -r requirements.txt```

### Usage
To use : ```python3 proton_rotator.py -n proton-username -u https://target.com -r 10```

