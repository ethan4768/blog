---
title: "WebCurl: 极简便捷的网页版API调试工具"
slug: webcurl-api-debugging-tool
description: |
  WebCurl是一款极简的网页版API调试工具，支持完整的HTTP请求转发，拥有完善的调试服务。其小巧的体积和无依赖的特性使其成为Postman的轻量替代，适合各类开发和调试场景，保障数据安全，适用于多种平台和环境。
tags: 
  - API
  - dev
  - tool
  - opensource
pubDatetime: 2025-08-01T14:10:10+08:00
ogImage: 
---

[原文链接](https://github.com/o8oo8o/WebCurl)

---

# 🚀 WebCurl - 极简网页版API调试神器

[](#-webcurl---极简网页版api调试神器)

> **⚡ 一个文件搞定所有API测试需求 | 🎯 替代Postman的轻量级选择 | 🔒 数据本地化，安全无忧**

[![Go Version](https://camo.githubusercontent.com/a17ff1d491a28da74eec6139e01e2916e4f22e33eaebaec3066e1f8b4eadbecd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f2d312e31392b2d626c75652e737667)](https://golang.org) [![License](https://camo.githubusercontent.com/28f4d479bf0a9b033b3a3b95ab2adc343da448a025b01aefdc0fbc7f0e169eb8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667)](https://github.com/o8oo8o/WebCurl/blob/main/LICENSE) [![Platform](https://camo.githubusercontent.com/5c36f7246501dd628beec5db96ec8d4a5fa6eb91a25bf314ffd546abfc94025c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506c6174666f726d2d57696e646f77732532302537432532304c696e75782532302537432532304d61634f5325323025374325323041524d2d6c69676874677265792e737667)](https://github.com/o8oo8o/WebCurl/blob/main)

> **联系我: QQ 774309635**

## ✨ 为什么选择 WebCurl？

[](#-为什么选择-webcurl)

还在为API调试工具而烦恼吗？Postman太臃肿？curl命令行太复杂？试试 **WebCurl** 吧！

🎉 **一个8MB的二进制文件 = 完整的API测试解决方案**

💡 **源码极简**：仅2个文件（`index.html` + `main.go`）实现完整功能

### 🌟 核心优势对比

[](#-核心优势对比)

| 特性         | WebCurl         | Postman  | curl    |
| ---------- | --------------- | -------- | ------- |
| **安装复杂度**  | ⭐ 一个文件          | ⭐⭐⭐ 需要安装 | ⭐⭐ 命令行  |
| **跨域支持**   | ✅ 完美解决          | ✅ 原生支持   | ✅ 原生支持  |
| **文件大小**   | 10MB            | 200MB+   | 系统自带    |
| **离线使用**   | ✅ 完全离线          | ❌ 需要登录   | ✅ 完全离线  |
| **数据安全**   | ✅ 本地存储          | ❌ 云端同步   | ✅ 本地存储  |
| **信创兼容**   | ✅ 完美支持          | ❌ 有限支持   | ✅ 完美支持  |
| **IPv6支持** | ✅ 完美支持          | ✅ 支持     | ✅ 原生支持  |
| **源码简洁**   | ✅ 仅2个文件         | ❌ 复杂项目   | ❌ 复杂项目  |
| **实时通信**   | ✅ WebSocket+SSE | ❌ 仅HTTP  | ❌ 仅HTTP |
| **调试接口**   | ✅ 内置EchoServer  | ❌ 需额外工具  | ❌ 需额外工具 |

## 📖 简介

[](#-简介)

本项目是一个极致轻量、跨平台、无依赖的 HTTP 请求转发与调试工具，**本质上就是一个网页版的API测试与调试工具**，适合接口开发、调试、测试等多种场景。

* **前端**：纯原生 HTML+JS+CSS，无任何第三方库或依赖，开箱即用，加载速度极快。
* **后端**：仅使用 Golang 标准库，无任何第三方依赖，安全可靠。
* **源码极简**：整个项目仅包含2个文件（`index.html` + `main.go`），代码结构清晰，易于理解和维护。
* **产物**：编译后仅有一个约 14M 的单一二进制文件（含前端页面），无需安装、无需环境、无需依赖，直接运行。
* **平台支持**：支持 Windows、Linux、MacOS、ARM、x86\_64、信创（国产芯片/操作系统）等主流及国产平台，真正做到"一次编译，到处运行"。
* **网络支持**：完美支持 IPv4 和 IPv6 网络协议，适应各种网络环境。
* **实时通信**：原生支持 WebSocket 和 SSE（Server-Sent Events），满足实时数据推送需求。
* **内置调试服务**：集成强大的EchoServer，提供完整的请求回显和响应控制功能。
* **适用场景**：接口联调、API 测试、前端跨域调试、信创环境接口测试、离线/内网环境接口调试等。
* **数据本地化存储,保障安全**：所有接口信息、历史记录、变量、全局头等均仅存储于本地浏览器（localStorage），不会同步到云端或外部服务器，保障接口数据的私密性与安全性，适合企业内网、敏感环境使用。

**主要用途**：API 测试与调试,替代某些需要登录才能使用工具(xxxxMan,xxxFox)

* 支持多种请求体格式（form-data、x-www-form-urlencoded、json、text、xml、binary）
* 支持文件上传、下载
* 支持请求重试、超时、SSL 验证、重定向等高级选项
* 支持 WebSocket 和 SSE（Server-Sent Events）实时通信
* 内置美观易用的前端页面，支持接口历史、变量、全局头、接口集合管理
* 支持命令行参数自定义监听端口、静态目录、日志、SSL 等
* **内置EchoServer调试服务**：提供完整的请求回显、响应控制、流式通信功能

***

[![演示截图](https://camo.githubusercontent.com/0a49d9a6b4f0af42a268223193da6a904ecc09d9a5bb9ed59fd16a3fe4ffe4c0/68747470733a2f2f67697465652e636f6d2f6f386f6f386f2f7075626c69632f7261772f6d61737465722f7765626375726c5f30312e706e67)](https://camo.githubusercontent.com/0a49d9a6b4f0af42a268223193da6a904ecc09d9a5bb9ed59fd16a3fe4ffe4c0/68747470733a2f2f67697465652e636f6d2f6f386f6f386f2f7075626c69632f7261772f6d61737465722f7765626375726c5f30312e706e67)

***

[![演示截图](https://camo.githubusercontent.com/68983a8bfeb5b00d092c6363a8c9ea09af4377d44c22cf03e3d6c9021374cd32/68747470733a2f2f67697465652e636f6d2f6f386f6f386f2f7075626c69632f7261772f6d61737465722f7765626375726c5f30322e706e67)](https://camo.githubusercontent.com/68983a8bfeb5b00d092c6363a8c9ea09af4377d44c22cf03e3d6c9021374cd32/68747470733a2f2f67697465652e636f6d2f6f386f6f386f2f7075626c69632f7261772f6d61737465722f7765626375726c5f30322e706e67)

***

### 打赏我：

[](#打赏我)

* **每一个开源项目的背后，都有一群默默付出、充满激情的开发者。他们用自己的业余时间，不断地优化代码、修复bug、撰写文档，只为让项目变得更好。如果您觉得我的项目对您有所帮助，如果您认可我的努力和付出，那么请考虑给予我一点小小的打赏，友情提示:打赏不退，怕被媳妇查到大额支出🤡，如果需要技术支持，需要收费哦**

\
\


[![打赏二维码](https://camo.githubusercontent.com/cfe60d46059183ec59c1376395c84c0d84ea302ae5962312d3932e87a0a291b3/68747470733a2f2f67697465652e636f6d2f6f386f6f386f2f7075626c69632f7261772f6d61737465722f7061792e706e67)](https://camo.githubusercontent.com/cfe60d46059183ec59c1376395c84c0d84ea302ae5962312d3932e87a0a291b3/68747470733a2f2f67697465652e636f6d2f6f386f6f386f2f7075626c69632f7261772f6d61737465722f7061792e706e67)

[项目推荐: https://github.com/o8oo8o/WebSSH 一个网页版的SSH管理工具](https://github.com/o8oo8o/WebSSH "一个网页版的SSH管理工具")

\


## 🛠️ 功能特性

[](#️-功能特性)

### 🔥 核心功能

[](#-核心功能)

* **🌐 网页版 Postman 体验**：无需安装客户端，浏览器即用，界面美观，功能丰富。
* **🔄 HTTP 请求转发**：前端通过 `/api/forward` 接口将请求参数提交给后端，后端代为转发并返回结果，突破浏览器跨域限制。
* **支持 HTTP CONNECT 代理隧道**：支持 HTTP CONNECT 方法，可作为 HTTPS/SSH 等协议的代理隧道，适用于 curl、ssh、ncat 等工具的代理转发。
* **📁 多种请求体支持**：支持 `form-data`（含多文件上传）、`x-www-form-urlencoded`、`json`、`text`、`xml`、`binary`。
* **🔧 请求头自定义**：支持自定义任意请求头。
* **📤 文件上传/下载**：支持多文件上传，响应内容可直接下载。
* **🔄 请求重试与超时**：可配置重试次数、重试间隔、超时时间。
* **🔒 SSL 验证与重定向**：可选择是否校验 SSL 证书、是否自动跟随重定向。
* **📚 前端功能丰富**：接口历史、接口集合、变量替换、全局请求头、导入导出等。
* **⚙️ 命令行灵活配置**：支持自定义监听地址、端口、静态目录、日志、SSL 证书等。
* **⚡ 极致轻量**：单一二进制文件，体积仅约 10M，部署、迁移、分发极其方便。
* **💾 无依赖、易运维**：无需数据库、无需外部依赖，直接运行。
* **🖥️ 跨平台/信创兼容**：支持主流操作系统及国产软硬件平台，适合信创环境、内网、离线等特殊场景。
* **🌐 网络协议支持**：完美支持 IPv4 和 IPv6 网络协议，适应各种网络环境。
* **🔌 实时通信支持**：原生支持 WebSocket 和 SSE（Server-Sent Events），满足实时数据推送需求。

### 🎯 EchoServer 调试服务

[](#-echoserver-调试服务)

* **🔄 智能请求回显**：自动解析并回显请求的URL、方法、请求头、请求体（文本、表单、文件、二进制等）。
* **🎛️ 灵活响应控制**：支持通过自定义请求头或URL参数灵活控制响应内容和行为。
* **📊 多种响应格式**：支持JSON、XML、Text等多种响应格式。
* **⏱️ 响应延迟控制**：可自定义响应延迟时间，模拟网络延迟场景。
* **📥 下载响应控制**：支持将响应内容作为文件下载。
* **🔌 流式通信支持**：SSE和WebSocket接口支持流式数据推送。
* **🎯 自定义数据队列**：支持预设响应数据，实现自定义流式推送。
* **🛡️ 健壮性保障**：内置panic恢复机制，防止服务崩溃。

### 🌐 静态文件服务器

[](#-静态文件服务器)

* **📁 完整文件服务**：类似Nginx的静态文件服务器功能，支持所有常见文件类型。
* **🎨 丰富MIME支持**：自动识别HTML、CSS、JS、图片、音频、视频、字体等文件类型。
* **🔒 安全防护**：防止路径遍历攻击，确保文件访问安全。
* **⚡ 高性能**：支持大文件传输，内置缓存控制。
* **🌍 CORS支持**：内置跨域资源共享支持，适合前端开发。
* **📱 移动友好**：支持移动设备访问，响应式设计。

### 🧰 常用工具

[](#-常用工具)

* **JWT解析**：支持一键解析 JWT Token，快速查看 Payload 信息，便于调试鉴权接口。
* **UUID生成**：支持生成标准 UUID，方便接口测试与数据填充。
* **时间戳转换**：支持毫秒/秒时间戳与日期时间的相互转换，适配多种场景。
* **Base64编解码**：支持 Base64 字符串的编码与解码，便于处理二进制与文本数据。
* **Token生成器**：支持自定义规则生成随机 Token，适合接口测试、模拟登录等场景。

***

## 🚀 快速开始

[](#-快速开始)

### 1️⃣ 编译 & 运行（30秒搞定）

[](#1️⃣-编译--运行30秒搞定)

**源码结构极简**：

```
WebCurl/
├── index.html    # 前端界面（纯原生HTML+JS+CSS）
└── main.go       # 后端服务（Go标准库）
```

```
# 编译
go build -o WebCurl main.go
# 也可以使用 sh build.sh 命令

# 运行（默认 0.0.0.0:4444，内嵌前端页面）
./WebCurl

# 浏览器访问
http://localhost:4444
```

> **注** ：构建所有平台可执行文件，请使用 `sh build.sh all` 命令，构建完成后在build目录下查找对应平台可执行文件。

### 2️⃣ 命令行参数

[](#2️⃣-命令行参数)

| 参数               | 说明                                      | 默认值           |
| ---------------- | --------------------------------------- | ------------- |
| `--host`         | 监听地址                                    | 0.0.0.0       |
| `--port`         | 监听端口                                    | 4444          |
| `--webroot`      | 静态文件根目录（为空用内嵌 index.html）               | 空             |
| `--daemon`       | 后台运行（支持 Windows/Linux/Mac）              | false         |
| `--echo-server`  | 是否开启EchoServer调试服务                      | true          |
| `--log-level`    | 日志级别（error, info, debug）                | error         |
| `--log-file`     | 日志文件路径                                  | post\_api.log |
| `--log-size`     | 日志文件大小限制（K/M/G）                         | 100M          |
| `--ssl-cert`     | SSL 证书文件路径                              | ssl\_cert.pem |
| `--ssl-cert-key` | SSL 证书密钥路径                              | ssl\_cert.key |
| `--upload-dir`   | form-data上传文件保存目录（为空仅透传）                | 空             |
| `--stdout-log`   | 是否在控制台打印日志，true为同时输出到控制台和文件，false仅输出到文件 | true          |

#### 启动示例

[](#启动示例)

```
# 默认（0.0.0.0:4444，内嵌index.html，开启EchoServer）
./WebCurl

# 指定端口和host
./WebCurl --host 127.0.0.1 --port 8888

# 指定静态目录
./WebCurl --webroot /tmp/www

# 控制日志是否输出到控制台
./WebCurl --stdout-log=false

# 开启静态文件服务器模式（指定目录）
./WebCurl --webroot /mnt/webroot

# 关闭EchoServer调试服务
./WebCurl --echo-server=false

# 后台运行（Linux/MacOS/Windows）
./WebCurl --daemon

# 组合
./WebCurl --host 0.0.0.0 --port 9000 --webroot /tmp/www --daemon --stdout-log=false
```

### 🐳 容器化部署 · 极速上云

[](#-容器化部署--极速上云)

### 🚀 一键 Docker 部署

[](#-一键-docker-部署)

WebCurl 天生适合容器化，支持 Docker/Kubernetes 等主流云原生环境，轻松实现弹性扩展与自动化运维！

#### 1️⃣ Docker 镜像构建与运行

[](#1️⃣-docker-镜像构建与运行)

```
# 构建镜像
docker build -t webcurl:2.2 .

# 运行容器（默认 0.0.0.0:4444）
docker run -d -p:4444:4444 --name webcurl  webcurl:2.2

# 指定数据/静态目录挂载
docker run -d --name webcurl -p 4444:4444 -v /usr/share/nginx/html/:/usr/local/WebCurl/webroot webcurl:2.2 /usr/local/WebCurl/WebCurl --webroot=/usr/local/WebCurl/webroot
```

#### 2️⃣ Kubernetes 极速部署

[](#2️⃣-kubernetes-极速部署)

WebCurl 完美兼容 K8S，支持无状态部署、弹性伸缩、健康检查等企业级需求。

**示例 Deployment 配置：**

```
######################################
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webcurl
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webcurl
  template:
    metadata:
      labels:
        app: webcurl
    spec:
      containers:
      - name: webcurl
        image: webcurl:2.2
        ports:
        - containerPort: 4444
#        args: ["/usr/local/WebCurl/WebCurl","--echo-server=true","--port=4444"]
---
apiVersion: v1
kind: Service
metadata:
  name: webcurl
spec:
  type: NodePort
  ports:
    - port: 4444
      targetPort: 4444
      nodePort: 30444
  selector:
    app: webcurl
######################################
```

> 只需 `kubectl apply -f webcurl.yaml`，即可在 K8s 集群中弹性部署 WebCurl！

### 🌈 容器化优势

[](#-容器化优势)

* **极致轻量**：单一二进制+极简镜像，启动快、资源占用低
* **云原生友好**：无状态设计，天然适配 K8S、Docker、OpenShift 等平台
* **弹性扩展**：支持副本横向扩展，轻松应对高并发
* **自动化运维**：支持健康检查、日志挂载、配置注入
* **一键迁移**：镜像即服务，随时随地部署到任意云/集群/本地

***

**WebCurl，让 API 调试与测试像部署静态网站一样简单，轻松上云，随时随地，安全高效！**

***

## 🎯 适用场景

[](#-适用场景)

### 💼 企业级应用

[](#-企业级应用)

* **内网环境**：数据不出内网，安全可控
* **信创环境**：完美支持国产芯片和操作系统
* **离线部署**：无网络环境也能正常使用
* **团队协作**：配置可导出分享，便于团队统一

### 👨‍💻 开发者日常

[](#-开发者日常)

* **接口联调**：前后端接口调试必备
* **API测试**：自动化测试前的接口验证
* **跨域调试**：完美解决前端跨域问题
* **文件上传测试**：支持多文件上传测试
* **接口调试**：EchoServer提供完整的请求回显和响应控制

### 🔧 运维测试

[](#-运维测试)

* **接口监控**：定期测试关键接口状态
* **性能测试**：支持重试和超时配置
* **SSL测试**：SSL证书验证测试
* **重定向测试**：自动跟随重定向测试
* **实时通信测试**：WebSocket连接和SSE事件流测试
* **网络延迟模拟**：EchoServer支持响应延迟控制

### 🌐 静态文件服务

[](#-静态文件服务)

* **网站托管**：快速部署静态网站，支持HTML、CSS、JS等
* **文件分享**：企业内部文件分享和下载服务
* **开发环境**：前端开发时的本地文件服务器
* **文档服务**：API文档、技术文档的在线访问
* **资源托管**：图片、视频、音频等多媒体资源托管
* **CDN替代**：小型项目的CDN服务替代方案

***

## 📖 前端使用说明

[](#-前端使用说明)

### 1. 访问页面

[](#1-访问页面)

启动后，浏览器访问 `http://localhost:4444`，即可进入 Postman 风格的调试页面。

### 2. 请求模式自动切换

[](#2-请求模式自动切换)

* 前端会自动请求 `/api/mode`，如返回 `{ "mode": "proxy" }`，则所有请求将通过后端 `/api/forward` 转发，解决跨域问题。
* 否则，前端直接用 fetch 发起请求。

### 3. 发送请求（代理模式）

[](#3-发送请求代理模式)

* 支持 GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS 等方法
* 支持多种请求体格式、文件上传、请求头自定义
* 支持变量替换、全局头、接口集合、历史记录等
* 支持请求参数、重试、超时、SSL 验证、重定向等高级选项

***

## 🔧 后端接口说明

[](#-后端接口说明)

### 1. `/api/forward`（POST）

[](#1-apiforwardpost)

用于前端通过 form-data 方式提交请求参数，由后端转发到目标接口。

#### 支持的 form-data 字段

[](#支持的-form-data-字段)

| 字段名              | 类型/说明   | 示例/说明                                          |
| ---------------- | ------- | ---------------------------------------------- |
| url              | string  | 目标接口地址                                         |
| time\_out        | int     | 超时时间（秒），0为不超时                                  |
| retry\_count     | int     | 重试次数，0为不重试                                     |
| retry\_delay     | int     | 重试间隔（秒），0为无间隔                                  |
| method           | string  | 请求方法，默认 GET                                    |
| body\_type       | string  | 请求体类型，见下表                                      |
| headers          | json字符串 | `[{"name":"X-Token","value":"abc"}]`           |
| file\_info       | json字符串 | `[{"field_name":"files","file_name":"a.txt"}]` |
| files            | 文件      | 支持多文件上传                                        |
| body             | string  | 请求体内容（json/xml/text等）                          |
| verify\_ssl      | Y/N     | 是否校验SSL，默认Y                                    |
| follow\_redirect | Y/N     | 是否自动跟随重定向，默认Y                                  |

#### body\_type 支持

[](#body_type-支持)

* `form-data`：多文件上传，表单参数
* `x-www-form-urlencoded`：标准表单
* `json`：application/json
* `text`：text/plain
* `xml`：application/xml
* `binary`：二进制文件上传
* `none`：无请求体

### 2. `/api/mode`（GET）

[](#2-apimodeget)

返回当前后端模式，前端据此判断是否需要通过后端转发。

**返回示例**

```
{ "mode": "proxy" }
```

### 3. EchoServer 调试接口

[](#3-echoserver-调试接口)

#### 3.1 `/api/echo`（所有HTTP方法）

[](#31-apiecho所有http方法)

**功能**：智能请求回显，支持灵活的响应控制。

**特性**：

* 支持所有HTTP方法（GET、POST、PUT、DELETE、PATCH、HEAD、OPTIONS等）
* 自动解析并回显请求的URL、方法、请求头、请求体
* 支持文本、表单、文件上传、二进制等多种请求体类型
* 支持通过自定义请求头或URL参数灵活控制响应

**响应控制参数**：

| 请求头                    | 作用                         | 示例值                    |
| ---------------------- | -------------------------- | ---------------------- |
| X-Response-Status-Code | 控制HTTP响应状态码                | 201、404、500            |
| X-Response-Location    | 设置响应Location头              | <https://www.qq.com>   |
| X-Response-Headers     | 批量设置响应头（JSON字符串，键值对）       | {"X-Foo":"Bar"}        |
| X-Response-Type        | 控制响应体格式（json/xml/text）     | json、xml、text          |
| X-Response-Sleep       | 控制响应延迟（单位：毫秒）              | 200、1000               |
| X-Response-Body        | 指定Base64编码的响应body内容（优先级最高） | `eyJtc2ciOiJoZWxsbyJ9` |
| X-Response-Download    | 控制响应为下载，指定下载文件名            | data.txt、result.json   |

**参数传递方式**：

* 支持请求头方式：`curl -H "X-Response-Status-Code: 202" http://localhost:4444/api/echo`
* 支持URL参数方式：`curl "http://localhost:4444/api/echo?X-Response-Status-Code=202"`
* **请求头优先级高于URL参数**

**基本用法示例**：

```
# 普通请求
curl -X GET http://localhost:4444/api/echo
curl -X POST -d 'Hello World' http://localhost:4444/api/echo

# 表单与文件上传
curl -X POST -F 'text=Hello' -F 'file=@/path/to/file' http://localhost:4444/api/echo

# 控制响应状态码
curl -H "X-Response-Status-Code: 202" http://localhost:4444/api/echo

# 控制响应类型
curl -H "X-Response-Type: xml" http://localhost:4444/api/echo
curl -H "X-Response-Type: text" -d "a simple text body" http://localhost:4444/api/echo

# 控制响应延迟
curl -H "X-Response-Sleep: 500" http://localhost:4444/api/echo

# 自定义响应体（Base64编码）
curl -H "X-Response-Body: eyJtc2ciOiJoZWxsbyJ9" http://localhost:4444/api/echo

# 下载响应内容
curl -H "X-Response-Download: data.txt" http://localhost:4444/api/echo -OJ
```

**响应结构**：

```
{
  "method": "POST",
  "url": "http://localhost:4444/api/echo",
  "headers": [
    {"key": "Content-Type", "value": "application/json"},
    ...
  ],
  "body": "Hello World"
}
```

#### 3.2 `/api/sse/echo`（SSE流式接口）

[](#32-apisseechosse流式接口)

**功能**：Server-Sent Events流式回显，适合前端流式消费。

**特性**：

* 支持所有HTTP方法
* 返回SSE流，每条消息为JSON
* 支持自定义响应参数
* 支持流式数据推送

**额外参数**：

* `X-Response-Sse-Count`：SSE消息条数，默认100
* `X-Response-Sleep`：每条SSE消息间隔（毫秒），默认500

**用法示例**：

```
# 基本SSE请求
curl http://localhost:4444/api/sse/echo

# POST带body
curl -X POST -d 'Hello SSE' http://localhost:4444/api/sse/echo

# 控制SSE消息条数和间隔
curl -H "X-Response-Sse-Count: 5" -H "X-Response-Sleep: 1000" http://localhost:4444/api/sse/echo

# SSE上传文件
curl -X POST -F 'file=@/path/to/file' http://localhost:4444/api/sse/echo
```

#### 3.3 `/api/ws/echo`（WebSocket接口）

[](#33-apiwsechowebsocket接口)

**功能**：WebSocket流式回显，适合前端WebSocket流式消费。

**特性**：

* 支持WebSocket协议，升级连接后推送多条消息
* 支持所有HTTP方法（WebSocket仅升级GET，其他方法通过header传递）
* 支持自定义响应参数

**额外参数**：

* `X-Response-Websocket-Count`：WebSocket消息条数，默认100
* `X-Response-Sleep`：每条消息间隔（毫秒），默认500

**用法示例**：

```
# WebSocket基本请求（需WebSocket客户端）
wscat -c ws://localhost:4444/api/ws/echo

# 控制消息条数和间隔
wscat -c "ws://localhost:4444/api/ws/echo?X-Response-Websocket-Count=5&X-Response-Sleep=1000"

# WebSocket自定义响应内容（Base64）
wscat -c "ws://localhost:4444/api/ws/echo?X-Response-Body=eyJtc2ciOiJoZWxsbyB3cyJ9"
```

#### 3.4 自定义数据队列接口

[](#34-自定义数据队列接口)

**`POST /api/sse/set`**：设置SSE响应的消息队列 **`POST /api/ws/set`**：设置WebSocket响应的消息队列

**功能**：预设响应数据，实现自定义流式推送。

**请求体格式**：

```
[
  {"value": {"v": 1, "data": "mydata"}},
  {"value": {"v": 2, "data": 123}},
  {"value": "mydata"},
  {"value": null},
  {"value": 123}
]
```

#### 3.5 响应模式控制

[](#35-响应模式控制)

通过请求头 `X-Response-Mode` 控制SSE/WS响应行为：

* `default`（默认）：原有回显逻辑，自动回显请求内容
* `user`：从预设队列中依次取出value作为响应体
* `react`：连接建立后等待用户推送数据（WebSocket专用）

**用法示例**：

```
# 设置SSE队列
curl -X POST -H "Content-Type: application/json" \
  -d '[{"value":{"v":1,"data":"mydata"}}, {"value":{"v":2,"data":123}}]' \
  http://localhost:4444/api/sse/set

# SSE user模式消费
curl -H "X-Response-Mode: user" http://localhost:4444/api/sse/echo

# 设置WS队列
curl -X POST -H "Content-Type: application/json" \
  -d '[{"value":{"v":1,"data":"mydata"}}, {"value":{"v":2,"data":123}}]' \
  http://localhost:4444/api/ws/set

# WS user模式消费
wscat -c "ws://localhost:4444/api/ws/echo?X-Response-Mode=user"
```

### 4. HTTP CONNECT 代理隧道支持

[](#4-http-connect-代理隧道支持)

**功能**：支持 HTTP CONNECT 方法，可作为 HTTPS/SSH 等协议的代理隧道。

* 可直接作为 curl、ssh、ncat 等工具的 HTTP 代理服务器。
* 通过 CONNECT 建立 TCP 隧道，支持 HTTPS、WebSocket、SSH 等协议的转发。
* 适合企业内网、开发测试等需要代理隧道的场景。

**用法示例**：

```
# curl 通过 HTTP 代理访问 HTTPS 站点
curl -k -x http://localhost:4444 https://www.example.com

# ssh 通过 HTTP 代理
ssh -o "ProxyCommand ncat --proxy 127.0.0.1:4444 --proxy-type http %h %p" user@host
```

* 该功能无需额外配置，服务启动后自动支持。
* 日志中会记录 CONNECT 隧道的建立与关闭。

***

## 🎨 前端高级功能

[](#-前端高级功能)

* **📊 接口历史**：自动保存最近 50 条请求历史，支持一键加载、导入导出、清空
* **📚 接口集合**：支持多集合管理，接口保存、导入导出、删除
* **🔧 变量管理**：支持变量定义与替换，便于环境切换
* **🎛️ 全局请求头**：支持全局头配置，自动合并到每次请求
* **⚙️ 请求配置**：支持 SSL 验证、重定向、超时、重试、缓存、mode、credentials、referrerPolicy 等高级 fetch 选项
* **💾 导入导出**：支持全部配置一键导入导出，便于迁移和备份

***

## 🔍 常见问题

[](#-常见问题)

### ❓ 为什么需要后端转发？

[](#-为什么需要后端转发)

> 由于浏览器同源策略，前端直接请求第三方接口会遇到 CORS 限制。通过本工具的后端转发，前端只需请求本地服务即可，后端再代为请求目标接口，绕过跨域限制。

### ❓ 如何上传多个文件？

[](#-如何上传多个文件)

> 在前端选择 `form-data`，每个文件都可单独选择，支持多文件上传。后端会自动处理。

### ❓ 如何保存上传的文件到指定目录？

[](#-如何保存上传的文件到指定目录)

> 启动时通过 `--upload-dir=/your/path` 参数指定目录，form-data上传的文件会自动保存到该目录（存在则覆盖）。目录需提前创建并有写权限。

### ❓ 如何自定义请求头？

[](#-如何自定义请求头)

> 在前端"请求头"标签页添加即可，支持变量替换。

### ❓ 如何切换为直接请求（不走代理）？

[](#-如何切换为直接请求不走代理)

> 只需关闭后端服务或修改 `/api/mode` 返回内容，前端会自动切换为直连模式。

### ❓ 数据安全吗？

[](#-数据安全吗)

> 所有数据仅存储在浏览器本地（localStorage），不会上传到任何服务器。企业内网、敏感环境使用无忧。

### ❓ 支持哪些平台？

[](#-支持哪些平台)

> 支持Windows、Linux、MacOS、ARM架构，包括国产信创平台。一次编译，到处运行。同时完美支持IPv4和IPv6网络协议。

### ❓ 源码有多复杂？

[](#-源码有多复杂)

> 整个项目仅包含2个文件：`index.html`（前端界面）和`main.go`（后端服务），代码结构极其简洁，易于理解和维护。

### ❓ 支持哪些通信协议？

[](#-支持哪些通信协议)

> 除了传统的HTTP/HTTPS请求，还原生支持WebSocket（双向通信）和SSE（Server-Sent Events，单向实时推送），满足各种实时通信需求。

### ❓ EchoServer有什么用？

[](#-echoserver有什么用)

> EchoServer提供完整的请求回显和响应控制功能，适合接口调试、自动化测试、网络延迟模拟等场景。支持多种响应格式和流式通信。

### ❓ 如何关闭EchoServer？

[](#-如何关闭echoserver)

> 启动时添加 `--echo-server=false` 参数即可关闭EchoServer调试服务。

### ❓ 如何开启静态文件服务器模式？

[](#-如何开启静态文件服务器模式)

> 使用 `--webroot` 参数启动静态文件服务器模式。所有API接口将失效，变成一个纯静态文件服务器。

### ❓ 静态文件服务器支持哪些文件类型？

[](#-静态文件服务器支持哪些文件类型)

> 支持所有常见文件类型：HTML、CSS、JS、图片（PNG/JPG/GIF/SVG）、音频（MP3/WAV）、视频（MP4）、字体文件、PDF、压缩包等。会自动设置正确的MIME类型。

***

## 🤝 贡献与反馈

[](#-贡献与反馈)

* 🐛 欢迎提交 issue 或 PR，完善功能和文档。
* 💡 如有建议或 bug，欢迎反馈！

***

## 📄 License

[](#-license)

MIT

***

如需进一步定制或有疑问，欢迎联系作者。

***

**⭐ 如果这个项目对你有帮助，请给我们一个Star！**

**💬 有任何问题或建议，欢迎在GitHub上讨论！**

***

*让API调试变得简单而优雅* ✨


