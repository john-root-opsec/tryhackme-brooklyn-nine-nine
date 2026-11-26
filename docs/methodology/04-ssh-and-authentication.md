# 05 — SSH Authentication Assessment

## Objective

Use the password-related clue from FTP to understand weak-password risk, prepare a wordlist and conduct controlled authentication testing against the authorized lab SSH service.

## 1. SSH service confirmation

The Nmap service scan identified SSH on TCP port 22 and reported an OpenSSH version string. A separate connectivity check confirmed that TCP port 22 accepted a connection. This established that SSH was reachable; it did not establish that a particular account could authenticate.

## 2. Wordlist preparation

The evidence shows the local RockYou compressed wordlist being inspected and decompressed for use by the lab exercise. RockYou is a set of candidate passwords; its size, provenance and quality influence the amount of work involved. A larger list is not automatically better.

The wordlist itself is not included in this repository.

## 3. Hydra password audit

The supplied terminal evidence shows Hydra performing a controlled SSH password audit in the TryHackMe environment. The output reported one valid credential pair for the lab account.

The successful password is intentionally not recorded in this public document. The technical significance is that a weak/reused password allowed an online authentication attempt to succeed in the controlled room.

Relevant Hydra concepts include account selection, wordlist input, service-module selection, concurrency and success detection from the service response. Attempt rate and account lockout behavior matter in any legitimate audit.

## 4. SSH session

The subsequent terminal capture shows an SSH session established as the discovered lab user. The prompt and session output confirm the authenticated account context.

A successful SSH login grants the permissions assigned to that account. It is not equivalent to root access.

## Defensive recommendations

- Enforce strong, unique passwords and monitor password reuse.
- Prefer public-key authentication with protected private keys where appropriate.
- Restrict SSH access to approved users and network sources.
- Add multi-factor authentication where supported.
- Apply rate limits and alert on repeated failures.
- Review successful logins as well as failed attempts.
- Never store passwords or private keys in Git.

## Result

The supplied evidence supports a successful controlled password audit and subsequent SSH access as a non-root lab user. The credential value is not published.

## Practical evidence

![Hydra reports a valid SSH credential pair](../evidence/10-hydra-result.png)

*Evidence 10 — Hydra reports one valid pair. The password value is redacted; the result is retained.*

![SSH login and authenticated Jake session](../evidence/11-ssh-session.png)

*Evidence 11 — The SSH session is established as the `jake` user; subsequent commands run in that account context.*
