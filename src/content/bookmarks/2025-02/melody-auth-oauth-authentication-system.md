---
title: "Melody Auth：一款针对Cloudflare Workers与Node.js的即开即用OAuth与认证系统"
slug: melody-auth-oauth-authentication-system
description: |
  Melody Auth是一款即开即用的OAuth与认证系统，可在Cloudflare的基础设施上无缝部署，支持Workers、D1和KV，或自托管于Node.js、Redis和PostgreSQL。该系统提供简单易用的解决方案，最小化配置，帮助用户快速建立自己的认证环境。
tags: 
  - OAuth
  - authentication
  - Cloudflare
  - dev
pubDatetime: 2025-02-06T09:59:36+08:00
ogImage: https://opengraph.githubassets.com/14b6ff882ff38008c88411cb5a03fd9c8dd05c3c265a2bac094e8d9fbae40f89/ValueMelody/melody-auth
---

[原文链接](https://github.com/ValueMelody/melody-auth?tab=readme-ov-file)

---

# Melody Auth

[](#melody-auth)

**Melody Auth** is turnkey OAuth & authentication system that can be seamlessly deployed on Cloudflare’s infrastructure, utilizing Workers, D1, and KV, or self-hosted with Node.js, Redis, and PostgreSQL. It provides a robust and user-friendly solution for implementing and hosting your own oauth and authentication system with minimal configuration required.

## Why Melody Auth?

[](#why-melody-auth)

### 1. Self-Controlled

[](#1-self-controlled)

[Server Setup (Cloudflare)](https://auth.valuemelody.com/auth-server.html#environment-setup-cloudflare)\
[Server Setup (Node)](https://auth.valuemelody.com/auth-server.html#environment-setup-node)\
[Mailer Setup](https://auth.valuemelody.com/auth-server.html#mailer-setup)\
[SMS Setup](https://auth.valuemelody.com/auth-server.html#sms-setup)\
[Configurations](https://auth.valuemelody.com/auth-server.html#additional-configs)

* Deploy the entire system within minutes, either using Cloudflare’s infrastructure or self-hosted with Node.js, Redis, and PostgreSQL.
* Minimize DevOps overhead by leveraging Cloudflare, or maintain full control with a self-hosted solution.
* Full access to the source code for customization and scalability.

### 2. Admin Panel

[](#2-admin-panel)

[Admin Panel Setup](https://auth.valuemelody.com/admin-panel.html)

* Web interface for managing apps, users, scopes, and roles
* Serves as a simple implementation example using the React SDK and Server-to-Server REST API

### 3. Server-to-Server REST API

[](#3-server-to-server-rest-api)

[REST API Swagger](https://auth-server.valuemelody.com/api/v1/swagger)

* Secure communication channel for backend services using client credentials token exchange flow
* Provides functionalities for managing apps, users, scopes, and roles with scope protection

### 4. React SDK

[](#4-react-sdk)

[React SDK Guidance](https://auth.valuemelody.com/react-sdk.html)

* Enables smooth integration between React applications and the authentication server
* Implements Proof Key for Code Exchange (PKCE) for enhanced security

## Features Supported

[](#features-supported)

* **OAuth 2.0**:

  * Authorize
  * Token Exchange
  * Refresh Token Revoke
  * App Consent
  * App Scopes
  * User Info Retrieval
  * openid-configuration

* **Authorization**:

  * Sign-In
  * Sign-Up
  * Sign-Out
  * Email Verification
  * Password Reset
  * Role-Based Access Control (RBAC)
  * Account Linking
  * Localization [How to support a new locale](https://auth.valuemelody.com/q_a.html#how-to-support-a-new-locale)

* **Social Sign-In**:

  * Google Sign-In
  * Facebook Sign-In
  * GitHub Sign-In

* **Multi-Factor Authentication** [How to setup MFA](https://auth.valuemelody.com/q_a.html#how-to-setup-mfa):

  * Email MFA
  * OTP MFA
  * SMS MFA
  * MFA Enrollment

* **Policy** [How to trigger a different policy](https://auth.valuemelody.com/q_a.html#how-to-trigger-a-different-policy)

  * sign\_in\_or\_sign\_up
  * change\_password
  * change\_email
  * reset\_mfa

* **Mailer Option**:

  * SendGrid
  * Mailgun
  * Brevo
  * STMP (Node.js environment only)

* **SMS Option**:
  * Twilio

* **JWT Authentication**:

  * RSA256 based JWT Authentication [How to verify a SPA access token](https://auth.valuemelody.com/q_a.html#how-to-verify-a-spa-access-token)
  * JWT Secret Rotate [How to rotate JWT secret](https://auth.valuemelody.com/q_a.html#how-to-rotate-jwt-secret)

* **Brute-force Protection**:

  * Log in attempts
  * Password reset attempts
  * OTP MFA attempts
  * SMS MFA attempts
  * Email MFA attempts
  * Change Email attempts

* **Organization**:
  * Branding config override

* **Logging**:

  * Email Logs
  * SMS Logs
  * Sign-in Logs

* **S2S REST API & Admin Panel**:

  * Manage Users
  * Manage Apps
  * Manage Scopes
  * Manage Roles
  * View Logs
  * Localization

### Screenshots

[](#screenshots)

[Authorization Screenshots](https://auth.valuemelody.com/screenshots.html#identity-pages-and-emails)\
[Admin Panel Screenshots](https://auth.valuemelody.com/screenshots.html#admin-panel-pages)

## License

[](#license)

This project is licensed under the MIT License. See the LICENSE file for details.


