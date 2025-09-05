---
title: "Visual Story-Writing: 利用视觉化手段重塑故事创作的AI工具"
slug: visual-story-writing-ai-tool
description: |
  Visual Story-Writing是一个创新的AI工具，通过操控故事的视觉表现来创作故事。利用GPT-4o，它能够自动化可视化故事情节、角色及其动作，用户可通过动态操作迅速编辑文本，以重塑故事的构架和细节。
tags: 
  - AI
  - writing
pubDatetime: 2025-09-05T17:17:01+08:00
ogImage: https://opengraph.githubassets.com/3263b992615dc06d87b5f5504fbf6f81d506ab93631f4f93c684c33b72a70d64/m-damien/VisualStoryWriting
---

[原文链接](https://github.com/m-damien/VisualStoryWriting?tab=readme-ov-file)

---

# Visual Story-Writing: Writing by Manipulating Visual Representations

[](#visual-story-writing-writing-by-manipulating-visual-representations)

[![](/m-damien/VisualStoryWriting/raw/main/demo.gif)](https://github.com/m-damien/VisualStoryWriting/blob/main/demo.gif)[![demo.gif](https://github.com/m-damien/VisualStoryWriting/raw/main/demo.gif) ](https://github.com/m-damien/VisualStoryWriting/blob/main/demo.gif)     [](https://github.com/m-damien/VisualStoryWriting/blob/main/demo.gif)

## [Online Demo](https://damienmasson.com/VisualStoryWriting) / [How to build](#how-to-build-and-run) / [Publication](#publication)

[](#online-demo--how-to-build--publication)

This system automatically **visualizes** a story (chronological events, character and their actions and movements) and allows users to **edit** the story by manipulating these visual representations. For example:

* Hover over the timeline allows reviewing the chronology of events and visualizing the movements of the characters
* Connecting two characters suggests edits to the text to reflect the new interaction
* Moving a character suggests edits to the text to reflect the new position
* Reordering the events in the timeline suggests edits to the text to reflect the new chronology

The system relies on a GPT-4o to extract the information from the text and suggest edits.

## How to build and run

[](#how-to-build-and-run)

The code is written in TypeScript and uses React and Vite. To build and run the code, you will need to have Node.js installed on your machine. You can download it [here](https://nodejs.org/en/download/). First install the dependencies:

```
npm install
```

Then build the code:

```
npm run dev
```

## How to use?

[](#how-to-use)

After entering your OpenAI API key, you can test Visual Story-Writing using the shortcuts or you can run the studies. Note that the system was tested and developped for recent versions of **Google Chrome** or **Mozilla Firefox**.

## How to get an OpenAI API key?

[](#how-to-get-an-openai-api-key)

Because Visual Story-Writing relies on the OpenAI API, you will need a key to make it work. You will need an account properly configured, see [here](https://platform.openai.com/account/api-keys) for more info. Your key is never stored and the application runs locally and sends requests to the OpenAI API only.

## Can I try without an API key?

[](#can-i-try-without-an-api-key)

The systen depends on the OpenAI API to work. If you enter an incorrect key, you will still be able to go through the study but executing prompts will yield an error.

## Where are the video tutorials?

[](#where-are-the-video-tutorials)

From the launcher, you can start the studies to see the exact ordering and video tutorials participants went through. Alternatively, you can go in the `public/videos` to review all the video tutorials.

## Publication

[](#publication)

Coming soon!

You can also find the paper on [arXiv](https://arxiv.org/abs/2410.07486)


