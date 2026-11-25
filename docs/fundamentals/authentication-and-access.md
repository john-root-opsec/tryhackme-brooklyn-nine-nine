# Authentication & Access — Lab Fundamentals

## Why this topic appears in the lesson

The instructor reviews file-transfer access first, then studies weak-password risk and remote SSH authentication. These are separate services and should be evaluated independently.

## FTP authentication

FTP is a file-transfer protocol that uses a control connection and a separate data connection. Traditional FTP does not encrypt credentials or file contents by default.

An FTP review should establish:
- which authentication modes are enabled;
- whether anonymous access is permitted;
- which directories can be listed;
- which files can be downloaded;
- whether upload, modification or deletion is permitted;
- whether access is restricted to the intended users.

A successful login alone does not establish that every file is readable or writable. Permissions must be assessed separately.

### FTP, FTPS and SFTP

- **FTP:** traditional file-transfer protocol; credentials and data are not protected by encryption by default.
- **FTPS:** FTP protected with TLS.
- **SFTP:** file-transfer subsystem carried over SSH; it is not FTP with TLS added.

## Password quality and wordlists

The lesson introduces RockYou as a password wordlist. A wordlist is a dataset of candidate passwords; it is not a credential database for a particular system and does not prove that an account uses one of its entries.

Weak or reused passwords create risk because an attacker can test common candidates against an exposed authentication service.

## Hydra and controlled authentication auditing

Hydra is used in the lesson to demonstrate password-based authentication testing in the authorized lab. The technical concepts to understand are:
- username and password candidate inputs;
- the target authentication service;
- response handling and success detection;
- attempt rate and service load;
- account lockout and monitoring;
- the distinction between a successful authentication and an authorized action.

Authentication testing must remain within the explicitly assigned room and accounts. Never test third-party accounts or production services.

## SSH authentication

SSH provides an encrypted channel for remote administration. The client verifies the server's host identity and then authenticates the user using a configured method.

Relevant controls include:
- strong, unique credentials;
- public-key authentication with protected private keys;
- multi-factor authentication where appropriate;
- limiting permitted users and source networks;
- monitoring successful and failed logins;
- rate limiting and alerting for repeated failures.

A successful SSH session gives the permissions of the authenticated account. It does not automatically grant root access.

## Defensive relevance

- Disable anonymous FTP unless there is a documented business need.
- Prefer encrypted file-transfer protocols.
- Enforce unique, strong passwords and multi-factor authentication.
- Restrict SSH exposure and allowed accounts.
- Monitor repeated authentication failures and unusual login patterns.
