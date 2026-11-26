# 04 — FTP Enumeration & File Investigation

## Objective

Review the FTP service's authentication behavior, identify what an anonymous session can access and inspect the file made available by the lab.

## 1. Service context

Nmap identified the FTP service as vsftpd 3.0.3 in the observed lab scan. FTP commonly uses a control connection for commands and a separate data connection for directory listings and file transfers. Traditional FTP does not encrypt credentials or transferred data by default.

## 2. Anonymous authentication

The supplied terminal screenshot shows an FTP client connecting to the lab service and selecting the `anonymous` account. The server returned a successful login response. The screenshot then shows a directory listing containing a text file.

This establishes that anonymous access was enabled and that the session could list the exposed directory. Authentication and authorization are distinct: a successful login does not imply write, modify or delete permissions.

## 3. File retrieval and review

The terminal evidence shows the listed text file being downloaded locally and opened. Its contents contained a message warning that a user's password was weak. The exact room-specific message and filename are omitted because they disclose a solution breadcrumb rather than a reusable technical concept.

The important reasoning step was to treat the file as a clue that informed the authentication review, rather than assuming FTP itself provided a shell.

## 4. Security interpretation

Anonymous FTP can expose internal notes or files to anyone who can reach the service. Even read-only access may disclose operational information that helps an attacker identify usernames, weak credentials or other attack surfaces.

## Defensive recommendations

- Disable anonymous access unless there is a documented business requirement.
- Prefer SFTP or FTPS over unencrypted FTP.
- Restrict directory visibility and file permissions.
- Keep transfer directories isolated from system and application files.
- Remove stale files and secrets from exposed directories.
- Monitor anonymous logins, listings and downloads.

## Result

The evidence supports anonymous FTP authentication, directory listing, retrieval of a text file and discovery of a password-related clue. The room-specific file content is not reproduced.