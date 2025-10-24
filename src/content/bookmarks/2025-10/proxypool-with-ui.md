---
title: "ProxyPoolWithUI：多功能现代代理池及管理系统"
slug: proxypool-with-ui
description: |
  ProxyPoolWithUI是一个基于Nuxt 3和Vue 3构建的现代化代理池管理系统，支持自动爬取、实时验证、Clash和V2Ray订阅、API管理等多项功能。系统提供安全的JWT认证机制与用户界面，支持多种代理协议，适合生产环境部署和使用。
tags: 
  - dev
  - opensource
  - proxy
pubDatetime: 2025-10-24T13:54:15+08:00
ogImage: https://opengraph.githubassets.com/b7fc9b7c0689f8b6bd9d6af4155a494f5fa0b5310ca3b6e1c444cd67aaa00a71/huppugo1/ProxyPoolWithUI
---

[原文链接](https://github.com/huppugo1/ProxyPoolWithUI)

---

# ProxyPool With UI

[](#proxypool-with-ui)

一个功能完善的代理池系统，带有现代化的 Web 管理界面，支持多种代理协议和 Clash 订阅。

[![term](/huppugo1/ProxyPoolWithUI/raw/main/docs/term.png)](https://github.com/huppugo1/ProxyPoolWithUI/blob/main/docs/term.png)

## ✨ 核心特性

[](#-核心特性)

* 🎯 **自动爬取** - 从 14+ 个免费代理源自动爬取代理
* ✅ **自动验证** - 实时验证代理可用性，只返回可用代理
* 🌐 **多协议支持** - HTTP、HTTPS、SOCKS4、SOCKS5
* 🎨 **现代化 UI** - 基于 Nuxt 3 + Vue 3 + Ant Design Vue
* ⚡ **Clash 订阅** - 一键导入 Clash，支持 50+ 国家节点筛选
* 🚀 **V2Ray 订阅** - 支持 V2Ray 客户端，Base64 编码格式
* 🔐 **安全订阅链接** - JWT加密的订阅链接，支持临时和永久链接
* 📋 **订阅管理** - 统一管理所有生成的订阅链接，支持刷新和删除
* 🔄 **实时监控** - 代理状态、爬取器状态实时展示
* 📍 **地理位置** - 自动识别代理 IP 归属地（国家/城市）
* 🛠️ **手动添加** - 支持手动添加自有代理
* 🔐 **登录鉴权** - JWT Token 认证，保护管理接口安全
* 🔒 **单实例运行** - 防止多实例冲突，确保数据一致性
* ⚙️ **API管理** - 支持禁用/启用特定API接口，状态持久化保存

## 🚀 快速开始

[](#-快速开始)

### 方式一：本地运行

[](#方式一本地运行)

```
# 1. 克隆项目
git clone https://github.com/huppugo1/ProxyPoolWithUI.git
cd ProxyPoolWithUI

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置安全设置（重要！）
python setup_security.py

# 4. 启动服务
python main.py
```

> **🔐 安全提示**: 首次运行前必须配置 JWT 密钥！运行 `python setup_security.py` 进行安全配置。

### 方式二：Docker 运行

[](#方式二docker-运行)

#### 快速开始

[](#快速开始)

**临时运行（数据不持久化）**

```
docker run -d \
  --name proxy-pool \
  -p 5000:5000 \
  ghcr.io/huppugo1/proxypoolwithui:latest
```

> ⚠️ **注意**: 容器删除后数据会丢失，仅适用于测试

**持久化运行（推荐）**

```
docker run -d \
  --name proxy-pool \
  -p 5000:5000 \
  -v $(pwd)/data:/proxy/data \
  ghcr.io/huppugo1/proxypoolwithui:latest
```

#### 数据持久化配置

[](#数据持久化配置)

**1. 使用绝对路径（推荐）**

```
# 创建数据目录
mkdir -p /home/yourusername/proxy-data

# 运行容器
docker run -d \
  --name proxy-pool \
  -p 5000:5000 \
  -v /home/yourusername/proxy-data:/proxy/data \
  ghcr.io/huppugo1/proxypoolwithui:latest
```

> ✅ **优势**: 路径明确，便于管理和备份

**2. 使用相对路径**

```
# 进入项目目录
cd /path/to/your/project

# 创建数据目录
mkdir -p ./data

# 运行容器
docker run -d \
  --name proxy-pool \
  -p 5000:5000 \
  -v ./data:/proxy/data \
  ghcr.io/huppugo1/proxypoolwithui:latest
```

> ✅ **优势**: 便于项目迁移，路径相对简单

**3. 使用Docker命名卷**

```
docker run -d \
  --name proxy-pool \
  -p 5000:5000 \
  -v proxy-data:/proxy/data \
  ghcr.io/huppugo1/proxypoolwithui:latest
```

> ✅ **优势**: Docker自动管理，适合生产环境

#### 完整部署示例

[](#完整部署示例)

```
# 1. 创建数据目录
mkdir -p ./data

# 2. 运行容器（生产环境配置）
docker run -d \
  --name proxy-pool \
  -p 5000:5000 \
  -v $(pwd)/data:/proxy/data \
  --restart unless-stopped \
  --memory=512m \
  --cpus=1.0 \
  ghcr.io/huppugo1/proxypoolwithui:latest

# 3. 验证部署
echo "等待服务启动..."
sleep 10

# 检查容器状态
docker ps | grep proxy-pool

# 查看数据目录
ls -la ./data/

# 查看服务日志
docker logs -f proxy-pool

# 测试API接口
curl http://localhost:5000/api/proxies
```

#### 常用管理命令

[](#常用管理命令)

```
# 查看容器状态
docker ps -a | grep proxy-pool

# 查看实时日志
docker logs -f proxy-pool

# 停止容器
docker stop proxy-pool

# 启动容器
docker start proxy-pool

# 重启容器
docker restart proxy-pool

# 删除容器（保留数据）
docker rm proxy-pool

# 删除容器和数据
docker rm -v proxy-pool
```

#### 数据备份与恢复

[](#数据备份与恢复)

```
# 备份数据
tar -czf proxy-data-backup-$(date +%Y%m%d).tar.gz ./data/

# 恢复数据
tar -xzf proxy-data-backup-20240101.tar.gz

# 迁移到新服务器
scp -r ./data/ user@new-server:/path/to/new/location/
```

国内用户可将镜像名替换为 `ghcr.nju.edu.cn/huppugo1/proxypoolwithui:latest`

启动成功后访问：**<http://localhost:5000/web>**

> 💡 首次启动需要等待 5-10 分钟让系统爬取和验证代理

### 默认登录账户

[](#默认登录账户)

* **用户名**: `admin`
* **密码**: `admin123`

> ⚠️ **重要提示**: 首次登录后请立即修改默认密码！

## 🔐 登录鉴权

[](#-登录鉴权)

系统已集成 JWT Token 认证机制，所有管理接口均需要登录后才能访问。

### 认证流程

[](#认证流程)

1. **登录获取 Token**

   ```
   curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "admin123"}'
   ```

   返回示例：

   ```
   {
     "success": true,
     "message": "登录成功",
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "user": {
       "username": "admin",
       "role": "admin"
     }
   }
   ```

2. **使用 Token 访问接口**

   ```
   curl http://localhost:5000/proxies_status \
     -H "Authorization: Bearer YOUR_TOKEN_HERE"
   ```

### 认证接口

[](#认证接口)

| 接口                      | 方法   | 说明       | 是否需要认证 |
| ----------------------- | ---- | -------- | ------ |
| `/auth/login`           | POST | 用户登录     | ❌      |
| `/auth/verify`          | GET  | 验证 Token | ✅      |
| `/auth/change_password` | POST | 修改密码     | ✅      |

### Token 说明

[](#token-说明)

* Token 有效期：24 小时（可在 `config.py` 中配置）
* Token 过期后需要重新登录
* 前端会自动处理 Token 过期跳转

### 修改默认密码

[](#修改默认密码)

登录后点击右上角用户名，选择"修改密码"即可修改。

或通过 API：

```
curl -X POST http://localhost:5000/auth/change_password \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"old_password": "admin123", "new_password": "your_new_password"}'
```

## 📡 API 接口

[](#-api-接口)

> ⚠️ **注意**: 除了 `/ping`、`/fetch_*`、`/clash*` 和 `/v2ray` 等代理获取接口外，其他管理接口均需要认证。

### 基础接口

[](#基础接口)

| 接口              | 说明             | 示例                                        |
| --------------- | -------------- | ----------------------------------------- |
| `/ping`         | 测试 API 状态      | `curl http://localhost:5000/ping`         |
| `/fetch_random` | 随机获取一个可用代理     | `curl http://localhost:5000/fetch_random` |
| `/fetch_all`    | 获取所有可用代理       | `curl http://localhost:5000/fetch_all`    |
| `/fetch_http`   | 获取一个 HTTP 代理   | `curl http://localhost:5000/fetch_http`   |
| `/fetch_https`  | 获取一个 HTTPS 代理  | `curl http://localhost:5000/fetch_https`  |
| `/fetch_socks5` | 获取一个 SOCKS5 代理 | `curl http://localhost:5000/fetch_socks5` |

### Clash 订阅接口

[](#clash-订阅接口)

| 接口               | 说明              | 参数                             |
| ---------------- | --------------- | ------------------------------ |
| `/clash`         | 获取 Clash 完整订阅配置 | `c`, `nc`, `protocol`, `limit` |
| `/clash/proxies` | 获取 Clash 代理节点列表 | `c`, `nc`, `protocol`, `limit` |

### V2Ray 订阅接口

[](#v2ray-订阅接口)

| 接口       | 说明                       | 参数                             |
| -------- | ------------------------ | ------------------------------ |
| `/v2ray` | 获取 V2Ray 订阅配置（Base64 编码） | `c`, `nc`, `protocol`, `limit` |

### 安全订阅接口（需要认证）

[](#安全订阅接口需要认证)

| 接口                                 | 说明                 | 参数                            |
| ---------------------------------- | ------------------ | ----------------------------- |
| `/generate_subscription_links`     | 生成加密的订阅链接          | `type`, `permanent`, `params` |
| `/subscribe/clash`                 | 使用加密token获取Clash配置 | `token`, `params`             |
| `/subscribe/v2ray`                 | 使用加密token获取V2Ray配置 | `token`, `params`             |
| `/subscription_links`              | 获取用户的订阅链接列表        | -                             |
| `/subscription_links/<id>`         | 删除指定订阅链接           | -                             |
| `/subscription_links/<id>/refresh` | 刷新订阅链接（重新生成token）  | -                             |

### API接口管理（需要认证）

[](#api接口管理需要认证)

| 接口                   | 说明              | 参数 |
| -------------------- | --------------- | -- |
| `/api_status`        | 获取所有API接口的启用状态  | -  |
| `/api_toggle/<path>` | 切换指定API的启用/禁用状态 | -  |

**参数说明：**

* `c` - 按国家筛选（如：`c=CN,US,JP`）
* `nc` - 排除指定国家（如：`nc=CN`）
* `protocol` - 筛选协议类型（`http`/`https`/`socks4`/`socks5`）
* `limit` - 限制返回数量（如：`limit=50`）

**支持的国家代码：** CN、HK、TW、US、CA、JP、SG、AU、RU、CH、DE、FR、GB、NL 等 50+ 个

**使用示例：**

```
# 获取所有代理
http://localhost:5000/clash
http://localhost:5000/v2ray

# 仅获取美国和日本的代理，限制 50 个
http://localhost:5000/clash?c=US,JP&limit=50
http://localhost:5000/v2ray?c=US,JP&limit=50

# 排除中国大陆的代理
http://localhost:5000/clash?nc=CN
http://localhost:5000/v2ray?nc=CN

# 仅获取 SOCKS5 代理
http://localhost:5000/clash?protocol=socks5
http://localhost:5000/v2ray?protocol=socks5
```

## 🎯 Clash 使用指南

[](#-clash-使用指南)

### 方法 A：直接订阅（推荐）

[](#方法-a直接订阅推荐)

1. 打开 Clash 客户端
2. 进入「配置」或「Profiles」
3. 添加订阅链接：`http://localhost:5000/clash`
4. 点击更新订阅并启用

### 方法 B：手动导入

[](#方法-b手动导入)

1. 访问：<http://localhost:5000/clash>
2. 复制返回的 YAML 配置
3. 在 Clash 中创建新配置文件并保存

### 支持的 Clash 客户端

[](#支持的-clash-客户端)

* ✅ Clash for Windows
* ✅ Clash for Android
* ✅ ClashX / ClashX Pro (macOS)
* ✅ Clash Premium
* ✅ Clash Meta / Mihomo

### 使用建议

[](#使用建议)

1. **定期更新** - 建议设置自动更新订阅（每 6 小时）
2. **限制数量** - 使用 `limit` 参数限制代理数量（推荐 20-50 个）
3. **自动测试** - 启用 Clash 自动测试，选择最快的代理
4. **节点名称** - 自动显示国家 emoji 和 IP（如：🇨🇳 中国+1.2.3.4）

## 🚀 V2Ray 使用指南

[](#-v2ray-使用指南)

### 方法 A：直接订阅（推荐）

[](#方法-a直接订阅推荐-1)

1. 打开 V2Ray 客户端（如 V2RayN、V2RayX、Qv2ray 等）
2. 进入「订阅」或「Subscription」
3. 添加订阅链接：`http://localhost:5000/v2ray`
4. 点击更新订阅并启用

### 方法 B：手动导入

[](#方法-b手动导入-1)

1. 访问：<http://localhost:5000/v2ray>
2. 复制返回的 Base64 编码内容
3. 在 V2Ray 客户端中导入订阅

## 🔐 安全订阅使用指南

[](#-安全订阅使用指南)

### 生成加密订阅链接

[](#生成加密订阅链接)

1. 登录管理界面：<http://localhost:5000/web>

2. 在首页点击「Clash 订阅」或「V2Ray 订阅」按钮

3. 选择订阅类型：

   * **临时链接**：1小时有效期，适合临时使用
   * **永久链接**：永久有效，直到用户被删除

4. 配置筛选参数（可选）：

   * 国家筛选：选择特定国家
   * 协议筛选：选择特定协议类型
   * 数量限制：限制代理数量

5. 点击「生成订阅链接」获取加密链接

### 使用加密订阅链接

[](#使用加密订阅链接)

**Clash 客户端：**

1. 复制生成的加密链接
2. 在 Clash 中添加订阅链接
3. 客户端会自动使用加密链接获取配置

**V2Ray 客户端：**

1. 复制生成的加密链接
2. 在 V2Ray 客户端中添加订阅
3. 客户端会自动解析加密链接

### 订阅管理

[](#订阅管理)

1. 访问「订阅管理」页面

2. 查看所有已生成的订阅链接

3. 支持的操作：

   * **复制链接**：快速复制订阅链接
   * **刷新链接**：重新生成token（保持原参数）
   * **删除链接**：删除不需要的订阅链接
   * **批量操作**：支持批量复制、刷新、删除

### 安全特性

[](#安全特性)

* **JWT 加密**：所有订阅链接使用 JWT 加密，确保安全性
* **参数保护**：筛选参数被加密保护，无法被篡改
* **用户隔离**：每个用户只能管理自己的订阅链接
* **自动过期**：临时链接自动过期，避免长期暴露

## ⚙️ API接口管理

[](#️-api接口管理)

### 管理API接口状态

[](#管理api接口状态)

系统支持禁用/启用特定的API接口，提供细粒度的接口控制。

#### 访问管理界面

[](#访问管理界面)

1. 登录管理界面：<http://localhost:5000/web>
2. 进入"API接口文档"页面
3. 展开"API接口管理"面板

#### 管理功能

[](#管理功能)

**单个接口管理：**

* 使用开关控件启用/禁用单个API
* 实时显示接口状态（绿色=启用，灰色=禁用）
* 支持按路径和分类搜索接口

**批量操作：**

* 全部启用：一键启用所有API接口
* 全部禁用：一键禁用所有API接口
* 刷新状态：重新加载接口状态

#### 接口分类

[](#接口分类)

* **认证接口**：登录、验证、修改密码等
* **代理接口**：获取代理相关接口
* **Clash接口**：Clash订阅相关接口
* **V2Ray接口**：V2Ray订阅相关接口
* **订阅接口**：安全订阅相关接口
* **管理接口**：系统管理相关接口

#### 状态持久化

[](#状态持久化)

* API状态保存在 `api_status.json` 文件中
* 重启服务后状态设置不会丢失
* 支持手动编辑配置文件

#### 安全特性

[](#安全特性-1)

* 禁用后的API返回403错误
* 错误信息包含明确的禁用提示
* 所有管理操作需要JWT认证

#### 使用示例

[](#使用示例)

```
# 获取所有API状态
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:5000/api_status

# 禁用特定API
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" http://localhost:5000/api_toggle/fetch_random

# 启用特定API
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" http://localhost:5000/api_toggle/fetch_random
```

### 支持的 V2Ray 客户端

[](#支持的-v2ray-客户端)

* ✅ V2RayN (Windows)
* ✅ V2RayX (macOS)
* ✅ Qv2ray (跨平台)
* ✅ V2RayNG (Android)
* ✅ Shadowrocket (iOS)
* ✅ ClashX (macOS)

### 代理格式说明

[](#代理格式说明)

V2Ray 订阅支持以下代理格式：

* **HTTP/HTTPS 代理** - 转换为 VMess 格式
* **SOCKS4/SOCKS5 代理** - 转换为 socks\:// 格式
* **认证信息** - 自动处理用户名密码认证

### 使用建议

[](#使用建议-1)

1. **定期更新** - 建议设置自动更新订阅（每 6 小时）
2. **限制数量** - 使用 `limit` 参数限制代理数量（推荐 20-50 个）
3. **协议选择** - 根据网络环境选择合适的协议类型
4. **节点测试** - 启用 V2Ray 自动测试，选择最快的代理

## 🐍 Python 使用示例

[](#-python-使用示例)

```
import requests

# 获取一个随机代理
proxy_uri = requests.get('http://localhost:5000/fetch_random').text

if proxy_uri:
    proxies = {'http': proxy_uri, 'https': proxy_uri}
    response = requests.get('https://www.example.com', proxies=proxies)
    print(response.text)
else:
    print('暂时没有可用代理')
```

## 📦 已集成的代理源

[](#-已集成的代理源)

| 名称          | 地址                                 | 备注       |
| ----------- | ---------------------------------- | -------- |
| 悠悠网络代理      | <https://uu-proxy.com/>            |          |
| 快代理         | <https://www.kuaidaili.com/>       |          |
| 全网代理        | <http://www.goubanjia.com/>        |          |
| 66代理        | <http://www.66ip.cn/>              |          |
| 云代理         | <http://www.ip3366.net/>           |          |
| 免费代理库       | <https://ip.jiangxianli.com/>      |          |
| 小幻HTTP代理    | <https://ip.ihuan.me/>             |          |
| 89免费代理      | <https://www.89ip.cn/>             |          |
| ProxyScan   | <https://www.proxyscan.io/>        |          |
| 开心代理        | <http://www.kxdaili.com/>          |          |
| 西拉代理        | <http://www.xiladaili.com/>        |          |
| 小舒代理        | <http://www.xsdaili.cn/>           |          |
| ProxyList   | <https://www.proxy-list.download/> |          |
| ProxyScrape | <https://proxyscrape.com/>         | 国内无法直接访问 |

## 📁 项目结构

[](#-项目结构)

```
ProxyPoolWithUI/
├── api/              # API 服务（Flask）
├── auth/             # 认证模块（JWT）
├── db/               # 数据库封装（SQLite）
├── fetchers/         # 代理爬取器
├── proc/             # 爬取和验证进程
├── frontend/         # Web 前端（Nuxt 3 + Vue 3）
├── utils/            # 工具类（IP 定位、单实例管理）
├── data/             # 数据目录（数据库、配置文件等）
│   ├── config.py     # 配置文件
│   ├── data.db       # SQLite 数据库
│   ├── users.json    # 用户数据
│   ├── api_status.json # API接口状态配置
│   └── sub.json      # 订阅链接存储
└── main.py           # 启动入口
```

## ⚙️ 配置说明

[](#️-配置说明)

大部分配置在 `data/config.py` 中，默认配置已经可以适应大部分情况。

### 数据目录结构

[](#数据目录结构)

所有数据文件和配置文件统一存放在 `data/` 目录下：

* **`data/config.py`** - 主配置文件，包含所有系统配置
* **`data/data.db`** - SQLite 数据库文件，存储代理数据
* **`data/users.json`** - 用户账户数据（用户名、密码哈希等）
* **`data/api_status.json`** - API接口启用/禁用状态配置
* **`data/sub.json`** - 生成的订阅链接存储

### 数据备份

[](#数据备份)

建议定期备份 `data/` 目录，包含所有重要的运行时数据：

```
# 备份数据目录
tar -czf proxypool_backup_$(date +%Y%m%d).tar.gz data/

# 恢复数据目录
tar -xzf proxypool_backup_20241019.tar.gz
```

### 主要配置项

[](#主要配置项)

* **验证超时时间** - 代理验证的超时设置
* **验证间隔** - 代理重新验证的时间间隔
* **爬取间隔** - 爬取器运行的时间间隔
* **数据库路径** - SQLite 数据库文件位置

### 认证配置

[](#认证配置)

在 `config.py` 中可以配置认证相关参数：

```
# JWT密钥 - 建议在生产环境使用环境变量
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-secret-key-change-it-in-production-2025')

# Token过期时间（小时）
TOKEN_EXPIRATION_HOURS = 24
```

生产环境建议设置环境变量：

```
export JWT_SECRET_KEY="your-very-strong-secret-key-here"
python main.py
```

## 🔧 高级功能

[](#-高级功能)

### 单实例运行保护

[](#单实例运行保护)

系统具备完善的单实例运行机制，防止多个实例同时运行：

* **端口占用检查** - 检测5000端口是否被占用
* **PID文件锁** - 在用户主目录创建PID文件记录进程ID
* **锁文件机制** - 创建包含时间戳的锁文件，支持过期清理
* **进程状态验证** - 验证PID对应的进程是否真实存在

如果检测到已有实例运行，系统会显示清理命令：

```
# Windows 清理命令
taskkill /f /im python.exe
del "%USERPROFILE%\.proxypoolwithui.pid"
del "%USERPROFILE%\.proxypoolwithui.lock"

# Linux/Unix 清理命令
pkill -f python.*main.py
rm -f ~/.proxypoolwithui.pid
rm -f ~/.proxypoolwithui.lock
```

### 添加自定义代理源

[](#添加自定义代理源)

详见：[fetchers/README.md](https://github.com/huppugo1/ProxyPoolWithUI/blob/main/fetchers/README.md)

### 自定义验证算法

[](#自定义验证算法)

详见：[db/README.md](https://github.com/huppugo1/ProxyPoolWithUI/blob/main/db/README.md)

### 前端开发指南

[](#前端开发指南)

详见：[frontend/src/README\_NUXT3.md](https://github.com/huppugo1/ProxyPoolWithUI/blob/main/frontend/src/README_NUXT3.md)

## 📊 工作流程

[](#-工作流程)

```
[代理源] → [爬取器] → [数据库] → [验证器] → [API] → [用户]
             ↓                      ↓
         [定时爬取]             [定时验证]
```

1. **爬取进程** - 定时从各代理源爬取代理，存入数据库
2. **验证进程** - 定时验证数据库中的代理是否可用
3. **API 服务** - 提供 HTTP 接口和 Web 界面

详细流程图：

[![workflow](/huppugo1/ProxyPoolWithUI/raw/main/docs/workflow.png)](https://github.com/huppugo1/ProxyPoolWithUI/blob/main/docs/workflow.png)

## 🔒 生产环境部署

[](#-生产环境部署)

### 安全检查清单

[](#安全检查清单)

在部署到生产环境之前，请确保完成以下安全检查：

#### 必须完成的项目

[](#必须完成的项目)

1. **JWT 密钥配置**

   * [ ] 修改默认 JWT 密钥
   * [ ] 使用环境变量存储密钥（推荐）
   * [ ] 密钥长度至少 32 位
   * [ ] 使用随机字符串作为密钥

   ```
   # 生成强密钥示例
   python -c "import secrets; print(secrets.token_urlsafe(32))"

   # 设置环境变量
   export JWT_SECRET_KEY="your-generated-secret-key"
   ```

2. **修改默认密码**

   * [ ] 首次登录后立即修改默认管理员密码
   * [ ] 新密码长度至少 8 位
   * [ ] 包含大小写字母、数字和特殊字符

3. **文件权限**

   ```
   chmod 600 users.json
   chmod 600 data.db
   ```

4. **网络安全**

   * [ ] 生产环境使用 HTTPS（必须）
   * [ ] 配置防火墙规则
   * [ ] 限制管理接口访问 IP（推荐）
   * [ ] 使用反向代理（Nginx/Apache）

### Nginx 反向代理配置

[](#nginx-反向代理配置)

```
server {
    listen 443 ssl http2;
    server_name your-domain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    # 安全头
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # 超时设置
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # 限制上传大小
    client_max_body_size 10M;
}

# HTTP 重定向到 HTTPS
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

### Systemd 服务配置

[](#systemd-服务配置)

创建 `/etc/systemd/system/proxypool.service`：

```
[Unit]
Description=ProxyPool Management System
After=network.target

[Service]
Type=simple
User=proxypool
WorkingDirectory=/path/to/ProxyPoolWithUI
Environment="JWT_SECRET_KEY=your-secret-key-here"
ExecStart=/usr/bin/python3 /path/to/ProxyPoolWithUI/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启动服务：

```
sudo systemctl daemon-reload
sudo systemctl enable proxypool
sudo systemctl start proxypool
sudo systemctl status proxypool
```

### Docker 部署安全配置

[](#docker-部署安全配置)

```
# 使用非 root 用户
RUN adduser --disabled-password --gecos '' proxypool
USER proxypool

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ping || exit 1
```

运行容器：

```
docker run -d \
  --name proxypool \
  -p 5000:5000 \
  -e JWT_SECRET_KEY="your-secret-key" \
  -v /path/to/data:/proxy \
  --restart unless-stopped \
  --read-only \
  --tmpfs /tmp \
  proxy_pool
```

## ❓ 常见问题

[](#-常见问题)

### Q: 没有可用代理？

[](#q-没有可用代理)

A: 首次启动需要等待 5-10 分钟。访问 <http://localhost:5000/web> 查看爬取和验证状态。

### Q: 代理不稳定？

[](#q-代理不稳定)

A: 免费代理质量参差不齐，建议：

* 使用 Clash 自动测试功能
* 定期更新订阅
* 使用 `limit` 参数限制数量

### Q: 如何禁用某个爬取器？

[](#q-如何禁用某个爬取器)

A: 在 Web 界面的「爬取器状态」页面中操作，或访问 API：

```
http://localhost:5000/fetcher_enable?name=爬取器名称&enable=0
```

### Q: 如何远程访问？

[](#q-如何远程访问)

A: 将 `localhost` 替换为服务器 IP，并确保防火墙允许 5000 端口。

### Q: Docker 容器如何持久化数据？

[](#q-docker-容器如何持久化数据)

A: 使用 `-v` 参数挂载数据目录：

```
docker run -p 5000:5000 -v /path/to/data:/proxy -d proxy_pool
```

### Q: 忘记密码怎么办？

[](#q-忘记密码怎么办)

A: 删除项目根目录下的 `users.json` 文件，重启服务会自动创建默认管理员账户。

### Q: 如何禁用登录认证？

[](#q-如何禁用登录认证)

A: 不建议禁用认证。如果确实需要，可以在 `api/api.py` 中移除需要保护接口的 `@token_required` 装饰器。

### Q: API 接口需要认证吗？

[](#q-api-接口需要认证吗)

A:

* **需要认证**：所有管理接口（代理状态、爬取器管理、添加代理、订阅管理等）
* **无需认证**：代理获取接口（`/fetch_*`、`/clash*`、`/v2ray`）和健康检查（`/ping`）
* **部分认证**：安全订阅接口（`/subscribe/clash`、`/subscribe/v2ray`）需要有效的JWT token

### Q: 支持哪些订阅格式？

[](#q-支持哪些订阅格式)

A:

* **Clash 订阅**：`/clash` - 返回 YAML 格式配置
* **V2Ray 订阅**：`/v2ray` - 返回 Base64 编码的代理链接
* **代理列表**：`/clash/proxies` - 仅返回 Clash 代理节点列表
* **安全订阅**：`/subscribe/clash`、`/subscribe/v2ray` - 使用JWT token的加密订阅

### Q: 提示"检测到已有实例在运行"？

[](#q-提示检测到已有实例在运行)

A: 系统具备单实例保护机制。如果确定没有其他实例运行，可以手动清理锁文件：

```
# Windows
del "%USERPROFILE%\.proxypoolwithui.pid"
del "%USERPROFILE%\.proxypoolwithui.lock"

# Linux/Mac
rm ~/.proxypoolwithui.pid
rm ~/.proxypoolwithui.lock
```

### Q: 如何修改 JWT 密钥？

[](#q-如何修改-jwt-密钥)

A: 生产环境建议使用环境变量：

```
export JWT_SECRET_KEY="your-very-strong-secret-key"
python main.py
```

### Q: 如何禁用特定的API接口？

[](#q-如何禁用特定的api接口)

A: 有两种方式：

1. **Web界面**：登录后进入"API接口文档"页面，展开"API接口管理"面板，使用开关控件管理
2. **API调用**：使用 `/api_toggle/<path>` 接口切换状态

### Q: API禁用状态保存在哪里？

[](#q-api禁用状态保存在哪里)

A: API状态保存在项目根目录的 `api_status.json` 文件中，重启服务后设置不会丢失。

### Q: 禁用的API会返回什么错误？

[](#q-禁用的api会返回什么错误)

A: 禁用的API会返回403状态码，错误信息为：`API接口 <path> 已被禁用`。

### Q: 如何批量管理API接口？

[](#q-如何批量管理api接口)

A: 在API管理界面中，可以使用"全部启用"和"全部禁用"按钮进行批量操作。

## 🛠️ 技术栈

[](#️-技术栈)

**后端：**

* Python 3.6+
* Flask - Web 框架
* SQLite - 数据库
* Requests - HTTP 库
* PyYAML - Clash 配置生成
* PyJWT - JWT 认证
* psutil - 进程管理

**前端：**

* Nuxt 3 - Vue 框架
* Vue 3 - JavaScript 框架
* TypeScript - 类型安全
* Ant Design Vue - UI 组件库
* Vite - 构建工具
* Axios - HTTP 客户端

## 🔐 安全配置

[](#-安全配置)

### JWT 密钥配置

[](#jwt-密钥配置)

ProxyPool 使用 JWT Token 进行身份认证，**必须配置强密钥**以确保系统安全。

#### 自动配置（推荐）

[](#自动配置推荐)

```
# 运行安全配置脚本，自动生成密钥并保存到 .env 文件
python setup_security.py
```

#### 手动配置

[](#手动配置)

1. **创建 .env 文件**：

   ```
   # 生成强密钥
   python -c "import secrets; print(secrets.token_urlsafe(32))"

   # 创建 .env 文件并添加密钥
   echo "JWT_SECRET_KEY=your-generated-secret-key" > .env
   ```

2. **编辑 .env 文件**：

   ```
   JWT_SECRET_KEY=your-strong-secret-key-here
   ```

#### 安全要求

[](#安全要求)

* ✅ 密钥长度至少 32 字符
* ✅ 使用随机生成的强密钥
* ❌ 禁止使用弱密钥（如：admin123、password、secret）
* ❌ 禁止将 .env 文件提交到版本控制

#### 验证配置

[](#验证配置)

```
# 检查配置是否正确
python -c "from config import JWT_SECRET_KEY; print('密钥长度:', len(JWT_SECRET_KEY))"
```

### 默认账户

[](#默认账户)

* **用户名**: `admin`
* **密码**: `admin123`
* **⚠️ 重要**: 首次登录后请立即修改密码！

## 📝 开发贡献

[](#-开发贡献)

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

[](#-许可证)

本项目采用 MIT 许可证 - 详见 [LICENSE](https://github.com/huppugo1/ProxyPoolWithUI/blob/main/LICENSE) 文件

## 🙏 致谢

[](#-致谢)

* 感谢所有免费代理源提供者
* 感谢开源社区的贡献者

***

**版本**: 2.0.2\
**更新时间**: 2025-10-19\
**状态**: ✅ 生产就绪

## 🔄 更新日志

[](#-更新日志)

### v2.0.2 (2025-10-19)

[](#v202-2025-10-19)

* 🔐 新增安全订阅链接功能
* 📋 订阅管理界面，支持链接的生成、刷新、删除
* 🔑 JWT加密的订阅链接，支持临时和永久链接
* 🛡️ 订阅参数加密保护，防止篡改
* 👥 用户隔离的订阅链接管理
* ⚙️ API接口管理功能，支持禁用/启用特定接口
* 💾 API状态持久化保存，重启后设置不丢失
* 🎨 优化前端界面，新增订阅管理和API管理页面
* 📁 重构数据目录结构，统一管理配置和数据文件
* 🧹 移除过时文档，优化项目结构

### v2.0.1 (2025-10-19)

[](#v201-2025-10-19)

* ✨ 新增 JWT Token 登录鉴权功能
* 🔐 所有管理接口添加认证保护
* 👤 用户管理：登录、修改密码
* 🎨 全新登录页面设计
* 🛡️ 自动 Token 刷新和过期处理
* 🔒 单实例运行保护机制
* 📝 完善的认证 API 文档
* 🧹 代码优化和文档合并

### v2.0.0

[](#v200)

* 初始版本发布


