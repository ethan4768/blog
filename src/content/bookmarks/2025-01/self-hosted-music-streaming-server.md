---
title: "Black Candy：自托管的音乐流媒体服务器"
slug: self-hosted-music-streaming-server
description: |
  Black Candy 是一个自托管的音乐流媒体服务器，让您轻松构建个人音乐中心。通过 Docker 安装，并支持 PostgreSQL 数据库。您可以在移动设备上使用 Black Candy 访问您的音乐库，体验个人化的音乐流媒体服务。
tags: 
  - selfhosted
  - dev
  - tool
  - music
pubDatetime: 2025-01-03T20:11:59+08:00
ogImage: https://opengraph.githubassets.com/956486f10e685f450452b49dbb08caaf3984a58460147dc4d2472cc2d1bb400a/blackcandy-org/blackcandy
---

[原文链接](https://github.com/blackcandy-org/blackcandy?tab=readme-ov-file)

---

[![Black Candy logo](https://raw.githubusercontent.com/blackcandy-org/black_candy/master/app/assets/images/logo.svg)](https://raw.githubusercontent.com/blackcandy-org/black_candy/master/app/assets/images/logo.svg)

# Black Candy

[](#black-candy)

[![CI](https://github.com/blackcandy-org/black_candy/actions/workflows/ci.yml/badge.svg)](https://github.com/blackcandy-org/black_candy/actions/workflows/ci.yml) [![Coverage Status](https://camo.githubusercontent.com/8ca1d878ecb6847c9042ccf042ef27695f509adff2c9545fdf367f41a8869545/68747470733a2f2f636f766572616c6c732e696f2f7265706f732f6769746875622f626c61636b63616e64792d6f72672f626c61636b63616e64792f62616467652e7376673f6272616e63683d6d6173746572)](https://coveralls.io/github/blackcandy-org/black_candy?branch=master) [![Ruby Style Guide](https://camo.githubusercontent.com/5338a68a0f130dc684279ff3e42e45c9c74006018a1bdeaac76905979b3ccd49/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64655f7374796c652d7374616e646172642d627269676874677265656e2e737667)](https://github.com/testdouble/standard) [![Docker Pulls](https://camo.githubusercontent.com/35a0f5dee1d6ea31fe1f598aa4be82b94628bd1f322a60ef969788f300794243/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f626c61636b63616e64792f626c61636b63616e6479)](https://camo.githubusercontent.com/35a0f5dee1d6ea31fe1f598aa4be82b94628bd1f322a60ef969788f300794243/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f626c61636b63616e64792f626c61636b63616e6479)

[![Screenshot](https://raw.githubusercontent.com/blackcandy-org/blackcandy/master/docs/images/screenshot_main.png)](https://raw.githubusercontent.com/blackcandy-org/blackcandy/master/docs/images/screenshot_main.png)

Black Candy is a self-hosted music streaming server, your personal music center.

## Try The Demo

[](#try-the-demo)

Please visit <https://demo.blackcandy.org> and use demo user (email: <admin@admin.com>, password: foobar) to log in. And feel free to try it.

Note

This demo user does not have administrator privileges. So you cannot experience all the features in Black Candy. And all music in the demo are from [Free Music Archive](https://freemusicarchive.org/). You can check their [licenses](https://github.com/blackcandy-org/blackcandy/blob/master/docs/demo_music_licenses.md).

## Installation

[](#installation)

Black Candy uses docker image to install easily. You can run Black Candy like this.

```
docker run -p 3000:3000 ghcr.io/blackcandy-org/blackcandy:latest 

# Or pull from Docker Hub.
docker run -p 3000:3000 blackcandy/blackcandy:latest 
```

That's all. Now, you can access either <http://localhost:3000> or <http://host-ip:3000> in a browser, and use initial admin user to log in (email: <admin@admin.com>, password: foobar).

## Upgrade

[](#upgrade)

Important

If you upgrade to a major version, you need to read the upgrade guide carefully before upgrade. Because there are some breaking changes in a major version.

* See [V3 Upgrade](https://github.com/blackcandy-org/blackcandy/blob/master/docs/v3_upgrade.md) for upgrade from V2 release.
* See [Edge Upgrade](https://github.com/blackcandy-org/blackcandy/blob/master/docs/edge_upgrade.md) for upgrade from edge release to latest stable release.

Upgrade Black Candy is pull new image from remote. Then remove an old container and create a new one.

```
docker pull ghcr.io/blackcandy-org/blackcandy:latest
docker stop <your_blackcandy_container>
docker rm <your_blackcandy_container>
docker run <OPTIONS> ghcr.io/blackcandy-org/blackcandy:latest 
```

With docker compose, you can upgrade Black Candy like this:

```
docker pull ghcr.io/blackcandy-org/blackcandy:latest
docker-compose down
docker-compose up
```

## Mobile Apps

[](#mobile-apps)

Black Candy mobile apps are available in the following app stores:

[![Get it on App Store](https://raw.githubusercontent.com/blackcandy-org/ios/master/images/appstore_badge.png)](https://apps.apple.com/app/blackcandy/id6444304071) [![Get it on F-Droid](https://raw.githubusercontent.com/blackcandy-org/android/master/images/fdroid_badge.png)](https://f-droid.org/packages/org.blackcandy.android/)

For Android app, you can also download APK from [GitHub Release](https://github.com/blackcandy-org/android/releases/latest)

## Configuration

[](#configuration)

### Port Mapping

[](#port-mapping)

Black Candy exports the 3000 port. If you want to be able to access it from the host, you can use the `-p` option to map the port.

```
docker run -p 3000:3000 ghcr.io/blackcandy-org/blackcandy:latest
```

### Media Files Mounts

[](#media-files-mounts)

You can mount media files from host to container and use `MEDIA_PATH` environment variable to set the media path for black candy.

```
docker run -v /media_data:/media_data -e MEDIA_PATH=/media_data ghcr.io/blackcandy-org/blackcandy:latest   
```

### Use PostgreSQL As Database

[](#use-postgresql-as-database)

Black Candy use SQLite as database by default. Because SQLite can simplify the process of installation, and it's an ideal choice for self-hosted small server. If you think SQLite is not enough, or you are using some cloud service like heroku to host Black Candy, you can also use PostgreSQL as database.

```
docker run -e DB_ADAPTER=postgresql -e DB_URL=postgresql://yourdatabaseurl ghcr.io/blackcandy-org/blackcandy:latest 
```

### How to Persist Data

[](#how-to-persist-data)

All the data that need to persist in Black Candy are stored in `/app/storage`, So you can mount this directory to host to persist data.

```
mkdir storage_data

docker run -v ./storage_data:/app/storage ghcr.io/blackcandy-org/blackcandy:latest 
```

### Nginx To Send File

[](#nginx-to-send-file)

Black Candy supports use Nginx to delivery audio file to the client. It's a more effective way than handled by Black Candy backend. And Black Candy docker image is also ready for [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy), which means you can set up a Nginx proxy for Black Candy easily.

You can use docker-compose to set up those services. The docker-compose.yml file looks like this:

```
version: '3'

services:
  nginx-proxy:
    image: nginxproxy/nginx-proxy
    ports:
      - "80:80"
    volumes:
      - ./blackcandy.local:/etc/nginx/vhost.d/blackcandy.local:ro
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - /media_data:/media_data # Keep the path of media files in container the same as blackcandy container.

  app:
    image: ghcr.io/blackcandy-org/blackcandy:latest 
    volumes:
      - ./storage_data:/app/storage
      - /media_data:/media_data
    environment:
      VIRTUAL_HOST: blackcandy.local
      MEDIA_PATH: /media_data
      NGINX_SENDFILE: "true" # Don't forget to set `NGINX_SENDFILE` environment variable to true to enable nginx sendfile.
```

```
# Get the default sendfile config for blackcandy. This file need to mount to nginx proxy container to add custom configuration for nginx.
curl https://raw.githubusercontent.com/blackcandy-org/blackcandy/v3.0.0/config/nginx/sendfile.conf > blackcandy.local

docker-compose up
```

### Logging

[](#logging)

Black Candy logs to `STDOUT` by default. So if you want to control the log, Docker already supports a lot of options to handle the log in the container. See: <https://docs.docker.com/config/containers/logging/configure/>.

## Environment Variables

[](#environment-variables)

| Name              | Default  | Description                                                                                                                                                                                                                                                                                     |
| ----------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DB\_URL           |          | The URL of PostgreSQL database. You must set this environment variable if you use PostgreSQL as database.                                                                                                                                                                                       |
| MEDIA\_PATH       |          | You can use this environment variable to set media path for Black Candy, otherwise you can set media path in settings page.                                                                                                                                                                     |
| DB\_ADAPTER       | "sqlite" | There are two adapters are supported, "sqlite" and "postgresql".                                                                                                                                                                                                                                |
| NGINX\_SENDFILE   | false    | Whether enable Nginx sendfile.                                                                                                                                                                                                                                                                  |
| SECRET\_KEY\_BASE |          | When the SECRET\_KEY\_BASE environment variable is not set, Black candy will generate SECRET\_KEY\_BASE environment variable every time when service start up. This will cause old sessions invalid, You can set your own SECRET\_KEY\_BASE environment variable on docker service to avoid it. |
| FORCE\_SSL        | false    | Force all access to the app over SSL.                                                                                                                                                                                                                                                           |
| DEMO\_MODE        | false    | Whether to enable demo mode, when demo mode is on, all users cannot access administrator privileges, even user is admin. And also users cannot change their profile.                                                                                                                            |

## Edge Version

[](#edge-version)

The edge version of Black Candy base on master branch, which means it's not stable, you may encounter data loss or other issues. However, I don't recommend normal user using an edge version. But if you are a developer who wants to test or contribute to Black Candy, you can use the edge version.

```
docker pull ghcr.io/blackcandy-org/blackcandy:edge
```

## Development

[](#development)

### Requirements

[](#requirements)

* Ruby 3.3
* Node.js 20
* libvips
* FFmpeg

Make sure you have installed all those dependencies.

### Install gem dependencies

[](#install-gem-dependencies)

```
bundle install
```

### Install JavaScript dependencies

[](#install-javascript-dependencies)

```
npm install
```

### Database Configuration

[](#database-configuration)

```
rails db:prepare
rails db:seed
```

### Start all services

[](#start-all-services)

After you’ve set up everything, now you can run `./bin/dev` to start all services you need to develop. Then visit <http://localhost:3000> use initial admin user to log in (email: <admin@admin.com>, password: foobar).

### Running tests

[](#running-tests)

```
# Running all test
$ rails test:all 

# Running lint
$ rails lint:all
```

## Integrations

[](#integrations)

Black Candy support get artist and album image from Discogs API. You can create an API token from Discogs and set Discogs token on Setting page to enable it.

## Sponsorship

[](#sponsorship)

This project is supported by:

[![](https://camo.githubusercontent.com/6fbfffc4bceb6b40e0f244330c13a2671e243a7c9e849033e20869b6445910a5/68747470733a2f2f6f70656e736f757263652e6e7963332e63646e2e6469676974616c6f6365616e7370616365732e636f6d2f6174747269627574696f6e2f6173736574732f5356472f444f5f4c6f676f5f686f72697a6f6e74616c5f626c75652e737667)](https://www.digitalocean.com/) [![](https://camo.githubusercontent.com/61be5a726132ae9b0cd6c732c6b20acf80fde151b7530c9b798a7517c6d2f6dd/68747470733a2f2f7265736f75726365732e6a6574627261696e732e636f6d2f73746f726167652f70726f64756374732f636f6d70616e792f6272616e642f6c6f676f732f6a625f7371756172652e737667)](https://www.jetbrains.com/community/opensource)


