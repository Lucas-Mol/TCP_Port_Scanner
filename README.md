# TCP_Port_Scanner
The TCP Port Scanner is a simple CLI tool to verify all open ports in a given range

## Intro

The TCP Port Scanner is a simple solution to verify open port. It was made to be easy and accessible CyberSecurity tool.

## Overview:

![Overview](https://github.com/Lucas-Mol/TCP_Port_Scanner/assets/93149981/884be64b-f760-40f5-8d9e-30fce4ecaa25)


## Arguments

| Arguments            | Command              | Description                                     |
|---------------------|-----------------------|-------------------------------------------------|
| Ip Address          |  `--ip \| -i`         |  IPv4 target                                    |
| Starting port       |  `--start \| -s`      |  Integer to be the start to port range          |
| Ending port         |  `--end \| -e`        |  Integer to be the end to port range            |
| Help                |  `--help \| -h`       |  call help instructions                         |

## How to use it:
Just use: `python tcp_port_scanner.py`

**Recommendation:**

You can install pyinstaller with: `pip install pyinstaller` <br/>
And use `pyinstaller  tcp_port_scanner.py`

It'll convert this project to an executable. Therefore, you can add this new executable as a environment variable on PATH and use it at any place on your terminal 😀

## Tech Stack

- Python
