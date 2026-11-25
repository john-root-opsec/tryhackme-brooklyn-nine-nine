# 02 — Network Reconnaissance

## Objective

Follow the instructor's network-scanning stage: use Nmap to identify reachable TCP ports, then perform service/version identification to understand what is listening.

## 1. Understand the scan type

The instructor demonstrates a TCP SYN scan. Before running it, understand:
- why packet-level scan methods need appropriate privileges on Linux;
- how a SYN probe is interpreted;
- how a firewall or packet filter can affect the response;
- why scan output is a point-in-time observation.

If Nmap reports that elevated privileges are required, the scan did not complete with the requested method. Correct the local permission issue before interpreting target results.

## 2. Read port states

| State | Interpretation |
|:--|:--|
| `open` | A service appears to accept connections on the port. |
| `closed` | The host responds, but no service is listening on that port. |
| `filtered` | Filtering prevents Nmap from determining the state. |

Do not treat a port number as proof of a specific product. Nmap's service label may initially be based on the conventional port mapping.

## 3. Identify services and versions

Service/version detection is a separate step from basic port discovery. It sends probes and compares responses to identify the application and possible version.

A version string:
- can help select the next investigation step;
- may be hidden, modified or incomplete;
- does not prove that the software is vulnerable;
- must be interpreted with patch status and configuration in mind.

## 4. Keep the scope precise

- Scan only the current target address shown by the active TryHackMe room.
- Do not use the historical target address from the instructor's video.
- Do not expand the scan to unrelated hosts or networks.
- Keep raw target output in private notes while the room's sharing restrictions apply.

## Defensive relevance

Port exposure should match an explicit business requirement. Defenders can reduce risk by disabling unused listeners, restricting administrative services, segmenting networks and monitoring unusual connection patterns.

## Related study

- [Networking & TCP/IP](../fundamentals/networking-and-tcp-ip.md)
- [Official Nmap documentation](../references/README.md)
