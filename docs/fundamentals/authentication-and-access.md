# Authentication & Access — Lab Fundamentals

## FTP authentication

FTP is a file-transfer protocol that uses a control connection and a separate data connection. Traditional FTP does not encrypt credentials or file contents by default.

An FTP review should establish which authentication modes are enabled, whether anonymous access is permitted, which directories can be listed, which files can be downloaded, whether write operations are allowed and whether access is restricted to intended users.

A successful login does not establish that every file is readable or writable. Permissions must be assessed separately.

### FTP, FTPS and SFTP

- **FTP:** traditional file-transfer protocol; credentials and data are not protected by encryption by default.
- **FTPS:** FTP protected with TLS.
- **SFTP:** file-transfer subsystem carried over SSH; it is not FTP with TLS added.

## Password quality and wordlists

A wordlist is a dataset of candidate passwords. The lab uses a known password dataset to demonstrate how weak or reused passwords can expose an account to online authentication testing.

A wordlist's provenance, encoding and size matter. Larger lists are not automatically better. Use only in an explicitly authorized assessment and consider attempt rate, account lockout and service load.

## Hydra and controlled authentication auditing

Hydra was used in the authorized lab to test password candidates against SSH. Understand the authorized host and account scope, candidate-password source, connection limits, response handling and success detection.

The lab produced a valid authentication result; the credential is intentionally not recorded here.

## SSH authentication

SSH provides an encrypted channel for remote administration. The client verifies server identity and authenticates the user using a configured method.

A successful SSH session grants the permissions of that account. It does not automatically provide root access.

## Defensive controls

- Disable anonymous FTP unless there is a documented business need.
- Prefer encrypted file-transfer protocols.
- Enforce unique, strong passwords and multi-factor authentication.
- Restrict SSH exposure and allowed accounts.
- Monitor repeated authentication failures and unusual successful logins.
- Protect private keys and credentials from source control.