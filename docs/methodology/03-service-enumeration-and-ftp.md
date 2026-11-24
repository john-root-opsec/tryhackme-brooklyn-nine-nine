# 03 — Service Enumeration & FTP

## Objective

Move from knowing that a port is reachable to understanding which service may be listening, how it behaves and which security controls matter.

## Service enumeration

Enumeration gathers details such as protocol behavior, product/version hints, authentication methods, accessible resources and configuration/permission boundaries.

A banner or version string can be inaccurate, altered or insufficient to identify patch status. Corroborate evidence before making claims.

## FTP fundamentals

FTP is a legacy file-transfer protocol. Traditional FTP uses separate control and data connections and does not encrypt credentials or content by default.

Important concepts:
- control connection and data connection;
- active and passive modes;
- anonymous access;
- read, write, upload and delete permissions;
- cleartext exposure;
- FTPS versus SFTP.

## Security questions

- Is anonymous access intentionally enabled?
- Which directories are exposed?
- Are users allowed to upload or modify files?
- Can files be read by identities that do not need them?
- Are credentials or sensitive data transmitted without encryption?
- Is the service necessary and appropriately restricted?

## Defensive perspective

Prefer secure transfer mechanisms, disable unnecessary anonymous access, enforce least privilege, isolate transfer directories, monitor file operations and remove sensitive data from exposed locations.

This page explains FTP concepts and review questions. Do not add room-specific file names, messages, credentials, flags or exploitation chains while the room is active.
