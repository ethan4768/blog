---
title: "微软发布Fluent System Icons：现代且友好的图标集合"
slug: microsoft-fluentui-system-icons
description: |
  Fluent System Icons是微软提供的一套现代、友好的图标集合。这些图标被设计用来提升用户体验，支持Android、iOS、macOS和Flutter等多种平台。开发者可以通过Maven、CocoaPods或直接SVG使用这些图标，轻松集成到自己的项目中。
tags: 
  - design
  - opensource
  - tool
  - dev
pubDatetime: 2025-06-16T11:43:13+08:00
ogImage: https://repository-images.githubusercontent.com/263452252/38008000-d28d-11ea-8ba0-73a56bab9a27
---

[原文链接](https://github.com/microsoft/fluentui-system-icons)

---

# Fluent UI System Icons

[](#fluent-ui-system-icons)

[![Pull request validation](https://github.com/microsoft/fluentui-system-icons/actions/workflows/pr.yml/badge.svg)](https://github.com/microsoft/fluentui-system-icons/actions/workflows/pr.yml/badge.svg)

Fluent UI System Icons are a collection of familiar, friendly and modern icons from Microsoft.

[![Fluent System Icons](/microsoft/fluentui-system-icons/raw/main/art/readme-banner.png)](https://github.com/microsoft/fluentui-system-icons/blob/main/art/readme-banner.png)

## Icon List

[](#icon-list)

* [View the full list of regular icons](https://github.com/microsoft/fluentui-system-icons/blob/main/icons_regular.md)

* [View the full list of filled icons](https://github.com/microsoft/fluentui-system-icons/blob/main/icons_filled.md)

## Direction

[](#direction)

Within the metadata.json file for an icon, a property named `directionType` is used to indicate the direction of the icon. This property can have one of the following values:

* `unique`, meaning that the icon is unique and has a specific RTL and LTR version
* `mirror`, meaning that the icon can be mirrored for RTL or LTR languages

The property `singleton` is also used to indicate the default direction that should be used for the icon.

## Installation

[](#installation)

### Android

[](#android)

The library is published via Maven Central, please ensure that the `mavenCentral()` repository has been added to the root `build.gradle` file:

```
repositories {
    ...
    mavenCentral()
}
```

Include the following dependency in your project's `build.gradle`:

```
implementation 'com.microsoft.design:fluent-system-icons:1.1.303@aar'
```

For library docs, see [android/README.md](https://github.com/microsoft/fluentui-system-icons/blob/main/android/README.md).

### iOS and macOS

[](#ios-and-macos)

#### CocoaPods

[](#cocoapods)

```
use_frameworks!

pod "FluentIcons", "1.1.303"
```

#### Carthage

[](#carthage)

```
git "git@github.com:microsoft/fluentui-system-icons.git" "1.1.303"
```

For library docs, see [ios/README.md](https://github.com/microsoft/fluentui-system-icons/blob/main/ios/README.md).

### Flutter

[](#flutter)

In the `pubspec.yaml` of your flutter project, add the following dependency:

```
dependencies:
  ...
  fluentui_system_icons: ^1.1.303
```

For library docs, see [flutter/README.md](https://github.com/microsoft/fluentui-system-icons/blob/main/flutter/README.md).

### Plain svg

[](#plain-svg)

Inline svg directly. See [packages/svg-icons/README.md](https://github.com/microsoft/fluentui-system-icons/blob/main/packages/svg-icons/README.md).

## Contributing

[](#contributing)

### Importer

[](#importer)

The importer generates the Android and iOS libraries from the icons in the `assets` directory.

Jump into the directory:

```
cd importer
```

Install npm dependencies:

```
npm install
npm run clean
```

List all the available commands:

```
npm run
```

### Build Pipeline

[](#build-pipeline)

Our [build pipeline](https://github.com/microsoft/fluentui-system-icons/actions) runs `deploy:android` and `deploy:ios` to create the libraries. The build definitions are located in `.github/workflows/`.

## Demo apps

[](#demo-apps)

You can build and run the demo apps following the steps below.

### Android

[](#android-1)

1. Follow the **Importer** section above and run the command `npm run deploy:android`
2. Open the [android](https://github.com/microsoft/fluentui-system-icons/blob/main/android) directory in Android Studio
3. Select the `sample-showcase` in the build configuration dropdown
4. Click run

### Flutter

[](#flutter-1)

Prerequisite: Make sure you have flutter configured in Android Studio

1. Open the [flutter](https://github.com/microsoft/fluentui-system-icons/blob/main/flutter) directory in Android Studio
2. Select the `example` in the directory and open it in Android Studio
3. Click run

## Contact

[](#contact)

Please feel free to [open a GitHub issue](https://github.com/microsoft/fluentui-system-icons/issues/new) and assign to the following points of contact with questions or requests.

* Jason Custer([@jasoncuster](https://github.com/jasoncuster)) / Spencer Nelson([@spencer-nelson](https://github.com/spencer-nelson)) / Joe Woodward([@thewoodpecker](https://github.com/thewoodpecker)) - Design
* Nick Romano([@rickromano](https://github.com/nickromano)) - iOS
* Will Hou([@willhou](https://github.com/willhou)) - Android
* Akashdeep Singh([@aakash1313](https://github.com/aakash1313)) - Flutter

## Code of Conduct

[](#code-of-conduct)

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct) or contact <opencode@microsoft.com> with any additional questions or comments.


