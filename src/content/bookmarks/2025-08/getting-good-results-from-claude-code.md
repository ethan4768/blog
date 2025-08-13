---
title: "使用Claude Code获得优异结果的技巧"
slug: getting-good-results-from-claude-code
description: |
  在使用大型语言模型(LLM)编程代理的过程中，Claude Code成为我的最爱。通过编写清晰的规格说明、提供项目文档和进行代码审查，我成功地在短时间内完成了12个项目。尽管AI生成的代码可能存在问题，但我依然负责最终提交的代码质量。
tags: 
  - AI
  - dev
  - tool
  - LLM
pubDatetime: 2025-08-13T11:19:11+08:00
ogImage: https://www.dzombak.com/content/images/2025/08/Designer-7.jpeg
---

[原文链接](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/)

---

Posted 08 Aug 2025 in [AI](https://www.dzombak.com/blog/tag/ai/)

I’ve been experimenting with LLM programming agents over the past few months. Claude Code has become my favorite.

It is not without issues, but it’s allowed me to write \~12 programs/projects in relatively little time, and I feel I would not have been able to do all this in the same amount of time without it. Most of them, I wouldn’t even have bothered to write without Claude Code, simply because they’d take too much of my time. (A list is included at the end of this post.)

I’m still far from a Claude Code expert, and I have a backlog of blog posts and documentation to review that might be useful. But — and this is critical — you don’t have to read everything that’s out there to start seeing results. You don’t even need to read *this* post; just type some prompts in and see what comes out.

That said, because I just wrote this up for a job application, **here’s how I’m getting good results from Claude Code**. I’ve added links to some examples where appropriate.

* A key is writing a clear spec ahead of time, which provides context to the agent as it works in the codebase. *(examples:&#x20;*[*1*](https://github.com/cdzombak/mac-install/blob/main/SPEC.md?ref=dzombak.com)*,&#x20;*[*2*](https://github.com/cdzombak/lychee-ai-organizer/blob/main/SPEC.md?ref=dzombak.com)*,&#x20;*[*3*](https://github.com/cdzombak/lychee-meta-tool/blob/main/SPEC.md?ref=dzombak.com)*,&#x20;*[*4*](https://github.com/cdzombak/xrp/blob/main/doc/SPEC.md?ref=dzombak.com)*)*
* Having a document for the agent that outlines the project’s structure and how to run e.g. builds and linters is helpful. *(examples:&#x20;*[*1*](https://github.com/cdzombak/xrp/blob/main/CLAUDE.md?ref=dzombak.com)*,&#x20;*[*2*](https://github.com/cdzombak/lychee-meta-tool/blob/main/CLAUDE.md?ref=dzombak.com)*,&#x20;*[*3*](https://github.com/cdzombak/lychee-ai-organizer/blob/main/CLAUDE.md?ref=dzombak.com)*)*
* Asking the agent to perform a code review on its own work is surprisingly fruitful.
* Finally, I have a personal “global” agent guide describing best practices for agents to follow, specifying things like problem-solving approach, use of TDD, etc. *(This file is listed near the end of this post.)*

Then there’s the question of **validating LLM-written code.**

AI-generated code *is* often incorrect or inefficient.

It’s important for me to call out that **I believe I’m ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced**.

Therefore, especially in any professional context, I manually review all AI-written code and test cases. I’ll add test cases for anything I think is missing or needs improvement, either manually or by asking the LLM to write those cases (which I then review).

At the end of the day, manual review is necessary to verify that behavior is implemented correctly and tested properly.

## [](#personal-global-agent-guide "Permalink to this header")Personal “global” agent guide

This lives at `~/.claude/CLAUDE.md`:

````markdown
# Development Guidelines

## Philosophy

### Core Beliefs

- **Incremental progress over big bangs** - Small changes that compile and pass tests
- **Learning from existing code** - Study and plan before implementing
- **Pragmatic over dogmatic** - Adapt to project reality
- **Clear intent over clever code** - Be boring and obvious

### Simplicity Means

- Single responsibility per function/class
- Avoid premature abstractions
- No clever tricks - choose the boring solution
- If you need to explain it, it's too complex

## Process

### 1. Planning & Staging

Break complex work into 3-5 stages. Document in `IMPLEMENTATION_PLAN.md`:

```markdown
## Stage N: [Name]
**Goal**: [Specific deliverable]
**Success Criteria**: [Testable outcomes]
**Tests**: [Specific test cases]
**Status**: [Not Started|In Progress|Complete]
```
- Update status as you progress
- Remove file when all stages are done

### 2. Implementation Flow

1. **Understand** - Study existing patterns in codebase
2. **Test** - Write test first (red)
3. **Implement** - Minimal code to pass (green)
4. **Refactor** - Clean up with tests passing
5. **Commit** - With clear message linking to plan

### 3. When Stuck (After 3 Attempts)

**CRITICAL**: Maximum 3 attempts per issue, then STOP.

1. **Document what failed**:
   - What you tried
   - Specific error messages
   - Why you think it failed

2. **Research alternatives**:
   - Find 2-3 similar implementations
   - Note different approaches used

3. **Question fundamentals**:
   - Is this the right abstraction level?
   - Can this be split into smaller problems?
   - Is there a simpler approach entirely?

4. **Try different angle**:
   - Different library/framework feature?
   - Different architectural pattern?
   - Remove abstraction instead of adding?

## Technical Standards

### Architecture Principles

- **Composition over inheritance** - Use dependency injection
- **Interfaces over singletons** - Enable testing and flexibility
- **Explicit over implicit** - Clear data flow and dependencies
- **Test-driven when possible** - Never disable tests, fix them

### Code Quality

- **Every commit must**:
  - Compile successfully
  - Pass all existing tests
  - Include tests for new functionality
  - Follow project formatting/linting

- **Before committing**:
  - Run formatters/linters
  - Self-review changes
  - Ensure commit message explains "why"

### Error Handling

- Fail fast with descriptive messages
- Include context for debugging
- Handle errors at appropriate level
- Never silently swallow exceptions

## Decision Framework

When multiple valid approaches exist, choose based on:

1. **Testability** - Can I easily test this?
2. **Readability** - Will someone understand this in 6 months?
3. **Consistency** - Does this match project patterns?
4. **Simplicity** - Is this the simplest solution that works?
5. **Reversibility** - How hard to change later?

## Project Integration

### Learning the Codebase

- Find 3 similar features/components
- Identify common patterns and conventions
- Use same libraries/utilities when possible
- Follow existing test patterns

### Tooling

- Use project's existing build system
- Use project's test framework
- Use project's formatter/linter settings
- Don't introduce new tools without strong justification

## Quality Gates

### Definition of Done

- [ ] Tests written and passing
- [ ] Code follows project conventions
- [ ] No linter/formatter warnings
- [ ] Commit messages are clear
- [ ] Implementation matches plan
- [ ] No TODOs without issue numbers

### Test Guidelines

- Test behavior, not implementation
- One assertion per test when possible
- Clear test names describing scenario
- Use existing test utilities/helpers
- Tests should be deterministic

## Important Reminders

**NEVER**:
- Use `--no-verify` to bypass commit hooks
- Disable tests instead of fixing them
- Commit code that doesn't compile
- Make assumptions - verify with existing code

**ALWAYS**:
- Commit working code incrementally
- Update plan documentation as you go
- Learn from existing implementations
- Stop after 3 failed attempts and reassess
````

## [](#projects-written-using-claude-code "Permalink to this header")Projects written using Claude Code

[GitHub - cdzombak/xrp: HTML/XML aware reverse proxy](https://github.com/cdzombak/xrp?ref=dzombak.com)

[HTML/XML aware reverse proxy. Contribute to cdzombak/xrp development by creating an account on GitHub.](https://github.com/cdzombak/xrp?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-24.svg)cdzombak](https://github.com/cdzombak/xrp?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/thumbnail/xrp)](https://github.com/cdzombak/xrp?ref=dzombak.com)

[GitHub - cdzombak/dzsolarized-vscode: Solarized variant for VS Code (light + dark modes supported)](https://github.com/cdzombak/dzsolarized-vscode?ref=dzombak.com)

[Solarized variant for VS Code (light + dark modes supported) - cdzombak/dzsolarized-vscode](https://github.com/cdzombak/dzsolarized-vscode?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-25.svg)GitHubcdzombak](https://github.com/cdzombak/dzsolarized-vscode?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/thumbnail/dzsolarized-vscode-1)](https://github.com/cdzombak/dzsolarized-vscode?ref=dzombak.com)

[GitHub - cdzombak/flickr-rss: Generate an RSS feed of a Flickr photostream or your Friends & Family feed](https://github.com/cdzombak/flickr-rss?ref=dzombak.com)

[Generate an RSS feed of a Flickr photostream or your Friends & Family feed - cdzombak/flickr-rss](https://github.com/cdzombak/flickr-rss?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-26.svg)GitHubcdzombak](https://github.com/cdzombak/flickr-rss?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/thumbnail/flickr-rss-1)](https://github.com/cdzombak/flickr-rss?ref=dzombak.com)

[GitHub - cdzombak/lychee-meta-tool: Quickly find & edit untitled photos in your Lychee photo library](https://github.com/cdzombak/lychee-meta-tool?ref=dzombak.com)

[Quickly find & edit untitled photos in your Lychee photo library - cdzombak/lychee-meta-tool](https://github.com/cdzombak/lychee-meta-tool?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-27.svg)GitHubcdzombak](https://github.com/cdzombak/lychee-meta-tool?ref=dzombak.com)

[![](https://opengraph.githubassets.com/0bc054b50f02fae2565fbd58e0233229978d67ef59f2d3c3a2c7584f3d2250ce/cdzombak/lychee-meta-tool)](https://github.com/cdzombak/lychee-meta-tool?ref=dzombak.com)

[GitHub - cdzombak/macos-screenlock-mqtt: Report macOS screen lock status to an MQTT broker](https://github.com/cdzombak/macos-screenlock-mqtt?ref=dzombak.com)

[Report macOS screen lock status to an MQTT broker. Contribute to cdzombak/macos-screenlock-mqtt development by creating an account on GitHub.](https://github.com/cdzombak/macos-screenlock-mqtt?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-28.svg)GitHubcdzombak](https://github.com/cdzombak/macos-screenlock-mqtt?ref=dzombak.com)

[![](https://opengraph.githubassets.com/2eac4061a0425efd3045d26d6ea8c3827670f1d8af1fad2e3a528df8193aebe8/cdzombak/macos-screenlock-mqtt)](https://github.com/cdzombak/macos-screenlock-mqtt?ref=dzombak.com)

[GitHub - cdzombak/lychee-birb-title: Set titles for Bird Buddy photos in your Lychee photo library](https://github.com/cdzombak/lychee-birb-title?ref=dzombak.com)

[Set titles for Bird Buddy photos in your Lychee photo library - cdzombak/lychee-birb-title](https://github.com/cdzombak/lychee-birb-title?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-29.svg)GitHubcdzombak](https://github.com/cdzombak/lychee-birb-title?ref=dzombak.com)

[![](https://opengraph.githubassets.com/60865f263a542ad9f7bc543702fd15ae3de260090e3e35edca63e6492d97da49/cdzombak/lychee-birb-title)](https://github.com/cdzombak/lychee-birb-title?ref=dzombak.com)

[GitHub - cdzombak/lychee-ai-organizer: Use local LLMs to organize your unsorted photos in Lychee](https://github.com/cdzombak/lychee-ai-organizer?ref=dzombak.com)

[Use local LLMs to organize your unsorted photos in Lychee - cdzombak/lychee-ai-organizer](https://github.com/cdzombak/lychee-ai-organizer?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-30.svg)GitHubcdzombak](https://github.com/cdzombak/lychee-ai-organizer?ref=dzombak.com)

[![](https://opengraph.githubassets.com/cfd5ea252de7e2e859a8b94d02f2cbaeb1d0ce6c05ad5c5f45b8aed5d3441052/cdzombak/lychee-ai-organizer)](https://github.com/cdzombak/lychee-ai-organizer?ref=dzombak.com)

[GitHub - cdzombak/mac-install: Idempotent software suite installer for macOS](https://github.com/cdzombak/mac-install?ref=dzombak.com)

[Idempotent software suite installer for macOS. Contribute to cdzombak/mac-install development by creating an account on GitHub.](https://github.com/cdzombak/mac-install?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-31.svg)GitHubcdzombak](https://github.com/cdzombak/mac-install?ref=dzombak.com)

[![](https://opengraph.githubassets.com/919d1e0000548235c07554e25b7b35eef8822b5989895b6ccef3ca60f542e930/cdzombak/mac-install)](https://github.com/cdzombak/mac-install?ref=dzombak.com)

[GitHub - cdzombak/rss.church: I Believe in RSS](https://github.com/cdzombak/rss.church?ref=dzombak.com)

[I Believe in RSS. Contribute to cdzombak/rss.church development by creating an account on GitHub.](https://github.com/cdzombak/rss.church?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-32.svg)GitHubcdzombak](https://github.com/cdzombak/rss.church?ref=dzombak.com)

[![](https://opengraph.githubassets.com/cf321c8e07a66765223c314ac40b5887dd2cf5f4c56150621e4ee3ffb83fa708/cdzombak/rss.church)](https://github.com/cdzombak/rss.church?ref=dzombak.com)

[GitHub - cdzombak/flickr-exporter: Export all your Flickr photos, or a selected set or collection, preserving title/description/tags and other metadata.](https://github.com/cdzombak/flickr-exporter?ref=dzombak.com)

[Export all your Flickr photos, or a selected set or collection, preserving title/description/tags and other metadata. - cdzombak/flickr-exporter](https://github.com/cdzombak/flickr-exporter?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-33.svg)GitHubcdzombak](https://github.com/cdzombak/flickr-exporter?ref=dzombak.com)

[![](https://opengraph.githubassets.com/5afb4c8d55872fcdceca3c34a1dfa299f558c4d195991224e95c39e516e76dae/cdzombak/flickr-exporter)](https://github.com/cdzombak/flickr-exporter?ref=dzombak.com)

[GitHub - cdzombak/gallerygen: Generate a static HTML gallery from a directory tree of images](https://github.com/cdzombak/gallerygen?ref=dzombak.com)

[Generate a static HTML gallery from a directory tree of images - cdzombak/gallerygen](https://github.com/cdzombak/gallerygen?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/icon/pinned-octocat-093da3e6fa40-34.svg)GitHubcdzombak](https://github.com/cdzombak/gallerygen?ref=dzombak.com)

[![](https://www.dzombak.com/content/images/thumbnail/gallerygen)](https://github.com/cdzombak/gallerygen?ref=dzombak.com)


