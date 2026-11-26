<div align="center">
<img src="../assets/motion/04-learning-log.svg" width="100%" alt="Documentation archive" />
**PRECINCT 99 / TECHNICAL KNOWLEDGE BASE**
<sub>COMPLETED LAB • PRACTICAL WALKTHROUGH • DEFENSIVE CONTEXT</sub>
</div>

# Documentation Index

This knowledge base documents the completed TryHackMe Brooklyn Nine-Nine lab. It preserves the instructor's practical sequence while separating observed actions, technical interpretation and defensive recommendations.

## 01 / Fundamentals

| Document | What it covers |
|:--|:--|
| [Networking & TCP/IP](fundamentals/networking-and-tcp-ip.md) | ICMP reachability, TCP ports, SYN scans and Nmap port states. |
| [Web & HTTP](fundamentals/web-and-http.md) | HTTP pages, source inspection, static assets, metadata and directory discovery. |
| [Linux & Permissions](fundamentals/linux-and-permissions.md) | Users, home directories, file permissions, sudo policy and privilege boundaries. |
| [Authentication & Access](fundamentals/authentication-and-access.md) | FTP access models, password auditing, wordlists and SSH authentication. |

## 02 / Assessment Walkthrough

| Stage | Document | Focus |
|:--:|:--|:--|
| 01 | [Environment & VPN](methodology/00-environment-setup.md) | Approved connection, tunnel interface, routing and reachability. |
| 02 | [Network Reconnaissance](methodology/02-network-reconnaissance.md) | TCP SYN scan, exposed services and service/version identification. |
| 03 | [Web Reconnaissance](methodology/01-web-reconnaissance.md) | HTTP page, source inspection, image retrieval, metadata and content discovery. |
| 04 | [FTP Investigation](methodology/03-service-enumeration-and-ftp.md) | Anonymous access, directory listing, file retrieval and defensive implications. |
| 05 | [SSH Authentication](methodology/04-ssh-and-authentication.md) | Wordlists, controlled password auditing and SSH access. |
| 06 | [Linux Enumeration](methodology/05-linux-enumeration.md) | Authenticated user context, home directories, files and permissions. |
| 07 | [Privilege Escalation](methodology/06-privilege-escalation.md) | Sudo policy, `less` shell capability and root-context verification. |

## 03 / Defensive Context

| Document | Related lesson |
|:--|:--|
| [Detection & Monitoring](defense/01-detection-and-monitoring.md) | Web discovery, scans, FTP access, SSH authentication and privileged activity. |
| [Hardening & Remediation](defense/02-hardening-and-remediation.md) | Restrict exposed services, protect files, harden authentication and narrow sudo permissions. |

## 04 / References & Templates

- [Official tool and protocol references](references/README.md)
- [Technical note template](templates/technical-note-template.md)
- [Security review template](templates/security-review-template.md)

## How to read the walkthrough

Each stage distinguishes:

1. **Objective** — the question the step was intended to answer.
2. **Observed evidence** — what is visible in the supplied terminal or browser captures.
3. **Command and options** — what the recorded command does and what its relevant parameters mean.
4. **Interpretation** — what the output supports, and what it does not prove.
5. **Next decision** — how the observation informed the next stage.
6. **Defensive relevance** — how a system owner could detect or reduce the risk.

## Evidence and privacy

The public write-up deliberately excludes working credentials, password values, flag values, VPN profile names and raw connection details. Public screenshots must be redacted before they are added to the repository. Evidence captions describe the event without exposing the secret itself.

The completion screen confirms the lab was completed. The original image includes a full personal identifier; use only a manually redacted copy if it is later added to the public repository.