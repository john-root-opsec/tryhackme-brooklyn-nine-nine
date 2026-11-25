# 03 — FTP Service Review

## Objective

After identifying the file-transfer service, follow the instructor's review of FTP authentication, directory access and file handling.

## FTP service context

FTP uses a control connection for commands and a separate data connection for directory listings and file transfers. Traditional FTP does not encrypt credentials or data by default.

Service identification can provide product and version information, but a version string alone is not proof of a vulnerability.

## Access review

The instructor checks the authentication behavior exposed by the FTP service. Understand the distinction between:
- named-user authentication;
- anonymous access;
- successful authentication;
- permission to list a directory;
- permission to download, upload, modify or delete a file.

These permissions are separate. Being able to log in does not automatically grant write access.

## Directory and file review

When access is permitted in the lab, directory listing and file retrieval help determine what information is exposed. Treat any retrieved content as sensitive lab evidence.

For the public repository, document only the general lesson:
- what anonymous access means;
- why file exposure matters;
- how permissions constrain operations;
- why cleartext protocols create confidentiality risks.

Do not publish room-specific file names, messages, credentials, flags or contents while the room is active.

## Defensive relevance

- Disable anonymous access unless there is a documented requirement.
- Prefer SFTP or FTPS over unencrypted FTP.
- Restrict read/write permissions to the minimum necessary.
- Isolate transfer directories from application and system files.
- Monitor authentication and file-transfer events.
- Remove sensitive or obsolete files from exposed directories.
