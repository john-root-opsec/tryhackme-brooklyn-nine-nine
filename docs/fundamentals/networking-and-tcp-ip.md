# Networking & TCP/IP Fundamentals

## Purpose

Network reconnaissance is meaningful only when the operator understands how devices address one another and how transport protocols expose services.

## IP addressing

An IP address identifies a network interface within an IP network. IPv4 addresses contain 32 bits and are commonly written in dotted-decimal notation. CIDR notation (for example, `192.0.2.10/24`) describes the prefix length used to identify the network portion.

A host may have several interfaces and addresses. Do not confuse a local LAN address, a VPN tunnel address, a public Internet address and a remote lab target.

## Routing

A routing table determines where packets are sent. A VPN commonly creates a virtual interface and adds routes for the permitted training network. A successful VPN connection alone does not prove that every target is reachable; route selection, firewall policy and target state also matter.

```bash
ip -br addr
ip route
ip route get 192.0.2.10
```

The example address belongs to the documentation range and is not a real lab target.

## TCP and UDP

**TCP** is connection-oriented. It uses sequence numbers, acknowledgements, retransmission and flow control to provide a reliable byte stream.

**UDP** is connectionless and provides datagrams without TCP's delivery and ordering guarantees. Applications may add their own reliability or transaction logic.

A service is associated with a transport protocol and port number. A TCP port and a UDP port with the same numeric value are separate endpoints.

## Ports and sockets

A port is a 16-bit transport-layer identifier. A network connection is commonly described by protocol, source IP, source port, destination IP and destination port.

A port scan reports what the scanner could infer at a particular time. It does not by itself establish that an application is vulnerable.

## TCP connection establishment

The normal TCP three-way handshake is:
1. Client sends **SYN**.
2. Server responds **SYN-ACK**.
3. Client sends **ACK**.

A SYN scan sends the initial SYN and interprets the response without completing the same full connection sequence as a normal TCP connect scan. Results can still be affected by firewalls, packet filtering, rate limits and network behavior.

## Common Nmap port states

| State | General meaning |
|:--|:--|
| `open` | An application is accepting connections or packets on that port. |
| `closed` | The host responded, but no application is listening on that port. |
| `filtered` | Filtering prevents Nmap from determining whether the port is open. |
| `open|filtered` | Nmap cannot distinguish an open port from filtering. |
| `closed|filtered` | Used by certain scan types when the state cannot be determined precisely. |

Port states are observations from a specific vantage point and time, not permanent properties.

## DNS and application protocols

DNS translates names to records such as IP addresses. HTTP carries web requests and responses. FTP is a legacy file-transfer protocol. SSH provides encrypted remote login and related secure channels.

## Security implications

- Exposed services increase the externally reachable attack surface.
- Unnecessary listeners should be disabled or restricted.
- Network segmentation limits the impact of compromise.
- Monitoring should capture relevant connection and authentication events.
- Encryption protects data in transit but does not correct weak authorization.

See [References](../references/README.md) for standards and official tool documentation.
