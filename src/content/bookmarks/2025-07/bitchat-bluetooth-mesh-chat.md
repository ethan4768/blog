---
title: "bitchat: 基于蓝牙网状网络的安全去中心化聊天应用"
slug: bitchat-bluetooth-mesh-chat
description: |
  bitchat是一个安全且去中心化的对等消息应用，通过蓝牙网状网络进行通信。无需互联网和服务器，仅依赖加密的通讯方式。它支持频道聊天、端到端加密，并提供隐私优先的特性，确保用户的安全与隐私不受侵犯。
tags: 
  - opensource
  - tool
pubDatetime: 2025-07-09T16:52:01+08:00
ogImage: https://opengraph.githubassets.com/c6b6738023b2739825df241a4919fba3e32dece85c86e7c285569d891de6f626/jackjackbits/bitchat
---

[原文链接](https://github.com/jackjackbits/bitchat)

---

[![ChatGPT Image Jul 5, 2025 at 06\_07\_31 PM](https://private-user-images.githubusercontent.com/212554440/462800094-2660f828-49c7-444d-beca-d8b01854667a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTIwNTEzNzksIm5iZiI6MTc1MjA1MTA3OSwicGF0aCI6Ii8yMTI1NTQ0NDAvNDYyODAwMDk0LTI2NjBmODI4LTQ5YzctNDQ0ZC1iZWNhLWQ4YjAxODU0NjY3YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwOVQwODUxMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xODQyMGVjNzcxNWMwZjA4OTRlMmI1OWY5ZTVmZmI5ZWIxNDkyYTRiMjE0NGQxMzQ0NmU2YzU0NWNmOTViZDFhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.SUUqUpLURPfDb9FSFm17KKHVIdNRpBrjNXzdHirF5Uk)](https://private-user-images.githubusercontent.com/212554440/462800094-2660f828-49c7-444d-beca-d8b01854667a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTIwNTEzNzksIm5iZiI6MTc1MjA1MTA3OSwicGF0aCI6Ii8yMTI1NTQ0NDAvNDYyODAwMDk0LTI2NjBmODI4LTQ5YzctNDQ0ZC1iZWNhLWQ4YjAxODU0NjY3YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwOVQwODUxMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xODQyMGVjNzcxNWMwZjA4OTRlMmI1OWY5ZTVmZmI5ZWIxNDkyYTRiMjE0NGQxMzQ0NmU2YzU0NWNmOTViZDFhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.SUUqUpLURPfDb9FSFm17KKHVIdNRpBrjNXzdHirF5Uk)

# bitchat

[](#bitchat)

A secure, decentralized, peer-to-peer messaging app that works over Bluetooth mesh networks. No internet required, no servers, no phone numbers - just pure encrypted communication.

## License

[](#license)

This project is released into the public domain. See the [LICENSE](https://github.com/jackjackbits/bitchat/blob/main/LICENSE) file for details.

## Features

[](#features)

* **Decentralized Mesh Network**: Automatic peer discovery and multi-hop message relay over Bluetooth LE
* **End-to-End Encryption**: X25519 key exchange + AES-256-GCM for private messages
* **Channel-Based Chats**: Topic-based group messaging with optional password protection
* **Store & Forward**: Messages cached for offline peers and delivered when they reconnect
* **Privacy First**: No accounts, no phone numbers, no persistent identifiers
* **IRC-Style Commands**: Familiar `/join`, `/msg`, `/who` style interface
* **Message Retention**: Optional channel-wide message saving controlled by channel owners
* **Universal App**: Native support for iOS and macOS
* **Cover Traffic**: Timing obfuscation and dummy messages for enhanced privacy
* **Emergency Wipe**: Triple-tap to instantly clear all data
* **Performance Optimizations**: LZ4 message compression, adaptive battery modes, and optimized networking

## Setup

[](#setup)

### Option 1: Using XcodeGen (Recommended)

[](#option-1-using-xcodegen-recommended)

1. Install XcodeGen if you haven't already:

   ```
   brew install xcodegen
   ```

2. Generate the Xcode project:

   ```
   cd bitchat
   xcodegen generate
   ```

3. Open the generated project:

   ```
   open bitchat.xcodeproj
   ```

### Option 2: Using Swift Package Manager

[](#option-2-using-swift-package-manager)

1. Open the project in Xcode:

   ```
   cd bitchat
   open Package.swift
   ```

2. Select your target device and run

### Option 3: Manual Xcode Project

[](#option-3-manual-xcode-project)

1. Open Xcode and create a new iOS/macOS App
2. Copy all Swift files from the `bitchat` directory into your project
3. Update Info.plist with Bluetooth permissions
4. Set deployment target to iOS 16.0 / macOS 13.0

## Usage

[](#usage)

### Basic Commands

[](#basic-commands)

* `/j #channel` - Join or create a channel
* `/m @name message` - Send a private message
* `/w` - List online users
* `/channels` - Show all discovered channels
* `/block @name` - Block a peer from messaging you
* `/block` - List all blocked peers
* `/unblock @name` - Unblock a peer
* `/clear` - Clear chat messages
* `/pass [password]` - Set/change channel password (owner only)
* `/transfer @name` - Transfer channel ownership
* `/save` - Toggle message retention for channel (owner only)

### Getting Started

[](#getting-started)

1. Launch bitchat on your device
2. Set your nickname (or use the auto-generated one)
3. You'll automatically connect to nearby peers
4. Join a channel with `/j #general` or start chatting in public
5. Messages relay through the mesh network to reach distant peers

### Channel Features

[](#channel-features)

* **Password Protection**: Channel owners can set passwords with `/pass`
* **Message Retention**: Owners can enable mandatory message saving with `/save`
* **@ Mentions**: Use `@nickname` to mention users (with autocomplete)
* **Ownership Transfer**: Pass control to trusted users with `/transfer`

## Security & Privacy

[](#security--privacy)

### Encryption

[](#encryption)

* **Private Messages**: X25519 key exchange + AES-256-GCM encryption
* **Channel Messages**: Argon2id password derivation + AES-256-GCM
* **Digital Signatures**: Ed25519 for message authenticity
* **Forward Secrecy**: New key pairs generated each session

### Privacy Features

[](#privacy-features)

* **No Registration**: No accounts, emails, or phone numbers required
* **Ephemeral by Default**: Messages exist only in device memory
* **Cover Traffic**: Random delays and dummy messages prevent traffic analysis
* **Emergency Wipe**: Triple-tap logo to instantly clear all data
* **Local-First**: Works completely offline, no servers involved

## Performance & Efficiency

[](#performance--efficiency)

### Message Compression

[](#message-compression)

* **LZ4 Compression**: Automatic compression for messages >100 bytes
* **30-70% bandwidth savings** on typical text messages
* **Smart compression**: Skips already-compressed data

### Battery Optimization

[](#battery-optimization)

* **Adaptive Power Modes**: Automatically adjusts based on battery level

  * Performance mode: Full features when charging or >60% battery
  * Balanced mode: Default operation (30-60% battery)
  * Power saver: Reduced scanning when <30% battery
  * Ultra-low power: Emergency mode when <10% battery

* **Background efficiency**: Automatic power saving when app backgrounded

* **Configurable scanning**: Duty cycle adapts to battery state

### Network Efficiency

[](#network-efficiency)

* **Optimized Bloom filters**: Faster duplicate detection with less memory
* **Message aggregation**: Batches small messages to reduce transmissions
* **Adaptive connection limits**: Adjusts peer connections based on power mode

## Technical Architecture

[](#technical-architecture)

### Binary Protocol

[](#binary-protocol)

bitchat uses an efficient binary protocol optimized for Bluetooth LE:

* Compact packet format with 1-byte type field
* TTL-based message routing (max 7 hops)
* Automatic fragmentation for large messages
* Message deduplication via unique IDs

### Mesh Networking

[](#mesh-networking)

* Each device acts as both client and peripheral
* Automatic peer discovery and connection management
* Store-and-forward for offline message delivery
* Adaptive duty cycling for battery optimization

For detailed protocol documentation, see the [Technical Whitepaper](https://github.com/jackjackbits/bitchat/blob/main/WHITEPAPER.md).

## Building for Production

[](#building-for-production)

1. Set your development team in project settings
2. Configure code signing
3. Archive and distribute through App Store or TestFlight

## Android Compatibility

[](#android-compatibility)

The protocol is designed to be platform-agnostic. An Android client can be built using:

* Bluetooth LE APIs
* Same packet structure and encryption
* Compatible service/characteristic UUIDs


