---
title: "NeatChat：精简优化版NextChat - GitHub项目"
slug: neatchat-optimized-version-nextchat
description: |
  NeatChat是基于NextChat的全新版本，增加了多项优质功能并进行优化，提供main、mini和preview三种分支，以适应不同用户需求。它支持vercel一键部署，经 docker 部署也很方便。详细使用方法请参考官方文档。
tags: 
  - AI
  - dev
  - opensource
  - chatgpt
  - webdev
pubDatetime: 2025-03-12T10:20:39+08:00
ogImage: https://opengraph.githubassets.com/460b999e122834c4d69818eb541a4cb98597f91e6de1a7b2f0e75acccdb88c29/tianzhentech/NeatChat
---

[原文链接](https://github.com/tianzhentech/NeatChat)

---

[![](https://raw.githubusercontent.com/tianzhentech/static/main/images/NeatChat-Dark.svg)](https://raw.githubusercontent.com/tianzhentech/static/main/images/NeatChat-Dark.svg)

[![Stars](https://camo.githubusercontent.com/f560270b03ea3cb32006fd4bcfcb145825e1aa5663f96da024ec195c83008963/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f7469616e7a68656e746563682f6e65617463686174)](https://camo.githubusercontent.com/f560270b03ea3cb32006fd4bcfcb145825e1aa5663f96da024ec195c83008963/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f7469616e7a68656e746563682f6e65617463686174) [![Forks](https://camo.githubusercontent.com/cada75788a601a950b02fba887f2cf95ffba380a7b504373b814fbe4faa97d7e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f7469616e7a68656e746563682f6e65617463686174)](https://camo.githubusercontent.com/cada75788a601a950b02fba887f2cf95ffba380a7b504373b814fbe4faa97d7e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f7469616e7a68656e746563682f6e65617463686174) [![Web](https://camo.githubusercontent.com/0fa1e9e043c1ae8e21ecde10b9b8d706e1e7d4f3bd6853b13082df28740beb90/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765622d5057412d6f72616e67653f6c6f676f3d6d6963726f736f667465646765)](https://camo.githubusercontent.com/0fa1e9e043c1ae8e21ecde10b9b8d706e1e7d4f3bd6853b13082df28740beb90/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765622d5057412d6f72616e67653f6c6f676f3d6d6963726f736f667465646765) [![Web](https://camo.githubusercontent.com/78666480b2e28531b4efc12a6b12e788b85c35355fb82702a9121da2241390c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d57696e646f77732d626c75653f6c6f676f3d77696e646f7773)](https://camo.githubusercontent.com/78666480b2e28531b4efc12a6b12e788b85c35355fb82702a9121da2241390c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d57696e646f77732d626c75653f6c6f676f3d77696e646f7773) [![Release Badge](https://camo.githubusercontent.com/c9e81f4208775eca2ffee2d95e4282395c23547a9927c6fed52060e72f97ef3d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f7469616e7a68656e746563682f6e656174636861742e737667)](https://camo.githubusercontent.com/c9e81f4208775eca2ffee2d95e4282395c23547a9927c6fed52060e72f97ef3d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f7469616e7a68656e746563682f6e656174636861742e737667) [![License](https://camo.githubusercontent.com/b9163c44798a0d4d68e4959f97e76361761de3527c30866556b37db7e01faaa9/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7469616e7a68656e746563682f6e656174636861742e737667)](https://camo.githubusercontent.com/b9163c44798a0d4d68e4959f97e76361761de3527c30866556b37db7e01faaa9/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7469616e7a68656e746563682f6e656174636861742e737667)

[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https://github.com/tianzhentech/NeatChat.git)

简体中文 | [English](https://github.com/tianzhentech/NeatChat/blob/main/README.en.md)

NeatChat是基于NextChat的一个全新的版本，并进行了多项优化。NeatChat目前有三个分支，分别是main分支，mini分支，preview分支。

preview分支是main分支的预览分支，在稳定之后会合并到main分支，mini分支是单独的一个精简分支（mini分支请移步至[NeatChat-Mini](https://github.com/tianzhentech/NeatChat-Mini)）。

main分支的使命在于优化UI和新增功能，以至于后面脱离NextChat，独立发展，而mini分支则会在NextChat的基础上进行微调和删减，紧跟NextChat的步伐，只有main分支特别重要的功能才会下放到mini分支。由于main分支和mini分支的目的不一样，所以也将有两套UI。

# 预览

[](#预览)

[![](https://raw.githubusercontent.com/tianzhentech/static/main/images/%7B326DD837-A2FE-4603-A289-47FD5FED329A%7D.png)](https://raw.githubusercontent.com/tianzhentech/static/main/images/%7B326DD837-A2FE-4603-A289-47FD5FED329A%7D.png) [![](https://raw.githubusercontent.com/tianzhentech/static/main/images/%7B1FB6B249-72D5-42F0-B861-7FE95ADCEEEE%7D.png)](https://raw.githubusercontent.com/tianzhentech/static/main/images/%7B1FB6B249-72D5-42F0-B861-7FE95ADCEEEE%7D.png) [![](https://raw.githubusercontent.com/tianzhentech/static/main/images/%7B6656232E-09F3-472D-A2B4-621DDD57D9CC%7D.png)](https://raw.githubusercontent.com/tianzhentech/static/main/images/%7B6656232E-09F3-472D-A2B4-621DDD57D9CC%7D.png)

> 更多内容请移步[演示站](https://neat.tz889.us.kg)

# 快速开始

[](#快速开始)

1. 支持vercel一键部署：[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https://github.com/tianzhentech/NeatChat.git)

2. docker只需要替换官方**yidadaa/chatgpt-next-web:版本号**为**tianzhentech/chatgpt-next-web:latest**即可

> 详细使用请参考[NextChat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)

# 版本说明

[](#版本说明)

从`v1.1.12`起，将采用新的版本号命名，所有正式版都只保留三位，比如以后的`v1.1.13`、`v1.1.14`都是正式版，也就是main分支的最新版。而所有的四位版本，比如`v1.1.12.1`、`v1.1.12.2`都是preview分支的增量更新，将作为`Pre-release`发布，preview分支所有的增量更新仍然会定期合并到下一个正式版中。

这么做是为了打包多平台有更兼容的版本号，免去一些不必要的麻烦。

# 赞助

[](#赞助)

本项目不求赞助，如果有可能的话，可以支持我一些硅基流动或者火山引擎赠金，我会更好的支持相关系列模型，或者日后考虑开设公益站给有需要的人使用，欢迎各位佬友赞助。

我的硅基流动邀请链接：<https://cloud.siliconflow.cn/i/tX3hT0Ly>

我的火山引擎邀请链接：<https://volcengine.com/L/i5QyNFSX>

![Star History Chart](https://camo.githubusercontent.com/8fbd31faf3cda3494ee0c951cec862a48fab437c2a97662671ef063a3a206842/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d7469616e7a68656e746563682f4e6561744368617426747970653d44617465)


