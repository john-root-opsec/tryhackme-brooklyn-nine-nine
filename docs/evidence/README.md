<div align="center">
  <img src="../../assets/motion/04-learning-log.svg" width="100%" alt="Evidence archive" />
  <p><strong>PRECINCT 99 / FIELD EVIDENCE ARCHIVE</strong></p>
  <p><sub>ORIGINAL LAB CAPTURES • REDACTED SECRETS • DOCUMENTED FINDINGS</sub></p>
</div>

# Practical Evidence

This directory contains the screenshots selected to demonstrate the work performed in the authorized TryHackMe Brooklyn Nine-Nine lab. Each capture is referenced from its corresponding methodology chapter.

> **Redaction note:** Passwords and flag values are intentionally obscured. The completion image retains only the first name João, as requested. The screenshots are genuine captures from the lab; redactions do not change the technical findings.

## 01 / Environment and reconnaissance

![OpenVPN tunnel initialization](01-vpn-tunnel.png)

*OpenVPN initialization completes and the tunnel interface is established.*

![ICMP reachability and Nmap SYN scan](02-network-scan.png)

*ICMP replies and a SYN scan show the target reachable with TCP/21, TCP/22 and TCP/80 open.*

## 02 / Web reconnaissance

![Target web page](03-web-service.png)

*The target serves the Brooklyn Nine-Nine themed page.*

![HTML source](04-html-source.png)

*The source reveals the brooklyn99.jpg asset and a steganography hint.*

![Image metadata](05-image-metadata.png)

*The image is downloaded and inspected locally with ExifTool.*

![Gobuster results](06-gobuster.png)

*Directory enumeration returns the index and several HTTP 403 responses.*

## 03 / FTP enumeration

![Anonymous FTP access](07-ftp-anonymous.png)

*Anonymous FTP login succeeds and the directory listing exposes note_to_jake.txt.*

![FTP download](08-ftp-download.png)

*The note is successfully retrieved; the transfer reports 119 bytes.*

![Password hint in retrieved note](09-clue-analysis.png)

*The note warns Jake about a weak password, informing the next authentication-testing step.*

## 04 / SSH access and Linux enumeration

![Hydra result](10-hydra-result.png)

*Hydra reports one valid SSH credential pair. The password is redacted.*

![SSH session](11-ssh-session.png)

*An SSH session is established as the jake account.*

![User flag retrieval](12-user-flag.png)

*Home-directory enumeration leads to user.txt. The flag is redacted.*

## 05 / Privilege escalation and completion

![Root verification](13-root-verification.png)

*The less shell escape provides a shell whose identity is confirmed by whoami returning root.*

![Root flag access](14-root-flag.png)

*The root flag file is accessed; its value is redacted.*

![TryHackMe room completion](15-lab-completed.png)

*TryHackMe confirms successful room completion. The personal identifier is redacted to the first name only.*

## Evidence handling

- Screenshots substantiate the described practical steps.
- Passwords and flag values are not published.
- The target IP shown in captures is the ephemeral address assigned by the room during the recorded session.
- A screenshot demonstrates what was observed at that moment; interpretation and security impact are explained in the corresponding walkthrough chapter.