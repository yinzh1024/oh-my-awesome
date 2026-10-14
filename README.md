# oh-my-awesome

> 我的 GitHub Star 导航 —— 自动同步、分类呈现。
> 数据来自 GitHub API，由本仓库的定时任务每 6 小时更新一次。

**快速了解**：分类规则在 [config.yaml](./config.yaml)（topics / languages / overrides 三
层机制），生成逻辑在 [src/oh_my_awesome](./src/oh_my_awesome)，定时任务在
[sync-stars.yml](./.github/workflows/sync-stars.yml)。

**本地更新**：

```bash
pip install .
export GITHUB_TOKEN=ghp_xxx   # 或写入 .env
oh-my-awesome sync --push     # 拉取 → 分类 → 生成 README → 提交推送
```

<!-- oh-my-awesome:begin -->
> 共 **454** 个项目 · 最后更新：2026-10-14 02:13 UTC · 数据采集：2026-10-14 02:13 UTC

## 目录

- [Awesome 列表](#awesome-列表) (13)
- [AI / LLM](#ai--llm) (62)
- [学习与教程](#学习与教程) (25)
- [音视频与流媒体](#音视频与流媒体) (51)
- [移动开发](#移动开发) (26)
- [前端与 Web](#前端与-web) (50)
- [Rust 生态](#rust-生态) (11)
- [Go 生态](#go-生态) (7)
- [终端与 CLI 工具](#终端与-cli-工具) (24)
- [网络与安全](#网络与安全) (14)
- [桌面与效率工具](#桌面与效率工具) (16)
- [系统与嵌入式](#系统与嵌入式) (114)
- [开发工具与 DevOps](#开发工具与-devops) (4)
- [Python 工具](#python-工具) (26)
- [字体与设计](#字体与设计) (4)
- [未分类](#未分类) (7)

## Awesome 列表

_收集类清单，找资料先看这里_

- [996icu/996.ICU](https://github.com/996icu/996.ICU) `★277.1k` - Repo for counting stars and contributing. Press F to pay respect to glorious developers.
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) `★121k` - A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- [fffaraz/awesome-cpp](https://github.com/fffaraz/awesome-cpp) `★73.8k` - A curated list of awesome C++ (or C) frameworks, libraries, resources, and shiny things. Inspired by awesome-... stuff.
- [1c7/chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) `★61.8k` - 👩🏿‍💻👨🏾‍💻👩🏼‍💻👨🏽‍💻👩🏻‍💻中国独立开发者项目列表 -- 分享大家都在做什么
- [herrbischoff/awesome-macos-command-line](https://github.com/herrbischoff/awesome-macos-command-line) `★31k` - Use your macOS terminal shell to do awesome things. _(archived)_
- [sindresorhus/awesome-electron](https://github.com/sindresorhus/awesome-electron) `★27.3k` - Useful resources for creating apps with Electron [SUBMISSIONS ARE TEMPORARILY PAUSED BECAUSE I'M TIRED OF REVIEWING LOW-QUALITY STUFF]
- [mzlogin/awesome-adb](https://github.com/mzlogin/awesome-adb) `★12.5k` - ADB Usage Complete / ADB 用法大全
- [jobbole/awesome-cpp-cn](https://github.com/jobbole/awesome-cpp-cn) `★11.2k` - C++ 资源大全中文版，标准库、Web应用框架、人工智能、数据库、图片处理、机器学习、日志、代码分析等。由「开源前哨」和「CPP开发者」微信公号团队维护更新。
- [jobbole/awesome-c-cn](https://github.com/jobbole/awesome-c-cn) `★6.7k` - C 资源大全中文版，包括了：构建系统、编译器、数据库、加密、初中高的教程/指南、书籍、库等。
- [LewisJEllis/awesome-lua](https://github.com/LewisJEllis/awesome-lua) `★4.6k` - A curated list of quality Lua packages and resources.
- [JsonChao/Awesome-Android-Notebook](https://github.com/JsonChao/Awesome-Android-Notebook) `★3.4k` - :computer: A complete plan for better android developers.（continuous updating ...）
- [pfalcon/awesome-micropython](https://github.com/pfalcon/awesome-micropython) `★192` - Curated list of awesome MicroPython resources
- [xuxiaodong/awesome-shell](https://github.com/xuxiaodong/awesome-shell) `★167` - Awesome Shell Chinese Edition

## AI / LLM

_大模型、Agent、语音与视觉 AI 工程实践_

- [affaan-m/ECC](https://github.com/affaan-m/ECC) `★278.6k` - The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. · JavaScript
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) `★253.5k` - The agent that grows with you · Python
- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) `★249k` - DeepSeek Harness: Everything is a Plugin. · TypeScript
- [morluto/rea](https://github.com/morluto/rea) `★210.1k` - Reverse engineer anything with agents, from app behavior down to native binaries. · TypeScript
- [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) `★165k` - Stable Diffusion web UI · Python
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) `★130.5k` - 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. · Python
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) `★97k` - Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. · Python
- [infiniflow/ragflow](https://github.com/infiniflow/ragflow) `★92.2k` - RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs · Go
- [opencv/opencv](https://github.com/opencv/opencv) `★91.2k` - Open Source Computer Vision Library · C++
- [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) `★91k` - Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. · Python
- [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) `★86.2k` - Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. · TypeScript
- [tt-a1i/archify](https://github.com/tt-a1i/archify) `★83.1k` - Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more. · JavaScript
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) `★81.7k` - Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows. · Python
- [netdata/netdata](https://github.com/netdata/netdata) `★80.9k` - The fastest path to AI-powered full stack observability, even for lean teams. · Go
- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) `★70k` - OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering. · TypeScript
- [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) `★64.3k` - A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES. · JavaScript _(archived)_
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) `★62.9k` - Write HTML. Render video. Built for agents. · TypeScript
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) `★54.2k` - Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, and Pi. 44 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop. · HTML
- [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) `★54.1k` - Breakthrough Method for Agile Ai Driven Development · Python
- [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr) `★39.6k` - An open-source engine that turns continuous content streams into search and monitoring. Durable ingestion, hybrid search, alerts, and plugins for formats, models and business rules. · Go
- [suno-ai/bark](https://github.com/suno-ai/bark) `★39.3k` - 🔊 Text-Prompted Generative Audio Model · Jupyter Notebook
- [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) `★37.9k` - An AI prompt optimizer for writing better prompts and getting better AI results. · TypeScript
- [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) `★36.6k` - NVR with realtime local object detection for IP cameras · Python
- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) `★35.8k` - A reliable coding agent for complex software engineering tasks. · Go
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) `★35.3k` - ⌥ Coding agent with the IDE wired in. Built by Stencil Labs. · TypeScript
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora) `★33.8k` - Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki. · Go
- [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) `★33k` - Fast, small, and fully autonomous AI personal assistant infrastructure, any OS, any platform — deploy anywhere, swap anything 🦀 · Rust
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) `★30.9k` - An MCP-based chatbot | 一个基于MCP的聊天机器人 · C++
- [alibaba/page-agent](https://github.com/alibaba/page-agent) `★29.4k` - JavaScript in-page GUI agent. Control web interfaces with natural language. · TypeScript
- [slopus/happy](https://github.com/slopus/happy) `★24.1k` - Orchestrate Claude, Codex and Grok in one app. Open-source (MIT), reuses the subscriptions you already pay for. · TypeScript
- [wechaty/wechaty](https://github.com/wechaty/wechaty) `★23.4k` - Conversational RPA SDK for Chatbot Makers. Join our Discord: https://discord.gg/7q8NBZbQzt · TypeScript
- [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) `★21.2k` - 🎭 277 个即插即用的 AI 专家角色 — 支持 Claude Code/Cursor/Copilot 等 20 种工具，覆盖工程/设计/营销/金融等 20 个部门。含 64 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉/Qt 上位机/机械设计）。搭配编排器 agency-orchestrator，一句话即可让多位专家按 DAG 自动协作。 · Shell
- [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) `★20k` - Give your agent CAD superpowers. · Python
- [lexmount/moli](https://github.com/lexmount/moli) `★18k` - Best headless browser for AI agents. Lite, Fast, High-Compatibility. Built in Rust · Rust
- [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) `★17.7k` - ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. · C
- [memvid/memvid](https://github.com/memvid/memvid) `★16.6k` - Memory layer for AI Agents. Replace complex RAG pipelines with a serverless, single-file memory layer. Give your agents instant retrieval and long-term memory. · Rust
- [microsoft/Bringing-Old-Photos-Back-to-Life](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life) `★15.7k` - Bringing Old Photo Back to Life (CVPR 2020 oral) · Python _(archived)_
- [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) `★15.3k` - Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, RK NPU, Axera NPU, Ascend NPU, x86_64 servers, websocket server/client, support 12 programming languages · C++
- [PaddlePaddle/PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech) `★12.7k` - Easy-to-use Speech Toolkit including Self-Supervised Learning model, SOTA/Streaming ASR with punctuation, Streaming TTS with text frontend, Speaker Verification System, End-to-End Speech Translation and Keyword Spotting. Won NAACL2022 Best Demo Award. · Python
- [dataelement/bisheng](https://github.com/dataelement/bisheng) `★12k` - BISHENG is an open LLM devops platform for next generation Enterprise AI applications. Powerful and comprehensive features include: GenAI workflow, RAG, Agent, Unified model management, Evaluation, SFT, Dataset Management, Enterprise-level System Management, Observability and more. · Python
- [x-hw/amazing-qr](https://github.com/x-hw/amazing-qr) `★10.8k` - 💮 amazing QRCode generator (supporting animated gif) - amazing 二维码生成器（支持 gif 动态图片二维码） · Python
- [niedev/RTranslator](https://github.com/niedev/RTranslator) `★10.5k` - Open source real-time translation app for Android that runs locally · Java
- [openframeworks/openFrameworks](https://github.com/openframeworks/openFrameworks) `★10.4k` - openFrameworks is a community-developed cross platform toolkit for creative coding in C++. · C++
- [pipipi-pikachu/PPTist](https://github.com/pipipi-pikachu/PPTist) `★9.4k` - PowerPoint-ist（/'pauəpɔintist/）, An online presentation application that replicates most of the commonly used features of MS PowerPoint, allowing for the editing and presentation of PPT online. It also supports AIPPT and local PPTX file preview. · Vue
- [wzpan/wukong-robot](https://github.com/wzpan/wukong-robot) `★7.1k` - 🤖 wukong-robot 是一个简单、灵活、优雅的中文语音对话机器人/智能音箱项目，支持ChatGPT多轮对话能力，还可能是首个支持脑机交互的开源智能音箱项目。 · Python
- [liuruoze/EasyPR](https://github.com/liuruoze/EasyPR) `★6.4k` - (CGCSTCD'2017) An easy, flexible, and accurate plate recognition project for Chinese licenses in unconstrained situations.  CGCSTCD = China Graduate Contest on Smart-city Technology and Creative Design · C++
- [chthollyphile/folia-major](https://github.com/chthollyphile/folia-major) `★5.9k` - 专注于绚丽的歌词动画效果的本地音乐/navidrome/第三方多平台在线音乐播放器 · TypeScript
- [memovai/mimiclaw](https://github.com/memovai/mimiclaw) `★5.8k` - MimiClaw: Personal Agent on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS. On device Muse. · C
- [the-open-agent/openagent](https://github.com/the-open-agent/openagent) `★5.7k` - ⚡️next-generation personal AI assistant powered by LLM, RAG and agent loops, supporting computer-use, browser-use and coding agent, demo: https://demo.openagentai.org · Go
- [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) `★4.5k` - A 100M-parameter multilingual TTS model for real-time CPU inference, voice cloning, and 48 kHz stereo generation · Python
- [ben1234560/AiLearning-Theory-Applying](https://github.com/ben1234560/AiLearning-Theory-Applying) `★3.6k` - 快速上手AI理论及应用实战：基础知识、Transformer、NLP、ML、DL、竞赛。含大量注释及数据集，力求每一位能看懂并复现。 · Jupyter Notebook
- [makelove/OpenCV-Python-Tutorial](https://github.com/makelove/OpenCV-Python-Tutorial) `★3.4k` - OpenCV问答群不再维护。有问题，自己去搜索。Google能找到大部分答案。 · Python
- [RightNow-AI/picolm](https://github.com/RightNow-AI/picolm) `★2.2k` - Run a 1-billion parameter LLM on a $10 board with 256MB RAM · C
- [Thmen/EGVSR](https://github.com/Thmen/EGVSR) `★955` - Efficient & Generic Video Super-Resolution · Python
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) `★867` - DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF） · HTML
- [Xiaobin-Rong/gtcrn](https://github.com/Xiaobin-Rong/gtcrn) `★753` - The official implementation of GTCRN, an ultra-lightweight SE model. · Python
- [symisc/ascii_art](https://github.com/symisc/ascii_art) `★741` - Real-Time ASCII Art Rendering Library · C
- [worldveil/photomosaic](https://github.com/worldveil/photomosaic) `★698` - Creating fun photomosaics, GIFs, and murals from your family pictures using ML & similarity search · Jupyter Notebook
- [huakunyang/SummerTTS](https://github.com/huakunyang/SummerTTS) `★545` - SummerTTS 是一个基于C++的独立编译的中文和英文语音合成项目，可以本地运行不需要网络，而且没有额外的依赖，一键编译完成即可用于中文和英文的语音合成。SummerTTS is a  standalone Chinese and English speech synthesis(TTS) project that has almost no dependency and could be easily used for Chinese TTS with just one key build out · C++
- [ranchlai/mandarin-tts](https://github.com/ranchlai/mandarin-tts) `★478` - Chinese Mandarin tts text-to-speech  中文 (普通话) 语音 合成 , by fastspeech 2 , implemented in pytorch, using waveglow as vocoder,  with biaobei and aishell3 datasets · Python
- [benjaminwan/ChineseTtsTflite](https://github.com/benjaminwan/ChineseTtsTflite) `★413` - Android Chinese TTS Engine Base On Tensorflow TTS , use for TfLite Models Test。安卓离线中文TTS引擎，在TensorflowTTS基础上开发，用于TfLite模型测试。 · Java
- [EdwinjJ1/3d-print-skill](https://github.com/EdwinjJ1/3d-print-skill) `★27` - Claude Code skill for 3D printing — search-first workflow, manifold-safe output for Bambu Studio / PrusaSlicer / Cura · Python

## 学习与教程

_教程、文档、面试与算法刷题_

- [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) `★204k` - Free domain registration and practical DNS learning resources for everyone. · Markdown
- [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) `★162.5k` - Master the command line, in one page
- [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) `★119.2k` - :books: 免费的计算机编程类中文书籍，欢迎投稿
- [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) `★82.8k` - 所有小初高、大学PDF教材。 · Roff
- [MisterBooo/LeetCodeAnimation](https://github.com/MisterBooo/LeetCodeAnimation) `★76.7k` - Demonstrate all the questions on LeetCode in the form of animation.（用动画的形式呈现解LeetCode题目的思路,完整单步/回看/变速/语音讲解在 algomooc.com） · Java
- [huihut/interview](https://github.com/huihut/interview) `★38.2k` - 📚 C/C++ 技术面试基础知识总结，包括语言、程序库、数据结构、算法、系统、网络、链接装载库等知识及面试经验、招聘、内推等信息。This repository is a summary of the basic knowledge of recruiting job seekers and beginners in the direction of C/C++ technology, including language, program library, data structure, algorithm, system, network, link loading library, interview experience, recruitment, recommendation, etc. · C++
- [exacity/deeplearningbook-chinese](https://github.com/exacity/deeplearningbook-chinese) `★37.8k` - Deep Learning Book Chinese Translation · TeX
- [0voice/interview_internal_reference](https://github.com/0voice/interview_internal_reference) `★37.3k` - 2025年最新总结，阿里，腾讯，百度，美团，头条等技术面试题目，以及答案，专家出题人分析汇总。 · Python
- [carbon-app/carbon](https://github.com/carbon-app/carbon) `★36.1k` - :black_heart: Create and share beautiful images of your source code · JavaScript
- [changkun/modern-cpp-tutorial](https://github.com/changkun/modern-cpp-tutorial) `★25.9k` - 📚 Modern C++ Tutorial: C++11 to C++26 On the Fly | https://changkun.de/modern-cpp/ · C++
- [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) `★21.9k` - 健康学习到150岁 - 人体系统调优不完全指南
- [SwiftGGTeam/the-swift-programming-language-in-chinese](https://github.com/SwiftGGTeam/the-swift-programming-language-in-chinese) `★21.2k` - 中文版 Apple 官方《Swift 编程语言》 · Markdown
- [programthink/books](https://github.com/programthink/books) `★20.3k` - 【编程随想】收藏的电子书清单（多个学科，含下载链接）
- [leandromoreira/digital_video_introduction](https://github.com/leandromoreira/digital_video_introduction) `★16.4k` - A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding). Translations: 🇺🇸 🇨🇳 🇯🇵 🇮🇹 🇰🇷 🇷🇺 🇧🇷 🇪🇸 · Jupyter Notebook
- [ruanyf/document-style-guide](https://github.com/ruanyf/document-style-guide) `★13k` - 中文技术文档的写作规范
- [0voice/from_coder_to_expert](https://github.com/0voice/from_coder_to_expert) `★11.2k` - 2021年最新总结，从程序员到CTO，从专业走向卓越，分享大牛企业内部pdf与PPT
- [redguardtoo/mastering-emacs-in-one-year-guide](https://github.com/redguardtoo/mastering-emacs-in-one-year-guide) `★6.4k` - Be great at emacs in one year
- [tboox/tbox](https://github.com/tboox/tbox) `★5.1k` - 🎁 A glib-like multi-platform c library · C
- [maicss/PyQt-Chinese-tutorial](https://github.com/maicss/PyQt-Chinese-tutorial) `★3.6k` - PyQt6中文教程
- [pezy/LeetCode](https://github.com/pezy/LeetCode) `★3.5k` - :pencil2: LeetCode solutions in C++ 11 and Python3 · C++
- [widuu/chinese_docker](https://github.com/widuu/chinese_docker) `★2.7k` - docker中文文档，docker Chinese Documation
- [emacs-china/Spacemacs-rocks](https://github.com/emacs-china/Spacemacs-rocks) `★2.1k` - Happy Hacking Emacs & Spacemacs (Simplified Chinese) · CSS
- [anjuke/zguide-cn](https://github.com/anjuke/zguide-cn) `★1.8k` - ZMQ 指南 · Raku
- [nivance/DPModel](https://github.com/nivance/DPModel) `★278` - 《设计模式之禅》原书源码学习 · Java
- [Akagi201/learning-python](https://github.com/Akagi201/learning-python) `★79` - notes and codes while learning python · Python

## 音视频与流媒体

_编解码、推拉流、播放器、摄像头与媒体服务_

- [storytold/photocraft](https://github.com/storytold/photocraft) `★58.1k` - PhotoCraft: An open-source, photo editor written by scratch in pure Rust · Rust
- [iina/iina](https://github.com/iina/iina) `★46.8k` - The modern video player for macOS. · Swift
- [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) `★46.3k` - The Secure CommsOS™ for mission-critical operations · TypeScript
- [mifi/lossless-cut](https://github.com/mifi/lossless-cut) `★44.5k` - The swiss army knife of lossless video/audio editing · TypeScript
- [portainer/portainer](https://github.com/portainer/portainer) `★38.7k` - Making Docker and Kubernetes management easy. · TypeScript
- [mpv-player/mpv](https://github.com/mpv-player/mpv) `★37.4k` - 🎥 Command line media player · C
- [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic) `★33.4k` - 高颜值的第三方网易云播放器，支持 Windows / macOS / Linux :electron: · Vue
- [ossrs/srs](https://github.com/ossrs/srs) `★29.3k` - SRS is a simple, high-performance, AI-driven real-time media server supporting RTMP, WebRTC, HLS, HTTP-FLV, HTTP-TS, SRT, MPEG-DASH, and GB28181, with codec support for H.264, H.265, AV1, VP9, AAC, Opus, and G.711. · C++
- [Guovin/iptv-api](https://github.com/Guovin/iptv-api) `★25.6k` - ⚡️ IPTV直播源自动更新工具：自动采集、校验、测速并生成可播放结果，支持 M3U/TXT/API 输出、自定义频道、IPv4/IPv6、Docker、GitHub Actions、CLI 与 GUI 多端部署 · Python
- [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) `★20.4k` - Ready-to-use Media-over-QUIC / SRT / WebRTC / RTSP / RTMP / LL-HLS / MPEG-TS / RTP live media server and media proxy that allows to read, publish, proxy, record and playback real-time video and audio streams. · Go
- [ZLMediaKit/ZLMediaKit](https://github.com/ZLMediaKit/ZLMediaKit) `★17.6k` - WebRTC/RTSP/RTMP/HTTP/HLS/HTTP-FLV/WebSocket-FLV/HTTP-TS/HTTP-fMP4/WebSocket-TS/WebSocket-fMP4/GB28181/SRT/STUN/TURN server and client framework based on C++11 · C++
- [AlexxIT/go2rtc](https://github.com/AlexxIT/go2rtc) `★14.4k` - Ultimate camera streaming application · Go
- [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) `★9.9k` - The only downloader you need. 下载器的集大成者。 · Python
- [sameersbn/docker-gitlab](https://github.com/sameersbn/docker-gitlab) `★8.1k` - Dockerized GitLab · Shell
- [mackron/miniaudio](https://github.com/mackron/miniaudio) `★7.4k` - Audio playback and capture library written in C, in a single source file. · C
- [648540858/wvp-GB28181-pro](https://github.com/648540858/wvp-GB28181-pro) `★7.4k` - 基于GB28181-2016、部标808、部标1078标准实现的开箱即用的网络视频平台。自带管理页面，支持NAT穿透，支持海康、大华、宇视等品牌的IPC、NVR接入。支持国标级联，支持将普通摄像机/直播流/直播推流转国标共享到国标平台。 · Java
- [xfangfang/Macast](https://github.com/xfangfang/Macast) `★7k` - Macast is a cross-platform application which using mpv as DLNA Media Renderer. · Python
- [illuspas/Node-Media-Server](https://github.com/illuspas/Node-Media-Server) `★6.2k` - A Node.js implementation of RTMP/HTTP-FLV Media Server · JavaScript
- [signalwire/freeswitch](https://github.com/signalwire/freeswitch) `★5.2k` - FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a versatile software implementation that runs on any commodity hardware. From a Raspberry PI to a multi-core server, FreeSWITCH can unlock the telecommunications potential of any device. · C
- [suxuang/myIPTV](https://github.com/suxuang/myIPTV) `★5.1k` - 【典藏版】高清直播源涵盖几乎所有卫视节目，内置完美台标加节目预告
- [motioneye-project/motioneye](https://github.com/motioneye-project/motioneye) `★4.7k` - A web frontend for the motion daemon. · Python
- [wang-bin/QtAV](https://github.com/wang-bin/QtAV) `★4.3k` - A cross-platform multimedia framework based on Qt and FFmpeg. 基于Qt和FFmpeg的跨平台高性能音视频播放框架. Recommand to use new sdk https://github.com/wang-bin/mdk-sdk · C++
- [jitwxs/163MusicLyrics](https://github.com/jitwxs/163MusicLyrics) `★4.1k` - 云音乐歌词获取处理工具【网易云、QQ音乐】 · C#
- [ireader/media-server](https://github.com/ireader/media-server) `★3.5k` - RTSP/RTP/RTMP/FLV/HLS/MPEG-TS/MPEG-PS/MPEG-DASH/MP4/fMP4/MKV/WebM · C
- [Kurento/kurento-media-server](https://github.com/Kurento/kurento-media-server) `★3.1k` - [ARCHIVED] Contents migrated to monorepo: https://github.com/Kurento/kurento · C++ _(archived)_
- [scottlawsonbc/audio-reactive-led-strip](https://github.com/scottlawsonbc/audio-reactive-led-strip) `★3k` - :musical_note: :rainbow: Real-time LED strip music visualization using Python and the ESP8266 or Raspberry Pi · Python
- [langhuihui/jessibuca](https://github.com/langhuihui/jessibuca) `★2.9k` - Jessibuca是一款开源的纯H5直播流播放器 · C
- [harlanc/xiu](https://github.com/harlanc/xiu) `★2.3k` - A simple,high performance and secure live media server in pure Rust (RTMP[cluster]/RTSP/WebRTC[whip/whep]/HTTP-FLV/HLS).🦀 · Rust
- [IENT/YUView](https://github.com/IENT/YUView) `★2.3k` - The Free and Open Source Cross Platform YUV Viewer with an advanced analytics toolset · C++
- [baresip/baresip](https://github.com/baresip/baresip) `★2.3k` - Baresip is a modular SIP User-Agent with audio and video support · C
- [giantpinkrobots/varia](https://github.com/giantpinkrobots/varia) `★1.9k` - Download manager that supports regular downloads, torrents and videos · Python
- [jxlarrea/kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) `★1.6k` - Turn any Android device into a beautiful, dedicated Home Assistant kiosk. Purpose-built for Home Assistant from the ground up. · Dart
- [mikeroyal/PipeWire-Guide](https://github.com/mikeroyal/PipeWire-Guide) `★1.5k` - PipeWire Guide. Learn about how PipeWire gives your Linux system a Professional Audio/Video Processing workflow. · Shell
- [ErosZy/WXInlinePlayer](https://github.com/ErosZy/WXInlinePlayer) `★1.5k` - 🤟 Super fast H.264/H.265 FLV player · C++
- [cycfi/q](https://github.com/cycfi/q) `★1.4k` - C++ Library for Audio Digital Signal Processing · C++
- [metartc/metaRTC](https://github.com/metartc/metaRTC) `★1.2k` - webrtc sdk for embedded / IoT / robotics devices · C
- [adamstark/AudioFile](https://github.com/adamstark/AudioFile) `★1.1k` - A simple C++ library for reading and writing audio files. · C++
- [PHZ76/RtspServer](https://github.com/PHZ76/RtspServer) `★1.1k` - RTSP Server , RTSP Pusher · C++
- [hvianna/audioMotion-analyzer](https://github.com/hvianna/audioMotion-analyzer) `★959` - High-resolution real-time graphic audio spectrum analyzer JavaScript module with no dependencies. · JavaScript
- [mogutt/TTServer](https://github.com/mogutt/TTServer) `★954` - 蘑菇街TeamTalk之消息服务器
- [larksuite/rsmpeg](https://github.com/larksuite/rsmpeg) `★879` - A Rust crate that exposes FFmpeg's power as much as possible. · Rust
- [tsingsee/EasyPlayer](https://github.com/tsingsee/EasyPlayer) `★687` - An free, elegant, simple, fast RTSP/RTMP/HLS/HTTP Player.EasyPlayer support RTSP(RTP over TCP/UDP)version& RTMP version & Pro version，cover all kinds of streaming media！EasyPlayer是一款免费、精炼、高效、稳定的流媒体播放器，分为RTSP版、RTMP版和Pro版本，支持各种各样的流媒体音视频播放！
- [gongluck/AnalysisAVP](https://github.com/gongluck/AnalysisAVP) `★645` - 音视频学习，相关文件格式/协议分析，框架学习等。encode decode；rgb yuv h264 aac flv mp4 rtmp；libyuv x264 openh264 faac faad2 fdk-aac librtmp ffmpeg sdl2 webrtc；android ios capture videotoolbox； · C++
- [OpenIPC/smolrtsp](https://github.com/OpenIPC/smolrtsp) `★510` - A lightweight real-time streaming library for IP cameras · C
- [scottlamb/retina](https://github.com/scottlamb/retina) `★376` - High-level RTSP multimedia streaming library, in Rust · Rust
- [zhw2590582/FlvPlayer](https://github.com/zhw2590582/FlvPlayer) `★305` - :lollipop: FlvPlayer.js is a JavaScript player for decode flv to the canvas · JavaScript _(archived)_
- [VideoExpertsGroup/RTSP.Player.Android](https://github.com/VideoExpertsGroup/RTSP.Player.Android) `★224` - RTSP player for Android / IP camera viewer · Java
- [huajiaofrontend/HJPlayer](https://github.com/huajiaofrontend/HJPlayer) `★169` - A HTML5 Player, can play flv and hls by Media Source Extension, based on typescript. · TypeScript
- [Mi-Bee-Studio/MiBeeNvr](https://github.com/Mi-Bee-Studio/MiBeeNvr) `★150` - Lightweight self-hosted NVR in Go — single static binary, zero dependencies, embedded web UI. RTSP/ONVIF/Xiaomi/GB28181 cameras, RTMP/SRT/WebRTC push-in ingest, WebRTC/HLS/FLV live view, audio, timelapse, continuous playback, browser-side AI detection. Runs on low-power ARM. · Go
- [koraa/sndlink](https://github.com/koraa/sndlink) `★16` - Realtime audio streaming · C++
- [tonarino/pulseaudio-webrtc-audio-processing](https://github.com/tonarino/pulseaudio-webrtc-audio-processing) `★7` - AudioProcessing library based on Google's implementation of WebRTC

## 移动开发

_Android / iOS / 跨平台移动端_

- [flutter/flutter](https://github.com/flutter/flutter) `★180.1k` - Flutter makes it easy and fast to build beautiful apps for mobile and beyond · Dart
- [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) `★151.1k` - A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience · Rust
- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) `★125.7k` - An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. · Rust
- [android/architecture-samples](https://github.com/android/architecture-samples) `★45.9k` - A collection of samples to discuss and showcase different architectural tools and patterns for Android apps. · Kotlin
- [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) `★41.5k` - Comfortably monitor your network traffic 🕵️‍♂️ · Rust
- [mattermost/mattermost](https://github.com/mattermost/mattermost) `★39.3k` - Mattermost is an open source platform for secure collaboration across the entire software development lifecycle.. · TypeScript
- [shadowsocks/ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG) `★32.9k` - Next Generation of ShadowsocksX · Swift
- [Trinea/android-open-project](https://github.com/Trinea/android-open-project) `★31.8k` - A categorized collection of Android Open Source Projects,  More powerful web version:
- [square/leakcanary](https://github.com/square/leakcanary) `★30k` - A memory leak detection library for Android. · Kotlin
- [ayangweb/BongoCat](https://github.com/ayangweb/BongoCat) `★23.9k` - 🐱 BongoCat — A cross-platform interactive desktop pet that brings fun to your desktop! · Rust
- [alibaba/flutter-go](https://github.com/alibaba/flutter-go) `★23.6k` - flutter 开发者帮助 APP，包含 flutter 常用 140+ 组件的demo 演示与中文文档 · Dart
- [CarGuo/gsy_github_app_flutter](https://github.com/CarGuo/gsy_github_app_flutter) `★15.5k` - Flutter 超完整的开源项目，功能丰富，适合学习和日常使用。GSYGithubApp 系列的优势：我们目前已经拥有 Flutter、Weex、ReactNative、Kotlin View、Kotlin Jetpack Compose ，Compose MultiPlatform，Harmony ArkUI 七个版本，功能齐全，项目框架内技术涉及面广，完成度高，持续维护，配套文章，适合全面学习，对比参考。 · Dart
- [orhanobut/logger](https://github.com/orhanobut/logger) `★13.8k` - ✔️ Simple, pretty and powerful logger for android · Kotlin
- [shiaho777/web-to-app](https://github.com/shiaho777/web-to-app) `★6.8k` - The most full featured web-to-app toolkit on Android, a complete APK workshop that runs entirely on your phone · Kotlin
- [ikarus23/MifareClassicTool](https://github.com/ikarus23/MifareClassicTool) `★6.5k` - An Android NFC app for reading, writing, analyzing, etc. MIFARE Classic RFID tags. · Java
- [1Remote/1Remote](https://github.com/1Remote/1Remote) `★6.1k` - One Remote Access Manager to Rule Them All · C#
- [lohanidamodar/flutter_ui_challenges](https://github.com/lohanidamodar/flutter_ui_challenges) `★4.7k` - Updated for Flutter 3.x ** 100+ Professional UI implementations with Code in Flutter. Available in Android, iOS, Linux and Web · Dart _(archived)_
- [alibaba/dexposed](https://github.com/alibaba/dexposed) `★4.5k` - dexposed enable 'god' mode for single android application. · Java _(archived)_
- [pjsip/pjproject](https://github.com/pjsip/pjproject) `★2.7k` - PJSIP project · C
- [dana-at-cp/backdoor-apk](https://github.com/dana-at-cp/backdoor-apk) `★2.4k` - backdoor-apk is a shell script that simplifies the process of adding a backdoor to any Android APK file. Users of this shell script should have working knowledge of Linux, Bash, Metasploit, Apktool, the Android SDK, smali, etc. This shell script is provided as-is without warranty of any kind and is intended for educational purposes only. · Shell
- [ZhaoKaiQiang/KLog](https://github.com/ZhaoKaiQiang/KLog) `★1.9k` - 这是一个Android专用的LogCat工具，主要功能为打印行号、函数调用、Json解析、XML解析、点击跳转、Log信息保存等功能 · Java
- [maoruibin/TranslateApp](https://github.com/maoruibin/TranslateApp) `★1.8k` - :memo: A translations app without interruptions, copy words and translate directly, show result by top view. · Java _(archived)_
- [Myzel394/Alibi](https://github.com/Myzel394/Alibi) `★1.7k` - Use your phone as a dashcam and save the last 30 minutes when you need them. · Kotlin
- [taka-no-me/android-cmake](https://github.com/taka-no-me/android-cmake) `★1.2k` - CMake toolchain file and other scripts for the Android NDK · CMake
- [foxglove/mcap](https://github.com/foxglove/mcap) `★1.1k` - MCAP is a modular, performant, and serialization-agnostic container file format, useful for pub/sub and robotics applications. · Rust
- [zibo-chen/SubnetDesk](https://github.com/zibo-chen/SubnetDesk) `★679` - LAN-only remote desktop based on RustDesk · Rust

## 前端与 Web

_Web 框架、UI 库与前端工程化_

- [anomalyco/opencode](https://github.com/anomalyco/opencode) `★213.3k` - The open source coding agent. · TypeScript
- [iptv-org/iptv](https://github.com/iptv-org/iptv) `★140.8k` - Collection of publicly available IPTV channels from all over the world · TypeScript
- [mrdoob/three.js](https://github.com/mrdoob/three.js) `★116.4k` - JavaScript 3D Library. · JavaScript
- [d3/d3](https://github.com/d3/d3) `★113.7k` - Bring data to life with SVG, Canvas and HTML. :bar_chart::chart_with_upwards_trend::tada: · Shell
- [ocornut/imgui](https://github.com/ocornut/imgui) `★76.6k` - Dear ImGui: Bloat-free Graphical User interface for C++ with minimal dependencies · C++
- [hakimel/reveal.js](https://github.com/hakimel/reveal.js) `★72.4k` - The HTML Presentation Framework · JavaScript
- [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) `★62.1k` - 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 · HTML
- [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) `★55.5k` - A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. · JavaScript
- [justjavac/wechat-miniapp-radar](https://github.com/justjavac/wechat-miniapp-radar) `★51.2k` - :traffic_light:小程序雷达：AI 驱动的小程序技术选型、趋势追踪和迁移诊断工具 · TypeScript
- [NaiboWang/EasySpider](https://github.com/NaiboWang/EasySpider) `★44.7k` - A visual no-code/code-free web crawler/spider易采集：一个可视化浏览器自动化测试/数据采集/网页爬虫软件，可以无代码图形化的设计和执行爬虫任务。别名：ServiceWrapper面向Web应用的智能化服务封装系统。 · JavaScript
- [impress/impress.js](https://github.com/impress/impress.js) `★38.2k` - It's a presentation framework based on the power of CSS3 transforms and transitions in modern browsers and inspired by the idea behind prezi.com. · JavaScript
- [fanmingming/live](https://github.com/fanmingming/live) `★28.6k` - ✯ 可直连访问的电视/广播图标库与相关工具项目 ✯ 🔕 永久免费 直连访问 完整开源 不断完善的台标 支持IPv4/IPv6双栈访问 🔕 · JavaScript
- [houshanren/hangzhou_house_knowledge](https://github.com/houshanren/hangzhou_house_knowledge) `★26.9k` - 2017年买房经历总结出来的买房购房知识分享给大家，希望对大家有所帮助。买房不易，且买且珍惜。Sharing the knowledge of buy an own house that according  to the experience at hangzhou in 2017 to all the people. It's not easy to buy a own house, so I hope that it would be useful to everyone. · CSS
- [lvgl/lvgl](https://github.com/lvgl/lvgl) `★24.9k` - LVGL is a free, full-featured embedded UI library for devices from small MCUs to 3D-capable MPUs, enhanced by LVGL Pro, a professional editor and tooling. · C
- [slint-ui/slint](https://github.com/slint-ui/slint) `★24.2k` - Slint is an open-source declarative GUI toolkit to build native user interfaces for Rust, C++, JavaScript, or Python apps. · Rust
- [dibingfa/flash-linux0.11-talk](https://github.com/dibingfa/flash-linux0.11-talk) `★22.7k` - 你管这破玩意叫操作系统源码 — 像小说一样品读 Linux 0.11 核心代码 · HTML
- [ruanyf/es6tutorial](https://github.com/ruanyf/es6tutorial) `★21.4k` - 《ECMAScript 6入门》是一本开源的 JavaScript 语言教程，全面介绍 ECMAScript 6 新增的语法特性。 · JavaScript
- [iissnan/hexo-theme-next](https://github.com/iissnan/hexo-theme-next) `★15.8k` - Elegant theme for Hexo. · JavaScript
- [cesanta/mongoose](https://github.com/cesanta/mongoose) `★13.1k` - Embedded web server, with TCP/IP network stack, MQTT and Websocket · C
- [ksky521/nodeppt](https://github.com/ksky521/nodeppt) `★10.3k` - This is probably the best web presentation tool so far! · JavaScript _(archived)_
- [nbedos/termtosvg](https://github.com/nbedos/termtosvg) `★9.8k` - Record terminal sessions as SVG animations · Python _(archived)_
- [jgraph/drawio](https://github.com/jgraph/drawio) `★8.7k` - draw.io is a JavaScript, client-side editor for general diagramming. · JavaScript
- [jerryscript-project/jerryscript](https://github.com/jerryscript-project/jerryscript) `★7.4k` - Ultra-lightweight JavaScript engine for the Internet of Things. · C
- [agegr/pi-web](https://github.com/agegr/pi-web) `★7.3k` - Web UI for the pi coding agent · TypeScript
- [phoboslab/jsmpeg](https://github.com/phoboslab/jsmpeg) `★6.5k` - MPEG1 Video Decoder in JavaScript · JavaScript
- [pablostanley/yoinks](https://github.com/pablostanley/yoinks) `★5.9k` - yoink any video from your terminal. no shady ads. · TypeScript
- [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons) `★5.8k` - Adds file type icons to Vim plugins such as: NERDTree, vim-airline, CtrlP, unite, Denite, lightline, vim-startify and many more · Vim Script
- [foru17/front-end-collect](https://github.com/foru17/front-end-collect) `★5.7k` - 分享自己长期关注的前端开发相关的优秀网站、博客、以及活跃开发者 · JavaScript
- [xuanli199/weekly](https://github.com/xuanli199/weekly) `★3.8k` - 保存玄离199每周科技补全中提到的各种软件和项目 · TypeScript
- [yzhu798/CodingInterviewsNotes](https://github.com/yzhu798/CodingInterviewsNotes) `★2.7k` - 涵盖C++ Primer 5th、 effective C++ 、 STL api和demos C++ 基础知识与理论、 智能指针、C++11、 Git教程 Linux命令 Unix操作系统（进程、线程、内存管理、信号）计算机网络、 数据结构（排序、查找）、数据库、、C++对象模型、 设计模式、算法（《剑指offer》、leetcode、lintcode、hihocoder、《王道程序员求职宝典》）、面试题、嵌入式相关等 · HTML
- [korbinjoe/excalidraw-cn](https://github.com/korbinjoe/excalidraw-cn) `★2.5k` - Excalidraw-CN 是支持中文手写和多画布的 Excalidraw 白板工具。Excalidraw-CN  is a whiteboard supporting Chinese hand draw font and multi-canvas based on Excalidraw. · TypeScript
- [cxinping/PyQt5](https://github.com/cxinping/PyQt5) `★2.4k` - 《PyQt5快速开发与实战》配套代码 · HTML
- [nyakang/nyaterm](https://github.com/nyakang/nyaterm) `★1.8k` - A modern remote terminal workspace · TypeScript
- [michaelliao/learn-javascript](https://github.com/michaelliao/learn-javascript) `★1.7k` - JavaScript全栈教程参考源码
- [binux/ThunderLixianExporter](https://github.com/binux/ThunderLixianExporter) `★747` - export thunder lixian url to aria2/wget · JavaScript
- [phodal/lan](https://github.com/phodal/lan) `★566` - Internet of Things Server Layer with CoAP, WebSocket, MQTT, HTTP Protocol. · JavaScript
- [lulop-k/kurento-rtsp2webrtc](https://github.com/lulop-k/kurento-rtsp2webrtc) `★563` - This example shows how to transform a RTSP feed or an HTTP feed into a low latency WebRTC stream in a simple and seamless manner. · JavaScript
- [chaseleantj/deskworlds](https://github.com/chaseleantj/deskworlds) `★441` - Interactive, living desktop wallpapers · JavaScript
- [fguby/Electron-elf](https://github.com/fguby/Electron-elf) `★317` - 使用electron和live2D开发的类似桌面精灵的应用（A desktop application developed using electron and live2D） · HTML
- [QiShaoXuan/live2DModel](https://github.com/QiShaoXuan/live2DModel) `★301` - 页面上加载的模型 · HTML
- [jae-jae/weapp-github-trending](https://github.com/jae-jae/weapp-github-trending) `★300` - 微信小程序：Github今日榜单 · JavaScript
- [sgl-org/sgl](https://github.com/sgl-org/sgl) `★193` - A modern GUI library for embedded systems · C
- [mfranzon/render](https://github.com/mfranzon/render) `★170` - Render is a skill to create beautiful 3D models directly from coding agents. · HTML
- [iHildy/opencode-synced](https://github.com/iHildy/opencode-synced) `★162` - Sync opencode global configurations between machines with a plugin · TypeScript
- [stayradiated/termcolors](https://github.com/stayradiated/termcolors) `★141` - Import and export between multiple terminal colour scheme formats · JavaScript
- [tjumyk/sdl-tutorial-cn](https://github.com/tjumyk/sdl-tutorial-cn) `★133` - A Chinese translation of Lazy Foo's tutorial for SDL 1.2 · HTML
- [kaiakz/walv](https://github.com/kaiakz/walv) `★116` - [WIP] A LittlevGL-GUI designer on your browser · HTML
- [abhra0897/LameUI](https://github.com/abhra0897/LameUI) `★114` - A very lame UI library for embedded systems. · C
- [YuzukiHD/YuzukiNeko](https://github.com/YuzukiHD/YuzukiNeko) `★85` - YuzukiNeko is a cute pico-sized board with Allwinner F101S3-CXX/F101S4-CXX · HTML
- [rm-hull/8-bit-trip](https://github.com/rm-hull/8-bit-trip) `★3` - Algorithmic music streaming · TypeScript

## Rust 生态

_用 Rust 写的工具与系统_

- [starship/starship](https://github.com/starship/starship) `★60.3k` - ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell! · Rust
- [helix-editor/helix](https://github.com/helix-editor/helix) `★46.6k` - A post-modern modal text editor. · Rust
- [nushell/nushell](https://github.com/nushell/nushell) `★40.7k` - A new type of shell · Rust
- [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) `★23.5k` - ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry. · Rust
- [hyperium/hyper](https://github.com/hyperium/hyper) `★16.4k` - An HTTP library for Rust · Rust
- [microsoft/RustTraining](https://github.com/microsoft/RustTraining) `★14.9k` - Beginner, advanced, expert level Rust training material · Rust
- [bootandy/dust](https://github.com/bootandy/dust) `★12.5k` - A more intuitive version of du in rust · Rust
- [johnthagen/min-sized-rust](https://github.com/johnthagen/min-sized-rust) `★9.9k` - 🦀 How to minimize Rust binary size 📦 https://github.com/johnthagen/min-sized-rust · Rust
- [agrinman/tunnelto](https://github.com/agrinman/tunnelto) `★7.1k` - Expose your local web server to the internet with a public URL. · Rust
- [image-rs/image](https://github.com/image-rs/image) `★5.9k` - Encoding and decoding images in Rust · Rust
- [ooolabdev/ooosplat](https://github.com/ooolabdev/ooosplat) `★2k` - A local desktop app that turns videos and images into 3D Gaussian Splats in one click. · Rust

## Go 生态

_用 Go 写的服务与工具_

- [astaxie/build-web-application-with-golang](https://github.com/astaxie/build-web-application-with-golang) `★43.9k` - A golang ebook intro how to build a web with golang · Go
- [sipeed/picoclaw](https://github.com/sipeed/picoclaw) `★30k` - Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity · Go
- [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) `★5.3k` - 一个基于 Go 语言的全网音乐搜索与下载工具。支持 CLI 命令行与 Web 服务双模式，内置网易云、QQ、酷狗、Bilibili、汽水音乐等 10+ 个主流平台，支持多源并发搜索与无损音质解析。music-dl交流群：755087923 · Go
- [SKeyerror/Psyduck](https://github.com/SKeyerror/Psyduck) `★4.4k` - Record CS knowlegement with XMind, version 2.0. 使用 XMind 记录 Linux 操作系统，网络，C++，Golang 以及数据库的一些设计 · Go
- [logdyhq/logdy-core](https://github.com/logdyhq/logdy-core) `★2.3k` - Realtime log viewer with web UI, tail -f for logs with a web interface browser. · Go
- [rogaha/docker-desktop](https://github.com/rogaha/docker-desktop) `★1.2k` - Docker Desktop enables you to create virtual desktops that can be accessed remotely. It comes with Firefox and Libreoffice already installed! · Shell
- [RonIovine/pshell](https://github.com/RonIovine/pshell) `★28` - A Lightweight, Process-Specific, Embedded Command Line Shell/CLI for C/C++/Python/Go Applications · C++

## 终端与 CLI 工具

_Shell、终端复用器与命令行效率工具_

- [zellij-org/zellij](https://github.com/zellij-org/zellij) `★35.7k` - A terminal workspace with batteries included · Rust
- [mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) `★27.3k` - Our next-generation, interactive app is currently in beta!  Come try it out at terminalthemes.com! Over 750 terminal color schemes/themes for iTerm, with ports to Terminal, Konsole, PuTTY, Xresources, XRDB, Remmina, Termite, XFCE, Tilda, FreeBSD VT, Terminator, Kitty, Windows, Visual Studio,, Ghostty, and dozens more · Shell
- [spf13/spf13-vim](https://github.com/spf13/spf13-vim) `★15.5k` - The ultimate vim distribution · Vim Script
- [bin456789/reinstall](https://github.com/bin456789/reinstall) `★13.7k` - 一键DD/重装脚本 (One-click reinstall OS on VPS) · Shell
- [juewuy/ShellCrash](https://github.com/juewuy/ShellCrash) `★13.6k` - Run sing-box/mihomo as client in shell · Shell
- [tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) `★13.1k` - Persists tmux environment across system restarts. · Shell
- [vnotex/vnote](https://github.com/vnotex/vnote) `★13k` - A pleasant note-taking platform in native C++. · C++
- [oh-my-fish/oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) `★11.4k` - The Fish Shell Framework · Shell
- [ohmybash/oh-my-bash](https://github.com/ohmybash/oh-my-bash) `★7.7k` - A delightful community-driven framework for managing your bash configuration, and an auto-update tool so that makes it easy to keep up with the latest updates from the community. · Shell
- [athityakumar/colorls](https://github.com/athityakumar/colorls) `★5.1k` - A Ruby gem that beautifies the terminal's ls command, with color and font-awesome icons. :tada: · Ruby
- [zhaojh329/rtty](https://github.com/zhaojh329/rtty) `★4k` - 🐛 Access your device from anywhere via the web. · C
- [wangdoc/javascript-tutorial](https://github.com/wangdoc/javascript-tutorial) `★4k` - JavaScript 教程 https://wangdoc.com/javascript · Shell
- [erikw/tmux-powerline](https://github.com/erikw/tmux-powerline) `★3.8k` - ⚡️ A tmux plugin giving you a hackable status bar consisting of dynamic & beautiful looking powerline segments, written purely in bash. · Shell
- [google/gif-for-cli](https://github.com/google/gif-for-cli) `★2.9k` · Python _(archived)_
- [liuchengxu/space-vim](https://github.com/liuchengxu/space-vim) `★2.9k` - :four_leaf_clover: Lean & mean spacemacs-ish Vim distribution · Vim Script
- [1N3/BruteX](https://github.com/1N3/BruteX) `★2.3k` - Automatically brute force all services running on a target. · Shell
- [mathiasbynens/evil.sh](https://github.com/mathiasbynens/evil.sh) `★2.2k` - :speak_no_evil: Subtle and not-so-subtle shell tweaks that will slowly drive people insane. · Shell
- [mislav/dotfiles](https://github.com/mislav/dotfiles) `★1.3k` - bash, zsh, git, tmux, personal toolbox · Shell
- [tmux-python/libtmux](https://github.com/tmux-python/libtmux) `★1.2k` - ⚙️ Python API / wrapper for tmux · Python
- [int32bit/dotfiles](https://github.com/int32bit/dotfiles) `★715` - A set of vim, zsh, git, and tmux configuration files. · Vim script
- [hardhackerlabs/oh-my-nvim](https://github.com/hardhackerlabs/oh-my-nvim) `★502` - A theme-driven, out-of-the-box modern configuration of neovim (HardHackerNvim)💎 · Lua
- [DemonCloud/dotfile](https://github.com/DemonCloud/dotfile) `★388` - YiJun's (Neo)Vim work file · Vim script
- [xuxiaodong/tmuxen](https://github.com/xuxiaodong/tmuxen) `★218` - tmux environment made easy. · Shell
- [lanxuezaipiao/zh-google-styleguide](https://github.com/lanxuezaipiao/zh-google-styleguide) `★71` - Google 开源项目风格指南 (中文版) · Shell

## 网络与安全

_网络协议、代理、翻墙工具与安全研究_

- [aria2/aria2](https://github.com/aria2/aria2) `★43.1k` - aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. It supports HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink. · C++
- [tailscale/tailscale](https://github.com/tailscale/tailscale) `★37.5k` - The easiest, most secure way to use WireGuard and 2FA. · Go
- [ehang-io/nps](https://github.com/ehang-io/nps) `★34.2k` - 一款轻量级、高性能、功能强大的内网穿透代理服务器。支持tcp、udp、socks5、http等几乎所有流量转发，可用来访问内网网站、本地支付接口调试、ssh访问、远程桌面，内网dns解析、内网socks5代理等等……，并带有功能强大的web管理端。a lightweight, high-performance, powerful intranet penetration proxy server, with a powerful web management terminal. · Go
- [gfwlist/gfwlist](https://github.com/gfwlist/gfwlist) `★25.7k` - The one and only one gfwlist here
- [FelisCatus/SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) `★22.6k` - No longer maintained, see pinned issues · CoffeeScript
- [uNetworking/uWebSockets](https://github.com/uNetworking/uWebSockets) `★19k` - Simple, secure & standards compliant web server for the most demanding of applications · C++
- [nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic) `★17.3k` - Revive unavailable songs for Netease Cloud Music · JavaScript
- [zeromq/libzmq](https://github.com/zeromq/libzmq) `★11k` - ZeroMQ core engine in C++, implements ZMTP/3.1 · C++
- [rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng) `★10.7k` - proxychains ng (new generation) - a preloader which hooks calls to sockets in dynamically linked programs and redirects it through one or more socks/http proxies. continuation of the unmaintained proxychains project. the sf.net page is currently not updated, use releases from github release page instead. · C
- [Serial-Studio/Serial-Studio](https://github.com/Serial-Studio/Serial-Studio) `★7.2k` - Open-source telemetry dashboard. Supports UART, BLE, MQTT, Modbus, CAN Bus and more. · C
- [acl-dev/acl](https://github.com/acl-dev/acl) `★3.1k` - C/C++ server and network library, including coroutine,redis client,http/https/websocket,mqtt, mysql/postgresql/sqlite client with C/C++ for Linux, Android, iOS, MacOS, Windows, Harmony,etc.. · C
- [Corvusoft/restbed](https://github.com/Corvusoft/restbed) `★2k` - Corvusoft's Restbed framework brings asynchronous RESTful functionality to C++ applications. · C++
- [Lozy/danted](https://github.com/Lozy/danted) `★1.7k` - Fast script for installing & configing Danted--Socks5 Proxy Server. · Roff
- [chronoxor/CppServer](https://github.com/chronoxor/CppServer) `★1.7k` - Ultra fast and low latency asynchronous socket server & client C++ library with support TCP, SSL, UDP, HTTP, HTTPS, WebSocket protocols and 10K connections problem solution · C++

## 桌面与效率工具

_桌面应用、笔记与效率增强_

- [agalwood/Motrix](https://github.com/agalwood/Motrix) `★56.7k` - A full-featured download manager. · TypeScript
- [WerWolv/ImHex](https://github.com/WerWolv/ImHex) `★55.2k` - 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM. · C++
- [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) `★39.9k` - Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. · TypeScript _(archived)_
- [sindresorhus/quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins) `★18.8k` - List of useful Quick Look plugins for developers
- [TKkk-iOSer/WeChatPlugin-MacOS](https://github.com/TKkk-iOSer/WeChatPlugin-MacOS) `★14.3k` - 微信小助手 · Objective-C
- [vurtun/nuklear](https://github.com/vurtun/nuklear) `★14k` - A single-header ANSI C gui library · C _(archived)_
- [sunnyyoung/WeChatTweak](https://github.com/sunnyyoung/WeChatTweak) `★13.8k` - A command-line tool for tweaking WeChat - 首款微信 macOS 客户端撤回拦截与多开 🔨 · Swift
- [albertlauncher/albert](https://github.com/albertlauncher/albert) `★8k` - A fast and flexible keyboard launcher · C++
- [lc-soft/LCUI](https://github.com/lc-soft/LCUI) `★4.3k` - C library for building user interfaces · C
- [zlgopen/awtk](https://github.com/zlgopen/awtk) `★3.3k` - AWTK = Toolkit AnyWhere(a cross-platform embedded GUI) · C
- [netnr/kms](https://github.com/netnr/kms) `★3.3k` - KMS 激活服务，slmgr 命令激活 Windows 系统、Office · HTML
- [cnjinhao/nana](https://github.com/cnjinhao/nana) `★2.5k` - a modern C++ GUI library · C++
- [mutouyun/cpp-ipc](https://github.com/mutouyun/cpp-ipc) `★2.2k` - C++ IPC Library: A high-performance inter-process communication using shared memory on Linux/Windows. · C++
- [alxnbl/onenote-md-exporter](https://github.com/alxnbl/onenote-md-exporter) `★1.7k` - ConsoleApp to export OneNote notebooks to Markdown formats · C#
- [taggon/highlight](https://github.com/taggon/highlight) `★379` - Rich featured syntax highlighter for Keynote slides. · Swift
- [kaiakz/lv_gui_designer](https://github.com/kaiakz/lv_gui_designer) `★79` - [Pause maintenance, my new related tool - walv]A drag-and-drop, simple LittlevGL-GUI designer built with LittlevGL · C _(archived)_

## 系统与嵌入式

_Linux 内核、驱动、C/C++ 与嵌入式物联网_

- [nlohmann/json](https://github.com/nlohmann/json) `★50.8k` - JSON for Modern C++ · C++
- [google/leveldb](https://github.com/google/leveldb) `★39.5k` - LevelDB is a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values. · C++
- [aristocratos/btop](https://github.com/aristocratos/btop) `★35k` - A monitor of resources · C++
- [nothings/stb](https://github.com/nothings/stb) `★34.8k` - stb single-file public domain libraries for C/C++ · C
- [gabime/spdlog](https://github.com/gabime/spdlog) `★29.7k` - Fast C++ logging library. · C++
- [ggreer/the_silver_searcher](https://github.com/ggreer/the_silver_searcher) `★27.1k` - A code-searching tool similar to ack, but faster. · C
- [fmtlib/fmt](https://github.com/fmtlib/fmt) `★25.9k` - A modern formatting library · C++
- [upx/upx](https://github.com/upx/upx) `★17.9k` - UPX - the Ultimate Packer for eXecutables · C++
- [chenshuo/muduo](https://github.com/chenshuo/muduo) `★16.3k` - Event-driven network library for multi-threaded Linux server in C++11 · C++
- [Tencent/rapidjson](https://github.com/Tencent/rapidjson) `★15.1k` - A fast JSON parser/generator for C++ with both SAX/DOM style API · C++
- [acaudwell/Gource](https://github.com/acaudwell/Gource) `★13.2k` - software version control visualization · C++
- [ShiqiYu/libfacedetection](https://github.com/ShiqiYu/libfacedetection) `★12.8k` - An open source library for face detection in images. The face detection speed can reach 1000FPS. · C++
- [xmake-io/xmake](https://github.com/xmake-io/xmake) `★12.3k` - 🔥 A cross-platform build utility based on Lua · Lua
- [eclipse-mosquitto/mosquitto](https://github.com/eclipse-mosquitto/mosquitto) `★11.3k` - Eclipse Mosquitto - An open source MQTT broker · C
- [jemalloc/jemalloc](https://github.com/jemalloc/jemalloc) `★11.2k` · C
- [bellard/quickjs](https://github.com/bellard/quickjs) `★11k` - Public repository of the QuickJS Javascript Engine. · C
- [r-lyeh/single_file_libs](https://github.com/r-lyeh/single_file_libs) `★10k` - List of single-file C/C++ libraries, with emphasis on clause-less licenses.
- [pocoproject/poco](https://github.com/pocoproject/poco) `★9.5k` - The POCO C++ Libraries are powerful cross-platform C++ libraries for building network- and internet-based applications that run on desktop, server, mobile, IoT, and embedded systems. · C++
- [electronicarts/EASTL](https://github.com/electronicarts/EASTL) `★9.4k` - EASTL stands for Electronic Arts Standard Template Library.  It is an extensive and robust implementation that has an emphasis on high performance. · C++
- [gperftools/gperftools](https://github.com/gperftools/gperftools) `★9k` - Main gperftools repository · C++
- [Xfennec/progress](https://github.com/Xfennec/progress) `★8.9k` - Linux tool to show progress for cp, mv, dd, ... (formerly known as cv) · C
- [Tencent/libco](https://github.com/Tencent/libco) `★8.7k` - libco is a coroutine library which is widely used in wechat  back-end service. It has been running on tens of thousands of machines since 2013. · C++
- [zaphoyd/websocketpp](https://github.com/zaphoyd/websocketpp) `★7.7k` - C++ websocket client/server library · C++
- [libcpr/cpr](https://github.com/libcpr/cpr) `★7.5k` - C++ Requests: Curl for People, a spiritual port of Python Requests. · C++
- [orangeduck/Cello](https://github.com/orangeduck/Cello) `★7.1k` - Higher level programming in C · C
- [me115/design_patterns](https://github.com/me115/design_patterns) `★7.1k` - 图说设计模式 · C++
- [rxi/microui](https://github.com/rxi/microui) `★6.9k` - A tiny immediate-mode UI library · C
- [peng-zhihui/HoloCubic](https://github.com/peng-zhihui/HoloCubic) `★6.7k` - 带网络功能的伪全息透明显示桌面站 · C
- [olikraus/u8g2](https://github.com/olikraus/u8g2) `★6.7k` - U8glib library for monochrome displays, version 2 · C
- [nanomsg/nanomsg](https://github.com/nanomsg/nanomsg) `★6.3k` - nanomsg library · C
- [memononen/nanovg](https://github.com/memononen/nanovg) `★5.7k` - Antialiased 2D vector drawing library on top of OpenGL for UI and visualizations. · C
- [google/bloaty](https://github.com/google/bloaty) `★5.6k` - Bloaty: a size profiler for binaries · C++
- [forhappy/Cplusplus-Concurrency-In-Practice](https://github.com/forhappy/Cplusplus-Concurrency-In-Practice) `★5.5k` - A Detailed Cplusplus Concurrency Tutorial 《C++ 并发编程指南》 · C++
- [google/tcmalloc](https://github.com/google/tcmalloc) `★5.4k` · C++
- [warmcat/libwebsockets](https://github.com/warmcat/libwebsockets) `★5.3k` - canonical libwebsockets.org networking library · C
- [chromiumembedded/cef](https://github.com/chromiumembedded/cef) `★4.8k` - Chromium Embedded Framework (CEF). A simple framework for embedding Chromium-based browsers in other applications. · C++
- [jarro2783/cxxopts](https://github.com/jarro2783/cxxopts) `★4.8k` - Lightweight C++ command line option parser · C++
- [armink/EasyLogger](https://github.com/armink/EasyLogger) `★4.8k` - An ultra-lightweight(ROM<1.6K, RAM<0.3k), high-performance C/C++ log library. | 一款超轻量级(ROM<1.6K, RAM<0.3k)、高性能的 C/C++ 日志库 · C
- [libjpeg-turbo/libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo) `★4.4k` - Main libjpeg-turbo repository · C
- [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) `★4.4k` - Controlling up to three chains of 64x64, 32x32, 16x32 or similar RGB LED displays using Raspberry Pi GPIO · C++
- [civetweb/civetweb](https://github.com/civetweb/civetweb) `★3.5k` - Embedded C/C++ web server · C
- [fukuchi/libqrencode](https://github.com/fukuchi/libqrencode) `★3k` - A fast and compact QR Code encoding library · C
- [mbebenita/Broadway](https://github.com/mbebenita/Broadway) `★2.8k` - A JavaScript H.264 decoder. · C
- [vczh-libraries/GacUI](https://github.com/vczh-libraries/GacUI) `★2.7k` - Native C++ UI library, cross-platform, MVVM and data binding, XML description, multi-language, core/renderer cross-process separation, etc · C++
- [jerryscript-project/iotjs](https://github.com/jerryscript-project/iotjs) `★2.6k` - Platform for Internet of Things with JavaScript http://www.iotjs.net · C
- [PortAudio/portaudio](https://github.com/PortAudio/portaudio) `★2.2k` - PortAudio is a cross-platform, open-source C language library for real-time audio input and output. · C
- [Tencent/TscanCode](https://github.com/Tencent/TscanCode) `★2.1k` - A static code analyzer for C++, C#, Lua · C++
- [NevermindZZT/letter-shell](https://github.com/NevermindZZT/letter-shell) `★1.9k` - letter shell · C
- [chenshuo/recipes](https://github.com/chenshuo/recipes) `★1.9k` - Some code snippets for sharing · C++
- [micknoise/Maximilian](https://github.com/micknoise/Maximilian) `★1.7k` - C++ Audio and Music DSP Library · C++
- [GreycLab/CImg](https://github.com/GreycLab/CImg) `★1.7k` - The CImg Library is a small and open-source C++ toolkit for image processing · C++
- [quiet/quiet](https://github.com/quiet/quiet) `★1.7k` - Transmit data with sound. Includes binaries for soundcards and .wav files. · C
- [embox/embox](https://github.com/embox/embox) `★1.6k` - Modular and configurable OS for embedded applications · C
- [MaJerle/lwrb](https://github.com/MaJerle/lwrb) `★1.5k` - Lightweight generic ring buffer manager library · C
- [jeremy-rifkin/cpptrace](https://github.com/jeremy-rifkin/cpptrace) `★1.5k` - Simple, portable, and self-contained stacktrace library for C++11 and newer · C++
- [achimdoebler/UGUI](https://github.com/achimdoebler/UGUI) `★1.4k` - µGUI - Open Source GUI module for embedded systems · C
- [nilstate/icey](https://github.com/nilstate/icey) `★1.4k` - Real-time media stack and lightweight libwebrtc alternative, built in C++20 · C++
- [eclipse-cyclonedds/cyclonedds](https://github.com/eclipse-cyclonedds/cyclonedds) `★1.4k` - Eclipse Cyclone DDS project · C
- [eliaskosunen/scnlib](https://github.com/eliaskosunen/scnlib) `★1.3k` - scanf for modern C++ · C++
- [bittorrent/libutp](https://github.com/bittorrent/libutp) `★1.2k` - uTorrent Transport Protocol library · C++
- [seppo0010/rlite](https://github.com/seppo0010/rlite) `★1.1k` - self-contained, serverless, zero-configuration, transactional redis-compatible database engine. rlite is to Redis what SQLite is to SQL. · C
- [justdan96/tsMuxer](https://github.com/justdan96/tsMuxer) `★1.1k` - tsMuxer is a transport stream muxer for remuxing/muxing elementary streams, EVO/VOB/MPG, MKV/MKA, MP4/MOV, TS, M2TS to TS to M2TS. Supported video codecs H.264/AVC, H.265/HEVC, VC-1, MPEG2. Supported audio codecs AAC, AC3 / E-AC3(DD+), DTS/ DTS-HD. · C++ _(archived)_
- [cinemast/libjson-rpc-cpp](https://github.com/cinemast/libjson-rpc-cpp) `★985` - C++ framework for json-rpc (json remote procedure call) · C++
- [chirlu/sox](https://github.com/chirlu/sox) `★967` - SoX, Swiss Army knife of sound processing · C
- [rm-hull/luma.oled](https://github.com/rm-hull/luma.oled) `★879` - Python module to drive a SSD1306 / SSD1309 / SSD1322 / SSD1325 / SSD1327 / SSD1331 / SSD1351 / SH1106 OLED · Python
- [MyGUI/mygui](https://github.com/MyGUI/mygui) `★850` - Fast, flexible and simple GUI. · C++
- [openxc/uds-c](https://github.com/openxc/uds-c) `★834` - Unified Diagnostics Service (UDS) and OBD-II (On Board Diagnostics for Vehicles) C Library · C
- [pfalcon/pycopy](https://github.com/pfalcon/pycopy) `★823` - Pycopy - a minimalist and memory-efficient Python dialect. Good for desktop, cloud, constrained systems, microcontrollers, and just everything. · C
- [aizvorski/h264bitstream](https://github.com/aizvorski/h264bitstream) `★809` - A complete set of functions to read and write H.264 video bitstreams, in particular to examine or modify headers. · C
- [Ampixa/sanoTTS](https://github.com/Ampixa/sanoTTS) `★794` - sanoTTS (सानो = 'small' in Nepali): a ~294k-1.4m param neural TTS that runs on a $3 chip or in the browser. Leads SCOREQ/UTMOS in the sub-15M class. · C
- [rachitiitr/modern-cpp-tricks](https://github.com/rachitiitr/modern-cpp-tricks) `★721` - Modern CPP Tricks often useful in Coding Interviews and Competitive Programming
- [ARM-software/optimized-routines](https://github.com/ARM-software/optimized-routines) `★717` - Optimized implementations of various library functions for ARM architecture processors · C
- [leixiaohua1020/VideoEye](https://github.com/leixiaohua1020/VideoEye) `★717` - open-source stream analysis software · C++
- [waywardgeek/sonic](https://github.com/waywardgeek/sonic) `★700` - Simple library to speed up or slow down speech · C
- [activesys/libcstl](https://github.com/activesys/libcstl) `★673` · C
- [gustavogenovese/curl-android-ios](https://github.com/gustavogenovese/curl-android-ios) `★653` - Static libcurl to be used in Android and iOS apps. Build scripts included. No Android source required · C
- [cesanta/slre](https://github.com/cesanta/slre) `★561` - Super Light Regexp engine for C/C++ · C
- [rm-hull/luma.led_matrix](https://github.com/rm-hull/luma.led_matrix) `★543` - Python module to drive LED Matrices & 7-segment displays (MAX7219) and RGB NeoPixels (WS2812 / APA102) · Python
- [crayzeewulf/libserial](https://github.com/crayzeewulf/libserial) `★494` - Serial Port Programming in C++ · C++
- [jorgen/json_struct](https://github.com/jorgen/json_struct) `★474` - json_struct is a single header only C++ library for parsing JSON directly to C++ structs and vice versa · C++
- [cool2528/GDownload](https://github.com/cool2528/GDownload) `★467` - A full-featured download manager developed in C++. · C++
- [ireader/sdk](https://github.com/ireader/sdk) `★461` - portable system call(aio/socket/thread/process/lock/event/pipe) · C
- [shichaog/WebRTC-audio-processing](https://github.com/shichaog/WebRTC-audio-processing) `★428` - webrtc audio processing · C++
- [virinext/hevcesbrowser](https://github.com/virinext/hevcesbrowser) `★387` - HEVCESBrowser is a tool for analyzing hevc(h265) bitstreams · C++
- [openxc/isotp-c](https://github.com/openxc/isotp-c) `★363` - An implementation of the ISO-TP (ISO15765-2) CAN protocol in C · C
- [Loki-Astari/ThorsAnvil](https://github.com/Loki-Astari/ThorsAnvil) `★318` - C++ Web-Libraries Server, Mongo, Slack, JSON, Slack · C++
- [raas/mbw](https://github.com/raas/mbw) `★292` - Memory Bandwidth Benchmark · C
- [fanchy/fflib](https://github.com/fanchy/fflib) `★291` - FFLib is a lightweight c++ framework.FFlib is mainly designed for game server developing. But some components in FFLib is in common use. For example socket&net module, log module, thread&lock, tools for performance & memory leak check.用于分布式程序的c++类库，封装了socket、rpc、lua、CQRS框架、算法等组件，适于SNS、WEBGAME、MMO后台程序， about C++,linux socket,lua,rpc,broker,cqrs,timer,log libary · C
- [hartkopp/can-isotp](https://github.com/hartkopp/can-isotp) `★289` - Linux Kernel Module for ISO 15765-2:2016 CAN transport protocol PLEASE NOTE: This module is part of the mainline Linux kernel since version 5.10 · C
- [esp-arduino-libs/ESP32_Display_Panel](https://github.com/esp-arduino-libs/ESP32_Display_Panel) `★283` - Display driver and GUI porting library designed for ESP series SoCs (ESP32, ESP32-S3, ESP32-P4, etc.) · C
- [xyz347/x2struct](https://github.com/xyz347/x2struct) `★265` - Convert between json string and c++ object.  json字符串和c++结构体之间互相转换 · C++
- [mikewei/shm_container](https://github.com/mikewei/shm_container) `★236` - A collection of shared memory containers for high performance server · C++
- [MaJerle/lwshell](https://github.com/MaJerle/lwshell) `★216` - Lightweight shell implementation for embedded systems · C
- [openxc/vi-firmware](https://github.com/openxc/vi-firmware) `★211` - OpenXC-compatible firmware for PIC32 and LPC1768 · C++
- [Privatehive/libONVIF](https://github.com/Privatehive/libONVIF) `★202` - Yet another ONVIF library · C++
- [fanchy/fflua](https://github.com/fanchy/fflua) `★200` - FFLUA 是嵌入LUA，注册C++相关的对象到lua的封装库, wraper for C++ embedding lua, extend C++ to lua · C++
- [dimtass/DSP-Cpp-filters](https://github.com/dimtass/DSP-Cpp-filters) `★188` - DSP C++ audio filters · C++
- [Ansersion/myRtspClient](https://github.com/Ansersion/myRtspClient) `★164` - A RTSP client based on jrtplib · C++
- [troglobit/sysklogd](https://github.com/troglobit/sysklogd) `★120` - BSD syslog daemon with syslog()/syslogp(), i.e., structured logging API replacement for Linux, RFC3164 + RFC5424 · C
- [roleoroleo/onvif_simple_server](https://github.com/roleoroleo/onvif_simple_server) `★94` - Light implementation of an onvif server intended for use in resource-constrained devices · C
- [OpenIPC/divinus](https://github.com/OpenIPC/divinus) `★80` - Multi-platform open source streamer · C
- [mobius3/font-chef](https://github.com/mobius3/font-chef) `★58` - A font cooking library · C
- [nwtime/linuxptp](https://github.com/nwtime/linuxptp) `★43` - Linux PTP Project · C
- [trezor-graveyard/trezor-qrenc](https://github.com/trezor-graveyard/trezor-qrenc) `★38` - :warning: OBSOLETE. DO NOT USE! · C
- [fengbingchun/OCR_Test](https://github.com/fengbingchun/OCR_Test) `★34` - it contains some open source ocr code · C
- [VFR-maniac/opencore-amr](https://github.com/VFR-maniac/opencore-amr) `★32` - Unofficial mirror of the official opencore-amr repository. · C++
- [ilixi/ilixi](https://github.com/ilixi/ilixi) `★23` - lightweight C++ application framework for embedded Linux systems · C++
- [lindenis-org/mpp_sample](https://github.com/lindenis-org/mpp_sample) `★20` - Allwinner V5 mpp sample code · C
- [Corvusoft/restless](https://github.com/Corvusoft/restless) `★19` - Corvusoft's Restless framework brings asynchronous RESTful client functionality to C++11 applications. http://www.corvusoft.co.uk · C++
- [codec2021/codecscope](https://github.com/codec2021/codecscope) `★18` · C++
- [jahrulnr/esp32-picoTTS](https://github.com/jahrulnr/esp32-picoTTS) `★15` - ESP32 TTS library with PicoTTS engine - Convert text to speech with multi-core processing and UTF-8 support · C
- [sunao2002002/mem_proc](https://github.com/sunao2002002/mem_proc) `★15` · C
- [byteman/mgcpp](https://github.com/byteman/mgcpp) `★5` - it's minigui 's c++ implement · C++
- [hevnsnt/artinchip-linux](https://github.com/hevnsnt/artinchip-linux) `★4` - Linux driver for ArtInChip USB bar monitors (ZHAOCAILIN 11.3" 1920x440). Reverse-engineered RSA auth + JPEG frame streaming. Supports websites, YouTube, video files. · Python

## 开发工具与 DevOps

_编辑器、Git、容器、CI/CD 与效率工具_

- [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) `★133.8k` - Virtual whiteboard for sketching hand-drawn like diagrams · TypeScript
- [littlecodersh/ItChat](https://github.com/littlecodersh/ItChat) `★26.5k` - A complete and graceful API for Wechat. 微信个人号接口、微信机器人及命令行微信，三十行即可自定义个人号机器人。 · Python
- [fangzesheng/free-api](https://github.com/fangzesheng/free-api) `★16.3k` - 收集免费的接口服务,做一个api的搬运工
- [Josverl/micropython-stubber](https://github.com/Josverl/micropython-stubber) `★255` - Generate and maintain stubs for different MicroPython ports to use with VSCode and Pylance, PyRight, Thonny, PyCharm or MyPy · Python

## Python 工具

_其余 Python 脚本与工具_

- [datalab-to/marker](https://github.com/datalab-to/marker) `★40.4k` - Convert PDF to markdown + JSON quickly with high accuracy · Python
- [Diolinux/PhotoGIMP](https://github.com/Diolinux/PhotoGIMP) `★18.4k` - A Patch for GIMP 3+ for Photoshop Users · Python
- [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) `★15.9k` - Open-source State-of-the-art TTS model which runs on a CPU 😻 · Python
- [pwr-Solaar/Solaar](https://github.com/pwr-Solaar/Solaar) `★9.5k` - Linux device manager for Logitech devices · Python
- [mesonbuild/meson](https://github.com/mesonbuild/meson) `★6.6k` - The Meson Build System · Python
- [thunil/TecoGAN](https://github.com/thunil/TecoGAN) `★6.1k` - This repo contains source code and materials for the TEmporally COherent GAN SIGGRAPH project. · Python
- [liuwons/wxBot](https://github.com/liuwons/wxBot) `★5.3k` - Deprecated · Python
- [gumyr/build123d](https://github.com/gumyr/build123d) `★3.4k` - A python CAD programming library · Python
- [mooz/percol](https://github.com/mooz/percol) `★3.3k` - adds flavor of interactive filtering to the traditional pipe concept of UNIX shell · Python
- [zhuifengshen/DingtalkChatbot](https://github.com/zhuifengshen/DingtalkChatbot) `★1.3k` - 钉钉群自定义机器人消息Python封装 · Python
- [rdnetto/YCM-Generator](https://github.com/rdnetto/YCM-Generator) `★904` - Generates config files for YouCompleteMe (https://github.com/Valloric/YouCompleteMe) · Python _(archived)_
- [taizilongxu/douban.fm](https://github.com/taizilongxu/douban.fm) `★780` - :radio: douban.fm based on Python · Python
- [xcLee001/SonicVale](https://github.com/xcLee001/SonicVale) `★633` - 一个开源的多角色、多情绪 AI 配音生成平台，支持小说、剧本、视频等内容的自动配音与导出。 · Python
- [tothi/pwn-hisilicon-dvr](https://github.com/tothi/pwn-hisilicon-dvr) `★384` · Python
- [sr99622/libonvif](https://github.com/sr99622/libonvif) `★329` - ONVIF library in python with utility program · C++
- [pfalcon/pycopy-lib](https://github.com/pfalcon/pycopy-lib) `★263` - Standard library of the Pycopy project, minimalist and light-weight Python language implementation · Python
- [2549850807/Easy_Menu](https://github.com/2549850807/Easy_Menu) `★190` - 简单、实用、适配所有显示设备、移植简单、支持可视化配置的嵌入式菜单框架。A simple, practical, adaptable to all display devices, easy-to-port, and supporting visual configuration embedded menu framework. · Python
- [nims11/IPod-Shuffle-4g](https://github.com/nims11/IPod-Shuffle-4g) `★175` - 4th gen IPod Shuffle songs and playlist tool. · Python
- [youkaichao/onenote-to-markdown](https://github.com/youkaichao/onenote-to-markdown) `★69` - OneNote导出成Markdown文件的脚本 · Python
- [danielballan/photomosaic](https://github.com/danielballan/photomosaic) `★57` - Assemble thumbnail-sized images from a large collection into a tiling which, viewed at a distance, gives the impression of one large photo. · Python
- [sumary/dmusic-plugin-baidumusic](https://github.com/sumary/dmusic-plugin-baidumusic) `★48` - BaiduMusic Plugin for Deepin Music Player · Python
- [dairoot/miloco-sdk](https://github.com/dairoot/miloco-sdk) `★44` · Python
- [562590763/CADDesigner-Code](https://github.com/562590763/CADDesigner-Code) `★24` · Python
- [csrgxtu/Drogo](https://github.com/csrgxtu/Drogo) `★24` - Hacker的微信聊天方式 · Python
- [PerpetualSmile/convert_picture_to_snowing_gif](https://github.com/PerpetualSmile/convert_picture_to_snowing_gif) `★10` - 给一张静态图片增加下雪动态效果，并生成gif效果图 · Python
- [coffee-it/uargparse](https://github.com/coffee-it/uargparse) `★2` - Argparse implementation for MicroPython · Python

## 字体与设计

_字体、图标与设计资源_

- [subframe7536/maple-font](https://github.com/subframe7536/maple-font) `★29.3k` - Maple Mono: Open source monospace font with round corner, ligatures and Nerd-Font icons for IDE and terminal, fine-grained customization options. 带连字和控制台图标的圆角等宽字体，中英文宽度完美2:1，细粒度的自定义选项 · Python
- [lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai) `★26.3k` - An open-source Chinese font derived from Fontworks' Klee One. 一款开源中文字体，基于 FONTWORKS 出品字体 Klee One 衍生。 · Shell
- [lxgw/LxgwWenKai-Screen](https://github.com/lxgw/LxgwWenKai-Screen) `★2.2k` - LXGW WenKai for Screen Reading.
- [jonacruz89/SAWARATSUKI.ServiceLogos](https://github.com/jonacruz89/SAWARATSUKI.ServiceLogos) `★456` - ロゴを可愛く作ろう できる限りForkはしないでください

## 未分类

_尚未归类，可在 config.yaml 中通过 topics / overrides 配置分类。_

- [geekan/HowToLiveLonger](https://github.com/geekan/HowToLiveLonger) `★35.8k` - 程序员延寿指南 | A programmer's guide to live longer
- [w7corp/easywechat](https://github.com/w7corp/easywechat) `★10.4k` - 📦 一个 PHP 微信 SDK · PHP
- [phaselden/FlipIt](https://github.com/phaselden/FlipIt) `★1.3k` - Flip Clock screensaver · C#
- [dieforfree/qart4j](https://github.com/dieforfree/qart4j) `★891` - QR code ASCII art for java · Java
- [cxmforever/notice-board](https://github.com/cxmforever/notice-board) `★412` - mmy
- [idealclover/Love-Gift](https://github.com/idealclover/Love-Gift) `★339` - 💌 A love gift for my ex-girlfriend. · CoffeeScript _(archived)_
- [xianweics/refator-code](https://github.com/xianweics/refator-code) `★86` - 重构 - 改善既有代码的设计

<!-- oh-my-awesome:end -->
