---
title: "VERT: 下一代开源文件转换器，永远免费并完全本地化"
slug: next-generation-file-converter
description: |
  VERT 是一种新一代文件转换工具，利用 WebAssembly 实现文件的本地转换，保证了隐私和安全。它支持多种文件格式，提供用户友好的界面，适合所有需要高效文件转换的用户。
tags: 
  - AI
  - tool
  - opensource
  - conversion
  - webdev
pubDatetime: 2025-04-15T09:51:49+08:00
ogImage: https://opengraph.githubassets.com/82e258574cf0c2df458b7de6c9c9aa4613c3c3cea78ac9ebfb03beafc999d591/VERT-sh/VERT
---

[原文链接](https://github.com/VERT-sh/VERT)

---

[![VERT's logo](https://private-user-images.githubusercontent.com/62841684/410688165-bf441748-0ec5-4c8a-b3e5-11301ee3f0bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ2ODIxOTQsIm5iZiI6MTc0NDY4MTg5NCwicGF0aCI6Ii82Mjg0MTY4NC80MTA2ODgxNjUtYmY0NDE3NDgtMGVjNS00YzhhLWIzZTUtMTEzMDFlZTNmMGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA0MTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNDE1VDAxNTEzNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNlZmViZjNmN2YxNjcwYzJkMjkxOTRiYmM1MjMyNzYwMDg2MGNjYmQwNDZmMzRlMGM5MjNlYTRhMTYwNjZiYTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Ae82rB9V_QiEBMmsUWgowWf69X1DaYvDXxV0-S2utys)](https://private-user-images.githubusercontent.com/62841684/410688165-bf441748-0ec5-4c8a-b3e5-11301ee3f0bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ2ODIxOTQsIm5iZiI6MTc0NDY4MTg5NCwicGF0aCI6Ii82Mjg0MTY4NC80MTA2ODgxNjUtYmY0NDE3NDgtMGVjNS00YzhhLWIzZTUtMTEzMDFlZTNmMGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA0MTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNDE1VDAxNTEzNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNlZmViZjNmN2YxNjcwYzJkMjkxOTRiYmM1MjMyNzYwMDg2MGNjYmQwNDZmMzRlMGM5MjNlYTRhMTYwNjZiYTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Ae82rB9V_QiEBMmsUWgowWf69X1DaYvDXxV0-S2utys)

# [VERT.sh](https://vert.sh)

[](#vertsh)

VERT is a file conversion utility that uses WebAssembly to convert files on your device instead of a cloud. Check out the live instance at [vert.sh](https://vert.sh).

VERT is built in Svelte and TypeScript.

## Features

[](#features)

* Convert files directly on your device using WebAssembly \*
* No file size limits
* Supports multiple file formats
* User-friendly interface built with Svelte

\* Non-local video conversion is available with our official instance, but the [daemon](https://github.com/VERT-sh/vertd) is easily self-hostable to maintain privacy and fully local functionality.

## Getting Started

[](#getting-started)

### Prerequisites

[](#prerequisites)

Make sure you have the following installed:

* [Bun](https://bun.sh/)

### Installation

[](#installation)

```
# Clone the repository
git clone https://github.com/VERT-sh/vert.git
cd vert
# Install dependencies
bun i
```

### Running Locally

[](#running-locally)

To run the project locally, run `bun dev`.

This will start a development server. Open your browser and navigate to `http://localhost:5173` to see the application.

### Building for Production

[](#building-for-production)

Before building for production, make sure you create a `.env` file in the root of the project with the following content:

```
PUB_HOSTNAME=example.com # change to your domain, only gets used for Plausible (for now)
PUB_PLAUSIBLE_URL=https://plausible.example.com # can be empty if not using Plausible
PUB_ENV=production # "production", "development" or "nightly"
```

To build the project for production, run `bun run build`

This will build the site to the `build` folder. You should then use a web server like [nginx](https://nginx.org) to serve the files inside that folder.

If using nginx, you can use the [nginx.conf](https://github.com/VERT-sh/VERT/blob/main/nginx.conf) file as a starting point. Make sure you keep [cross-origin isolation](https://web.dev/articles/cross-origin-isolation-guide) enabled.

### With Docker

[](#with-docker)

Clone the repository, then build a Docker image with:

```
$ docker build -t VERT-sh/vert \
	--build-arg PUB_ENV=production \
	--build-arg PUB_HOSTNAME=vert.sh \
	--build-arg PUB_PLAUSIBLE_URL=https://plausible.example.com .
```

You can then run it by using:

```
$ docker run --restart unless-stopped -p 3000:3000 -d --name "vert" VERT-sh/vert
```

We also have a `docker-compose.yml` file available. Use `docker compose up` if you want to start the stack, or `docker compose down` to bring it down. You can pass `--build` to `docker compose up` to rebuild the Docker image (useful if you've changed any of the environment variables) as well as `-d` to start it in detached mode. You can read more about Docker Compose in general [here](https://docs.docker.com/compose/intro/compose-application-model/).

## License

[](#license)

This project is licensed under the AGPL-3.0 License, please see the [LICENSE](https://github.com/VERT-sh/VERT/blob/main/LICENSE) file for details.


