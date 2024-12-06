---
title: asciinema：轻量级终端会话录制工具，提升文档效率
slug: asciinema-terminal-session-recorder
description: asciinema是一款轻量级终端会话录制工具，可将终端会话记录为.asciicast格式的文件，便于回放和分享。它以Rust编写，非常适合希望简化工作流文档的开发者。可以通过asciinema服务器轻松共享录制内容。
tags: 
  - dev
  - tool
  - opensource
  - writing
pubDatetime: 2024-12-06T10:00:39+08:00
ogImage: https://opengraph.githubassets.com/776ea4278b0ffad95cc065b00745700c83fb269435ba4a9e23b722f5498b596f/asciinema/asciinema
---

[原文链接](https://github.com/asciinema/asciinema?tab=readme-ov-file)

---

# asciinema

[](#asciinema)

[![Build Status](https://github.com/asciinema/asciinema/actions/workflows/ci.yml/badge.svg)](https://github.com/asciinema/asciinema/actions/workflows/asciinema.yml) [![license](https://camo.githubusercontent.com/2e134df563bed64892ff149f3ccf7b7d782bd3614ca97d483a685db80cb784c8/687474703a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d474e552d626c75652e737667)](https://raw.githubusercontent.com/asciinema/asciinema/master/LICENSE)

**asciinema** (aka asciinema CLI or asciinema recorder) is a command-line tool for recording terminal sessions.

Unlike typical *screen* recording software, which records visual output of a screen into a heavyweight video files (`.mp4`, `.mov`), asciinema recorder runs *inside a terminal*, capturing terminal session output into a lightweight recording files in the [asciicast](https://docs.asciinema.org/manual/asciicast/v2/) format (`.cast`).

The recordings can be replayed in a terminal, embedded on a web page with the [asciinema player](https://docs.asciinema.org/manual/player/), or published to an [asciinema server](https://docs.asciinema.org/manual/server/), such as [asciinema.org](https://asciinema.org), for further sharing.

[![asciinema CLI demo](https://camo.githubusercontent.com/46465ef3b4cb84525b87c95fcab8c9ebc6177eecc9a61dc97fbaecddf5bdd630/68747470733a2f2f61736369696e656d612e6f72672f612f383552346a54746a4b565249595854634b434e7130767a59482e737667)](https://asciinema.org/a/85R4jTtjKVRIYXTcKCNq0vzYH?autoplay=1)

Notable features:

* [recording](https://docs.asciinema.org/manual/cli/usage/#asciinema-rec-filename) and [replaying](https://docs.asciinema.org/manual/cli/usage/#asciinema-play-filename) of sessions inside a terminal,
* live streaming of terminal sessions, with local HTTP server mode, and a relay forwarding mode,
* [light-weight recording format](https://docs.asciinema.org/manual/asciicast/v2/), which is highly compressible (down to 15% of the original size e.g. with `zstd` or `gzip`),
* integration with [asciinema server](https://docs.asciinema.org/manual/server/), e.g. [asciinema.org](https://asciinema.org), for easy recording hosting.

To record a session run this command in your shell:

```
asciinema rec demo.cast
```

To stream a session via built-in HTTP server run:

```
asciinema stream --serve
```

To stream a session via a relay (asciinema server) run:

```
asciinema stream --relay
```

Check out the [Getting started guide](https://docs.asciinema.org/getting-started/) for installation and usage overview.

## Building

[](#building)

Building asciinema from source requires the [Rust](https://www.rust-lang.org/) compiler (1.70 or later), and the [Cargo package manager](https://doc.rust-lang.org/cargo/). If they are not available via your system package manager then use [rustup](https://rustup.rs/).

To download the source code, build the asciinema binary, and install it in `$HOME/.cargo/bin` run:

```
cargo install --locked --git https://github.com/asciinema/asciinema
```

Then, ensure `$HOME/.cargo/bin` is in your shell's `$PATH`.

Alternatively, you can manually download the source code and build the asciinema binary with:

```
git clone https://github.com/asciinema/asciinema
cd asciinema
cargo build --release
```

This produces the binary in *release mode* (`--release`) at `target/release/asciinema`. You can just copy the binary to a directory in your `$PATH`.

To generate man pages and shell completion files, set `ASCIINEMA_GEN_DIR` to the path where these artifacts should be stored. For example:

```
ASCIINEMA_GEN_DIR=/foo cargo build --release
```

The above command will build the binary and place the man pages in `/foo/man/`, and the shell completion files in the `/foo/completion/` directory.

Note

Windows is currently not supported. *(See [#467](https://github.com/asciinema/asciinema/issues/467))*

## Development

[](#development)

This branch contains the next generation of the asciinema CLI, written in Rust ([about the rewrite](https://discourse.asciinema.org/t/rust-rewrite-of-the-asciinema-cli/777)). It is still in a work-in-progress stage, so if you wish to propose any code changes, please first reach out to the team via [forum](https://discourse.asciinema.org/), [Matrix](https://matrix.to/#/#asciinema:matrix.org) or [IRC](https://web.libera.chat/#asciinema).

The previous generation of the asciinema CLI, written in Python, can be found in the `main` branch.

## Donations

[](#donations)

Sustainability of asciinema development relies on donations and sponsorships.

Please help the software project you use and love. Become a [supporter](https://docs.asciinema.org/donations/#individuals) or a [corporate sponsor](https://docs.asciinema.org/donations/#corporate-sponsorship).

asciinema is sponsored by:

* [Brightbox](https://www.brightbox.com/)
* [DataDog](https://datadoghq.com/)

## Consulting

[](#consulting)

If you're interested in integration or customization of asciinema to suit your needs, check [asciinema consulting services](https://docs.asciinema.org/consulting/).

## License

[](#license)

© 2011 Marcin Kulik.

All code is licensed under the GPL, v3 or later. See [LICENSE](https://github.com/asciinema/asciinema/blob/develop/LICENSE) file for details.


