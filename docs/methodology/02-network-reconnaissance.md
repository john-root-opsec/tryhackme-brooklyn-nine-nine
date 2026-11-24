# 02 — Network Reconnaissance

## Objective

Identify which network services are reachable in the authorized scope and understand the limits of a port-scan result.

## Before scanning

- Confirm the target address from the currently deployed lab page.
- Confirm the scan is permitted by the room and platform rules.
- Identify the intended protocol and scope.
- Understand the selected scan type and timing.
- Save output responsibly; do not commit target-specific output while room restrictions apply.

## Concepts

- TCP and UDP port spaces
- TCP three-way handshake
- SYN scanning versus full TCP connect scanning
- Port states: open, closed and filtered
- Firewalls, packet filtering and network paths
- Common-port scans versus full-range scans
- Service identification versus service-version detection

## Nmap interpretation

Nmap can perform host discovery, port scanning, service/version detection and script-assisted checks. These functions are distinct. A basic port scan does not establish software version, and a version guess is not proof of vulnerability.

When reading output, distinguish host availability, protocol and port, reported state, service-name guess, version evidence and scan limitations.

## Common mistakes

- Treating a port number as proof of the exact application.
- Assuming a host is offline when ICMP is blocked.
- Treating `filtered` as `closed`.
- Claiming vulnerability based only on a service banner.
- Scanning outside the authorized range.

## Defensive perspective

Reduce exposed listeners, filter unnecessary access, segment networks, maintain an asset inventory and monitor unexpected connection attempts.

See [Networking & TCP/IP](../fundamentals/networking-and-tcp-ip.md) and [official references](../references/README.md).
