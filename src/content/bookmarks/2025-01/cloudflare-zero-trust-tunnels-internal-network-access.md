---
title: "通过Cloudflare Zero Trust 实现内网穿透，访问本地项目无需公网IP或VPS"
slug: cloudflare-zero-trust-tunnels-internal-network-access
description: |
  通过Cloudflare的Zero Trust Tunnels，可以轻松实现内网穿透，无需额外的公网IPv4地址或VPS。本文提供详细步骤，教你如何使用现有的域名访问本地搭建的项目，让你在任何地方都能轻松访问。
tags: 
  - cloudflare
  - dev
  - tool
pubDatetime: 2025-01-09T11:12:34+08:00
ogImage: https://linux.do/uploads/default/original/3X/9/d/9dd49731091ce8656e94433a26a3ef36062b3994.png
---

[原文链接](https://linux.do/t/topic/293931)

---

1.首先需要解决域名问题\
2.注册一个cloud flare账号并将域名挂载到cloud flare上\
挂载教程：\
(<https://www.youtube.com/watch?v=Y0s0oRaDYyM&t=644s>)\
3.注册一个zero trust

[![9c82ea97-6863-472a-bd37-61163f9038ce](https://linux.do/uploads/default/optimized/4X/f/9/1/f9102f620831332a5fed3a662227c535530a78cb_2_250x500.png)](https://linux.do/uploads/default/original/4X/f/9/1/f9102f620831332a5fed3a662227c535530a78cb.png "9c82ea97-6863-472a-bd37-61163f9038ce")

第一次注册会让你添加付款方式，可以直接返回到cf主页然后再打开zero trust，然后就不需要添加支付方式了。\
4.我们找到

[![659eefe4-a4d0-43e4-a543-cb22638fe860](https://linux.do/uploads/default/optimized/4X/8/f/f/8ffc51c8dc5af63c825d878392fc68b33a46a8d7_2_671x500.png)](https://linux.do/uploads/default/original/4X/8/f/f/8ffc51c8dc5af63c825d878392fc68b33a46a8d7.png "659eefe4-a4d0-43e4-a543-cb22638fe860")

5.点击创建

[![image](https://linux.do/uploads/default/original/4X/9/d/0/9d03535916a2d09d76d8eceb5cd8b5d93c57897d.png)](https://linux.do/uploads/default/original/4X/9/d/0/9d03535916a2d09d76d8eceb5cd8b5d93c57897d.png "image")

6.选择左边这个

[![image](https://linux.do/uploads/default/optimized/4X/f/1/0/f10fa3fcf29a872f65da6b8dec77eccff28a9b61_2_690x408.png)](https://linux.do/uploads/default/original/4X/f/1/0/f10fa3fcf29a872f65da6b8dec77eccff28a9b61.png "image")

7.输入项目名称

[![image](https://linux.do/uploads/default/optimized/4X/a/4/0/a40d2f713013aaafb82b1c14d5de7eefdeee0512_2_690x284.png)](https://linux.do/uploads/default/original/4X/a/4/0/a40d2f713013aaafb82b1c14d5de7eefdeee0512.png "image")

8.选择系统，我们以Windows为例，选择合适你的安装包，点击下载

[![image](https://linux.do/uploads/default/optimized/4X/f/6/4/f64a1faddfa471d90a2aae8e45c19b98282922e9_2_690x411.png)](https://linux.do/uploads/default/original/4X/f/6/4/f64a1faddfa471d90a2aae8e45c19b98282922e9.png "image")

9.在电脑安装\
![image](https://linux.do/uploads/default/original/4X/5/5/7/557bdce75a099c447920f447f658aaf90cb1f2b7.png)\
10.以管理员身份运行cmd（一定要管理员身份运行，不然会运行失败），并复制代码安装cf服务

[![image](https://linux.do/uploads/default/optimized/4X/2/0/5/20517c766d56fbab591fdb338b0ef0918da42383_2_690x274.png)](https://linux.do/uploads/default/original/4X/2/0/5/20517c766d56fbab591fdb338b0ef0918da42383.png "image")

这里我已经安装完成

[![image](https://linux.do/uploads/default/original/4X/b/1/1/b119bf1aba93790da148014312c09bbe41d67a8e.png)](https://linux.do/uploads/default/original/4X/b/1/1/b119bf1aba93790da148014312c09bbe41d67a8e.png "image")

11.点击下一步

[![image](https://linux.do/uploads/default/optimized/4X/a/c/1/ac1b06ed669a0d4399e82c90f89e998f8a98b74b_2_690x336.png)](https://linux.do/uploads/default/original/4X/a/c/1/ac1b06ed669a0d4399e82c90f89e998f8a98b74b.png "image")

12.输入项目名称，选择挂载好的域名，协议选择https，url填入你部署项目的端口（格式为localhost:部署项目端口）

[![image](https://linux.do/uploads/default/optimized/4X/3/b/0/3b01a4041125a6db7a3f1eaa0c20daff3d1749c8_2_690x198.png)](https://linux.do/uploads/default/original/4X/3/b/0/3b01a4041125a6db7a3f1eaa0c20daff3d1749c8.png "image")

13.然后点击右下角保存，显示健康即为成功。\
![image](https://linux.do/uploads/default/original/4X/5/2/a/52a9f58f2cf80cb925bd388d29a99f200589fc02.png)\
以我搭建于本地的alist服务为例，通过<https://alist.bohemiaalist.click/>\
可以实现从外部访问。通过127.0.0.1:5244也可以访问，无需公网ipv4

我自己使用下来觉得速度慢（没进行优选），alist拉NAS的东西基本没什么速度

### 此话题将在最后一个回复的1 个月后关闭。

<!---->


