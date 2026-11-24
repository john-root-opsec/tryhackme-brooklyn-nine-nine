# 05 — Linux Enumeration

## Objective

Understand the identity and security context of an authorized Linux session.

## Areas to examine conceptually

- Current user and group membership
- Hostname and operating-system information
- Home directories and ownership
- File and directory permissions
- Running processes and services
- Listening sockets
- Environment variables and shell context
- Scheduled tasks and service configuration
- Sudo policy and privilege boundaries

## Important distinctions

- A user identity is not the same as a process identity.
- File read permission differs from directory traversal permission.
- A running service may have a separate, restricted service account.
- Root is the superuser identity, but applications may also receive specific Linux capabilities.
- Visible configuration is not automatically exploitable.

## Evidence discipline

Record what was observed, the context in which it was observed and any limitations. Avoid storing private host details, credentials or room-specific evidence in public-facing documentation.

## Defensive perspective

Use dedicated service accounts, restrict file permissions, minimize installed software, review sudo policy and monitor unexpected process or service changes.
