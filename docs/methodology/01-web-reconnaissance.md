# 01 — Web Reconnaissance

## Objective

Follow the instructor's first technical investigation: inspect the HTTP page, understand its HTML, retrieve a referenced image, examine the image metadata and discover candidate web paths.

## 1. Inspect the page in the browser

Open the HTTP service from the currently deployed lab machine. Observe:
- visible page content and title;
- page layout and background image;
- links and referenced resources;
- browser errors and redirects.

Use **View Source** to inspect the HTML delivered by the server. Use Developer Tools when the live DOM or network requests need to be compared with the original source.

## 2. Retrieve the referenced image

The instructor identifies an image resource referenced by the page and downloads it for local analysis. The purpose of this step is to move from a visual clue in the browser to a file that can be examined with local tools.

Use the current resource reference from the authorized lab session. Do not publish the room-specific URL or the retrieved file's answer-bearing contents.

## 3. Review image metadata with ExifTool

ExifTool reads metadata embedded in supported file formats. Review the fields it actually reports:
- file format and dimensions;
- timestamps;
- author/software information;
- comments or other descriptive fields.

Do not assume that every image contains hidden information. If the metadata report contains only ordinary file properties, record that accurately.

## 4. Discover candidate web paths with Gobuster

The instructor uses Gobuster in directory-discovery mode with a common-path wordlist. SecLists is the source of candidate path names.

Understand:
- target base URL;
- wordlist selection;
- HTTP method and request behavior;
- negative status-code handling;
- response code and response size;
- why candidate paths require manual validation.

A response such as 403 indicates that the server refused the request; it does not mean that the resource does not exist. A 200 response indicates that the server returned content, not that the content is vulnerable.

## Tools in this stage

- Firefox / Developer Tools
- `wget`
- ExifTool
- SecLists
- Gobuster

## Defensive interpretation

The security concern is unintended information or functionality exposed through source code, static assets, metadata or web paths.

Defensive controls include removing unused files, sanitizing metadata, disabling unnecessary directory listing, enforcing server-side authorization and monitoring repeated path-guessing requests.

## Publication boundary

Document the technique and HTTP concepts only. Do not publish room-specific paths, file contents, discovered secrets or answer-bearing observations while the room is active.
