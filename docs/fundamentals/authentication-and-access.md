# Authentication & Access Fundamentals

## Authentication, authorization and accounting

- **Authentication:** establishes who or what is requesting access.
- **Authorization:** determines which actions that identity may perform.
- **Accounting:** records activity for review and audit.

A successful login does not imply administrative authorization.

## Password security

Defenses include unique passwords, password managers, multi-factor authentication, breached-password screening, rate limiting and monitoring.

Systems should store password verifiers using purpose-built password hashing schemes with unique salts and appropriate work factors—not reversible encryption or plain text.

## SSH

SSH provides encrypted remote access. Authentication may use passwords, public-key cryptography or other configured methods.

Public-key authentication uses a private key kept by the client and a corresponding public key authorized by the server. Private keys must never be committed to source control.

Defensive controls include disabling unused authentication methods, restricting who may log in, protecting private keys, monitoring failed and successful logins and limiting network exposure.

## FTP and secure alternatives

Traditional FTP does not provide confidentiality for credentials or file contents by default. FTPS adds TLS to FTP. SFTP is a file-transfer subsystem carried over SSH; it is not simply FTP with encryption.

## Password-guessing risk

Repeated authentication attempts can indicate password spraying, brute-force attempts, credential stuffing or legitimate user error. A single failed login is not enough to classify an attack.

Defenses include rate limiting, multi-factor authentication, source/account monitoring and alerting on abnormal failure patterns.

## Scope and authorization

Authentication-testing tools must only be used against accounts and services explicitly included in the authorized exercise. Never test real users, public services or unrelated systems.
