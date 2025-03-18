---
title: "GoHomeEasy：基于Cloudflare Workers的Shadowsocks订阅管理工具，专为家庭用户设计"
slug: gohomeeasy-cloudflare-workers-shadowsocks-manager
description: |
  GoHomeEasy是一个基于Cloudflare Workers的Shadowsocks订阅管理工具，专为没有公网IP的家庭宽带用户设计，能够实现远程访问家庭网络。它支持Lucky Webhook自动更新和动态配置，用户可随时访问家中服务器，操作简便。
tags: 
  - AI
  - cloudflare
  - tool
  - shadowsocks
  - remote
pubDatetime: 2025-03-18T10:08:54+08:00
ogImage: https://opengraph.githubassets.com/08ca88075efa0507cf7a09f92a661fd6133391843dd9dfbc21932bb24f2cc438/kanshurichard/GoHomeEasy
---

[原文链接](https://github.com/kanshurichard/GoHomeEasy)

---

# 🚀 GoHomeEasy

[](#-gohomeeasy)

## English | [中文](https://github.com/kanshurichard/GoHomeEasy/blob/main/README_CN.md)

[](#english--中文)

**GoHomeEasy** is a Shadowsocks subscription management tool based on Cloudflare Workers, designed specifically for **home broadband users without a public IP** to access their home network remotely.

It leverages **Lucky's NAT traversal** and automatic subscription updates, allowing users to **access their home Shadowsocks server from anywhere** without frequently changing dynamic IP addresses and ports manually.

***

## 🌟 **Features**

[](#-features)

✅ **Ideal for home broadband users without a public IP to access their home LAN remotely**\
✅ **Supports Lucky Webhook for automatic Shadowsocks subscription updates**\
✅ **Supports dynamic configuration of Shadowsocks `method` (encryption method) and `password`**\
✅ **Based on Cloudflare Workers + KV, no need for a self-hosted server**\
✅ **API Key authentication ensures data security**\
✅ **Supports Cloudflare custom domain access to bypass `workers.dev` restrictions in Mainland China**

***

## ⚙️ **Prerequisites**

[](#️-prerequisites)

To successfully deploy **GoHomeEasy**, prepare the following:

🔹 **Linux home server or OpenWRT router**\
🔹 **Shadowsocks server setup** (Recommended: [PassWall2 plugin](https://github.com/xiaorouji/openwrt-passwall2) for OpenWRT)\
🔹 **Install [Lucky NAT Traversal](https://lucky666.cn)** and map the Shadowsocks server port to the public network\
🔹 **Cloudflare account** (free account is sufficient for Workers deployment)\
🔹 **Domain managed by Cloudflare DNS** (optional, for bypassing `workers.dev` restrictions in China)\
🔹 **Shadowsocks-compatible client for mobile/PC** (e.g., Shadowrocket on iOS)

***

## 💻 **Shadowsocks Server Configuration**

[](#-shadowsocks-server-configuration)

Using PassWall2 as an example:

1. Navigate to the "Server" tab in PassWall2 and click "Add"

2. Configure as follows:

   * Enable: ✅ Checked
   * Name: Custom
   * Type: Sing-Box
   * Protocol: Shadowsocks
   * Listening Port: 8000 (or custom)
   * Password: Custom
   * Encryption: Recommended `chacha20-ietf-poly1305`
   * Allow LAN Access: ✅ Checked
   * Keep other settings default

3. Click **Save & Apply**, return to the main menu

4. Check "Enable" and click **Save & Apply**

***

## 🛠 **Cloudflare Workers Configuration**

[](#-cloudflare-workers-configuration)

### 1️⃣ **Create a Workers Service**

[](#1️⃣-create-a-workers-service)

1. Log in to **[Cloudflare Dashboard](https://dash.cloudflare.com/)**
2. Go to **Workers & Pages**, click **Create**
3. Select **"Start from template" → "Hello world"**
4. Enter **Service Name** (e.g., `GoHomeEasy`), click **Deploy**

### 2️⃣ **Edit Workers Code**

[](#2️⃣-edit-workers-code)

1. Open the newly created Worker, click **"< / >"** to edit the code
2. Delete the default code
3. Paste **`GoHomeEasy.js` code** from this repository
4. Modify `"your_secure_api_key"` in the source code and keep it safe
5. Click **Deploy**

### 3️⃣ **Bind Cloudflare KV Storage**

[](#3️⃣-bind-cloudflare-kv-storage)

1. Navigate to **Objects & Storage → KV**

2. Click **+ Create**, name it `GoHomeEasy_KV`

3. Go to your **Worker** → **Settings**

4. Click **Bindings → + Add KV Namespace**

   * **Variable Name**: `KV_NAMESPACE`
   * **KV Namespace**: Select `GoHomeEasy_KV`

5. Click **Deploy**

***

## 🌍 **Use Cloudflare Custom Domain (Optional, only recommend for Mainland China Users)**

[](#-use-cloudflare-custom-domain-optional-only-recommend-for-mainland-china-users)

Follow these steps: [EdgeTunnel Issue #27](https://github.com/zizifn/edgetunnel/issues/27)

***

## 🔗 **Configure Lucky Webhook**

[](#-configure-lucky-webhook)

In **Lucky Webhook Settings**, enter the following:

### 1️⃣ **Webhook URL (POST Request)**

[](#1️⃣-webhook-url-post-request)

* **Cloudflare Workers Native Domain**:

  ```
  https://your-worker-name.workers.dev/
  ```

* **Cloudflare Custom Domain**:

  ```
  https://gohome.yourdomain.com/
  ```

### 2️⃣ **Request Headers**

[](#2️⃣-request-headers)

```
  Content-Type: application/json
  Authorization: Bearer your_secure_api_key
```

### 3️⃣ **Request Body**

[](#3️⃣-request-body)

```
{
  "ip": "#{ip}",
  "port": "#{port}",
  "method": "chacha20-ietf-poly1305",
  "password": "your_password"
}
```

***

## 📥 **Client Subscription Configuration**

[](#-client-subscription-configuration)

Using Shadowrocket 🚀 as an example:

### 1️⃣ **Add Subscription URL**

[](#1️⃣-add-subscription-url)

1. Open **Shadowrocket**, tap `+`, select "Subscription"

2. Enter **Subscription URL**:

   * **Cloudflare Workers Native Domain**:

     ```
     https://your-worker-name.workers.dev/?api_key=your_secure_api_key
     ```

   * **Cloudflare Custom Domain**:

     ```
     https://gohome.yourdomain.com/?api_key=your_secure_api_key
     ```

3. Tap **Save**, subscription updates automatically ✅

***

### 2️⃣ **Modify Shadowrocket Rules**

[](#2️⃣-modify-shadowrocket-rules)

1. Go to **Settings → Rules**

2. Add a rule:

   * **Type**: `IP-CIDR`
   * **IP CIDR**: `192.168.1.0/24` (or your home LAN segment)
   * **Policy**: `GoHomeEasy` proxy node

3. Save and restart VPN ✅

***

🚀 **GoHomeEasy - Access your home LAN from anywhere, even without a public IP!** 🌎

***


