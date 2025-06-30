---
title: "FlashSpace：一款快速的macOS虚拟工作空间管理器"
slug: flashspace-fast-virtual-workspace-manager
description: |
  FlashSpace 是一款为 macOS 设计的快速虚拟工作空间管理器，旨在增强和替代原生的 macOS Spaces。它可以快速切换工作空间，支持多显示器，提升工作流程的效率和灵活性。
tags: 
  - dev
  - tool
  - macos
  - opensource
pubDatetime: 2025-06-30T10:36:24+08:00
ogImage: https://opengraph.githubassets.com/ea032126870e59f8354b62befefb73e80f40e33f4acfa8f13aafef6bc9fd9545/wojciech-kulik/FlashSpace
---

[原文链接](https://github.com/wojciech-kulik/FlashSpace)

---

[![GitHub Release](https://camo.githubusercontent.com/e6c6c47124a3c9f2cfff3a55803b80533c4271be3cd6ae50effacc5fb56baa26/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f776f6a63696563682d6b756c696b2f466c61736853706163653f636f6c6f723d384132424532)](https://github.com/wojciech-kulik/FlashSpace/releases)[![Homebrew Cask Version](https://camo.githubusercontent.com/5b47e91f76e1b2557c38eb45c2b23890308e7e4a8522b311dcbda9323249969f/68747470733a2f2f696d672e736869656c64732e696f2f686f6d65627265772f6361736b2f762f666c6173687370616365)](https://formulae.brew.sh/cask/flashspace)[![min macOS](https://camo.githubusercontent.com/15209e50423be67a97aa21bbd132ffc55c2a5752fc43ad1f94e57dfb8b7e8f1f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61634f532d31342e302b2d73696c766572)](#)[![CI Status](https://camo.githubusercontent.com/3bcf4c0f8f2a61040df5a08d5710f9ff1b4bbab4bf480fffcb6fc3dad6cd9349/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f776f6a63696563682d6b756c696b2f466c61736853706163652f78636f64652d6275696c642d636865636b2e796d6c)](https://github.com/wojciech-kulik/FlashSpace/actions/workflows/xcode-build-check.yml)

# ⚡ FlashSpace

[](#-flashspace)

FlashSpace is a blazingly-fast virtual workspace manager for macOS, designed to enhance and replace native macOS Spaces. No more waiting for macOS animations.

[![FlashSpace](https://private-user-images.githubusercontent.com/3128467/415329923-94e8bc2d-f7b3-47b5-94b9-865a192c951b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEyNTEyMTksIm5iZiI6MTc1MTI1MDkxOSwicGF0aCI6Ii8zMTI4NDY3LzQxNTMyOTkyMy05NGU4YmMyZC1mN2IzLTQ3YjUtOTRiOS04NjVhMTkyYzk1MWIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDYzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA2MzBUMDIzNTE5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTFjODc3Y2FhNDIzZDVlNWQxYTUzMzkzMWVlNjE1MmQxN2Y4YjUxYzM2YTliODE3YWI1ZDMwMTcyNjgyYzlhMSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.v1vavsBB_dO8FSgdTK6b_tRKtR0RQrUZ9pz9xRly17I)](https://private-user-images.githubusercontent.com/3128467/415329923-94e8bc2d-f7b3-47b5-94b9-865a192c951b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEyNTEyMTksIm5iZiI6MTc1MTI1MDkxOSwicGF0aCI6Ii8zMTI4NDY3LzQxNTMyOTkyMy05NGU4YmMyZC1mN2IzLTQ3YjUtOTRiOS04NjVhMTkyYzk1MWIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDYzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA2MzBUMDIzNTE5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTFjODc3Y2FhNDIzZDVlNWQxYTUzMzkzMWVlNjE1MmQxN2Y4YjUxYzM2YTliODE3YWI1ZDMwMTcyNjgyYzlhMSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.v1vavsBB_dO8FSgdTK6b_tRKtR0RQrUZ9pz9xRly17I)

## ⚙️ Installation

[](#️-installation)

**Requirements:**

* macOS 14.0 or later.
* Enabled "Displays have separate Spaces" in "Desktop & Dock" system settings.

### Homebrew

[](#homebrew)

```
brew install flashspace
```

### Download Binary

[](#download-binary)

See: [Releases Page](https://github.com/wojciech-kulik/FlashSpace/releases).

### Build From Source

[](#build-from-source)

See: [Build From Source](#%EF%B8%8F-build-from-source).

## 🎥 Demo

[](#-demo)

The video shows a sample configuration where I use 3 workspaces and switch between them using hotkeys.

FlashSpace.mp4

[](https://private-user-images.githubusercontent.com/3128467/428763622-09c574c5-512f-47b5-b644-feac0e1de4b0.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEyNTEyMTksIm5iZiI6MTc1MTI1MDkxOSwicGF0aCI6Ii8zMTI4NDY3LzQyODc2MzYyMi0wOWM1NzRjNS01MTJmLTQ3YjUtYjY0NC1mZWFjMGUxZGU0YjAubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDYzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA2MzBUMDIzNTE5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTEwZjhhZTQzOGMyOGVmZTllOGUwMzU0MWQxODRmMTM0OWM1NzBkNzI3YjQ2NjY2ZTU5MmFhOWFjYTkwZGEzZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.4AzI0c7EfP6Q4vfPcqOPZ6jkjKPIQpmTWQbWSOHauuM)

## 💬 How to use

[](#-how-to-use)

1. Move all your apps to a single macOS space (per display).
2. Create a workspace.
3. Assign apps to it.
4. Assign a display to the workspace.
5. Set a hotkey for quick workspace activation.
6. Follow the same steps for other workspaces.
7. Switch between configured workspaces using hotkeys.

### The Same App In Multiple Workspaces

[](#the-same-app-in-multiple-workspaces)

If you want to keep the same app in multiple workspaces, you can use the "Floating Apps" feature from the app settings or you can add the app to multiple workspaces from the main app window.

## 👉 How it works

[](#-how-it-works)

FlashSpace allows to define virtual workspaces and assign apps to them. Each workspace is also assigned to a specific display. When you switch to a workspace, the assigned apps are automatically presented and all other apps from the assigned display are hidden.

The app allows workspaces to be switched independently on each display.

## ✨ Features

[](#-features)

* [x] Blazingly fast workspace switching
* [x] Multiple displays support
* [x] Space Control - preview all workspaces and switch between them
* [x] Hotkeys - manage apps and workspaces using keyboard
* [x] Focus detection - activate workspace on app focus
* [x] Focus manager - switch focus between apps using keyboard
* [x] Cursor manager - auto-center the cursor in the active window
* [x] Profiles - quickly switch between different configurations
* [x] Menu bar - configurable icon & text (per workspace)
* [x] Swipe Gestures - customize swipe gesture actions for your trackpad
* [x] Floating apps - keep apps visible across all workspaces
* [x] Configuration through GUI and config file
* [x] Support for multiple config file formats: JSON, YAML, and TOML
* [x] [CLI](#-command-line-interface) - interact with the app using the command line interface
* [x] [Picture-in-Picture](#-picture-in-picture-support) support
* [x] [SketchyBar](https://github.com/FelixKratz/SketchyBar) integration

## ⚖️ Project Values

[](#️-project-values)

* **Performance** - The app should be as fast as possible.
* **Simplicity** - The app should be easy to use and configure.
* **Reliability** - The app should work without glitches and unexpected behavior.
* **Invisible** - The app should help, not disturb.
* **UNIX Philosophy** - The app should do one thing and do it well - manage workspaces.

## 🔭 Space Control

[](#-space-control)

Space Control allows you to preview all workspaces on a grid and switch between them.

Use 0-9 and arrow keys to switch between workspaces.

[![FlashSpace-Space Control](https://private-user-images.githubusercontent.com/3128467/413094362-97d8f94a-00c3-47c1-af82-5934bcba4d13.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEyNTEyMTksIm5iZiI6MTc1MTI1MDkxOSwicGF0aCI6Ii8zMTI4NDY3LzQxMzA5NDM2Mi05N2Q4Zjk0YS0wMGMzLTQ3YzEtYWY4Mi01OTM0YmNiYTRkMTMuanBlZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA2MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNjMwVDAyMzUxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAyZTg2MGQyYmY1OWY5MjZiZjhmOTg1OTgxNWM3MTcxMDNlZWE2MjRmZmQ4NzVkM2ZiY2JiMTBlYzgxZmMwZGEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.3rg-3ymVvyCpo9qqAOPPzfTaoPqXogJIpBcUnH8fyzE)](https://private-user-images.githubusercontent.com/3128467/413094362-97d8f94a-00c3-47c1-af82-5934bcba4d13.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEyNTEyMTksIm5iZiI6MTc1MTI1MDkxOSwicGF0aCI6Ii8zMTI4NDY3LzQxMzA5NDM2Mi05N2Q4Zjk0YS0wMGMzLTQ3YzEtYWY4Mi01OTM0YmNiYTRkMTMuanBlZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA2MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNjMwVDAyMzUxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAyZTg2MGQyYmY1OWY5MjZiZjhmOTg1OTgxNWM3MTcxMDNlZWE2MjRmZmQ4NzVkM2ZiY2JiMTBlYzgxZmMwZGEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.3rg-3ymVvyCpo9qqAOPPzfTaoPqXogJIpBcUnH8fyzE)

## 🪟 Focus Manager

[](#-focus-manager)

FlashSpace enables fast switching of focus between windows. Use hotkeys to shift focus in any desired direction. It also allows you to jump between displays.

FocusManager.mp4

[](https://private-user-images.githubusercontent.com/3128467/411269421-9bc22b19-7cd7-48f8-a679-0adf4adc3aef.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEyNTEyMTksIm5iZiI6MTc1MTI1MDkxOSwicGF0aCI6Ii8zMTI4NDY3LzQxMTI2OTQyMS05YmMyMmIxOS03Y2Q3LTQ4ZjgtYTY3OS0wYWRmNGFkYzNhZWYubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDYzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA2MzBUMDIzNTE5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZWQ0YWNjMjlmNDQ1ZGIwZDg5ZDZhMjc5YjA4ZmRiNGMwNDc3ZGFhOWY5MDJhNjQzNWEzMzQ5OTg5OWYwZWEwMSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.bobmIWJZjdDOwNrLCnUaMxeHd0PRMsurumS-zPsOwZM)

## 🎥 Picture-In-Picture Support

[](#-picture-in-picture-support)

FlashSpace supports Picture-In-Picture mode. This is an experimental feature and can be disabled in the App Settings -> Workspaces.

macOS does not offer a public API to hide a specific window, and hiding the app also hides the PiP window. To work around this issue, FlashSpace identifies if the app supports PiP and **hides in a screen corner** all windows except the PiP window.

If the PiP window is not visible, the standard behavior is applied.

Supported browsers: Safari, Zen Browser, Chrome, Firefox, Brave, Vivaldi, Arc, Opera.

## 🖥️ SketchyBar Integration

[](#️-sketchybar-integration)

FlashSpace can be integrated with [SketchyBar](https://github.com/FelixKratz/SketchyBar) and other tools. The app runs a configurable script when the workspace is changed.

You can enable the integration in the app settings.

Configuration Example

### Only Active Workspace

[](#only-active-workspace)

##### `sketchybarrc`

[](#sketchybarrc)

```
sketchybar --add item flashspace left \
  --set flashspace \
  background.color=0x22ffffff \
  background.corner_radius=5 \
  label.padding_left=5 \
  label.padding_right=5 \
  script="$CONFIG_DIR/plugins/flashspace.sh" \
  --add event flashspace_workspace_change \
  --subscribe flashspace flashspace_workspace_change
```

##### `plugins/flashspace.sh`

[](#pluginsflashspacesh)

```
#!/bin/bash

sketchybar --set $NAME label="$WORKSPACE - $DISPLAY"
```

### All Workspaces

[](#all-workspaces)

##### `sketchybarrc`

[](#sketchybarrc-1)

```
sketchybar --add event flashspace_workspace_change

SID=1
WORKSPACES=$(/Applications/FlashSpace.app/Contents/Resources/flashspace list-workspaces)

for workspace in $WORKSPACES; do
  sketchybar --add item flashspace.$SID left \
    --subscribe flashspace.$SID flashspace_workspace_change \
    --set flashspace.$SID \
    background.color=0x22ffffff \
    background.corner_radius=5 \
    background.padding_left=5 \
    label.padding_left=5 \
    label.padding_right=5 \
    label="$workspace" \
    script="$CONFIG_DIR/plugins/flashspace.sh $workspace"

  SID=$((SID + 1))
done
```

##### `plugins/flashspace.sh`

[](#pluginsflashspacesh-1)

```
#!/bin/bash

if [ "$1" = "$WORKSPACE" ]; then
  sketchybar --set $NAME label.color=0xffff0000
else
  sketchybar --set $NAME label.color=0xffffffff
fi
```

## 💻 Command-Line Interface

[](#-command-line-interface)

FlashSpace provides a command-line interface to interact with the app. You can use it to manage workspaces, apps, and profiles.

First, install the CLI in the App Settings -> CLI. Then, use the `flashspace` command to interact with the app. Run the following command to see all available commands:

```
flashspace --help
```

## 📝 Design Decisions

[](#-design-decisions)

### 👉 Non-disruptive Behavior

[](#-non-disruptive-behavior)

FlashSpace doesn't actively manage windows, so if you switch to a workspace and call another app that is not assigned to the workspace, it will be shown on top of the workspace apps.

It is considered to be a desired behavior as it allows quickly accessing other apps without glitches or switching between workspaces.

Glitches are common in tiling window managers, often caused by not configured pop-ups or dialog windows. FlashSpace prevents these issues by not managing windows & apps that are unassigned allowing you to interact with the system in a non-disruptive way.

### 👉 No Support For Individual App Windows Per Workspace

[](#-no-support-for-individual-app-windows-per-workspace)

FlashSpace doesn't support the concept of individual app windows per workspace. This is a conscious decision to keep the app simple and fast.

This way, FlashSpace can rely on native show & hide functionality ensuring the most efficient way of managing and switching between workspaces. Additionally, this hack-free approach is battery-friendly and doesn't break other features in the system like Mission Control.

Supporting individual windows per workspace would introduce significant complexity and could negatively impact the app's performance. This limitation results from the lack of a public API in macOS to hide specific windows. Currently, the only options are to move a window to a screen corner or minimize it - neither of which provides an ideal user experience.

### 👉 No Support For Layouts

[](#-no-support-for-layouts)

FlashSpace doesn't support moving windows, resizing, or changing their layout. This is a conscious decision to keep the app simple and fast.

This feature would introduce significant complexity and could negatively impact the app's performance. Additionally, it would require a lot of work to support all edge cases and glitches. The app is designed to manage workspaces and it follows the UNIX philosophy of doing one thing and doing it well.

There are many great and free window management apps available that can be used in conjunction with FlashSpace, so there is no need to duplicate this functionality. Examples of such apps are Magnet, Rectangle, Raycast, and many others.

## 🛠️ Build From Source

[](#️-build-from-source)

FlashSpace uses [XcodeGen](https://github.com/yonaskolb/XcodeGen) to generate the Xcode project from the `project.yml` file.

1. Clone the repository.
2. Navigate to the project directory.
3. Run `brew bundle` to install dependencies.
4. Run `xcodegen generate`.
5. Open `FlashSpace.xcodeproj` in Xcode.
6. Click on the `FlashSpace` target, click on the `Signing & Capabilities` tab, and select your team.
7. Build & run the app.

Remember to run `xcodegen generate` every time you change branch or pull changes.

If you want to generate the project with configured signing, you can run:

```
XCODE_DEVELOPMENT_TEAM=YOUR_TEAM_ID xcodegen generate
```

You can also set this variable globally in your shell.

## 💡 Tips & Tricks

[](#-tips--tricks)

### 👉 Apps Appear On The Wrong Display After Sleep

[](#-apps-appear-on-the-wrong-display-after-sleep)

macOS has a bug that causes apps to appear on the wrong display after sleep. This happens if the app is hidden while the Mac is in sleep mode.

There is one workaround that can help with this issue. When you wake up your Mac, make sure to turn on all displays before logging in. This way, all apps should be shown on the correct display.

### 👉 Move & Resize Windows

[](#-move--resize-windows)

macOS 15 introduced new features that allow you to move & resize windows without 3rd party apps. To see all available options, select "Window" from the menu bar and go to "Move & Resize" submenu.

Adjusting shortcuts is quite limited, but it's possible: [see here](https://discussions.apple.com/thread/255773494?sortBy=rank). However, the most flexible approach would be to use Raycast, Magnet, or other window management apps.

### 👉 Switch Between Windows

[](#-switch-between-windows)

macOS allows you to switch focus between windows of the same app using the `` Cmd + ` `` shortcut.

### 👉 SKHD

[](#-skhd)

There is a great command-line tool called [SKHD](https://github.com/koekeishiya/skhd) that allows you to define custom global shortcuts. You can use it also with FlashSpace through the CLI.

You could even define some shortcuts that are not available in FlashSpace, like switching between specific profiles.

## 💛 Sponsors

[](#-sponsors)

Big thanks to all the sponsors who support this project 🍻!

### Monthly Sponsors

[](#monthly-sponsors)

[![@bjrmatos](https://avatars.githubusercontent.com/u/4262050 "bjrmatos")](https://github.com/bjrmatos) [![@notlus](https://avatars.githubusercontent.com/u/828989 "notlus")](https://github.com/notlus) [![@frankroeder](https://avatars.githubusercontent.com/u/19746932 "frankroeder")](https://github.com/frankroeder) [![@Cyberax](https://avatars.githubusercontent.com/u/1136550 "Cyberax")](https://github.com/Cyberax)

### One Time Sponsors

[](#one-time-sponsors)

[![@danscheer](https://avatars.githubusercontent.com/u/56642865 "danscheer")](https://github.com/danscheer) [![@felipeva](https://avatars.githubusercontent.com/u/4754195 "felipeva")](https://github.com/felipeva) [![@sinan-guler](https://avatars.githubusercontent.com/u/37443512 "sinan-guler")](https://github.com/sinan-guler) [![@maxschipper](https://avatars.githubusercontent.com/u/150921823 "maxschipper")](https://github.com/maxschipper) [![@sergiopatino](https://avatars.githubusercontent.com/u/868839 "sergiopatino")](https://github.com/sergiopatino) [![@ashaney](https://avatars.githubusercontent.com/u/25646923 "ashaney")](https://github.com/ashaney) [![@exsesx](https://avatars.githubusercontent.com/u/20399517 "exsesx")](https://github.com/exsesx) [![@konpa](https://avatars.githubusercontent.com/u/778731 "konpa")](https://github.com/konpa)

 


