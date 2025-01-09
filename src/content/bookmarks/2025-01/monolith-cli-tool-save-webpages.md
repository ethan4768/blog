---
title: "Y2Z/monolith: 一个命令行工具，快速将完整网页保存为单个HTML文件"
slug: monolith-cli-tool-save-webpages
description: |
  Y2Z/monolith是一个高效的命令行工具，能够将任何网页打包为单个HTML文件。与传统的“另存为”不同，monolith将CSS、图像和JavaScript资源嵌入到一个HTML5文档中，便于存储和分享。
tags: 
  - dev
  - tool
  - opensource
  - webdev
pubDatetime: 2025-01-09T10:00:46+08:00
ogImage: https://opengraph.githubassets.com/a7361e999e9c3000f9102e9fce5826af1cf86ec7c28a760cef5e9b6c22cf08d0/Y2Z/monolith
---

[原文链接](https://github.com/Y2Z/monolith)

---

[![monolith build status on GNU/Linux](https://github.com/Y2Z/monolith/workflows/GNU%2FLinux/badge.svg)](https://github.com/Y2Z/monolith/actions?query=workflow%3AGNU%2FLinux)[![monolith build status on macOS](https://github.com/Y2Z/monolith/workflows/macOS/badge.svg)](https://github.com/Y2Z/monolith/actions?query=workflow%3AmacOS)[![monolith build status on Windows](https://github.com/Y2Z/monolith/workflows/Windows/badge.svg)](https://github.com/Y2Z/monolith/actions?query=workflow%3AWindows)

```
 _____     ______________    __________      ___________________    ___
|     \   /              \  |          |    |                   |  |   |
|      \_/       __       \_|    __    |    |    ___     ___    |__|   |
|               |  |            |  |   |    |   |   |   |   |          |
|   |\     /|   |__|    _       |__|   |____|   |   |   |   |    __    |
|   | \___/ |          | \                      |   |   |   |   |  |   |
|___|       |__________|  \_____________________|   |___|   |___|  |___|
```

A data hoarder’s dream come true: bundle any web page into a single HTML file. You can finally replace that gazillion of open tabs with a gazillion of .html files stored somewhere on your precious little drive.

Unlike the conventional “Save page as”, `monolith` not only saves the target document, it embeds CSS, image, and JavaScript assets **all at once**, producing a single HTML5 document that is a joy to store and share.

If compared to saving websites with `wget -mpk`, this tool embeds all assets as data URLs and therefore lets browsers render the saved page exactly the way it was on the Internet, even when no network connection is available.

***

## Installation

[](#installation)

#### Using [Cargo](https://crates.io/crates/monolith) (cross-platform)

[](#using-cargo-cross-platform)

```
cargo install monolith
```

#### Via [Homebrew](https://formulae.brew.sh/formula/monolith) (macOS and GNU/Linux)

[](#via-homebrew-macos-and-gnulinux)

```
brew install monolith
```

#### Via [Chocolatey](https://community.chocolatey.org/packages/monolith) (Windows)

[](#via-chocolatey-windows)

```
choco install monolith
```

#### Via [Scoop](https://scoop.sh/#/apps?q=monolith) (Windows)

[](#via-scoop-windows)

```
scoop install main/monolith
```

#### Via [Winget](https://winstall.app/apps/Y2Z.Monolith) (Windows)

[](#via-winget-windows)

```
winget install --id=Y2Z.Monolith -e
```

#### Via [MacPorts](https://ports.macports.org/port/monolith/summary) (macOS)

[](#via-macports-macos)

```
sudo port install monolith
```

#### Using [Snapcraft](https://snapcraft.io/monolith) (GNU/Linux)

[](#using-snapcraft-gnulinux)

```
snap install monolith
```

#### Using [Guix](https://packages.guix.gnu.org/packages/monolith) (GNU/Linux)

[](#using-guix-gnulinux)

```
guix install monolith
```

#### Using [NixPkgs](https://search.nixos.org/packages?channel=unstable\&show=monolith\&query=monolith)

[](#using-nixpkgs)

```
nix-env -iA nixpkgs.monolith
```

#### Using [Flox](https://flox.dev)

[](#using-flox)

```
flox install monolith
```

#### Using [Pacman](https://archlinux.org/packages/extra/x86_64/monolith) (Arch Linux)

[](#using-pacman-arch-linux)

```
pacman -S monolith
```

#### Using [aports](https://pkgs.alpinelinux.org/packages?name=monolith) (Alpine Linux)

[](#using-aports-alpine-linux)

```
apk add monolith
```

#### Using [XBPS Package Manager](https://voidlinux.org/packages/?q=monolith) (Void Linux)

[](#using-xbps-package-manager-void-linux)

```
xbps-install -S monolith
```

#### Using [FreeBSD packages](https://svnweb.freebsd.org/ports/head/www/monolith/) (FreeBSD)

[](#using-freebsd-packages-freebsd)

```
pkg install monolith
```

#### Using [FreeBSD ports](https://www.freshports.org/www/monolith/) (FreeBSD)

[](#using-freebsd-ports-freebsd)

```
cd /usr/ports/www/monolith/
make install clean
```

#### Using [pkgsrc](https://pkgsrc.se/www/monolith) (NetBSD, OpenBSD, Haiku, etc)

[](#using-pkgsrc-netbsd-openbsd-haiku-etc)

```
cd /usr/pkgsrc/www/monolith
make install clean
```

#### Using [containers](https://www.docker.com/)

[](#using-containers)

```
docker build -t y2z/monolith .
sudo install -b dist/run-in-container.sh /usr/local/bin/monolith
```

#### From [source](https://github.com/Y2Z/monolith)

[](#from-source)

Dependencies: `libssl`, `cargo`

Install cargo (GNU/Linux)

Check if cargo is installed

```
cargo -v
```

If cargo is not already installed, install and add it to your existing `$PATH` (paraphrasing the [official installation instructions](https://doc.rust-lang.org/cargo/getting-started/installation.html)):

```
curl https://sh.rustup.rs -sSf | sh
. "$HOME/.cargo/env"
```

Proceed with installing from source:

```
git clone https://github.com/Y2Z/monolith.git
cd monolith
make install
```

#### Using [pre-built binaries](https://github.com/Y2Z/monolith/releases) (Windows, ARM-based devices, etc)

[](#using-pre-built-binaries-windows-arm-based-devices-etc)

Every release contains pre-built binaries for Windows, GNU/Linux, as well as platforms with non-standard CPU architecture.

***

## Usage

[](#usage)

```
monolith https://lyrics.github.io/db/P/Portishead/Dummy/Roads/ -o portishead-roads-lyrics.html
```

```
cat some-site-page.html | monolith -aIiFfcMv -b https://some.site/ - > some-site-page-with-assets.html
```

***

## Options

[](#options)

* `-a`: Exclude audio sources
* `-b`: Use `custom base URL`
* `-B`: Forbid retrieving assets from specified domain(s)
* `-c`: Exclude CSS
* `-C`: Read cookies from `file`
* `-d`: Allow retrieving assets only from specified `domain(s)`
* `-e`: Ignore network errors
* `-E`: Save document using `custom encoding`
* `-f`: Omit frames
* `-F`: Exclude web fonts
* `-h`: Print help information
* `-i`: Remove images
* `-I`: Isolate the document
* `-j`: Exclude JavaScript
* `-k`: Accept invalid X.509 (TLS) certificates
* `-M`: Don't add timestamp and URL information
* `-n`: Extract contents of NOSCRIPT elements
* `-o`: Write output to `file` (use “-” for STDOUT)
* `-s`: Be quiet
* `-t`: Adjust `network request timeout`
* `-u`: Provide `custom User-Agent`
* `-v`: Exclude videos

***

## Whitelisting and blacklisting domains

[](#whitelisting-and-blacklisting-domains)

Options `-d` and `-B` provide control over what domains can be used to retrieve assets from, e.g.:

```
monolith -I -d example.com -d www.example.com https://example.com -o example-only.html
```

```
monolith -I -B -d .googleusercontent.com -d googleanalytics.com -d .google.com https://example.com -o example-no-ads.html
```

***

## Dynamic content

[](#dynamic-content)

Monolith doesn't feature a JavaScript engine, hence websites that retrieve and display data after initial load may require usage of additional tools.

For example, Chromium (Chrome) can be used to act as a pre-processor for such pages:

```
chromium --headless --window-size=1920,1080 --run-all-compositor-stages-before-draw --virtual-time-budget=9000 --incognito --dump-dom https://github.com | monolith - -I -b https://github.com -o github.html
```

***

## Proxies

[](#proxies)

Please set `https_proxy`, `http_proxy`, and `no_proxy` environment variables.

***

## Contributing

[](#contributing)

Please open an issue if something is wrong, that helps make this project better.

***

## License

[](#license)

To the extent possible under law, the author(s) have dedicated all copyright related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.


