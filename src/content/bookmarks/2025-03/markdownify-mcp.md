---
title: "Markdownify MCP: 将多种格式转换为Markdown的强大工具"
slug: markdownify-mcp
description: |
  Markdownify是一个Model Context Protocol (MCP)服务器，能够将多种文件类型和网页内容转换为Markdown格式。支持PDF、图像、音频、DOCX等文件，以及YouTube视频和网页内容，方便用户快速获取可分享的文本内容。
tags: 
  - AI
  - tool
  - markdown
  - dev
  - opensource
pubDatetime: 2025-03-06T15:38:01+08:00
ogImage: https://opengraph.githubassets.com/faaf223c38c522a49c91ca5ea760c2d704bbb42e19b57e663932b405d01dc898/zcaceres/markdownify-mcp
---

[原文链接](https://github.com/zcaceres/markdownify-mcp)

---

# Markdownify MCP Server

[](#markdownify-mcp-server)

Markdownify is a Model Context Protocol (MCP) server that converts various file types and web content to Markdown format. It provides a set of tools to transform PDFs, images, audio files, web pages, and more into easily readable and shareable Markdown text.

[![Markdownify Server MCP server](https://camo.githubusercontent.com/265a89790d12652eaa816421dbc6cc76451746a605537fd3ec879265ffd79253/68747470733a2f2f676c616d612e61692f6d63702f736572766572732f626e35713462306574742f6261646765)](https://glama.ai/mcp/servers/bn5q4b0ett)

## Features

[](#features)

* Convert multiple file types to Markdown:

  * PDF
  * Images
  * Audio (with transcription)
  * DOCX
  * XLSX
  * PPTX

* Convert web content to Markdown:

  * YouTube video transcripts
  * Bing search results
  * General web pages

* Retrieve existing Markdown files

## Getting Started

[](#getting-started)

1. Clone this repository

2. Install dependencies:

   ```
   pnpm install
   ```

Note: this will also install `uv` and related Python depdencies.

3. Build the project:

   ```
   pnpm run build
   ```

4. Start the server:

   ```
   pnpm start
   ```

## Development

[](#development)

* Use `pnpm run dev` to start the TypeScript compiler in watch mode
* Modify `src/server.ts` to customize server behavior
* Add or modify tools in `src/tools.ts`

## Usage with Desktop App

[](#usage-with-desktop-app)

To integrate this server with a desktop app, add the following to your app's server configuration:

```
{
  "mcpServers": {
    "markdownify": {
      "command": "node",
      "args": [
        "{ABSOLUTE PATH TO FILE HERE}/dist/index.js"
      ],
      "env": {
        // By default, the server will use the default install location of `uv`
        "UV_PATH": "/path/to/uv"
      }
    }
  }
}
```

## Available Tools

[](#available-tools)

* `youtube-to-markdown`: Convert YouTube videos to Markdown
* `pdf-to-markdown`: Convert PDF files to Markdown
* `bing-search-to-markdown`: Convert Bing search results to Markdown
* `webpage-to-markdown`: Convert web pages to Markdown
* `image-to-markdown`: Convert images to Markdown with metadata
* `audio-to-markdown`: Convert audio files to Markdown with transcription
* `docx-to-markdown`: Convert DOCX files to Markdown
* `xlsx-to-markdown`: Convert XLSX files to Markdown
* `pptx-to-markdown`: Convert PPTX files to Markdown
* `get-markdown-file`: Retrieve an existing Markdown file

## Contributing

[](#contributing)

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[](#license)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/zcaceres/markdownify-mcp/blob/main/LICENSE) file for details.


