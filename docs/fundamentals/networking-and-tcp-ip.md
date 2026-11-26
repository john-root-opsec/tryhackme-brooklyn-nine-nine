# Networking & TCP/IP — Lab Fundamentals

## Why this topic appears in the lesson

The instructor verifies that the deployed host is reachable, then uses Nmap to identify exposed TCP services. Understanding ICMP, TCP and port states is necessary to interpret those results correctly.

## ICMP reachability

`ping` sends ICMP Echo Requests and waits for Echo Replies. It is a basic connectivity check, not a port scan and not proof that an application is available.

- Replies received: the tested path supports the ICMP exchange.
- Packet loss: some probes did not receive replies.
- No reply: the host may be down, filtering ICMP or unreachable along the current route.

A host can block ICMP and still expose TCP services.

## TCP ports and services

TCP provides a reliable, connection-oriented byte stream. A listening application binds to a local address and port. A remote scan tests whether a connection can be established or inferred at that destination.

A port number is not definitive proof of the software running behind it. The conventional association of a port with FTP, SSH or HTTP is an initial service hint; version detection is a separate Nmap task.

## TCP three-way handshake

1. **SYN** — the client requests a connection.
2. **SYN-ACK** — the server acknowledges and offers its sequence number.
3. **ACK** — the client acknowledges the response.

## SYN scanning

The instructor demonstrates a SYN scan. Nmap sends a SYN probe and interprets the response without completing the full application connection in the same way as a TCP connect scan.

A SYN scan needs packet privileges on Linux. If Nmap reports that elevated privileges are required, that is a local permissions issue with the scan method, not evidence that the target is unreachable.

## Port states

| Nmap state | Meaning |
|:--|:--|
| `open` | A service appears to be accepting connections on the port. |
| `closed` | The host is reachable, but no service is listening on the port. |
| `filtered` | Filtering prevents Nmap from deciding whether the port is open. |
| `open|filtered` | The scan cannot distinguish an open port from a filtered response. |

A state describes what the scan could infer from one network position at one point in time.

## Service/version detection

Port discovery answers **which ports appear open**. Service/version detection attempts to identify **which application and version respond**. A banner or version result is useful evidence, but does not by itself prove that a vulnerability exists.

## Routing and VPN context

When Kali connects to TryHackMe through OpenVPN, a virtual interface and routes are added. Verify local addressing and routing before testing the lab host:

```bash
ip -br addr
ip route
```

Use only the current target address shown by the TryHackMe room. Never copy the instructor's historical target address.

## Defensive relevance

- Restrict unnecessary inbound ports.
- Expose administrative services only to trusted networks.
- Monitor repeated connection attempts and broad port sweeps.
- Maintain an accurate service inventory.
- Do not treat an open port alone as a confirmed vulnerability.

## References

See [Nmap and protocol references](../references/README.md).