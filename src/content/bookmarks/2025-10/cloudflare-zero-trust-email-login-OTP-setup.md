---
title: "Cloudflare Zero Trust访问的邮箱一次性密码登录设置指南"
slug: cloudflare-zero-trust-email-login-OTP-setup
description: |
  本文详细介绍了如何为Cloudflare Zero Trust (Access) 配置邮箱一次性密码（OTP）登录验证。这种方式通过邮箱发送验证码，简化了用户登录，提高了安全性。你的应用将享有灵活的访问控制，确保只有特定用户可以登录。
tags: 
  - Cloudflare
  - ZeroTrust
  - tool
pubDatetime: 2025-10-22T20:20:20+08:00
ogImage: 
---

[原文链接](https://blog.galois21.com/archives/2360)

---

<!-- .entry-meta -->

1. [核心优势](#toc-0)
2. [第一步：启用 “一次性密码 (One-Time PIN)” 登录方法](#toc-1)
3. [第二步：添加并配置需要保护的应用程序](#toc-2)
4. [第三步：创建访问策略 (Access Policy)](#toc-3)
5. [用户登录体验](#toc-4)

由于Cloudflare 隧道的域名对外可以访问（参考之前的 [如何把局域网电脑里的 AI 模型的 api暴露到外网？——Cloudflare Tunnel](https://blog.galois21.com/archives/2285 "参考之前的 如何把局域网电脑里的 AI 模型的 api暴露到外网？——Cloudflare Tunnel：") ），如果网站本身没有用户管理系统的话，网址泄露会被其他人访问到。而如果你恰好不希望被访问，只是企业内部人员使用，使用Cloudflare Zero Trust 的邮箱验证是比较好的办法。

您可以按照以下步骤，为您的应用程序配置 Cloudflare Zero Trust (Access) 的邮箱一次性密码（One-Time PIN, OTP）登录验证。这种方式无需集成复杂的身份提供商（IdP），仅通过向用户邮箱发送验证码即可实现安全访问。

注意：Cloudflare可选英文语言，更好跟随操作

### 核心优势

* **简化登录:** 用户无需记住额外的密码，只需通过邮箱接收验证码即可登录。
* **提升安全:** 为您的应用程序增加了一层关键的身份验证，有效防止未经授权的访问。
* **灵活性高:** 可以精确控制允许哪些邮箱或邮箱域的用户访问特定应用。

设置步骤：整个配置过程主要分为三个部分：**启用登录方法** -> **配置应用程序** -> **创建访问策略**。

***

### 第一步：启用 “一次性密码 (One-Time PIN)” 登录方法

首先，您需要在 Cloudflare Zero Trust 的全局设置中启用邮箱一次性密码的登录选项。

1. 登录到您的 [Cloudflare Zero Trust 仪表板](https://blog.galois21.com/privacy/Jump_ExternalUrl.php?url=https://one.dash.cloudflare.com/)。
2. 在左侧导航栏中，找到并点击 **Settings** > **Authentication**。
3. 在 **Login methods** 卡片中，点击 **Add new**。
4. 从列表中选择 **One-time PIN**。
5. 点击 **Save**。至此，您的账户已开启邮箱验证码登录功能。通常情况下，无需进行额外配置。

***

### 第二步：添加并配置需要保护的应用程序

接下来，您需要指定要使用此登录方式保护的具体应用程序。您可以添加一个新的自托管应用，也可以为现有应用进行配置。

1. 在 Zero Trust 仪表板的左侧导航栏中，转到 **Access** > **Applications**。

2. 点击 **Add an application**。

3. 选择您要保护的应用类型。对于网站或 Web 服务，最常见的选项是 **Self-hosted**。

4. 进入应用配置页面，填写以下信息：

   * **Application name:** 为您的应用设置一个易于识别的名称。

   * **Session Duration:** 设置用户登录会话的有效时间，例如 `24 hours`。

   * **Application domain:** 这是最关键的一步。输入您要保护的网站的完整域名或子域名（例如 `service.yourdomain.com`）。该域名必须已经在您的 Cloudflare 账户下进行管理。\


     > 注意：Cloudflare免费版只支持二级子域名，不要abc.service.yourdomain.com这种，可以改成abc-service.yourdomain.com

   * **Login methods（可选）**

     * 取消勾选 “Accept all available identity providers” (如已勾选)。开启标识多个可用身份验证都可以支持登录。
     * 在下方的列表中，确保 **One-time PIN** 是**唯一**被选中的选项（如果您只想使用邮箱验证登录）。

5. 完成上述配置后，点击 **Next** 进入策略配置页面。

***

### 第三步：创建访问策略 (Access Policy)

访问策略定义了“谁”可以访问这个应用程序。Cloudflare Access 默认拒绝所有访问，因此您必须创建一个“允许 (Allow)”策略。

1. 在应用程序配置的第二步“Policies”中，点击 **Add a policy**。

2. 为您的策略命名，例如“允许特定邮箱访问”。

3. 配置策略规则 (Configure rules)：

   * **Action:** 选择 **Allow**。

   * **Rule type (Selector):** 这是定义访问条件的核心。对于邮箱验证，您可以选择以下几种：

     * **Emails:** 输入一个或多个具体的邮箱地址，只有这些邮箱才能收到验证码并登录。
     * **Emails ending in:** 输入一个或多个邮箱域名（例如 `yourcompany.com`），所有使用该域名后缀的邮箱都将可以登录。
     * **Everyone:** 允许任何人尝试通过输入他们的邮箱来获取验证码。这适用于您希望向公众开放但仍需验证身份的场景。

   * **Value:** 根据您选择的 Selector 输入对应的值。

   **示例：只允许特定邮箱登录**

   * **Selector:** `Emails`
   * **Value:** `admin@yourdomain.com`

   **示例：只允许公司员工邮箱登录**

   * **Selector:** `Emails ending in`
   * **Value:** `yourcompany.com`

4. 您可以根据需要添加更多的规则，例如限制特定国家/地区的访问 (Geo) 或要求用户通过 WARP 客户端连接 (Require WARP)。

5. 完成规则配置后，点击 **Next**。

6. 在最后的 "Setup" 页面，您可以保持默认设置，然后点击 **Add application** 完成所有配置。

### 用户登录体验

配置完成后，当用户尝试访问您指定的应用域名（例如 `service.yourdomain.com`）时，他们将被重定向到一个 Cloudflare Access 的登录页面。

1. 用户需要输入他们的电子邮件地址。
2. 如果该邮箱地址符合您在策略中设置的规则，Cloudflare 会向该邮箱发送一封包含一次性密码（通常是6位数字）的邮件。
3. 用户在登录页面输入收到的验证码。
4. 验证通过后，用户将被允许访问受保护的应用程序。

通过以上步骤，您就可以成功地为您的应用设置一个简单而有效的邮箱登录验证系统，从而在不增加用户密码负担的情况下，显著提升应用程序的安全性。

<!-- .entry-content -->

浏览量(**929**) | 此条目发表在[计算机](https://blog.galois21.com/archives/category/computer)分类目录，贴了[Cloudflare](https://blog.galois21.com/archives/tag/cloudflare), [Zero Trust](https://blog.galois21.com/archives/tag/zero-trust)标签。将[固定链接](https://blog.galois21.com/archives/2360 "链向Cloudflare Zero Trust（Access）的邮箱登录验证的设置方法的固定链接")加入收藏夹。

<!-- .entry-utility -->


