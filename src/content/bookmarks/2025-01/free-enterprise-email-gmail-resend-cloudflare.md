---
title: "如何使用Gmail、Resend和Cloudflare搭建免费的企业邮箱"
slug: free-enterprise-email-gmail-resend-cloudflare
description: |
  本文详细介绍了使用Gmail、Resend和Cloudflare搭建免费的企业邮箱的方法，支持接收和发送企业域名邮件。通过绑定域名、配置DNS解析及邮件转发功能，实现企业邮箱的全面应用，是初创企业和开发者的理想选择。
tags: 
  - dev
  - tool
  - startup
  - mail
pubDatetime: 2025-01-02T10:13:16+08:00
ogImage: https://javayhu.com/content/images/2024/12/photo-essay-1735661348758.png
---

[原文链接](https://javayhu.com/da-jian-mian-fei-de-qi-ye-you-xiang-gmail-resend-cloudflare/)

---

By [javayhu](https://javayhu.com/author/javayhu/) in [Email](https://javayhu.com/tag/email/) — 01 Jan 2025

本文介绍如何使用Gmail+Resend+Cloudflare搭建免费的企业邮箱，不仅支持接收企业域名邮件，同时支持发送企业域名邮件。

![搭建免费的企业邮箱(Gmail+Resend+Cloudflare)](https://javayhu.com/content/images/size/w1200/2024/12/photo-essay-1735661348758.png)

搭建免费的企业邮箱(Gmail+Resend+Cloudflare)

本文介绍如何使用Gmail+Resend+Cloudflare搭建免费的企业邮箱，不仅支持接收企业域名邮件，同时支持发送企业域名邮件。

[Gmail](https://mail.google.com/?ref=javayhu.com)是Google提供的免费邮件服务；[Resend](https://resend.com/?ref=javayhu.com)是一个为开发者提供邮件服务的平台，专注于提高邮件送达率和开发者体验，它的免费计划每天可以免费发送100封邮件；[Cloudflare](https://www.cloudflare.com/?ref=javayhu.com)是赛博菩萨，提供各种免费服务，其中就包括免费的邮件转发功能。

## 1、在Resend绑定企业域名

我们首先要在Resend绑定企业域名，这样的话我们就可以通过Resend以企业邮箱地址发送邮件了。

### 1.1 添加域名

在Resend的Domains中，点击add domain。

![](https://javayhu.com/content/images/2024/12/image-38.png)

resend add domain

### 1.2 添加DNS解析记录

按照提示，将需要添加的DNS解析记录，添加到Cloudflare的域名DNS解析中。

![](https://javayhu.com/content/images/2024/12/image-40.png)

resend add domain dns records

![](https://javayhu.com/content/images/2024/12/image-42.png)

cloudflare domain dns records

### 1.3 等待验证通过

添加了DNS解析记录之后，回到Resend点击Verify然后等待验证通过。

![](https://javayhu.com/content/images/2024/12/image-41.png)

resend verify dns records success

验证通过之后，你就拥有了 xxx\@domain.com 的企业邮箱了，现在的问题是，用户发给企业邮箱地址的邮件，我们怎么接收呢？

## 2、在Cloudflare上开启邮件转发

接下来要配置的就是让Cloudflare帮我们把企业邮箱收到的邮件转发到我们的Gmail邮箱，这样就解决了收邮件的问题。

### 2.1 开启邮件路由功能

在Cloudflare域名下的Email中的Email Routing中，点击Get started。

![](https://javayhu.com/content/images/2024/12/image-43.png)

cloudflare email routing

### 2.2 设置企业邮箱地址和转发到的目标邮箱

设置你要是用的企业邮箱地址，和将邮件转发到的目标邮箱。

![](https://javayhu.com/content/images/2024/12/image-44.png)

cloudflare custom address

### 2.3 验证目标邮箱地址

这一步要验证你的目标邮箱地址。

![](https://javayhu.com/content/images/2024/12/image-45.png)

cloudflare verify destination address

### 2.4 配置DNS解析

这步提示要配置DNS记录，点击Add records，Cloudflare会自动帮你添加。

![](https://javayhu.com/content/images/2024/12/image-46.png)

cloudflare email add dns records

### 2.5 开启Catch-all的路由规则

这步要开启Catch-all，这样的话所有发给企业域名邮箱的都会发送到目标邮箱。

![](https://javayhu.com/content/images/2024/12/image-47.png)

cloudflare email catch-all address

### 2.6 测试接收邮件

用邮箱地址A给这个企业邮箱地址发邮件，测试目标邮箱地址B能够收到邮件。

💡

如果收件箱中没有收到邮件的话，可以看下垃圾箱中是否有邮件。

![](https://javayhu.com/content/images/2024/12/image-36.png)

gmail send test email

![](https://javayhu.com/content/images/2024/12/image-37.png)

gmail receive email

上面通过Cloudflare的邮件转发功能实现了接收企业邮箱邮件的功能，现在我们想要以这个企业邮箱地址的身份发送邮件怎么办？

## 3、在Gmail中添加企业邮箱账号

接下来我们要在Gmail中添加企业邮箱账号，这样的话，回信时我们就可以选择这个账号而不是私人账号来回信了。

### 3.1 在设置中找到Accounts设置

在Accounts设置中，找到Send mail as，点击add other email address。

![](https://javayhu.com/content/images/2024/12/image-48.png)

gmail accounts settings

### 3.2 添加其他的邮箱地址

填入你的企业邮箱地址，填好之后点击Next Step，会要求我们填写账号信息。

![](https://javayhu.com/content/images/2024/12/image-49.png)

gmail add another email address

### 3.2 在Resend新建API Key

在Resend新建API Key，这个就是你的企业邮箱地址发送邮件的密码，保存下来。

![](https://javayhu.com/content/images/2024/12/image-50.png)

resend add api key

进入Resend的[SMTP](https://resend.com/settings/smtp?ref=javayhu.com)设置，这里就有企业邮箱的发送邮件的账号密码。

![](https://javayhu.com/content/images/2024/12/image-51.png)

resend smtp settings

### 3.3 配置企业邮箱账号的信息

根据上面SMTP的信息，填写企业邮箱账号的信息，注意port和username。

![](https://javayhu.com/content/images/2024/12/image-52.png)

gmail add another email address

### 3.4 确认添加企业邮箱地址

Google会给企业邮箱地址发送邮件，前面我们已经配置了邮件转发，所以邮件会转发到你设置的目标邮箱，你点击链接确认即可。

![](https://javayhu.com/content/images/2024/12/image-54.png)

gmail confirmation

### 3.5 测试企业邮件账号发送邮件

用刚刚添加的企业邮件账号测试发送邮件，如果收到了那么流程就走通了。

![](https://javayhu.com/content/images/2024/12/image-55.png)

gmail send test email

![](https://javayhu.com/content/images/2024/12/image-56.png)

gmail receive test email

至此，你就实现了使用Gmail+Resend+Cloudflare搭建免费的企业邮箱，不仅支持接收企业域名邮件，同时支持发送企业域名邮件。


