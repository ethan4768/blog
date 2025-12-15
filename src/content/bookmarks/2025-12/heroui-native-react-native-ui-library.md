---
title: "HeroUI Native: 一款美观、快速且现代的React Native UI库"
slug: heroui-native-react-native-ui-library
description: |
  HeroUI Native是一款美观、快速且现代的React Native UI库，提供丰富的组件和主题自定义选项，适合快速构建移动应用。支持expo，可以轻松体验示例应用，快速入门开发。
tags: 
  - ReactNative
  - UI
  - dev
  - opensource
pubDatetime: 2025-12-15T10:31:28+08:00
ogImage: https://repository-images.githubusercontent.com/995504072/65b1b2de-ddba-4c5f-978e-a7a782faf17e
---

[原文链接](https://github.com/heroui-inc/heroui-native/)

---

[![heroui](https://camo.githubusercontent.com/fe4c9bd5a371e247d6a42bab8622f9c161024565777348fb1d2c87fe62e99ba5/68747470733a2f2f6865726f75692d6173736574732e6e7963332e63646e2e6469676974616c6f6365616e7370616365732e636f6d2f696d616765732f6865726f75692d6e61746976652d7265706f2d322e706e67)](https://heroui.com)

Beautiful, fast and modern React Native UI library

v1.0.0-beta.8

## Preview App

[](#preview-app)

Experience HeroUI Native components in action with our preview app! You can explore all components and their variants directly on your device.

### Prerequisites

[](#prerequisites)

Make sure you have the latest version of [Expo Go](https://expo.dev/go) installed on your mobile device

### How to Access

[](#how-to-access)

Choose one of the following methods to access the preview app:

#### Option 1: Scan the QR Code

[](#option-1-scan-the-qr-code)

Use your device's camera or Expo Go app to scan:

[![Expo Go QR Code](https://camo.githubusercontent.com/38468f806873d979ddf5ad5d3fa4bfefb7f8c5cca114da6b616e2591dc118312/68747470733a2f2f6865726f75692d6173736574732e6e7963332e63646e2e6469676974616c6f6365616e7370616365732e636f6d2f696d616765732f71722d636f64652d6e61746976652e706e67)](https://camo.githubusercontent.com/38468f806873d979ddf5ad5d3fa4bfefb7f8c5cca114da6b616e2591dc118312/68747470733a2f2f6865726f75692d6173736574732e6e7963332e63646e2e6469676974616c6f6365616e7370616365732e636f6d2f696d616765732f71722d636f64652d6e61746976652e706e67)

> **Note for Android users:** If scanning the QR code with your device's camera or other scanner apps redirects to a browser and shows a 404 error, open Expo Go first and use its built-in QR scanner instead.

#### Option 2: Click the Link

[](#option-2-click-the-link)

**[📱 Open Demo App in Expo Go](https://link.heroui.com/native-demo)**

This will automatically open the app in Expo Go if it's installed on your device.

## Quick Start with Example App

[](#quick-start-with-example-app)

Want to start building with HeroUI Native immediately? We provide a standalone example app that's fully configured and ready to use:

**[🚀 HeroUI Native Example App](https://github.com/heroui-inc/heroui-native-example)**

This repository contains a pre-configured React Native app with HeroUI Native already set up, including:

* All necessary dependencies installed
* Uniwind configuration ready
* Example components showcasing best practices
* Perfect for quickly prototyping or starting a new project

Simply clone, install, and start building!

## Getting Started

[](#getting-started)

### 1. Install HeroUI Native

[](#1-install-heroui-native)

```
npm install heroui-native
```

### 2. Install Mandatory Peer Dependencies

[](#2-install-mandatory-peer-dependencies)

```
npm install react-native-screens@~4.16.0 react-native-reanimated@~4.1.1 react-native-worklets@0.5.1 react-native-safe-area-context@~5.6.0 react-native-svg@15.12.1 tailwind-variants@^3.2.2 tailwind-merge@^3.4.0 @gorhom/bottom-sheet@^5
```

> **Important:** It's recommended to use the exact versions specified above to avoid compatibility issues. Version mismatches may cause unexpected bugs.

### 3. Set Up Uniwind

[](#3-set-up-uniwind)

Follow the [Uniwind installation guide](https://docs.uniwind.dev/quickstart) to set up Tailwind CSS for React Native.

If you're migrating from NativeWind, see the [migration guide](https://docs.uniwind.dev/migration-from-nativewind).

### 4. Configure global.css

[](#4-configure-globalcss)

Inside your `global.css` file add the following imports:

```
@import 'tailwindcss';
@import 'uniwind';

@import 'heroui-native/styles';

/* Path to the heroui-native lib inside node_modules from the root of your project */
@source './node_modules/heroui-native/lib';
```

> **Note:** If you need the color scheme from the alpha version of HeroUI Native, you can find it in [example/themes/alpha.css](https://github.com/heroui-inc/heroui-native/blob/beta/example/themes/alpha.css).

#### Running on Web (Expo)

[](#running-on-web-expo)

> **Note:** We are currently focusing on the mobile version. Using HeroUI Native on web is not recommended at this time.

If you're using Expo and want to run your app on web, follow these additional steps:

1. **Install web dependencies:**

```
npx expo install react-dom react-native-web @expo/metro-runtime
```

2. **Update your `app.json`:**

```
{
  "expo": {
    "web": {
      "bundler": "metro"
    }
  }
}
```

### 5. Wrap Your App with Provider

[](#5-wrap-your-app-with-provider)

Wrap your application with `HeroUINativeProvider`. Since HeroUI Native uses `react-native-gesture-handler` under the hood, you must wrap it with `GestureHandlerRootView`:

```
import { HeroUINativeProvider } from 'heroui-native';
import { GestureHandlerRootView } from 'react-native-gesture-handler';

export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <HeroUINativeProvider>{/* Your app content */}</HeroUINativeProvider>
    </GestureHandlerRootView>
  );
}
```

> **Note:** `react-native-gesture-handler` is required because HeroUI Native uses it internally for gesture handling. Make sure to install it if you haven't already: `npm install react-native-gesture-handler`

### 6. Use Your First Component

[](#6-use-your-first-component)

```
import { Button } from 'heroui-native';
import { View } from 'react-native';

export default function MyComponent() {
  return (
    <View className="flex-1 justify-center items-center bg-background">
      <Button onPress={() => console.log('Pressed!')}>Get Started</Button>
    </View>
  );
}
```

## Documentation

[](#documentation)

### Core

[](#core)

* [Provider Configuration](https://github.com/heroui-inc/heroui-native/blob/beta/src/providers/hero-ui-native/provider.md) - Complete setup and configuration guide
* [Theming](https://github.com/heroui-inc/heroui-native/blob/beta/src/styles/theme.md) - Theme customization, colors, fonts and dark mode

### Components

[](#components)

* [Accordion](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/accordion/accordion.md)
* [Avatar](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/avatar/avatar.md)
* [Button](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/button/button.md)
* [Card](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/card/card.md)
* [Checkbox](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/checkbox/checkbox.md)
* [Chip](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/chip/chip.md)
* [Dialog](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/dialog/dialog.md)
* [Divider](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/divider/divider.md)
* [Error View](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/error-view/error-view.md)
* [Form Field](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/form-field/form-field.md)
* [Popover](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/popover/popover.md)
* [Pressable Feedback](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/pressable-feedback/pressable-feedback.md)
* [Radio Group](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/radio-group/radio-group.md)
* [Scroll Shadow](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/scroll-shadow/scroll-shadow.md)
* [Select](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/select/select.md)
* [Skeleton](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/skeleton/skeleton.md)
* [Skeleton Group](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/skeleton-group/skeleton-group.md)
* [Spinner](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/spinner/spinner.md)
* [Surface](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/surface/surface.md)
* [Switch](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/switch/switch.md)
* [Tabs](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/tabs/tabs.md)
* [Text Field](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/text-field/text-field.md)
* [Toast](https://github.com/heroui-inc/heroui-native/blob/beta/src/components/toast/toast.md)

## Changelog

[](#changelog)

See [CHANGELOG.md](https://github.com/heroui-inc/heroui-native/blob/beta/CHANGELOG.md) for a history of changes to this library.

## Roadmap

[](#roadmap)

See [Roadmap](https://herouinative.featurebase.app/roadmap) to see what we're working on.

## Community

[](#community)

We're excited to see the community adopt HeroUI, raise issues, and provide feedback. Whether it's a feature request, bug report, or a project to showcase, please get involved!

* [Discord](https://discord.gg/9b6yyZKmH4)
* [X](https://x.com/hero_ui)
* [GitHub Discussions](https://github.com/heroui-inc/heroui/discussions)

## Contributing

[](#contributing)

Contributions are always welcome! We appreciate your help in making HeroUI Native better.

### How to Contribute

[](#how-to-contribute)

* **Bug Fixes**: Check our [GitHub Issues](https://github.com/heroui-inc/heroui-native/issues) for bugs that need fixing
* **New Components**: Only core team can add new components. Check our [Roadmap](https://herouinative.featurebase.app/roadmap) to see what's planned
* **Feature Proposals**: Start a discussion in [GitHub Discussions](https://github.com/heroui-inc/heroui/discussions) before implementing

**Important:** Please do not add new components or variants, change existing designs, or modify component behavior without prior discussion. We follow a strict design system based on our Figma designs and roadmap.

For detailed guidelines, see [CONTRIBUTING.md](https://github.com/heroui-inc/heroui-native/blob/main/CONTRIBUTING.md).

Please adhere to this project's [CODE\_OF\_CONDUCT](https://github.com/heroui-inc/heroui-native/blob/main/CODE_OF_CONDUCT.md).

## License

[](#license)

[MIT](https://github.com/heroui-inc/heroui-native/blob/beta/LICENSE)


