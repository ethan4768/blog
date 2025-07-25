---
title: "Frappe HR: 现代开源人力资源与薪资管理软件"
slug: frappe-open-source-hr-payroll-software
description: |
  Frappe HR 是一款现代化的开源人力资源和薪资管理软件，提供超过13个不同模块，涵盖员工管理、入职、请假、薪资和税务等功能。通过便捷的移动应用，随时随地轻松管理人力资源，提升企业效率。
tags: 
  - AI
  - opensource
  - HR
  - tool
  - productivity
pubDatetime: 2025-07-25T21:39:26+08:00
ogImage: https://repository-images.githubusercontent.com/501292795/010f358b-8afb-4e41-a7c8-8444983055c8
---

[原文链接](https://github.com/frappe/hrms)

---

[![Frappe HR Logo](/frappe/hrms/raw/develop/.github/frappe-hr-logo.png)](https://frappe.io/hr)

## Frappe HR

[](#frappe-hr)

Open Source, modern, and easy-to-use HR and Payroll Software

[![CI](https://github.com/frappe/hrms/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/frappe/hrms/actions/workflows/ci.yml) [![codecov](https://camo.githubusercontent.com/2f3806753e87f599c69e9f3ed9e3d3aefb58953cc473844c7c2409c8ef62c0c7/68747470733a2f2f636f6465636f762e696f2f67682f6672617070652f68726d732f6272616e63682f646576656c6f702f67726170682f62616467652e7376673f746f6b656e3d30547776795567334935)](https://codecov.io/gh/frappe/hrms)

[![](/frappe/hrms/raw/develop/.github/hrms-hero.png)](https://github.com/frappe/hrms/blob/develop/.github/hrms-hero.png)

[Website](https://frappe.io/hr) - [Documentation](https://docs.frappe.io/hr/introduction)

## Frappe HR

[](#frappe-hr-1)

Frappe HR has everything you need to drive excellence within the company. It's a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!

## Motivation

[](#motivation)

When Frappe team started growing in terms of size, we needed an open-source HR and Payroll software. We didn't find any "true" open-source HR software out there and so decided to build one ourselves. Initially, it was a set of modules within ERPNext but version 14 onwards, as the modules became more mature, Frappe HR was created as a separate product.

## Key Features

[](#key-features)

* **Employee Lifecycle**: From onboarding employees, managing promotions and transfers, all the way to documenting feedback with exit interviews, make life easier for employees throughout their life cycle.
* **Leave and Attendance**: Configure leave policies, pull regional holidays with a click, check-in and check-out with geolocation capturing, track leave balances and attendance with reports.
* **Expense Claims and Advances**: Manage employee advances, claim expenses, configure multi-level approval workflows, all this with seamless integration with ERPNext accounting.
* **Performance Management**: Track goals, align goals with key result areas (KRAs), enable employees to evaluate themselves, make managing appraisal cycles easy.
* **Payroll & Taxation**: Create salary structures, configure income tax slabs, run standard payroll, accomodate additional salaries and off cycle payments, view income breakup on salary slips and so much more.
* **Frappe HR Mobile App**: Apply for and approve leaves on the go, check-in and check-out, access employee profile right from the mobile app.

View Screenshots

[![](/frappe/hrms/raw/develop/.github/hrms-appraisal.png)](https://github.com/frappe/hrms/blob/develop/.github/hrms-appraisal.png) [![](/frappe/hrms/raw/develop/.github/hrms-requisition.png)](https://github.com/frappe/hrms/blob/develop/.github/hrms-requisition.png) [![](/frappe/hrms/raw/develop/.github/hrms-attendance.png)](https://github.com/frappe/hrms/blob/develop/.github/hrms-attendance.png) [![](/frappe/hrms/raw/develop/.github/hrms-salary.png)](https://github.com/frappe/hrms/blob/develop/.github/hrms-salary.png) [![](/frappe/hrms/raw/develop/.github/hrms-pwa.png)](https://github.com/frappe/hrms/blob/develop/.github/hrms-pwa.png)

### Under the Hood

[](#under-the-hood)

* [**Frappe Framework**](https://github.com/frappe/frappe): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

* [**Frappe UI**](https://github.com/frappe/frappe-ui): A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

## Production Setup

[](#production-setup)

### Managed Hosting

[](#managed-hosting)

You can try [Frappe Cloud](https://frappecloud.com), a simple, user-friendly and sophisticated [open-source](https://github.com/frappe/press) platform to host Frappe applications with peace of mind.

It takes care of installation, setup, upgrades, monitoring, maintenance and support of your Frappe deployments. It is a fully featured developer platform with an ability to manage and control multiple Frappe deployments.

[![Try on Frappe Cloud](https://camo.githubusercontent.com/3504853621567c7e6baa18ee00e7d3ec0431742b5f493d19dc5cec16e2cbe8bc/68747470733a2f2f6672617070652e696f2f66696c65732f7472792d6f6e2d66632d626c61636b2e706e67)](https://frappecloud.com/hrms/signup)

## Development setup

[](#development-setup)

### Docker

[](#docker)

You need Docker, docker-compose and git setup on your machine. Refer [Docker documentation](https://docs.docker.com/). After that, run the following commands:

```
git clone https://github.com/frappe/hrms
cd hrms/docker
docker-compose up
```

Wait for some time until the setup script creates a site. After that you can access `http://localhost:8000` in your browser and the login screen for HR should show up.

Use the following credentials to log in:

* Username: `Administrator`
* Password: `admin`

### Local

[](#local)

1. Set up bench by following the [Installation Steps](https://frappeframework.com/docs/user/en/installation) and start the server and keep it running

   ```
   $ bench start
   ```

2. In a separate terminal window, run the following commands

   ```
   $ bench new-site hrms.local
   $ bench get-app erpnext
   $ bench get-app hrms
   $ bench --site hrms.local install-app hrms
   $ bench --site hrms.local add-to-hosts
   ```

3. You can access the site at `http://hrms.local:8080`

## Learning and Community

[](#learning-and-community)

1. [Frappe School](https://frappe.school) - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. [Documentation](https://docs.frappe.io/hr) - Extensive documentation for Frappe HR.
3. [User Forum](https://discuss.erpnext.com/) - Engage with the community of ERPNext users and service providers.
4. [Telegram Group](https://t.me/frappehr) - Get instant help from the community of users.

## Contributing

[](#contributing)

1. [Issue Guidelines](https://github.com/frappe/erpnext/wiki/Issue-Guidelines)
2. [Report Security Vulnerabilities](https://erpnext.com/security)
3. [Pull Request Requirements](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines)

## Logo and Trademark Policy

[](#logo-and-trademark-policy)

Please read our [Logo and Trademark Policy](https://github.com/frappe/hrms/blob/develop/TRADEMARK_POLICY.md).

\
\


[![Frappe Technologies](https://camo.githubusercontent.com/bfd1a7022e304544a19fa29e8f21213dc31ad3b146dd474d59470c7feef36a5d/68747470733a2f2f6672617070652e696f2f66696c65732f4672617070652d626c61636b2e706e67)](https://frappe.io)


