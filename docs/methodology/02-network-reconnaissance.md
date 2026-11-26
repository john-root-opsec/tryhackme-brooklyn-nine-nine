# 02 — Network Reconnaissance & Service Identification

## Objective

Identify reachable TCP services on the current lab target, then use service detection to gather product and version information.

## 1. TCP SYN discovery

The supplied evidence shows a TCP SYN scan using Nmap's `-sS` mode with `--open` to limit displayed results to ports reported open.

```bash
sudo nmap -sS --open <LAB_TARGET>
```

| Option | Meaning |
|:--|:--|
| `sudo` | Runs Nmap with elevated local privileges needed for raw-packet SYN scanning on this system. |
| `nmap` | Network exploration and port-scanning utility. |
| `-sS` | TCP SYN scan. Nmap sends SYN probes and interprets responses to classify port states. |
| `--open` | Displays open or potentially open ports rather than listing every closed/filtered result. |
| `<LAB_TARGET>` | Placeholder for the current room-assigned target address. |

The observed scan reported the host as up and identified three open TCP ports corresponding to FTP, SSH and HTTP. The raw target address is omitted from this report.

A SYN scan is a discovery technique, not a complete security assessment. Filtering, packet loss, service changes and timing can affect results.

## 2. Service/version detection

The supplied evidence also shows a targeted service/version scan:

```bash
sudo nmap -sV -p21,22,80 <LAB_TARGET>
```

| Option | Meaning |
|:--|:--|
| `-sV` | Probes open ports to identify the service and, where possible, its version. |
| `-p21,22,80` | Restricts the scan to TCP ports 21, 22 and 80. |
| `sudo` | Supplies local privileges required by the selected scan behavior. |

The screenshot reports:

| Port | Service | Observed identification |
|:--:|:--|:--|
| 21/tcp | FTP | vsftpd 3.0.3 |
| 22/tcp | SSH | OpenSSH 7.6p1 (Ubuntu build string shown by Nmap) |
| 80/tcp | HTTP | Apache httpd 2.4.29 (Ubuntu) |

These are scanner observations from the lab at the time of testing. A banner or version string alone does not establish exploitability; patch level, configuration and reachable functionality must also be assessed.

## 3. Why this changed the next step

The scan provided a service map for the next investigation stages: HTTP was investigated through browser/source inspection, FTP was reviewed for authentication and file access, and SSH was reviewed as a remote-authentication surface.

## Defensive relevance

- Expose only required services.
- Restrict administrative services to trusted network paths.
- Keep service packages patched.
- Review service banners and avoid unnecessary information disclosure.
- Monitor unusual connection patterns and repeated service probing.