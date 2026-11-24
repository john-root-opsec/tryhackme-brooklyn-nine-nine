# 04 — SSH & Authentication

## Objective

Understand secure remote administration and the risks created by weak authentication controls.

## SSH fundamentals

SSH establishes an encrypted channel for remote access and related functions. It supports host identification and user authentication. Password and public-key authentication have different security properties and operational requirements.

## Key concepts

- Client and server roles
- Host keys and server identity
- Public/private key pairs
- Password authentication
- Authorized keys
- SSH configuration and access restrictions
- Session logs and authentication events

## Password-testing concepts

Hydra is an authentication-testing tool. In a controlled lab, the learning objective is to understand how weak passwords and insufficient controls can expose accounts—not to test unrelated accounts or services.

Wordlists such as RockYou illustrate the scale and predictability of commonly reused passwords. A wordlist is not evidence that an account is vulnerable.

## Defensive controls

- Prefer well-managed SSH keys or stronger authentication.
- Use multi-factor authentication where appropriate.
- Restrict access by user, group and network.
- Apply rate limiting and monitoring.
- Disable unused accounts and authentication methods.
- Alert on repeated failures and unusual login patterns.

A successful authentication establishes access as a particular account. It does not establish root privileges or permission to access every resource.
