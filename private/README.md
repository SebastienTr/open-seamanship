# Private shelf

This folder is for documents you may keep for yourself but must not share:
manuals you bought or downloaded for your own boat (for example the Volvo
Penta owner's or workshop manual for your engine), and your own notes (engine
serial number, filter part numbers, your maintenance log).

```sh
make private     # packs this folder into dist/private/open-seamanship-private_<date>.zim
```

Then copy that ZIM to your Kiwix library, or deploy it with
`./install.sh --deploy --zim dist/private/open-seamanship-private_<date>.zim`.

Rules, enforced by the build:

- Git ignores everything here except this README. Nothing here is committed,
  built by CI, or put in a public release.
- The public pack never reads this folder.
- Do not share the private ZIM: it contains other people's copyrighted work.

Accepted files: PDF, Markdown notes (`.md`, rendered as pages), HTML, text,
PNG and JPEG. Subfolders become headings on the index page, for example
`private/volvo-penta-md2020/` and `private/my-boat/`.
