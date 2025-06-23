---
title: "pyfuze：将Python项目打包成可执行文件的工具"
slug: pyfuze-package-python-executables
description: |
  pyfuze是一个强大的工具，可将您的Python项目打包为单个可执行文件。它支持多种打包模式，包括独立模式、在线模式和便携模式，以满足不同的需求。无论您是简化分发还是优化兼容性，pyfuze都能助您一臂之力。
tags: 
  - tool
  - dev
  - opensource
  - python
pubDatetime: 2025-06-23T10:17:26+08:00
ogImage: https://opengraph.githubassets.com/9e02699f969942007e33903448f75e3b3e6202c28b0b78610e0ca4925b43df0e/TanixLu/pyfuze
---

[原文链接](https://github.com/TanixLu/pyfuze)

---

# pyfuze

[](#pyfuze)

[![GitHub](https://camo.githubusercontent.com/4839f33f789dbd530b38516885fcc4634a9fdc4443a48e1c3553e12e308296f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d356335633563)](https://github.com/TanixLu/pyfuze) [![PyPI - Version](https://camo.githubusercontent.com/a3cdaa1882cd3d53bb9e75de904f7a22cac88e7ed71df836cda4d7ff99aa344d/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f707966757a65)](https://pypi.org/project/pyfuze/)

## Description

[](#description)

pyfuze packages your Python project into one single executable.

This project is primarily built on top of [cosmopolitan](https://github.com/jart/cosmopolitan) and [uv](https://github.com/astral-sh/uv).

## Packaging Modes

[](#packaging-modes)

| Mode                   | Standalone | Cross-Platform | Size      | Compatibility |
| ---------------------- | ---------- | -------------- | --------- | ------------- |
| **Bundle** *(default)* | ✅          | ❌              | 🔴 Large  | 🟢 High       |
| **Online**             | ❌          | ✅              | 🟢 Small  | 🟢 High       |
| **Portable**           | ✅          | ✅              | 🟡 Medium | 🔴 Low        |

**Bundle** mode packages your application with Python and all dependencies included. It only runs on the same platform it was packaged on, providing the highest compatibility. The package extracts its contents to `--unzip-path` at runtime.

**Online** mode produces a smaller, cross-platform package. At runtime, it extracts the package and downloads necessary dependencies to `--unzip-path` (internet connection required). This keeps the package lightweight and adaptable across different systems.

**Portable** mode creates a standalone, cross-platform executable that requires no extraction or internet connection. It supports only pure Python projects and dependencies. This mode is based on [python.com](https://github.com/jart/cosmopolitan/wiki/python.com) from the [cosmos-4.0.2.zip](https://github.com/jart/cosmopolitan/releases/tag/4.0.2) release, currently fixed to Python version 3.12.3.

## Cross-Platform Support

[](#cross-platform-support)

The cross-platform capability of the **online** mode is mainly limited by uv: <https://docs.astral.sh/uv/reference/policies/platforms/>

The **portable** mode’s cross-platform support depends on the APE specification itself: <https://github.com/jart/cosmopolitan/blob/master/ape/specification.md>

In summary, both modes are expected to run on macOS (ARM64 and AMD64), Linux (AMD64), and Windows (AMD64).

## Install

[](#install)

```
pip install pyfuze
```

Alternatively, you can run it directly with uvx:

```
uvx pyfuze -h
```

## Usage

[](#usage)

```
Usage: pyfuze [OPTIONS] PYTHON_PROJECT

  Package Python projects into executables.

Options:
  --mode TEXT                     Available modes:

                                  - bundle(default): Includes Python and all
                                  dependencies. Runs only on the same
                                  platform. Highest compatibility. Extracts to
                                  --unzip-path at runtime.

                                  - online: Small and cross-platform. Extracts
                                  and downloads dependencies to --unzip-path
                                  at runtime (requires internet).

                                  - portable: Standalone cross-platform
                                  executable. No extraction and internet
                                  needed. Supports only pure Python and
                                  --output-name, --entry, --reqs, --include,
                                  --exclude.

  --output-name TEXT              Output executable name [default:
                                  <project_name>.com]
  --entry TEXT                    Entry Python file. Used when your project is
                                  a folder.  [default: main.py]
  --reqs TEXT                     Add requirements.txt file to specify
                                  dependencies (input comma-separated string
                                  OR file path)
  --include TEXT                  Include extra files or folders (e.g.
                                  config.ini) (source[::destination])
                                  (repeatable)
  --exclude TEXT                  Exclude project files or folders (e.g.
                                  build.py) (repeatable).
  --unzip-path TEXT               Unzip path for bundle and online modes
                                  (default: /tmp/<project_name>)
  --python TEXT                   Add .python-version file to specify Python
                                  version (e.g. 3.11)
  --pyproject FILE                Include pyproject.toml to specify project
                                  dependencies
  --uv-lock FILE                  Include uv.lock file to lock dependencies
  --win-gui                       Hide the console window on Windows
  --env TEXT                      Add environment variables such as
                                  INSTALLER_DOWNLOAD_URL,
                                  UV_PYTHON_INSTALL_MIRROR and
                                  UV_DEFAULT_INDEX (key=value) (repeatable)
  --uv-install-script-windows TEXT
                                  UV installation script URI for Windows (URL
                                  or local path)  [default:
                                  https://astral.sh/uv/install.ps1]
  --uv-install-script-unix TEXT   UV installation script URI for Unix (URL or
                                  local path)  [default:
                                  https://astral.sh/uv/install.sh]
  -d, --debug                     Enable debug logging
  -v, --version                   Show the version and exit.
  -h, --help                      Show this message and exit.
```

## Examples

[](#examples)

### Portable Mode

[](#portable-mode)

Use portable mode to generate a standalone, cross-platform executable. Best suited for simple scripts like `simple.py`.

```
pyfuze ./examples/simple.py --mode portable --reqs requests
```

### Bundle Mode

[](#bundle-mode)

This command generates `complex.com` in the `dist` folder using the bundle mode. Since `complex` is a folder-based project, we specify the entry file using `--entry`.

We include `pyproject.toml` and `uv.lock` via `--pyproject` and `--uv-lock` to define the project's dependencies.

By default, `pyfuze` packages all Python files and packages (i.e. folders with `__init__.py`) recursively in the project directory.

The `--include` flag adds extra files like `config.txt`, while `--exclude` skips files such as `build.py`.

The default extraction path is `/tmp/complex`, but here we set it to a local `./complex` directory using `--unzip-path`. This is useful if you want to preserve files like `config.txt` across reboots, since temporary directories may be cleared. Alternatively, you can have your Python script copy `config.txt` to a persistent location, such as `%LocalAppData%` on Windows.

Finally, the `--win-gui` option hides the console window on Windows, making it ideal for GUI applications.

```
pyfuze ./examples/complex \
  --entry app.py \
  --pyproject ./examples/complex/pyproject.toml \
  --uv-lock ./examples/complex/uv.lock \
  --include ./examples/complex/config.txt \
  --exclude ./examples/complex/build.py \
  --unzip-path complex \
  --win-gui
```

### Online Mode

[](#online-mode)

Use online mode to generate a smaller, cross-platform package. It requires an internet connection to download Python and dependencies at runtime.

To improve reliability in restricted networks, you can use `--uv-install-script-windows`, `--uv-install-script-unix`, and `--env` to specify mirror URLs.

```
pyfuze ./examples/complex \
  --entry app.py \
  --pyproject ./examples/complex/pyproject.toml \
  --uv-lock ./examples/complex/uv.lock \
  --include ./examples/complex/config.txt \
  --exclude ./examples/complex/build.py \
  --unzip-path complex \
  --win-gui \
  --mode online \
  --uv-install-script-windows <uv-windows-installer-mirror-url> \
  --uv-install-script-unix <uv-unix-installer-mirror-url> \
  --env INSTALLER_DOWNLOAD_URL=<uv-binary-mirror-url> \
  --env UV_PYTHON_INSTALL_MIRROR=<python-install-mirror-url> \
  --env UV_DEFAULT_INDEX=<pypi-mirror-url>
```


