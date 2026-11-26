# Web & HTTP — Lab Fundamentals

## Why this topic appears in the lesson

The instructor inspects the page, checks its delivered HTML, retrieves a referenced image, reviews file metadata and uses directory discovery to map additional web resources.

## Browser inspection

Start by observing the page as a user would: its title and visible content, layout and background resources, links, referenced assets, redirects and browser errors.

The browser's **View Source** displays the HTML document delivered by the server. The live DOM in Developer Tools may differ because client-side JavaScript can modify it after loading.

## HTTP requests and responses

HTTP follows a request/response model. A browser or command-line client sends a request and receives a status code, headers and, when applicable, a response body.

| Code | Meaning |
|:--:|:--|
| `200` | The requested resource was returned successfully. |
| `301` / `302` | The resource redirects to another location. |
| `403` | The server understood the request but refuses access. |
| `404` | The requested resource was not found. |
| `5xx` | The server encountered an error processing the request. |

A `403` response does not mean that the resource is absent. Discovery results require interpretation.

## Static assets and file metadata

A page may reference images or other static files that can be retrieved separately. The lesson uses `wget` to save an image locally and ExifTool to inspect its metadata.

Metadata may contain file format and dimensions, timestamps, author/software fields, device information or comments. Not every image contains useful metadata. An ordinary metadata report is still a valid result; do not invent a finding when the tool reports none.

## Directory and content discovery

Gobuster's directory mode requests candidate paths from a wordlist. SecLists provides collections of candidate names commonly used for authorized assessment.

When interpreting results, review status codes, response size and redirects; understand negative status-code handling; compare suspicious responses with normal not-found behavior; and manually validate candidate resources in scope.

A discovered path is not automatically a vulnerability. It becomes security-relevant when the resource exposes information or functionality that should not be available.

## Tools in this stage

- **Firefox / Developer Tools:** inspect the page, source and network requests.
- **wget:** retrieve a referenced asset for local review.
- **ExifTool:** inspect the asset's metadata.
- **SecLists:** provide a candidate-path wordlist.
- **Gobuster:** discover candidate directories and files.

## Defensive relevance

- Remove unnecessary files and development artifacts from web roots.
- Avoid exposing directory listings and sensitive backup files.
- Review images and documents before publication.
- Keep access-control decisions on the server, not only in the client.
- Monitor unusual requests for repeated path guessing.

## Scope

Use only the web service deployed for the authorized TryHackMe room. Do not publish discovered room-specific paths, file contents or answer-bearing information while the room is active.