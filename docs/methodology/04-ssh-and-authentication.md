# 04 — SSH Authentication Review

## Objective

Follow the instructor's transition from a password-security clue to controlled wordlist-based authentication testing and SSH remote access.

## Wordlists and RockYou

A wordlist is a collection of password candidates. The instructor refers to RockYou to demonstrate how previously exposed and commonly reused passwords can be used in a controlled password audit.

Important concepts:
- wordlist source and provenance;
- file format and character encoding;
- size and resource requirements;
- password reuse and predictable patterns;
- safe handling of downloaded datasets.

Do not add a downloaded wordlist to this repository. It is unnecessary for documentation and may be large.

## Hydra

Hydra is used in the lesson to demonstrate password-based authentication testing against the authorized lab service.

Understand the components of an authentication audit:
- the explicitly authorized host and service;
- the account scope;
- the candidate-password source;
- connection and attempt limits;
- the service response used to evaluate an attempt;
- the risk of account lockout or service degradation.

This document intentionally omits target-specific Hydra arguments, usernames, successful credentials and output.

## SSH

SSH provides encrypted remote administration. The client should verify the server's host identity and then authenticate using a method permitted by the server.

A successful login grants the permissions of the authenticated account. It is not equivalent to root access.

## Defensive controls

- Prefer strong, unique passwords or managed public-key authentication.
- Use multi-factor authentication where appropriate.
- Restrict SSH access to approved users and network sources.
- Apply rate limits and monitor repeated failures.
- Protect private keys and never commit credentials to Git.
- Review successful logins as well as failed attempts.

## Publication boundary

Do not publish the room's user name, password, successful Hydra result, SSH command line or active-room walkthrough.
