# Hardening & Remediation — Lessons from the Lab

## Objective

Translate each area investigated in the room into a defensive control. A security review should end with a correction and a verification step.

## Web server

- Remove unused files, backups and development artifacts from the web root.
- Review page source and static assets before publication.
- Strip unnecessary metadata from public images and documents.
- Disable directory listing where it is not required.
- Enforce authorization on the server.
- Monitor repeated path-guessing and unusual HTTP responses.

## Network exposure

- Disable listeners that have no operational requirement.
- Restrict services to trusted source networks.
- Place administrative services behind suitable network controls.
- Maintain an inventory of exposed ports and services.
- Monitor unexpected connection attempts.

## FTP and file transfer

- Disable anonymous access unless it is explicitly required and safely constrained.
- Prefer SFTP or FTPS over unencrypted FTP.
- Restrict directory listing and file operations by role.
- Separate upload areas from application and system files.
- Monitor downloads, uploads, renames and deletions.

## Passwords and SSH

- Enforce unique, strong passwords and prevent known-compromised password choices.
- Use multi-factor authentication where appropriate.
- Prefer managed SSH keys with protected private keys.
- Restrict SSH access to approved users and networks.
- Apply rate limiting and monitor repeated authentication failures.
- Remove stale accounts and rotate credentials after suspected exposure.

## Linux privileges

- Apply least privilege to user and service accounts.
- Limit sudo rules to the exact required command and arguments.
- Avoid unrestricted delegation of general-purpose utilities.
- Review passwordless privileged commands.
- Audit SUID/SGID permissions and Linux capabilities where relevant.
- Protect privileged scripts, configuration files and parent directories.

## Verification

A change is complete only after its effect is tested. Verify that:
- the unnecessary resource or service is no longer exposed;
- legitimate users can still perform required tasks;
- access permissions match the approved design;
- authentication controls behave as expected;
- logs capture the expected security events.

## Reporting

Describe the affected service, the unsafe condition, potential impact, evidence, recommended control and how the correction was verified. Do not overstate exploitability when evidence is incomplete.
