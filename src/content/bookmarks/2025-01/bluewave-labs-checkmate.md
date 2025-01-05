---
title: "Checkmate: 一款开源自托管的服务器监控工具，实时跟踪服务器硬件状态"
slug: bluewave-labs-checkmate
description: |
  Checkmate 是一款开源自托管工具，旨在实时跟踪和监控服务器硬件、正常运行时间、响应时间和事件，并提供美观的可视化界面。它支持网站和基础设施监控，能够即时发出警报，确保您获得最佳的系统性能。
tags: 
  - opensource
  - dev
  - tool
  - monitor
pubDatetime: 2025-01-05T19:33:53+08:00
ogImage: https://repository-images.githubusercontent.com/793866369/d0a1ab96-c391-42a8-ae35-3fa3943ee8ba
---

[原文链接](https://github.com/bluewave-labs/checkmate)

---

# **We're opening our $5000 grant funding announcement soon, powered by Checkmate and [UpRock](https://uprock.com) - check [our web page](https://checkmate.so) for preliminary details.**

[](#were-opening-our-5000-grant-funding-announcement-soon-powered-by-checkmate-and-uprock---check-our-web-page-for-preliminary-details)

**If you would like to support us, please consider giving it a ⭐, and think about contributing or providing feedback. Need support or have a suggestion? Check our [Discord channel](https://discord.gg/NAb6H3UTjK) or [Discussions](https://github.com/bluewave-labs/checkmate/discussions) forum.**

[![Frame 34](https://private-user-images.githubusercontent.com/167266851/399539762-d491a734-fd7a-4841-9f84-fb5bef5ad586.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk5NTM5NzYyLWQ0OTFhNzM0LWZkN2EtNDg0MS05Zjg0LWZiNWJlZjVhZDU4Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00MmI0MzNmZGNiZDczOGJmMTE5MmM1ODlhNWFlODUzYzU5NzAzMThjZGJiODU0NmJlMDVhMzQ5ZmU5YzA2NTZlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.jyaATLB2IWjLrDyFz9vuy829xV01voO7MPsPTiGukKQ)](https://private-user-images.githubusercontent.com/167266851/399539762-d491a734-fd7a-4841-9f84-fb5bef5ad586.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk5NTM5NzYyLWQ0OTFhNzM0LWZkN2EtNDg0MS05Zjg0LWZiNWJlZjVhZDU4Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00MmI0MzNmZGNiZDczOGJmMTE5MmM1ODlhNWFlODUzYzU5NzAzMThjZGJiODU0NmJlMDVhMzQ5ZmU5YzA2NTZlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.jyaATLB2IWjLrDyFz9vuy829xV01voO7MPsPTiGukKQ)

[![](https://camo.githubusercontent.com/0ef5777550ca627a6b6d0da193f9bc9a0879f3d992ab6e2454336388f4cc8859/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/0ef5777550ca627a6b6d0da193f9bc9a0879f3d992ab6e2454336388f4cc8859/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f626c7565776176652d6c6162732f636865636b6d617465) [![](https://camo.githubusercontent.com/e66402c86839f24d013e05ebaa1707c00c2cd56253a191e1618e543288b263ed/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/e66402c86839f24d013e05ebaa1707c00c2cd56253a191e1618e543288b263ed/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f626c7565776176652d6c6162732f636865636b6d617465) [![](https://camo.githubusercontent.com/c662d7726d7e76118b6dab25673820062cd603a75e7fa304b3543ae3da6635f2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/c662d7726d7e76118b6dab25673820062cd603a75e7fa304b3543ae3da6635f2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f626c7565776176652d6c6162732f636865636b6d617465) [![](https://camo.githubusercontent.com/bdbb4fafcd707e1cc1c54a146688e72e6d0486ebe3f0ce45321d488685d99e26/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/bdbb4fafcd707e1cc1c54a146688e72e6d0486ebe3f0ce45321d488685d99e26/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f626c7565776176652d6c6162732f636865636b6d617465) [![](https://camo.githubusercontent.com/4da275d60779ef64702698950ff276db81f98cd294eab82ff696e76debf58148/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c616e6775616765732f746f702f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/4da275d60779ef64702698950ff276db81f98cd294eab82ff696e76debf58148/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c616e6775616765732f746f702f626c7565776176652d6c6162732f636865636b6d617465) [![](https://camo.githubusercontent.com/d1545c1ba2ff4db9f53e4af30a1fd196e0482fce29ebfab2e1d89ee73bf238ae/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/d1545c1ba2ff4db9f53e4af30a1fd196e0482fce29ebfab2e1d89ee73bf238ae/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f626c7565776176652d6c6162732f636865636b6d617465) [![](https://camo.githubusercontent.com/470b0409fd251607b3b15fa498c662a3ab5c4eeea22613ba24c63a13142fc506/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722f626c7565776176652d6c6162732f636865636b6d617465)](https://camo.githubusercontent.com/470b0409fd251607b3b15fa498c662a3ab5c4eeea22613ba24c63a13142fc506/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722f626c7565776176652d6c6162732f636865636b6d617465)

# [Checkmate](https://bluewavelabs.ca)

[](#checkmate)

**An open source server and infrastructure monitoring application**

[![Dashboard-dark](https://private-user-images.githubusercontent.com/167266851/364595677-db875138-164f-453c-a75e-889f88747578.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzY0NTk1Njc3LWRiODc1MTM4LTE2NGYtNDUzYy1hNzVlLTg4OWY4ODc0NzU3OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kNGNmNzQzYTIxY2RmMDAxYTlkNDQzNDdlY2NiYmVjOGVhZmJhOGZiNjUyNGIxZWVjZmUwNTA0YmI2YWMzMjI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-FTN4UVPrI91GkHB_eYtQWAS-rXk0PFHj-iuxjWmCTA)](https://private-user-images.githubusercontent.com/167266851/364595677-db875138-164f-453c-a75e-889f88747578.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzY0NTk1Njc3LWRiODc1MTM4LTE2NGYtNDUzYy1hNzVlLTg4OWY4ODc0NzU3OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kNGNmNzQzYTIxY2RmMDAxYTlkNDQzNDdlY2NiYmVjOGVhZmJhOGZiNjUyNGIxZWVjZmUwNTA0YmI2YWMzMjI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-FTN4UVPrI91GkHB_eYtQWAS-rXk0PFHj-iuxjWmCTA)

Checkmate is an open source monitoring tool used to track the operational status and performance of servers and websites. It regularly checks whether a server/website is accessible and performs optimally, providing real-time alerts and reports on the monitored services' availability, downtime, and response time.

Checkmate also has an agent, called [Capture](https://github.com/bluewave-labs/capture), to retrieve data from remote servers. While Capture is not required to run Checkmate, it provides additional insigths about your servers' CPU, RAM, disk and temperature status.

Checkmate has ben stress tested with 1000+ active monitors without any particular issues or performance bottlenecks.

We **love** what we are building here, and we contibuously learn a few things about Reactjs, Nodejs, MongoDB and Docker while building Checkmate.

## 📦 Demo

[](#-demo)

See [Checkmate](https://checkmate-demo.bluewavelabs.ca/) in action. The username is <uptimedemo@demo.com> and the password is Demouser1! (just a note that we update the demo server from time to time, so if it doesn't work for you, please ping us on Discussions channel).

## 🔗 User's guide

[](#-users-guide)

Usage instructions can be found [here](https://bluewavelabs.gitbook.io/checkmate). It's still WIP and some of the information there might be outdated. Rest assured, we are doing our best! :)

## 🛠️ Installation

[](#️-installation)

See installation instructions in [Checkmate documentation portal](https://bluewavelabs.gitbook.io/checkmate/quickstart). Alternatively, you can also use [Coolify](https://coolify.io/) for a one click Docker deployment. If you would like to monitor your server infrastructure, you'll need [Capture agent](https://github.com/bluewave-labs/capture). Capture repository also contains the installation instructions.

## 💚 Questions & ideas

[](#-questions--ideas)

If you have any questions, suggestions or comments, please use our [Discord channel](https://discord.gg/NAb6H3UTjK). We've also launched our [Discussions](https://github.com/bluewave-labs/bluewave-uptime/discussions) page! Feel free to ask questions or share your ideas—we'd love to hear from you!

## 🧩 Features

[](#-features)

* Completely open source, deployable on your servers
* Website monitoring
* Page speed monitoring
* Infrastructure monitoring (memory, disk usage, CPU performance etc) - requires [Capture](https://github.com/bluewave-labs/capture)
* Docker monitoring
* Ping monitoring
* SSL monitoring
* Incidents at a glance
* E-mail notifications
* Scheduled maintenance

**Short term roadmap:**

* Port monitoring (**complete**, waiting to be deployed to stable version)
* Global (distributed) uptime checking on Solana network (**in progress**)
* Status pages (**in progress**)
* Better notification options (Webhooks, Discord, Telegram, Slack)
* More configuration options
* Translations
* Tagging/grouping monitors
* DNS monitoring

## 🏗️ Screenshots

[](#️-screenshots)

[![Group 3765](https://private-user-images.githubusercontent.com/167266851/394149815-8e8144f2-a769-4707-8ea1-99cf758284a8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk0MTQ5ODE1LThlODE0NGYyLWE3NjktNDcwNy04ZWExLTk5Y2Y3NTgyODRhOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZDIwNjliNjEzOGI2Y2NiZjkyMGJhZmRhMzBkYTgxMjU4NWEwZmRkOWYyMjVlMTFhYWVkMTUyNGQ1NzgzNzBhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.W8eioYYuGAGgvhRtEViDY-AhySSbi7BBuwGmM9oBGps)](https://private-user-images.githubusercontent.com/167266851/394149815-8e8144f2-a769-4707-8ea1-99cf758284a8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk0MTQ5ODE1LThlODE0NGYyLWE3NjktNDcwNy04ZWExLTk5Y2Y3NTgyODRhOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZDIwNjliNjEzOGI2Y2NiZjkyMGJhZmRhMzBkYTgxMjU4NWEwZmRkOWYyMjVlMTFhYWVkMTUyNGQ1NzgzNzBhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.W8eioYYuGAGgvhRtEViDY-AhySSbi7BBuwGmM9oBGps)

[![Group 3768](https://private-user-images.githubusercontent.com/167266851/394150533-05aed2f2-2cf7-487f-879b-cf8bfb0e9241.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk0MTUwNTMzLTA1YWVkMmYyLTJjZjctNDg3Zi04NzliLWNmOGJmYjBlOTI0MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZmJlNzk3YjliZDI0MmIzMDBiZjA3MDVjYmZiZjVlNDYwMGJlYmQwOGJiZjBiNjJhNTUxYTk0M2MyMTdjMGY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.oJ3gGfYtmTIIoAb-IlDLtGdneGM6wbiRQM9Vt6nLl4c)](https://private-user-images.githubusercontent.com/167266851/394150533-05aed2f2-2cf7-487f-879b-cf8bfb0e9241.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk0MTUwNTMzLTA1YWVkMmYyLTJjZjctNDg3Zi04NzliLWNmOGJmYjBlOTI0MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZmJlNzk3YjliZDI0MmIzMDBiZjA3MDVjYmZiZjVlNDYwMGJlYmQwOGJiZjBiNjJhNTUxYTk0M2MyMTdjMGY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.oJ3gGfYtmTIIoAb-IlDLtGdneGM6wbiRQM9Vt6nLl4c)

[![Group 3768-1](https://private-user-images.githubusercontent.com/167266851/394150591-d4ee4bcf-4d69-4e4a-9bce-fd3541129c24.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk0MTUwNTkxLWQ0ZWU0YmNmLTRkNjktNGU0YS05YmNlLWZkMzU0MTEyOWMyNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MjcwZGJmZWNhYWM2YmQyOTNlMWFhMDk0MGQzOTUxZjc3YjI0ZDg2MjQ0Y2MzNmU5MmZhNTIwNTIwM2RiZTA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.mOkBUzMy-nZhSjOeUUafqbs3xIx_Yad6bZeJFZFPqNE)](https://private-user-images.githubusercontent.com/167266851/394150591-d4ee4bcf-4d69-4e4a-9bce-fd3541129c24.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwNzY5NTEsIm5iZiI6MTczNjA3NjY1MSwicGF0aCI6Ii8xNjcyNjY4NTEvMzk0MTUwNTkxLWQ0ZWU0YmNmLTRkNjktNGU0YS05YmNlLWZkMzU0MTEyOWMyNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxMTMwNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MjcwZGJmZWNhYWM2YmQyOTNlMWFhMDk0MGQzOTUxZjc3YjI0ZDg2MjQ0Y2MzNmU5MmZhNTIwNTIwM2RiZTA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.mOkBUzMy-nZhSjOeUUafqbs3xIx_Yad6bZeJFZFPqNE)

## 🏗️ Tech stack

[](#️-tech-stack)

* [ReactJs](https://react.dev/)
* [MUI (React framework)](https://mui.com/)
* [Node.js](https://nodejs.org/en)
* [MongoDB](https://mongodb.com)
* Lots of other open source components!

## 🤝 Contributing

[](#-contributing)

We pride ourselves on building strong connections with contributors at every level. Despite being a young project, Checkmate has already earned 2700 stars and attracted almost 40 contributors from around the globe. So, don’t hold back — jump in, contribute and learn with us!

Here's how you can contribute:

1. Star this repo :)
2. Check [Contributor's guideline](https://github.com/bluewave-labs/bluewave-uptime/blob/master/CONTRIBUTING.md). First timers are encouraged to check `good-first-issue` tag.
3. Optionally, read [project structure](https://bluewavelabs.gitbook.io/checkmate/developers-guide/general-project-structure) and [high level overview](https://bluewavelabs.gitbook.io/checkmate/developers-guide/high-level-overview).
4. Have a look at our Figma designs [here](https://www.figma.com/design/RPSfaw66HjzSwzntKcgDUV/Uptime-Genie?node-id=0-1\&t=WqOFv9jqNTFGItpL-1) if you are going to use one of our designs. We encourage you to copy to your own Figma page, then work on it as it is read-only.
5. Open an issue if you believe you've encountered a bug.
6. Check for good-first-issue's if you are a newcomer.
7. Make a pull request to add new features/make quality-of-life improvements/fix bugs.

[![](https://camo.githubusercontent.com/43e8cdfe8ba0efff9a7adf72e901555807acebf4b42787d152ed1f591d2b8839/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d626c7565776176652d6c6162732f636865636b6d617465)](https://github.com/bluewave-labs/checkmate/graphs/contributors)

[![Star History Chart](https://camo.githubusercontent.com/9d64fbd8d38e9051f42b79ad3efd01433dc8666601514f514bd4365230ebda0e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d626c7565776176652d6c6162732f636865636b6d61746526747970653d44617465)](https://star-history.com/#bluewave-labs/bluewave-uptime\&Date)

Also check other developer and contributor-friendly projects of BlueWave:

* [BlueWave DataRoom](https://github.com/bluewave-labs/bluewave-dataroom), an secure file sharing application, aka dataroom.
* [BlueWave HRM](https://github.com/bluewave-labs/bluewave-hrm), a complete Human Resource Management platform.
* [BlueWave Onboarding](https://github.com/bluewave-labs/bluewave-onboarding), an application that helps new users learn how to use your product via hints, tours, popups and banners.
* [VerifyWise](https://github.com/bluewave-labs/verifywise), the first open source AI governance platform.


