# 03 — Web Reconnaissance

## Objective

Inspect the HTTP page and its source, identify a referenced image, retrieve it for local inspection, review its metadata and enumerate candidate web paths.

## 1. Browser inspection and HTML source

The browser evidence shows the target's HTTP page displaying a Brooklyn Nine-Nine image. Inspecting the page source revealed a background image resource named `brooklyn99.jpg`, CSS controlling its presentation and an HTML comment referring to steganography.

The comment was treated as an investigative clue, not proof that hidden data existed. The image was retrieved and examined locally.

## 2. Retrieve the referenced image

The terminal evidence shows `wget` retrieving the referenced JPEG and receiving HTTP `200 OK`. This saved the resource locally for file inspection. The room-specific URL is omitted from this public report.

## 3. Metadata inspection with ExifTool

The downloaded file was examined with:

```bash
exiftool brooklyn99.jpg
```

- `exiftool` reads and displays metadata from supported file formats.
- `brooklyn99.jpg` is the local input file in the observed command.

The visible output reports ordinary file properties, including JPEG format, dimensions of 533 × 300 pixels, file size and filesystem timestamps. It does not show a clear embedded author comment or an obvious hidden payload.

**Interpretation:** metadata inspection characterized the file, but the visible metadata output alone does not demonstrate successful steganographic extraction. No hidden message is claimed from this step.

## 4. Gobuster content discovery

The supplied terminal screenshot shows Gobuster v3.8.2 running in directory-enumeration mode against the HTTP service using the SecLists `common.txt` wordlist.

The visible results include:

| Candidate | Observed HTTP response |
|:--|:--|
| `index.html` | 200 |
| `.htaccess`, `.htpasswd`, `.hta`, `server-status` | 403 |

A 403 response means the server refused access to the requested resource. It is not equivalent to a 404 and should not be interpreted as proof that the path is absent. A 200 response confirms that the server returned content, not that the resource is vulnerable.

The recorded command structure was:

```bash
gobuster dir -u <HTTP_BASE_URL> -w <WORDLIST>
```

- `dir` selects directory/file discovery mode.
- `-u` supplies the base URL.
- `-w` selects the candidate-path wordlist.

## Why this stage mattered

Source inspection identified a static asset and an investigative clue. Metadata review characterized the downloaded file. Gobuster broadened the view beyond the page visible in the browser and demonstrated why HTTP status codes need interpretation.

## Defensive relevance

- Remove unused resources and sensitive files from web roots.
- Avoid embedding operational clues or internal paths in public source.
- Sanitize metadata before publishing images.
- Disable unnecessary server-status endpoints and restrict configuration-file access.
- Monitor path-guessing patterns and validate access controls server-side.