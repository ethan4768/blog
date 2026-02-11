---
title: "hoochanlon/Free-NTFS-for-Mac: Nigate: An open-source NTFS utility for Mac. It supports all Mac models (Intel and Apple Silicon), providing full read-write access, mounting, and management for NTFS drives."
slug: hoochanlon-free-ntfs-for-mac-nigate-an-open-source-ntfs-utility-for-mac-it-supports-all-mac-models-intel-and-apple-silicon-providing-full-read-write-access-mounting-and-management-for-ntfs-drives
description: |
  Nigate: An open-source NTFS utility for Mac. It supports all Mac models (Intel and Apple Silicon), providing full read-write access, mounting, and management for NTFS drives. - hoochanlon/Free-NTFS...
tags: 
  - macos
  - toos
pubDatetime: 2026-02-11T16:48:41+08:00
ogImage: https://repository-images.githubusercontent.com/580705530/d669e6ea-5b9b-4408-bee5-c4362e39636a
---

[原文链接](https://github.com/hoochanlon/Free-NTFS-for-Mac/tree/main)

---

## Nigate

[](#nigate)

**Language / 言語 / 语言**: [English](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/README.md) | [日本語](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/README.ja.md) | [中文](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/README.cn.md)

[![Main Interface](/hoochanlon/Free-NTFS-for-Mac/raw/main/src/imgs/example/2026-01-21-10.51.01.png)](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/src/imgs/example/2026-01-21-10.51.01.png)

This is the Electron GUI version of Nigate, which provides a modern and intuitive interface for NTFS device management while retaining the original geek terminal version.[1](#user-content-fn-1-400312701b17c7e73b3c7768b6a5e29c)

### Features

[](#features)

* 🎨 **Modern Interface** - Dark theme with clean and beautiful design
* 📱 **Real-time Monitoring** - Automatically detects NTFS device connections
* ✅ **Dependency Check** - Automatically checks and installs required system dependencies
* 🔄 **One-Click Mount** - Easily mount read-only NTFS devices in read-write mode
* ⚡ **Auto Read-Write** - When enabled, newly inserted NTFS devices will be automatically mounted in read-write mode without manual operation. Intelligently skips devices you manually set to read-only, respecting your choices
* 📊 **Status Display** - Clearly displays device status and operation logs
* 🛡️ **Secure & Reliable** - Uses Electron security best practices and provides a non-destructive disk repair **Reset** button
* ☕ **Prevent Sleep** - One-click toggle to prevent system sleep, ensuring the system stays awake during long operations
* 🍃 **Status Protection** - Long press for 3s to toggle protection status. When protected, auto read-write, tray mode, and prevent sleep features will be disabled to prevent accidental operations
* 🥷 **Ninja Tools** - Provide cross-filesystem mounting and end-to-end scripts from development to release, with one-click permission fixes and multi-language output to simplify complex operations and lower the usage barrier
* 💻 **Arm & Intel Mac Support** - Full support for Apple Silicon (arm64) and Intel-based Macs (x64 architecture)

### Important Notes

[](#important-notes)

Caution

The stable operation and data integrity of this software depend on the performance of storage devices. To avoid data read/write errors, transfer interruptions, or device recognition failures, it is recommended to use USB drives made with high-quality flash memory chips that have reliable read/write performance.

Important

**Read-Write Notes**:

* **Basic Operations**: Supports file copy, cut, delete, and rename (metadata-level operations)
* **Write Limitations (GUI Application)**: The GUI application (Electron GUI version) does not support direct in-place data modification on original files due to lack of kernel write permissions
* **Editing Recommendations**: Please use editors that support Atomic Write (such as VS Code / Kate). These tools save files by "creating new and replacing old files", thereby bypassing in-place overwrite limitations. Alternatively, we recommend copying files to your local Mac for editing, then copying them back
* **Additional Note**: Ninja Tools `/ninja/kamui.sh` supports direct in-place data modification on original files, suitable for scenarios requiring direct file editing [2](#user-content-fn-2-400312701b17c7e73b3c7768b6a5e29c)

- **Administrator Privileges**: Mounting operations require administrator privileges, and the system will prompt for a password

- **Windows Fast Startup**: If the device uses Fast Startup in Windows, mounting may fail. It is recommended to fully shut down (not hibernate) in Windows, or disable Fast Startup

- **Device Name**: USB drive names do not support spaces or illegal characters

- **Gatekeeper (Allow Anywhere)**: First-time use may require disabling Gatekeeper to allow unsigned applications. Run in terminal: `sudo spctl --master-disable`. After disabling, you can see the "Anywhere" option in "System Settings" > "Privacy & Security"

- **System Integrity Protection (SIP)** (Optional): To disable SIP, you need to operate in Recovery Mode:

  1. Restart Mac, hold the power button until the Apple logo and progress bar appear, enter Recovery Mode
  2. Find and open Terminal from the toolbar at the top of the screen, enter command: `csrutil disable`
  3. Close Terminal and restart Mac
  4. After restart, you can run `csrutil status` in terminal to check the status

- **Bootable USB Drives**: If a USB drive has been used to create bootable media like Ventoy or WePE, it may take some time when mounting it in read-write mode

### Quick Start

[](#quick-start)

#### Method 1: Online Experience (Shell - Ninja Tools)

[](#method-1-online-experience-shell---ninja-tools)

The following scripts are from the `ninja/` folder's Ninja Tools collection, providing command-line support for NTFS and Linux filesystem read-write access.

**🌍 All scripts support multiple languages!** Use `LANG=ja` or `LANG=zh` to set the language.

##### NTFS Read-Write Support

[](#ntfs-read-write-support)

Copy and paste into a ***terminal with full administrative privileges*** and press Enter:

```
# English (default)
/bin/bash -c \"$(curl -fsSL https://cdn.statically.io/gh/hoochanlon/Free-NTFS-for-Mac/main/ninja/nigate.sh)\"

# Japanese
LANG=ja /bin/bash -c \"$(curl -fsSL https://cdn.statically.io/gh/hoochanlon/Free-NTFS-for-Mac/main/ninja/nigate.sh)\"

# Chinese
LANG=zh /bin/bash -c \"$(curl -fsSL https://cdn.statically.io/gh/hoochanlon/Free-NTFS-for-Mac/main/ninja/nigate.sh)\"
```

##### Linux ext4 and Other Filesystem Read-Write Support

[](#linux-ext4-and-other-filesystem-read-write-support)

Supports ext2/3/4, btrfs, xfs, zfs, NTFS, exFAT, LUKS encryption, LVM, RAID, and many other filesystems:

```
# English (default)
/bin/bash -c \"$(curl -fsSL https://cdn.statically.io/gh/hoochanlon/Free-NTFS-for-Mac/main/ninja/kamui.sh)\"

# Japanese
LANG=ja /bin/bash -c \"$(curl -fsSL https://cdn.statically.io/gh/hoochanlon/Free-NTFS-for-Mac/main/ninja/kamui.sh)\"

# Chinese
LANG=zh /bin/bash -c \"$(curl -fsSL https://cdn.statically.io/gh/hoochanlon/Free-NTFS-for-Mac/main/ninja/kamui.sh)\"
```

#### Method 2: Download Locally (Shell - Ninja Tools)

[](#method-2-download-locally-shell---ninja-tools)

After downloading, you can directly type `nigate` to start:

```
curl https://fastly.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac/ninja/nigate.sh > ~/Public/nigate.sh && sudo -S mkdir -p /usr/local/bin && cd /usr/local/bin && sudo ln -s ~/Public/nigate.sh nigate.shortcut && echo \"alias nigate='bash nigate.shortcut'\" >> ~/.zshrc && osascript -e 'tell application \"Terminal\" to do script \"nigate\"'
```

#### Method 3: GUI Version (Electron)

[](#method-3-gui-version-electron)

Download and use from [tags](https://github.com/hoochanlon/Free-NTFS-for-Mac/tags).

* **🌍 Application interface supports multiple languages**: Chinese (Simplified/Traditional), Japanese, English, German, and more

**Tray**

[![ ](/hoochanlon/Free-NTFS-for-Mac/raw/main/src/imgs/example/2026-01-21-10.52.29.png)](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/src/imgs/example/2026-01-21-10.52.29.png)

### Dependency Management

[](#dependency-management)

#### One-Click Install Dependencies

[](#one-click-install-dependencies)

```
# English (default)
/bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/kunai.sh)\"

# Japanese
LANG=ja /bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/kunai.sh)\"

# Chinese
LANG=zh /bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/kunai.sh)\"
```

#### One-Click Uninstall Dependencies

[](#one-click-uninstall-dependencies)

```
# English (default)
/bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/ninpo.sh)\"

# Japanese
LANG=ja /bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/ninpo.sh)\"

# Chinese
LANG=zh /bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/ninpo.sh)\"
```

### System Permission Settings

[](#system-permission-settings)

Configure system permissions and security settings (Gatekeeper, SIP, etc.):

```
# English (default)
/bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/shuriken.sh)\"

# Japanese
LANG=ja /bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/shuriken.sh)\"

# Chinese
LANG=zh /bin/bash -c \"$(curl -fsSL https://cdn.jsdelivr.net/gh/hoochanlon/Free-NTFS-for-Mac@main/ninja/shuriken.sh)\"
```

> For more information, see: [Ninja Tools Testing #39](https://github.com/hoochanlon/Free-NTFS-for-Mac/issues/39) and [Ninja Tools Documentation](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/docs/07-%E5%BF%8D%E8%80%85%E5%B7%A5%E5%85%B7%E9%9B%86%E5%86%85%E5%AE%B9%E8%AF%B4%E6%98%8E.md)

### Operations & Development

[](#operations--development)

### 🚀 One-Click Run (Recommended for Beginners)

[](#-one-click-run-recommended-for-beginners)

**Users without any development environment can deploy in one step!**

The project provides intelligent one-click run scripts that automatically detect and install all necessary tools (Node.js, pnpm, dependencies, etc.), then automatically compile and start the application.

#### Method 1: Use One-Click Script in Project Root (Recommended)

[](#method-1-use-one-click-script-in-project-root-recommended)

```
# Clone project
git clone <repository-url>
cd Free-NTFS-for-Mac

# One-click run (auto-install environment, compile, start)
./dev.sh
```

Or use the script in the ninja directory:

```
./ninja/izanaki.sh
```

**The script automatically completes:**

* ✅ Detects and installs Node.js (if not present)
* ✅ Detects and installs pnpm (if not present)
* ✅ Syncs version numbers
* ✅ Installs project dependencies
* ✅ Compiles TypeScript code
* ✅ Compiles Stylus styles
* ✅ Starts application (development mode)

#### Method 2: Manual Installation (For Experienced Developers)

[](#method-2-manual-installation-for-experienced-developers)

1. **Clone and Initialize**

```
git clone <repository-url>
cd Free-NTFS-for-Mac
pnpm install
```

2. **Run Application**

```
# Production mode
pnpm start

# Development mode (automatically opens DevTools)
pnpm run dev
```

3. **Build Application**

```
pnpm run build
```

### 🌍 Multi-Language Support

[](#-multi-language-support)

All scripts and tools support multiple languages, can be set via `LANG` environment variable:

```
# English (default)
./dev.sh

# Japanese
LANG=ja ./dev.sh

# Chinese
LANG=zh ./dev.sh
```

Supported scripts include:

* `dev.sh` / `ninja/izanaki.sh` - One-click run script
* `ninja/kamui.sh` - Linux filesystem mount
* `ninja/nigate.sh` - NTFS auto mount
* `ninja/build.sh` - Application packaging
* `ninja/shuriken.sh` - System permission settings
* And all other ninja tools collection scripts

#### Project Setup Script

[](#project-setup-script)

If you encounter errors with `pnpm run dev`, run the setup script to fix them:

```
pnpm run setup
```

Or run directly:

```
./ninja/izanaki.sh
```

This script automatically:

* ✅ Checks if required files exist
* ✅ Sets script execution permissions
* ✅ Creates necessary directory structure
* ✅ Syncs version numbers
* ✅ Compiles TypeScript and Stylus
* ✅ Verifies critical files

After building, you can find the packaged application in the `dist` directory.

### Mac Packaging Instructions

[](#mac-packaging-instructions)

After packaging, the following will be generated in the `dist` directory:

* **DMG File**: Installation package for distribution
* **ZIP File**: Compressed application package

Other notes:

* Use `./ninja/build.sh` script for more flexible packaging
* First run may require right-clicking the application and selecting "Open" (macOS security restrictions)

### Troubleshooting

[](#troubleshooting)

#### Mount Failure

[](#mount-failure)

1. Check if all dependencies are installed
2. Confirm the device is not occupied by other programs
3. If it's a Windows Fast Startup issue, fully shut down the device in Windows

#### Dependency Installation Failure

[](#dependency-installation-failure)

1. Ensure network connection is normal
2. Check if Homebrew is correctly installed
3. May need to manually run installation commands in terminal

#### Application Won't Start

[](#application-wont-start)

1. Check if Node.js version meets requirements
2. Delete `node_modules` and rerun `pnpm install`
3. Check console error messages

### Acknowledgments

[](#acknowledgments)

Thank you to all developers, testers, and users who have contributed to this project! See [ACKNOWLEDGMENTS.md](https://github.com/hoochanlon/Free-NTFS-for-Mac/blob/main/ACKNOWLEDGMENTS.md) for details.

## Footnotes

1. **Note**: Using this tool to mount or modify NTFS devices carries a risk of data loss. It is strongly recommended to backup important data before operation. This tool is provided "as is" without any warranty. The developer is not responsible for data loss caused by using this tool. [↩](#user-content-fnref-1-400312701b17c7e73b3c7768b6a5e29c)

2. Powered by [nohajc/anylinuxfs](https://github.com/nohajc/anylinuxfs) with secondary encapsulation [↩](#user-content-fnref-2-400312701b17c7e73b3c7768b6a5e29c)


