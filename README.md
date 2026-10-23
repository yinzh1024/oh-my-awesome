# oh-my-awesome

> 我的 GitHub Star 导航 —— 自动同步、分类呈现。
> 数据来自 GitHub API，由本仓库的定时任务每 6 小时更新一次。

**快速了解**：分类规则在 [config.yaml](./config.yaml)（topics / languages / overrides 三
层机制），生成逻辑在 [src/oh_my_awesome](./src/oh_my_awesome)，定时任务在
[sync-stars.yml](./.github/workflows/sync-stars.yml)。

**本地更新**：

```bash
pip install .
export GITHUB_TOKEN=ghp_xxx      # 或写入 .env
export DEEPSEEK_API_KEY=sk-xxx   # LLM 中文摘要（可选，不设则跳过）
oh-my-awesome sync --llm --push  # 拉取 → 摘要 → 分类 → 生成 README → 提交推送
```

<!-- oh-my-awesome:begin -->
> 共 **454** 个项目 · 最后更新：2026-10-23 11:50 UTC · 数据采集：2026-10-23 11:50 UTC

## 目录

- [Awesome 列表](#awesome-列表) (13)
- [AI / LLM](#ai--llm) (62)
- [学习与教程](#学习与教程) (25)
- [音视频与流媒体](#音视频与流媒体) (51)
- [移动开发](#移动开发) (25)
- [前端与 Web](#前端与-web) (52)
- [Rust 生态](#rust-生态) (11)
- [Go 生态](#go-生态) (7)
- [终端与 CLI 工具](#终端与-cli-工具) (24)
- [网络与安全](#网络与安全) (14)
- [桌面与效率工具](#桌面与效率工具) (16)
- [系统与嵌入式](#系统与嵌入式) (114)
- [开发工具与 DevOps](#开发工具与-devops) (4)
- [Python 工具](#python-工具) (26)
- [字体与设计](#字体与设计) (4)
- [未分类](#未分类) (6)

## Awesome 列表

_收集类清单，找资料先看这里_

- [996icu/996.ICU](https://github.com/996icu/996.ICU) `★277.2k` - 抗议996工作制的GitHub仓库，开发者可添加公司黑名单并star表达支持
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) `★123.1k` - 收录各大品牌设计系统的 DESIGN.md 文件，放入项目即可让编码 Agent 生成风格统一的 UI
- [fffaraz/awesome-cpp](https://github.com/fffaraz/awesome-cpp) `★74k` - 精选 C/C++ 框架、库、资源和工具链的 awesome 清单，涵盖 cppcon 等社区动态
- [1c7/chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) `★61.9k` - 汇集中国独立开发者项目与产品，展示大家都在做什么，涵盖各类创意作品与技术实践
- [herrbischoff/awesome-macos-command-line](https://github.com/herrbischoff/awesome-macos-command-line) `★31k` - 汇总 macOS 终端命令行技巧与工具的资源列表，涵盖系统管理、网络、安全等实用命令 _(archived)_
- [sindresorhus/awesome-electron](https://github.com/sindresorhus/awesome-electron) `★27.3k` - 汇集用 Electron 构建跨平台桌面应用所需的工具、库、教程与示例资源，是精选的 awesome 清单
- [mzlogin/awesome-adb](https://github.com/mzlogin/awesome-adb) `★12.5k` - 汇总 ADB 常用命令与用法，涵盖设备连接、应用管理、文件传输、日志调试等 Android 开发调试场景
- [jobbole/awesome-cpp-cn](https://github.com/jobbole/awesome-cpp-cn) `★11.2k` - C++ 资源大全中文版，涵盖标准库、Web 框架、AI、数据库、图像处理、机器学习、日志与代码分析等，由开源前哨和 CPP开发者 维护
- [jobbole/awesome-c-cn](https://github.com/jobbole/awesome-c-cn) `★6.7k` - C 资源大全中文版，涵盖构建系统、编译器、数据库、加密、教程指南、书籍与库等
- [LewisJEllis/awesome-lua](https://github.com/LewisJEllis/awesome-lua) `★4.6k` - 精选优质 Lua 库与资源合集，涵盖包管理、框架、工具等分类
- [JsonChao/Awesome-Android-Notebook](https://github.com/JsonChao/Awesome-Android-Notebook) `★3.4k` - 面向 Android 开发者的完整进阶学习与面试指南，涵盖 Java、Android 知识点，持续更新
- [pfalcon/awesome-micropython](https://github.com/pfalcon/awesome-micropython) `★192` - 精选 MicroPython 资源合集，涵盖嵌入式与 IoT 开发库、工具、教程及项目
- [xuxiaodong/awesome-shell](https://github.com/xuxiaodong/awesome-shell) `★167` - 精选 Shell 脚本、命令行工具与框架的中文资源合集，涵盖 Bash、Zsh 等实用技巧

## AI / LLM

_大模型、Agent、语音与视觉 AI 工程实践_

- [morluto/rea](https://github.com/morluto/rea) `★370k` - 用 AI agent 逆向分析应用行为与原生二进制，TypeScript 编写的 CLI 工具，支持 Claude Code 和 Codex，适用于 CTF · TypeScript
- [affaan-m/ECC](https://github.com/affaan-m/ECC) `★286.9k` - 为 Claude Code、Codex、Cursor 等 AI 编程代理提供技能、记忆、安全与性能优化的 harness 系统 · JavaScript
- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) `★258.9k` - 基于 TypeScript 的 AI Agent 框架，一切皆插件，支持 cordis 依赖注入与 dsh 插件生态 · TypeScript
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) `★256.4k` - 基于Python的AI代理框架，支持Anthropic、ChatGPT、Claude等模型，可随使用不断成长进化 · Python
- [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) `★165.1k` - 基于 Gradio 的 Stable Diffusion 浏览器界面，支持文生图、图生图与插件扩展 · Python
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) `★134.4k` - 输入主题或关键词，用 LLM 加自动化流程一键生成高清短视频，Python 实现，支持字幕与 FFmpeg 合成 · Python
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) `★101.2k` - 让 AI agent 用一条 CLI 读取和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书，零 API 费用 · Python
- [infiniflow/ragflow](https://github.com/infiniflow/ragflow) `★92.7k` - 融合前沿 RAG 与 Agent 能力的开源检索引擎，为 LLM 构建优质上下文层，支持智能体检索与搜索 · Go
- [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) `★91.6k` - 轻量级 OCR 工具包，将 PDF 或图片转为结构化数据，支持 100 多种语言，衔接图像与 LLM · Python
- [opencv/opencv](https://github.com/opencv/opencv) `★91.3k` - 开源计算机视觉库，提供图像处理、目标检测与深度学习推理等 C++ 与 Python 接口 · C++
- [tt-a1i/archify](https://github.com/tt-a1i/archify) `★88.1k` - 把想法、方案或代码库转成精美交互式架构图，支持 Claude Code、Codex 等编码智能体的 Agent Skill · JavaScript
- [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) `★87.8k` - 把任意代码转成可交互知识图谱，支持探索、搜索与提问，兼容 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等，TypeS · TypeScript
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) `★82.4k` - 将 PDF、Office 等复杂文档转为 LLM 可用的 Markdown/JSON，基于 Python，支持 OCR 与版面分析，服务 Agentic 工作流 · Python
- [netdata/netdata](https://github.com/netdata/netdata) `★81.1k` - 面向精益团队的 AI 全栈可观测性平台，用 Go 编写，支持实时监控、告警与数据可视化，兼容 Docker 和 Grafana · Go
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) `★70.4k` - 用 HTML 写动画，经 Puppeteer 与 FFmpeg 渲染成视频，内置 GSAP 与 MCP，专为 AI agent 设计 · TypeScript
- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) `★70.3k` - 输入 mass ulw 关键词即可调度多 AI 代理做图工程，TypeScript 编写，兼容 Claude、ChatGPT、Codex 等 · TypeScript
- [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) `★64.2k` - 为 Claude Code 打造的轻量级元提示与上下文工程系统，用规范驱动开发流程 · JavaScript _(archived)_
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) `★60.2k` - 为 Claude Code、Codex、GitHub Copilot 等 AI 编程工具提供 45 种编辑级图表设计，输出自包含 HTML + SVG，拒绝 M · HTML
- [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) `★54.5k` - 面向敏捷 AI 驱动开发的突破性方法论，用 Python 实现，融合上下文工程与规范驱动开发，覆盖完整 SDLC · Python
- [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr) `★39.6k` - 开源引擎，将连续内容流转化为搜索与监控，支持持久化摄取、混合搜索、告警及格式模型业务规则插件，Go 编写 · Go
- [suno-ai/bark](https://github.com/suno-ai/bark) `★39.3k` - 基于文本提示生成逼真多语言语音及音效的Transformer音频模型，支持笑声、音乐等非语言声音 · Jupyter Notebook
- [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) `★39k` - 基于 TypeScript 的 AI 提示词优化工具，可改写润色 prompt 并支持测试对比，提升 LLM 输出效果 · TypeScript
- [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) `★36.8k` - 基于实时本地目标检测的 IP 摄像头 NVR，支持 Google Coral 与 Home Assistant 集成 · Python
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) `★36.3k` - 深度集成 IDE 的编码智能体，基于 TypeScript 与 Bun 构建，支持 Claude 等 LLM · TypeScript
- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) `★35.9k` - 基于 DeepSeek 的 Go 语言命令行编码智能体，专攻复杂软件工程任务 · Go
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora) `★35.2k` - 开源 LLM 知识平台，用 Go 编写，将原始文档转化为可查询的 RAG、自主推理 Agent 和自我维护的 Wiki · Go
- [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) `★33k` - 基于 Rust 的轻量高速全自主 AI 个人助理基础设施，跨 OS 跨平台部署，组件可自由替换 · Rust
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) `★31.8k` - 基于MCP协议的ESP32聊天机器人，用C++开发，可在嵌入式硬件上实现语音交互 · C++
- [alibaba/page-agent](https://github.com/alibaba/page-agent) `★29.6k` - 用自然语言操控网页界面的 TypeScript 页面内 GUI agent，支持 MCP · TypeScript
- [slopus/happy](https://github.com/slopus/happy) `★24.3k` - 一个 TypeScript 应用，统一调度 Claude、Codex 和 Grok，复用你已付费的订阅，MIT 开源 · TypeScript
- [wechaty/wechaty](https://github.com/wechaty/wechaty) `★23.4k` - TypeScript 编写的对话式 RPA SDK，六行代码即可接入微信、QQ 等平台构建聊天机器人 · TypeScript
- [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) `★22.7k` - 让 AI agent 通过 Python 生成 STEP、STL 等 CAD 模型，为机械工程与机器人设计赋予建模超能力 · Python
- [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) `★21.5k` - 277 个即插即用 AI 专家角色，适配 Claude Code、Cursor、Copilot 等 20 种工具，覆盖 20 个部门，含 64 个中国市场原创智 · Shell
- [lexmount/moli](https://github.com/lexmount/moli) `★20.2k` - 为 AI agent 打造的无头浏览器，Rust 编写，轻量快速且高兼容，支持 Playwright 与 Puppeteer · Rust
- [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) `★17.7k` - 免费开源的图像处理套件，支持200多种格式，提供命令行工具和API，可用于创建、编辑、转换和显示图像，跨平台集成 · C
- [memvid/memvid](https://github.com/memvid/memvid) `★16.6k` - 用 Rust 编写的无服务器单文件记忆层，替代复杂 RAG 流程，为 AI Agent 提供即时检索与长期记忆 · Rust
- [microsoft/Bringing-Old-Photos-Back-to-Life](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life) `★15.7k` - 基于 PyTorch 的 GAN 框架，修复破损老照片的划痕、噪点并还原色彩，CVPR 2020 oral 论文官方实现 · Python _(archived)_
- [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) `★15.5k` - 基于 next-gen Kaldi 和 onnxruntime 的离线语音工具包，支持语音识别、合成、说话人分离、增强、分离与 VAD，覆盖嵌入式、Androi · C++
- [PaddlePaddle/PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech) `★12.7k` - 基于 PaddlePaddle 的易用语音工具箱，涵盖自监督学习、流式 ASR 与标点恢复、流式 TTS、声纹识别、端到端语音翻译及关键词检测，曾获 NAACL · Python
- [dataelement/bisheng](https://github.com/dataelement/bisheng) `★12.1k` - 面向企业级 AI 应用的开源大模型 DevOps 平台，集成 GenAI 工作流、RAG、Agent、模型管理、评测、SFT 与可观测性 · Python
- [x-hw/amazing-qr](https://github.com/x-hw/amazing-qr) `★10.8k` - 用 Python 生成艺术化二维码，支持彩色图片与 GIF 动态二维码 · Python
- [niedev/RTranslator](https://github.com/niedev/RTranslator) `★10.5k` - 基于 ONNX Runtime 与 NLLB 模型的 Android 本地实时翻译应用，支持蓝牙 LE 耳机，无需联网 · Java
- [openframeworks/openFrameworks](https://github.com/openframeworks/openFrameworks) `★10.4k` - 社区驱动的跨平台 C++ 创意编程工具包，支持图形、音频、计算机视觉，可部署到 iOS、Android、Linux 及 Emscripten · C++
- [pipipi-pikachu/PPTist](https://github.com/pipipi-pikachu/PPTist) `★9.4k` - 基于 Vue 的在线 PPT 应用，复刻 PowerPoint 常用功能，支持在线编辑演示、AIPPT 和本地 PPTX 预览 · Vue
- [chthollyphile/folia-major](https://github.com/chthollyphile/folia-major) `★9k` - 基于 TypeScript 与 React 的 PWA 音乐播放器，支持本地、Navidrome 及第三方在线音源，主打绚丽歌词动画与 AI 能力 · TypeScript
- [wzpan/wukong-robot](https://github.com/wzpan/wukong-robot) `★7.1k` - 简单灵活的中文语音对话机器人，支持ChatGPT多轮对话与脑机交互，基于Python，可作智能音箱 · Python
- [liuruoze/EasyPR](https://github.com/liuruoze/EasyPR) `★6.4k` - 基于 OpenCV 的 C++ 中文车牌识别项目，支持非受限场景，提供数据集与神经网络模型，曾用于 CGCSTCD 2017 竞赛 · C++
- [memovai/mimiclaw](https://github.com/memovai/mimiclaw) `★5.8k` - 在5美元芯片上跑个人 AI 助手，无需 Linux、Node.js、树莓派或 VPS，用 C 实现端侧硬件智能体操作系统与记忆 · C
- [the-open-agent/openagent](https://github.com/the-open-agent/openagent) `★5.7k` - 基于 LLM、RAG 与 agent 循环的下一代个人 AI 助手，用 Go 编写，支持 computer-use、browser-use 和编码 agent · Go
- [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) `★4.5k` - 1 亿参数多语言 TTS 模型，支持 CPU 实时推理、声音克隆与 48 kHz 立体声生成，基于 ONNX · Python
- [ben1234560/AiLearning-Theory-Applying](https://github.com/ben1234560/AiLearning-Theory-Applying) `★3.6k` - 涵盖AI基础、Transformer、NLP、ML、DL与Kaggle竞赛的实战教程，含大量注释和数据集，助你快速上手并复现 · Jupyter Notebook
- [makelove/OpenCV-Python-Tutorial](https://github.com/makelove/OpenCV-Python-Tutorial) `★3.4k` - 基于 Python 的 OpenCV 教程，涵盖 imread、imshow、VideoCapture 与 Kinect 等图像和视频处理示例 · Python
- [RightNow-AI/picolm](https://github.com/RightNow-AI/picolm) `★2.2k` - 在256MB内存的10美元开发板上运行10亿参数大模型，C语言实现，支持量化与嵌入式推理 · C
- [Thmen/EGVSR](https://github.com/Thmen/EGVSR) `★957` - 基于Python的高效通用视频超分辨率框架，支持实时VSR处理 · Python
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) `★899` - DeepSeek Harness 从零上手手册，涵盖安装、插件开发、性能调优与多 Agent 实测对比，附中英 PDF · HTML
- [Xiaobin-Rong/gtcrn](https://github.com/Xiaobin-Rong/gtcrn) `★758` - 超轻量级语音增强模型GTCRN的官方Python实现，适合边缘设备部署 · Python
- [symisc/ascii_art](https://github.com/symisc/ascii_art) `★742` - 纯C实现的实时ASCII艺术渲染库，可将图像转为字符画，适用于嵌入式与图像处理场景 · C
- [worldveil/photomosaic](https://github.com/worldveil/photomosaic) `★698` - 用机器学习与相似度搜索把家庭照片拼成趣味马赛克、GIF和壁画，基于 Jupyter Notebook 实现 · Jupyter Notebook
- [huakunyang/SummerTTS](https://github.com/huakunyang/SummerTTS) `★545` - 基于 C++ 的独立中英文语音合成项目，无需网络和额外依赖，一键编译即可本地运行，采用 VITS 模型 · C++
- [ranchlai/mandarin-tts](https://github.com/ranchlai/mandarin-tts) `★477` - 基于 PyTorch 实现 FastSpeech 2 的中文普通话语音合成，用 WaveGlow 声码器，支持标贝和 AISHELL-3 数据集 · Python
- [benjaminwan/ChineseTtsTflite](https://github.com/benjaminwan/ChineseTtsTflite) `★416` - 基于TensorFlow TTS的安卓离线中文语音合成引擎，用Java开发，专为TfLite模型测试打造 · Java
- [EdwinjJ1/3d-print-skill](https://github.com/EdwinjJ1/3d-print-skill) `★29` - 为 Claude Code 提供 3D 打印技能，先搜索后建模，输出适配 Bambu Studio、PrusaSlicer、Cura 的流形安全模型 · Python

## 学习与教程

_教程、文档、面试与算法刷题_

- [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) `★205.5k` - 免费域名注册平台，配套实用 DNS 学习教程与文档，帮助任何人轻松上手域名解析 · Markdown
- [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) `★162.6k` - 一页掌握命令行，涵盖 bash、Linux、macOS、Unix 和 Windows 的实用技巧与快捷键
- [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) `★119.3k` - 收录免费中文编程书籍，涵盖 Android、iOS、JavaScript、Kotlin 等方向，支持社区投稿
- [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) `★83.4k` - 收录小学到大学各阶段PDF教材，覆盖全学科，适合自学与备课参考 · Roff
- [MisterBooo/LeetCodeAnimation](https://github.com/MisterBooo/LeetCodeAnimation) `★76.7k` - 用动画演示 LeetCode 题解思路，支持单步、回看、变速与语音讲解，涵盖 Java、C 等多语言实现 · Java
- [huihut/interview](https://github.com/huihut/interview) `★38.3k` - 涵盖 C/C++ 面试核心知识，含语言、数据结构、算法、操作系统、网络与链接装载库，附面经和内推 · C++
- [exacity/deeplearningbook-chinese](https://github.com/exacity/deeplearningbook-chinese) `★38k` - 深度学习经典教材 Deep Learning 中文翻译，基于 TeX 排版，社区协作完成 · TeX
- [0voice/interview_internal_reference](https://github.com/0voice/interview_internal_reference) `★37.3k` - 汇总阿里腾讯百度美团头条等大厂2025年最新技术面试题与答案，覆盖MySQL、Redis、Nginx、MongoDB、网络及高性能等方向 · Python
- [carbon-app/carbon](https://github.com/carbon-app/carbon) `★36.1k` - 把源码变成精美图片并分享，支持 GitHub Gist 导入，基于 JavaScript 的代码截图工具 · JavaScript
- [changkun/modern-cpp-tutorial](https://github.com/changkun/modern-cpp-tutorial) `★25.9k` - 覆盖 C++11 到 C++26 新特性的实战教程，含代码示例与在线电子书 · C++
- [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) `★21.9k` - 从睡眠、饮食、运动到情绪管理，系统梳理人体调优方法，助你健康活到150岁
- [SwiftGGTeam/the-swift-programming-language-in-chinese](https://github.com/SwiftGGTeam/the-swift-programming-language-in-chinese) `★21.2k` - Apple 官方 Swift 编程语言指南的中文翻译，基于 Markdown 持续同步更新 · Markdown
- [programthink/books](https://github.com/programthink/books) `★20.3k` - 涵盖多学科的电子书资源清单，附下载链接，由编程随想整理
- [leandromoreira/digital_video_introduction](https://github.com/leandromoreira/digital_video_introduction) `★16.4k` - 动手学视频技术：图像、编解码（av1、vp9、h265）与 ffmpeg 编码，含多国语言翻译 · Jupyter Notebook
- [ruanyf/document-style-guide](https://github.com/ruanyf/document-style-guide) `★13k` - 阮一峰制定的中文技术文档写作规范，涵盖标题、段落、标点、代码等排版约定
- [0voice/from_coder_to_expert](https://github.com/0voice/from_coder_to_expert) `★11.2k` - 汇集大厂内部PDF与PPT，梳理程序员晋升CTO所需的技术与管理知识体系
- [redguardtoo/mastering-emacs-in-one-year-guide](https://github.com/redguardtoo/mastering-emacs-in-one-year-guide) `★6.4k` - 一年内从零掌握 Emacs 的进阶指南，涵盖配置、插件与高效工作流
- [tboox/tbox](https://github.com/tboox/tbox) `★5.1k` - 类 glib 的跨平台 C 库，涵盖容器、算法、协程、迭代器、JSON、网络与 plist 解析 · C
- [maicss/PyQt-Chinese-tutorial](https://github.com/maicss/PyQt-Chinese-tutorial) `★3.6k` - 基于 GitBook 的 PyQt5/PyQt6 中文教程，系统讲解 Python3 桌面 GUI 开发
- [pezy/LeetCode](https://github.com/pezy/LeetCode) `★3.5k` - 用 C++11 和 Python3 实现 LeetCode 题解，附带思路笔记 · C++
- [widuu/chinese_docker](https://github.com/widuu/chinese_docker) `★2.7k` - Docker 中文文档，系统讲解镜像、容器、仓库等核心概念与命令用法
- [emacs-china/Spacemacs-rocks](https://github.com/emacs-china/Spacemacs-rocks) `★2.1k` - 面向中文用户的 Emacs 与 Spacemacs 入门教程，涵盖配置、插件与实战技巧 · CSS
- [anjuke/zguide-cn](https://github.com/anjuke/zguide-cn) `★1.8k` - ZeroMQ 官方指南中文版，系统讲解消息队列模式与套接字用法 · Raku
- [nivance/DPModel](https://github.com/nivance/DPModel) `★278` - 《设计模式之禅》原书 Java 源码，涵盖 23 种经典设计模式的实现范例，适合对照书本学习 · Java
- [Akagi201/learning-python](https://github.com/Akagi201/learning-python) `★79` - Python 学习笔记与示例代码合集，覆盖标准库和常用库用法，适合边学边练 · Python

## 音视频与流媒体

_编解码、推拉流、播放器、摄像头与媒体服务_

- [storytold/photocraft](https://github.com/storytold/photocraft) `★71.6k` - 纯 Rust 从零编写的开源照片编辑器，支持图像编辑与处理 · Rust
- [iina/iina](https://github.com/iina/iina) `★46.9k` - 基于 mpv 的 macOS 现代视频播放器，用 Swift 编写，支持几乎所有格式与网络流 · Swift
- [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) `★46.3k` - 面向关键任务的安全通信平台，基于 TypeScript 与 Meteor 构建，支持自托管聊天协作，开源免费 · TypeScript
- [mifi/lossless-cut](https://github.com/mifi/lossless-cut) `★45k` - 基于 FFmpeg 的无损音视频剪切工具，支持多格式快速裁剪合并，无需重新编码 · TypeScript
- [portainer/portainer](https://github.com/portainer/portainer) `★38.7k` - 基于 TypeScript 的 Docker 与 Kubernetes 可视化管理界面，支持容器、镜像、Swarm 和 Compose 的部署与监控 · TypeScript
- [mpv-player/mpv](https://github.com/mpv-player/mpv) `★37.5k` - 基于 FFmpeg 的命令行媒体播放器，支持几乎所有音视频格式，以高性能、高质量渲染和高度可配置脚本著称 · C
- [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic) `★33.4k` - 基于 Electron 和 Vue 的高颜值第三方网易云音乐播放器，支持 Windows、macOS 和 Linux · Vue
- [ossrs/srs](https://github.com/ossrs/srs) `★29.4k` - 高性能实时媒体服务器，支持 RTMP、WebRTC、HLS、SRT、GB28181 等协议及 H.264/H.265/AV1 编解码，AI 驱动，C++ 编写 · C++
- [Guovin/iptv-api](https://github.com/Guovin/iptv-api) `★25.7k` - 自动采集校验测速 IPTV 直播源并生成可播放结果，支持 M3U/TXT/API 输出、IPv4/IPv6、Docker 与 GitHub Actions 部署 · Python
- [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) `★20.5k` - 基于 Go 的即用型实时音视频服务器与代理，支持 RTSP、RTMP、WebRTC、SRT、LL-HLS、MPEG-TS、RTP 及 Media-over-QU · Go
- [ZLMediaKit/ZLMediaKit](https://github.com/ZLMediaKit/ZLMediaKit) `★17.6k` - 基于 C++11 的流媒体服务器与客户端框架，支持 WebRTC、RTSP、RTMP、HLS、GB28181、SRT 等十余种协议 · C++
- [AlexxIT/go2rtc](https://github.com/AlexxIT/go2rtc) `★14.5k` - 用 Go 编写的全能摄像头流媒体服务器，支持 RTSP、WebRTC、HLS、MJPEG 等协议，可接入 Home Assistant、HomeKit 与 FF · Go
- [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) `★10.2k` - 基于 Python asyncio 的跨平台下载管理器，支持 HTTP 与 BitTorrent，采用 Fluent Design 界面 · Python
- [sameersbn/docker-gitlab](https://github.com/sameersbn/docker-gitlab) `★8.1k` - 用 Docker 一键部署 GitLab CE 的容器镜像，基于 Shell 脚本，简化自建代码托管平台的安装与配置 · Shell
- [mackron/miniaudio](https://github.com/mackron/miniaudio) `★7.4k` - 单文件 C 音频库，支持播放、采集与 FLAC 解码，跨 Android、BSD、Emscripten 等平台 · C
- [648540858/wvp-GB28181-pro](https://github.com/648540858/wvp-GB28181-pro) `★7.4k` - 开箱即用的国标视频平台，支持GB28181、部标808/1078，兼容海康大华宇视设备接入与NAT穿透，可级联共享 · Java
- [xfangfang/Macast](https://github.com/xfangfang/Macast) `★7k` - 跨平台 DLNA 媒体渲染器，以 mpv 为播放核心，支持 Windows、macOS 和 Linux · Python
- [illuspas/Node-Media-Server](https://github.com/illuspas/Node-Media-Server) `★6.2k` - 基于 Node.js 的 RTMP/HTTP-FLV 流媒体服务器，支持 H.264/H.265/AV1 编码与直播推流 · JavaScript
- [signalwire/freeswitch](https://github.com/signalwire/freeswitch) `★5.3k` - 开源软件定义电信栈，用 C 实现 SIP 与 VoIP 通信，可在树莓派到多核服务器等任意通用硬件上替代专有交换机 · C
- [suxuang/myIPTV](https://github.com/suxuang/myIPTV) `★5.1k` - 高清直播源覆盖几乎所有卫视，内置台标与节目预告，支持 IPTV 播放
- [motioneye-project/motioneye](https://github.com/motioneye-project/motioneye) `★4.7k` - 为 motion 守护进程提供 Web 前端，用 Python 编写，可在树莓派上实现摄像头监控与运动检测 · Python
- [wang-bin/QtAV](https://github.com/wang-bin/QtAV) `★4.3k` - 基于 Qt 和 FFmpeg 的跨平台高性能音视频播放框架，支持 C++ 开发，推荐迁移至新 SDK mdk-sdk · C++
- [jitwxs/163MusicLyrics](https://github.com/jitwxs/163MusicLyrics) `★4.2k` - 支持网易云与QQ音乐的歌词获取处理工具，可导出 LRC 和 SRT 字幕，基于 C# 开发 · C#
- [ireader/media-server](https://github.com/ireader/media-server) `★3.5k` - 基于 C 语言的流媒体服务器，支持 RTSP、RTMP、HLS、MPEG-DASH、MP4、MKV 等协议与封装格式的推流、拉流及转封装 · C
- [Kurento/kurento-media-server](https://github.com/Kurento/kurento-media-server) `★3.1k` - 已归档的 WebRTC 媒体服务器，支持实时音视频流处理与转码，代码已迁移至 Kurento 单体仓库 · C++ _(archived)_
- [scottlawsonbc/audio-reactive-led-strip](https://github.com/scottlawsonbc/audio-reactive-led-strip) `★3k` - 用 Python 和 ESP8266 或树莓派实时把音乐节奏变成 LED 灯带律动 · Python
- [langhuihui/jessibuca](https://github.com/langhuihui/jessibuca) `★2.9k` - 纯 H5 直播流播放器，基于 WebAssembly 与 WebGL 解码渲染，支持 H264/H265、HTTP-FLV 和 WebSocket-FLV · C
- [harlanc/xiu](https://github.com/harlanc/xiu) `★2.3k` - 纯 Rust 实现的高性能安全直播流媒体服务器，支持 RTMP 集群、RTSP、WebRTC WHIP/WHEP、HTTP-FLV 和 HLS · Rust
- [IENT/YUView](https://github.com/IENT/YUView) `★2.3k` - 免费开源跨平台 YUV 查看器，基于 C++ 与 FFmpeg，支持 H.265/HEVC 等编码，内置高级分析工具集 · C++
- [baresip/baresip](https://github.com/baresip/baresip) `★2.3k` - 模块化 SIP 用户代理，用 C 编写，支持音视频通话，适用于 VoIP 与 WebRTC 场景 · C
- [jxlarrea/kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) `★1.9k` - 把闲置 Android 设备变成 Home Assistant 专用壁挂面板，基于 Dart 开发，集成 BLE 代理、摄像头、DLNA 与 ESPHome · Dart
- [giantpinkrobots/varia](https://github.com/giantpinkrobots/varia) `★1.9k` - 基于 Python 与 GTK4/libadwaita 的 GNOME 下载管理器，支持普通下载、BT 种子和视频，底层集成 aria2 · Python
- [mikeroyal/PipeWire-Guide](https://github.com/mikeroyal/PipeWire-Guide) `★1.5k` - 介绍 Linux 音频视频处理框架 PipeWire 的指南，涵盖 ALSA、DAW、音频流与压缩器等专业工作流 · Shell
- [ErosZy/WXInlinePlayer](https://github.com/ErosZy/WXInlinePlayer) `★1.5k` - 基于 WebAssembly 的极速 H.264/H.265 FLV 播放器，用 Canvas 渲染、AudioContext 输出音频 · C++
- [cycfi/q](https://github.com/cycfi/q) `★1.4k` - 基于 C++20 的音频数字信号处理库，提供 DSP 算法与工具 · C++
- [metartc/metaRTC](https://github.com/metartc/metaRTC) `★1.2k` - 面向嵌入式、IoT 与机器人设备的 WebRTC SDK，用 C 编写，支持 WHIP/WHEP 协议 · C
- [adamstark/AudioFile](https://github.com/adamstark/AudioFile) `★1.1k` - 轻量 C++ 音频读写库，支持 WAV 和 AIF 格式 · C++
- [PHZ76/RtspServer](https://github.com/PHZ76/RtspServer) `★1.1k` - 基于 C++ 的 RTSP 服务器与推流器，支持 RTP 传输，可用于直播场景 · C++
- [hvianna/audioMotion-analyzer](https://github.com/hvianna/audioMotion-analyzer) `★965` - 高分辨率实时音频频谱分析 JavaScript 模块，零依赖，基于 Web Audio API 实现可视化 · JavaScript
- [mogutt/TTServer](https://github.com/mogutt/TTServer) `★954` - 蘑菇街开源 TeamTalk 的即时通讯消息服务器，基于 C++ 与 protobuf 实现，支持高并发长连接与消息路由
- [larksuite/rsmpeg](https://github.com/larksuite/rsmpeg) `★879` - 用 Rust 封装 FFmpeg 的 crate，通过 FFI 绑定暴露其几乎全部能力，方便处理视频编解码 · Rust
- [tsingsee/EasyPlayer](https://github.com/tsingsee/EasyPlayer) `★687` - 免费高效的流媒体播放器，支持 RTSP、RTMP、HLS、HTTP 协议，覆盖 Android、iOS 等平台
- [gongluck/AnalysisAVP](https://github.com/gongluck/AnalysisAVP) `★645` - 音视频编解码与格式协议分析学习项目，涵盖 h264/aac/flv/mp4/rtmp，集成 ffmpeg、x264、fdk-aac、webrtc、sdl2 等， · C++
- [OpenIPC/smolrtsp](https://github.com/OpenIPC/smolrtsp) `★511` - 面向 IP 摄像头的轻量级实时流媒体 C 库，支持 H264/H265 与音频，适用于嵌入式设备 · C
- [scottlamb/retina](https://github.com/scottlamb/retina) `★378` - 基于 Rust 的高层 RTSP 多媒体流库，面向 IP 摄像头，简化实时视频流的拉取与处理 · Rust
- [zhw2590582/FlvPlayer](https://github.com/zhw2590582/FlvPlayer) `★303` - 用 JavaScript 将 FLV 视频流解码到 canvas 播放，支持 H.264、AAC 与 HTTP-FLV · JavaScript _(archived)_
- [VideoExpertsGroup/RTSP.Player.Android](https://github.com/VideoExpertsGroup/RTSP.Player.Android) `★224` - 基于Java的Android RTSP/RTMP播放器，可查看IP摄像头直播流，支持解码与广播 · Java
- [huajiaofrontend/HJPlayer](https://github.com/huajiaofrontend/HJPlayer) `★169` - 基于 TypeScript 的 HTML5 播放器，借助 Media Source Extension 实现 FLV 和 HLS 流媒体播放 · TypeScript
- [Mi-Bee-Studio/MiBeeNvr](https://github.com/Mi-Bee-Studio/MiBeeNvr) `★165` - 用 Go 写的轻量自托管 NVR，单个静态二进制零依赖，内置 Web UI，支持 RTSP/ONVIF/小米/GB28181/WHIP 摄像头与 RTMP/SR · Go
- [koraa/sndlink](https://github.com/koraa/sndlink) `★16` - 基于 C++ 的命令行工具，实现低延迟实时音频流传输 · C++
- [tonarino/pulseaudio-webrtc-audio-processing](https://github.com/tonarino/pulseaudio-webrtc-audio-processing) `★7` - 基于 Google WebRTC 实现的音频处理库，为 PulseAudio 提供回声消除、降噪与自动增益控制

## 移动开发

_Android / iOS / 跨平台移动端_

- [flutter/flutter](https://github.com/flutter/flutter) `★180.3k` - 基于 Dart 的跨平台 UI 框架，一套代码快速构建 Android、iOS、桌面等平台精美原生应用 · Dart
- [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) `★153.4k` - 基于 Tauri 和 Rust 打造的现代跨平台代理客户端，支持 Windows、macOS 和 Linux，内置 Clash Meta 内核 · Rust
- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) `★126.7k` - 开源远程桌面应用，支持自托管，可替代 TeamViewer，基于 Rust 与 Flutter 构建，覆盖 Windows、macOS、Linux、iOS、An · Rust
- [android/architecture-samples](https://github.com/android/architecture-samples) `★45.9k` - 展示 Android 应用多种架构工具与模式的 Kotlin 示例合集，涵盖 MVVM、MVI 等方案 · Kotlin
- [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) `★41.7k` - 基于 Rust 和 iced 的跨平台 GUI 工具，实时监控网络流量并支持 IP 地理位置识别 · Rust
- [mattermost/mattermost](https://github.com/mattermost/mattermost) `★39.4k` - 基于 Go 与 React 的开源安全协作平台，覆盖软件开发全生命周期，支持自托管与端到端加密 · TypeScript
- [shadowsocks/ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG) `★32.9k` - macOS 上的 Shadowsocks 图形客户端，Swift 编写，支持 v2ray-plugin 与 hysteria2 · Swift
- [Trinea/android-open-project](https://github.com/Trinea/android-open-project) `★31.8k` - 分类整理 Android 开源项目合集，涵盖各类库与工具，并提供功能更强的网页版检索
- [square/leakcanary](https://github.com/square/leakcanary) `★30k` - Android 内存泄漏检测库，自动监控并生成引用链报告，支持 Java 与 Kotlin · Kotlin
- [ayangweb/BongoCat](https://github.com/ayangweb/BongoCat) `★24.1k` - 基于 Rust 的跨平台桌面宠物，猫咪会跟随鼠标和键盘操作实时互动 · Rust
- [alibaba/flutter-go](https://github.com/alibaba/flutter-go) `★23.6k` - Flutter 开发者帮助 APP，提供 140+ 常用组件 demo 演示与中文文档，基于 Dart 构建 · Dart
- [CarGuo/gsy_github_app_flutter](https://github.com/CarGuo/gsy_github_app_flutter) `★15.5k` - 基于 Dart 与 Flutter 的 GitHub 客户端，覆盖跨平台多端实现，功能完整、持续维护，适合学习与日常使用 · Dart
- [orhanobut/logger](https://github.com/orhanobut/logger) `★13.8k` - 为 Android 打造的简洁美观日志库，支持 JSON 格式化、线程信息与 Logcat 输出，兼容 Timber · Kotlin
- [ikarus23/MifareClassicTool](https://github.com/ikarus23/MifareClassicTool) `★6.5k` - Android NFC 应用，用于读写和分析 MIFARE Classic RFID 标签，支持密钥管理与安全研究 · Java
- [1Remote/1Remote](https://github.com/1Remote/1Remote) `★6.1k` - 基于 C# 的 Windows 远程连接管理器，统一整合 RDP、SSH、VNC、SFTP 等协议，一站式管理所有远程会话 · C#
- [lohanidamodar/flutter_ui_challenges](https://github.com/lohanidamodar/flutter_ui_challenges) `★4.7k` - 100+ 专业 Flutter UI 实现，含完整代码，适配 Flutter 3.x，支持 Android、iOS、Linux 和 Web · Dart _(archived)_
- [alibaba/dexposed](https://github.com/alibaba/dexposed) `★4.5k` - 基于Java的Android热修复框架，无需重启即可动态替换应用方法，实现单应用级别的上帝模式 · Java _(archived)_
- [pjsip/pjproject](https://github.com/pjsip/pjproject) `★2.7k` - 基于 C 语言的多媒体通信库，实现 SIP、RTP 等 VoIP 协议，支持 NAT 穿透，可跨 Android、iOS 等平台构建语音视频通话应用 · C
- [dana-at-cp/backdoor-apk](https://github.com/dana-at-cp/backdoor-apk) `★2.4k` - 用 Shell 脚本向任意 Android APK 注入后门，依赖 Apktool、Metasploit、smali 与 Android SDK，仅供安全教学研 · Shell
- [ZhaoKaiQiang/KLog](https://github.com/ZhaoKaiQiang/KLog) `★1.9k` - Android 专用 LogCat 工具，支持打印行号与函数调用栈、解析 JSON/XML、点击跳转源码、保存日志 · Java
- [maoruibin/TranslateApp](https://github.com/maoruibin/TranslateApp) `★1.8k` - 复制单词即译的 Android 翻译应用，结果以顶部悬浮视图展示，基于 Java 与 Dagger、MVP 架构 · Java _(archived)_
- [Myzel394/Alibi](https://github.com/Myzel394/Alibi) `★1.7k` - 把 Android 手机变成行车记录仪，循环录制并保留最近 30 分钟，基于 Kotlin 与 Jetpack Compose 构建，注重隐私 · Kotlin
- [taka-no-me/android-cmake](https://github.com/taka-no-me/android-cmake) `★1.2k` - 为 Android NDK 提供 CMake 工具链文件及配套脚本，简化交叉编译配置 · CMake
- [foxglove/mcap](https://github.com/foxglove/mcap) `★1.1k` - 模块化高性能且与序列化无关的容器文件格式，适用于 pub/sub 和机器人应用，支持 C++、Go、Python、Swift 等多语言 · Rust
- [zibo-chen/SubnetDesk](https://github.com/zibo-chen/SubnetDesk) `★716` - 基于 RustDesk 的局域网远程桌面，用 mDNS 自动发现设备，Flutter 界面，数据不出内网 · Rust

## 前端与 Web

_Web 框架、UI 库与前端工程化_

- [anomalyco/opencode](https://github.com/anomalyco/opencode) `★220.4k` - 开源编码智能体，TypeScript 编写，可自动完成代码生成与修改任务 · TypeScript
- [iptv-org/iptv](https://github.com/iptv-org/iptv) `★142.1k` - 汇集全球公开 IPTV 频道，提供 M3U 播放列表，用 TypeScript 维护 · TypeScript
- [mrdoob/three.js](https://github.com/mrdoob/three.js) `★116.8k` - 基于 WebGL 的 JavaScript 3D 引擎，可在浏览器中构建 3D 场景、VR 与 AR 体验，支持 Canvas、SVG 和 WebAudio · JavaScript
- [d3/d3](https://github.com/d3/d3) `★113.8k` - 用 SVG、Canvas 和 HTML 让数据可视化活起来，基于 Web 标准的经典图表库 · Shell
- [ocornut/imgui](https://github.com/ocornut/imgui) `★76.8k` - 轻量级 C++ 即时模式 GUI 库，无冗余依赖，适合游戏引擎与工具开发 · C++
- [hakimel/reveal.js](https://github.com/hakimel/reveal.js) `★72.5k` - 基于 HTML 的演示文稿框架，用 JavaScript 编写，支持幻灯片、演讲和网页幻灯片展示 · JavaScript
- [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) `★68.2k` - 用HTML整理的高性价比生活指南，覆盖健康、理财、法律、社保、婚育、创业等，每条标注成本收益、证据等级与期刊或官方出处 · HTML
- [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) `★59.2k` - 基于 Cesium 的浏览器端卫星侦察模拟器，在逼真 3D 地球上实时呈现航班追踪等开源地理空间情报 · JavaScript
- [justjavac/wechat-miniapp-radar](https://github.com/justjavac/wechat-miniapp-radar) `★51.2k` - AI 驱动的小程序技术选型、趋势追踪与迁移诊断工具，TypeScript 实现，支持微信小程序生态 · TypeScript
- [NaiboWang/EasySpider](https://github.com/NaiboWang/EasySpider) `★44.7k` - 可视化无代码网页爬虫与浏览器自动化工具，图形化设计执行采集任务，基于 JavaScript · JavaScript
- [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) `★39.9k` - 聚合34家免费LLM供应商与635个模型端点，统一为单个/v1接口并支持自定义OpenAI兼容端点，具备智能路由、自动故障转移和密钥加密 · TypeScript
- [impress/impress.js](https://github.com/impress/impress.js) `★38.2k` - 基于 CSS3 变换与过渡的演示框架，灵感来自 Prezi，用 JavaScript 在浏览器中实现缩放旋转式幻灯片 · JavaScript
- [geekan/HowToLiveLonger](https://github.com/geekan/HowToLiveLonger) `★35.8k` - 面向程序员的健康长寿指南，涵盖饮食运动睡眠等科学建议，支持8种语言 · HTML
- [fanmingming/live](https://github.com/fanmingming/live) `★28.7k` - 提供可直连访问的电视广播台标库与工具，支持 IPv4/IPv6 双栈、EPG 与 m3u/m3u8 转换，永久免费开源 · JavaScript
- [houshanren/hangzhou_house_knowledge](https://github.com/houshanren/hangzhou_house_knowledge) `★26.9k` - 2017年杭州买房实战经验总结，涵盖购房流程与避坑知识，用CSS搭建的知识分享站 · CSS
- [lvgl/lvgl](https://github.com/lvgl/lvgl) `★25k` - 免费开源嵌入式图形库，用 C 编写，覆盖从单片机到支持 3D 的 MPU，配套专业编辑器 LVGL Pro · C
- [slint-ui/slint](https://github.com/slint-ui/slint) `★24.3k` - 开源声明式 GUI 工具包，用 Rust 编写，可为 Rust、C++、JavaScript 或 Python 应用构建原生界面，支持桌面与嵌入式设备 · Rust
- [dibingfa/flash-linux0.11-talk](https://github.com/dibingfa/flash-linux0.11-talk) `★22.7k` - 以小说式笔法逐行解读 Linux 0.11 内核源码，带你轻松读懂操作系统底层原理 · HTML
- [ruanyf/es6tutorial](https://github.com/ruanyf/es6tutorial) `★21.4k` - 全面讲解 ECMAScript 6 新增语法特性的开源 JavaScript 教程，由阮一峰编写 · JavaScript
- [iissnan/hexo-theme-next](https://github.com/iissnan/hexo-theme-next) `★15.7k` - 为 Hexo 打造的优雅主题，支持多种配色方案与自定义布局，界面简洁美观 · JavaScript
- [cesanta/mongoose](https://github.com/cesanta/mongoose) `★13.1k` - 面向嵌入式设备的 C 语言网络库，集成 TCP/IP 协议栈、HTTP、WebSocket、MQTT 与 TLS 1.3，适用于 IoT 场景 · C
- [ksky521/nodeppt](https://github.com/ksky521/nodeppt) `★10.3k` - 基于 HTML5 与 CSS3 的网页演示工具，支持 Markdown 编写和多种动画效果 · JavaScript _(archived)_
- [nbedos/termtosvg](https://github.com/nbedos/termtosvg) `★9.8k` - 用 Python 把终端会话录制成 SVG 动画，可嵌入网页，无需视频格式 · Python _(archived)_
- [jgraph/drawio](https://github.com/jgraph/drawio) `★8.9k` - 基于 JavaScript 的纯客户端图表编辑器，支持流程图、白板等通用绘图，无需服务端 · JavaScript
- [agegr/pi-web](https://github.com/agegr/pi-web) `★7.7k` - 为 pi 编码代理提供 Web 界面，基于 TypeScript 构建 · TypeScript
- [jerryscript-project/jerryscript](https://github.com/jerryscript-project/jerryscript) `★7.4k` - 超轻量级 JavaScript 引擎，用 C 编写，专为物联网设备提供脚本运行时 · C
- [phoboslab/jsmpeg](https://github.com/phoboslab/jsmpeg) `★6.5k` - 纯 JavaScript 实现的 MPEG1 视频解码器，可在浏览器中直接解码播放 MPEG1 视频流 · JavaScript
- [pablostanley/yoinks](https://github.com/pablostanley/yoinks) `★6.2k` - 终端下载任意视频的 TypeScript 工具，无广告骚扰 · TypeScript
- [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons) `★5.8k` - 为 NERDTree、vim-airline、CtrlP 等 Vim 插件添加文件类型图标，基于 Nerd Fonts 字形 · Vim Script
- [foru17/front-end-collect](https://github.com/foru17/front-end-collect) `★5.7k` - 汇集长期关注的前端优秀网站、博客与活跃开发者，JavaScript 前端资源导航 · JavaScript
- [xuanli199/weekly](https://github.com/xuanli199/weekly) `★3.8k` - 收录玄离199每周科技补全视频提及的软件与项目，TypeScript 整理，方便查找 · TypeScript
- [yzhu798/CodingInterviewsNotes](https://github.com/yzhu798/CodingInterviewsNotes) `★2.7k` - 涵盖C++基础、智能指针、C++11、STL、设计模式、算法刷题与Linux、网络、数据库等面试知识，含剑指offer和LeetCode题解 · HTML
- [korbinjoe/excalidraw-cn](https://github.com/korbinjoe/excalidraw-cn) `★2.5k` - 基于 Excalidraw 的白板工具，支持中文手写字体和多画布，用 TypeScript 开发 · TypeScript
- [cxinping/PyQt5](https://github.com/cxinping/PyQt5) `★2.4k` - 《PyQt5快速开发与实战》配套源码，含大量示例，助你快速掌握PyQt5桌面应用开发 · HTML
- [nyakang/nyaterm](https://github.com/nyakang/nyaterm) `★1.9k` - 基于 Tauri 和 React 的现代远程终端工作区，集成 SSH、SFTP 与串口连接，支持 OTP 认证 · TypeScript
- [michaelliao/learn-javascript](https://github.com/michaelliao/learn-javascript) `★1.7k` - 廖雪峰 JavaScript 全栈教程配套源码，涵盖基础语法到 Node.js 后端开发
- [binux/ThunderLixianExporter](https://github.com/binux/ThunderLixianExporter) `★747` - 把迅雷离线下载链接导出给 aria2 或 wget 使用，基于 JavaScript 实现 · JavaScript
- [phodal/lan](https://github.com/phodal/lan) `★565` - 基于 JavaScript 的物联网服务层，支持 CoAP、WebSocket、MQTT、HTTP 协议接入 · JavaScript
- [lulop-k/kurento-rtsp2webrtc](https://github.com/lulop-k/kurento-rtsp2webrtc) `★563` - 将 RTSP 或 HTTP 流转换为低延迟 WebRTC 流的 JavaScript 示例，基于 Kurento 实现 · JavaScript
- [chaseleantj/deskworlds](https://github.com/chaseleantj/deskworlds) `★453` - 用 JavaScript 打造可交互的动态桌面壁纸，让桌面随操作实时响应 · JavaScript
- [fguby/Electron-elf](https://github.com/fguby/Electron-elf) `★317` - 基于 Electron 和 Live2D 打造的桌面精灵应用，支持 macOS，用 HTML 实现可交互的虚拟角色 · HTML
- [QiShaoXuan/live2DModel](https://github.com/QiShaoXuan/live2DModel) `★301` - 提供可直接在网页加载的 Live2D 模型资源，基于 HTML 展示 · HTML
- [jae-jae/weapp-github-trending](https://github.com/jae-jae/weapp-github-trending) `★300` - 用 JavaScript 开发的微信小程序，实时查看 GitHub 今日趋势榜单 · JavaScript
- [sgl-org/sgl](https://github.com/sgl-org/sgl) `★195` - 面向嵌入式系统的现代 C 语言 GUI 库，轻量高效，适合资源受限设备 · C
- [mfranzon/render](https://github.com/mfranzon/render) `★173` - 让编码代理直接生成精美 3D 模型，基于 HTML 实现 · HTML
- [iHildy/opencode-synced](https://github.com/iHildy/opencode-synced) `★166` - 基于 TypeScript 的 opencode 插件，在多台机器间同步全局配置 · TypeScript
- [stayradiated/termcolors](https://github.com/stayradiated/termcolors) `★141` - 用 JavaScript 实现终端配色方案多格式互转，支持导入导出 · JavaScript
- [tjumyk/sdl-tutorial-cn](https://github.com/tjumyk/sdl-tutorial-cn) `★133` - Lazy Foo 的 SDL 1.2 游戏开发教程中文翻译，HTML 编写，适合入门学习 · HTML
- [kaiakz/walv](https://github.com/kaiakz/walv) `★116` - 浏览器里的 LittlevGL 图形界面设计器，用 HTML 打造，可在线拖拽布局并生成 UI 代码 · HTML
- [abhra0897/LameUI](https://github.com/abhra0897/LameUI) `★114` - 面向嵌入式系统的轻量级 C 语言 UI 库，适用于单片机和 GUI 开发 · C
- [YuzukiHD/YuzukiNeko](https://github.com/YuzukiHD/YuzukiNeko) `★102` - 搭载全志F101S3/F101S4芯片的迷你可爱开发板，尺寸仅pico级别 · HTML
- [rm-hull/8-bit-trip](https://github.com/rm-hull/8-bit-trip) `★3` - 基于 TypeScript 与 WebAudio 的算法音乐流媒体，实时生成 8-bit 风格旋律 · TypeScript

## Rust 生态

_用 Rust 写的工具与系统_

- [starship/starship](https://github.com/starship/starship) `★60.4k` - 用 Rust 编写的极速极简命令行提示符，支持 bash、fish、zsh、PowerShell 等任意 shell，可无限自定义 · Rust
- [helix-editor/helix](https://github.com/helix-editor/helix) `★46.7k` - 基于 Rust 的模态文本编辑器，融合 Kakoune 与 Vim 操作理念，支持多选编辑与内置 LSP · Rust
- [nushell/nushell](https://github.com/nushell/nushell) `★40.7k` - 用 Rust 编写的结构化数据处理 shell，将文件和命令输出视为表格，支持管道式操作与跨平台运行 · Rust
- [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) `★24k` - 用 Rust 编写的原生本地优先罗技鼠标配置工具，通过 HID++ 协议重映射按键、DPI 和 SmartShift，无需账号与遥测 · Rust
- [hyperium/hyper](https://github.com/hyperium/hyper) `★16.4k` - Rust 的高性能 HTTP 底层库，支持 HTTP/1 与 HTTP/2，是众多框架的底层依赖 · Rust
- [microsoft/RustTraining](https://github.com/microsoft/RustTraining) `★15k` - 微软出品的 Rust 分级培训材料，覆盖入门、进阶到专家三个层次 · Rust
- [bootandy/dust](https://github.com/bootandy/dust) `★12.5k` - 用 Rust 重写的 du 替代品，以树状图和直观排序展示磁盘占用，比原版更易读 · Rust
- [johnthagen/min-sized-rust](https://github.com/johnthagen/min-sized-rust) `★9.9k` - 教你用 Cargo 配置、LTO、strip、no_std、UPX 等手段把 Rust 二进制体积压到最小 · Rust
- [agrinman/tunnelto](https://github.com/agrinman/tunnelto) `★7.1k` - 用 Rust 编写的隧道工具，一条命令把本地 Web 服务暴露到公网并生成可访问的公开 URL · Rust
- [image-rs/image](https://github.com/image-rs/image) `★5.9k` - 用 Rust 实现的图像编解码库，支持多种格式读写与像素处理 · Rust
- [ooolabdev/ooosplat](https://github.com/ooolabdev/ooosplat) `★2.1k` - 本地桌面应用，一键将视频和图片转为 3D Gaussian Splatting 模型，基于 Rust 构建 · Rust

## Go 生态

_用 Go 写的服务与工具_

- [astaxie/build-web-application-with-golang](https://github.com/astaxie/build-web-application-with-golang) `★43.9k` - 用 Go 从零构建 Web 应用的入门电子书，涵盖路由、模板、数据库、部署等实战内容 · Go
- [sipeed/picoclaw](https://github.com/sipeed/picoclaw) `★30.1k` - 基于 Go 的轻量级 AI 助手，体积小、速度快，可部署在任何环境，自动处理琐事 · Go
- [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) `★5.6k` - 基于 Go 的全网音乐搜索下载工具，支持 CLI 与 Web 双模式，聚合网易云、QQ、酷狗、Bilibili 等 10+ 平台，多源并发搜索并无损解析 · Go
- [SKeyerror/Psyduck](https://github.com/SKeyerror/Psyduck) `★4.4k` - 用 XMind 2.0 整理 Linux、网络、C++、Golang 与数据库设计等计算机知识 · Go
- [logdyhq/logdy-core](https://github.com/logdyhq/logdy-core) `★2.3k` - 基于 Go 的实时日志查看器，提供 Web UI，像 tail -f 一样在浏览器中追踪日志 · Go
- [rogaha/docker-desktop](https://github.com/rogaha/docker-desktop) `★1.2k` - 基于 Docker 的远程虚拟桌面，内置 Firefox 和 LibreOffice，支持无 root 运行与 SSH 访问 · Shell
- [RonIovine/pshell](https://github.com/RonIovine/pshell) `★28` - 轻量级进程专用嵌入式命令行 shell，支持 C/C++/Python/Go 应用，通过回调函数注册命令 · C++

## 终端与 CLI 工具

_Shell、终端复用器与命令行效率工具_

- [zellij-org/zellij](https://github.com/zellij-org/zellij) `★35.8k` - Rust 编写的终端复用器与工作区，开箱即用，支持多路复用、布局和插件 · Rust
- [mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) `★27.3k` - 收录超 750 套终端配色方案，覆盖 iTerm2 并移植到 Konsole、PuTTY、Kitty、Windows Terminal 等数十种终端 · Shell
- [spf13/spf13-vim](https://github.com/spf13/spf13-vim) `★15.5k` - 终极 Vim 配置发行版，集成插件、配色与快捷键，开箱即用 · Vim Script
- [bin456789/reinstall](https://github.com/bin456789/reinstall) `★13.8k` - 一键重装 VPS 系统，支持 Alpine、Debian、Ubuntu 等，通过 netboot 引导无需救援模式 · Shell
- [juewuy/ShellCrash](https://github.com/juewuy/ShellCrash) `★13.6k` - 用 Shell 脚本在路由器等设备上运行 sing-box/mihomo 客户端，支持订阅管理与开机自启 · Shell
- [tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) `★13.1k` - 保存并恢复 tmux 会话、窗口、面板及运行中的程序，重启系统后环境不丢失，纯 Shell 实现 · Shell
- [vnotex/vnote](https://github.com/vnotex/vnote) `★13k` - 基于 C++ 的本地笔记平台，主打 Markdown、思维导图、Typst 与纯文本编辑，支持 Vim 操作，原生速度流畅 · C++
- [oh-my-fish/oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) `★11.4k` - 为 Fish Shell 提供插件管理、主题与提示符定制的框架，类似 oh-my-zsh，用 Shell 编写 · Shell
- [ohmybash/oh-my-bash](https://github.com/ohmybash/oh-my-bash) `★7.8k` - 社区驱动的 Bash 配置管理框架，内置自动更新工具，支持主题和插件扩展，让终端更高效 · Shell
- [athityakumar/colorls](https://github.com/athityakumar/colorls) `★5.1k` - 用 Ruby 编写的终端 ls 增强工具，为文件和目录添加颜色与 Font Awesome 图标，让命令行输出更美观易读 · Ruby
- [zhaojh329/rtty](https://github.com/zhaojh329/rtty) `★4k` - 通过 Web 远程访问设备终端，支持穿透 NAT 与 HTTP 代理，实现远程 Shell、控制台和调试，C 语言编写 · C
- [wangdoc/javascript-tutorial](https://github.com/wangdoc/javascript-tutorial) `★4k` - 阮一峰编写的开源 JavaScript 教程，涵盖语法、标准库与浏览器 API，适合系统学习与查阅 · Shell
- [erikw/tmux-powerline](https://github.com/erikw/tmux-powerline) `★3.8k` - 纯 Bash 编写的 tmux 状态栏插件，提供可自定义的动态 powerline 分段 · Shell
- [google/gif-for-cli](https://github.com/google/gif-for-cli) `★2.9k` - 用 Python3 编写的命令行工具，在终端里播放 GIF 动图 · Python _(archived)_
- [liuchengxu/space-vim](https://github.com/liuchengxu/space-vim) `★2.9k` - 受 spacemacs 启发、基于 Vim Script 的轻量 Vim/Neovim 配置发行版，适合新手快速上手 · Vim Script
- [1N3/BruteX](https://github.com/1N3/BruteX) `★2.3k` - 自动爆破目标主机上所有运行服务的 Shell 脚本，支持多种协议，适用于渗透测试与漏洞赏金 · Shell
- [mathiasbynens/evil.sh](https://github.com/mathiasbynens/evil.sh) `★2.2k` - 用 Shell 脚本对终端做隐蔽或明显的恶作剧调整，慢慢把使用者逼疯 · Shell
- [mislav/dotfiles](https://github.com/mislav/dotfiles) `★1.3k` - 涵盖 bash、zsh、git、tmux 和 vim 配置的个人工具箱，集成 rbenv 管理 Ruby 版本 · Shell
- [tmux-python/libtmux](https://github.com/tmux-python/libtmux) `★1.2k` - 用 Python 封装 tmux 的 API 库，可在脚本中编程控制会话、窗口和面板 · Python
- [int32bit/dotfiles](https://github.com/int32bit/dotfiles) `★715` - 一套面向 Linux 的 vim、zsh、git 和 tmux 配置文件集合，开箱即用 · Vim script
- [hardhackerlabs/oh-my-nvim](https://github.com/hardhackerlabs/oh-my-nvim) `★502` - 主题驱动、开箱即用的现代 Neovim 配置，基于 Lua 编写 · Lua
- [DemonCloud/dotfile](https://github.com/DemonCloud/dotfile) `★388` - 基于 Vim script 的 (Neo)Vim 配置与工作文件集合，涵盖 vimrc 等 dotfiles · Vim script
- [xuxiaodong/tmuxen](https://github.com/xuxiaodong/tmuxen) `★218` - 用 Shell 脚本简化 tmux 环境配置，一键管理会话与窗口布局 · Shell
- [lanxuezaipiao/zh-google-styleguide](https://github.com/lanxuezaipiao/zh-google-styleguide) `★71` - Google 开源项目风格指南中文版，涵盖 C++、Java、Python 等语言的编码规范与最佳实践 · Shell

## 网络与安全

_网络协议、代理、翻墙工具与安全研究_

- [aria2/aria2](https://github.com/aria2/aria2) `★43.2k` - 轻量级命令行下载工具，支持 HTTP/HTTPS、FTP、SFTP、BitTorrent 和 Metalink 多协议多源，C++11 编写，跨平台 · C++
- [tailscale/tailscale](https://github.com/tailscale/tailscale) `★38k` - 基于 WireGuard 的零配置 VPN，支持 2FA、OAuth 和 SSO，用 Go 编写 · Go
- [ehang-io/nps](https://github.com/ehang-io/nps) `★34.3k` - 基于 Go 的轻量级内网穿透代理服务器，支持 tcp、udp、socks5、http 等流量转发，自带 Web 管理端 · Go
- [gfwlist/gfwlist](https://github.com/gfwlist/gfwlist) `★25.7k` - 汇集被中国防火墙屏蔽的域名列表，供代理工具自动分流使用
- [FelisCatus/SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) `★22.6k` - 已停止维护的 Chrome/Edge 代理切换扩展，基于 PAC 与情景模式自动切换，用 CoffeeScript 编写 · CoffeeScript
- [uNetworking/uWebSockets](https://github.com/uNetworking/uWebSockets) `★19k` - 高性能 C++ Web 服务器，支持 WebSocket、发布订阅与代理协议，跨平台且符合标准 · C++
- [nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic) `★17.3k` - 为网易云音乐解锁灰色歌曲，基于 Node.js 代理服务器，支持自定义音源替换 · JavaScript
- [zeromq/libzmq](https://github.com/zeromq/libzmq) `★11k` - C++ 实现的高性能异步消息库，支持 ZMTP/3.1 协议，提供发布订阅、推拉等多种并发通信模式 · C++
- [rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng) `★10.7k` - 通过 LD_PRELOAD 劫持动态链接程序的 socket 调用，将流量重定向到 SOCKS/HTTP 代理，是已停止维护的 proxychains 的续作， · C
- [Serial-Studio/Serial-Studio](https://github.com/Serial-Studio/Serial-Studio) `★7.3k` - 开源遥测仪表盘，支持 UART、BLE、MQTT、Modbus、CAN Bus 等协议，用 C 语言开发，适用于嵌入式与工业物联网 · C
- [acl-dev/acl](https://github.com/acl-dev/acl) `★3.1k` - C/C++ 网络与服务器库，内置协程、Redis/MySQL/PostgreSQL/SQLite 客户端及 HTTP/HTTPS/WebSocket/MQTT， · C
- [Corvusoft/restbed](https://github.com/Corvusoft/restbed) `★2k` - 为 C++ 应用提供异步 RESTful 能力的框架，支持 HTTP/HTTP2 与 Comet 推送 · C++
- [Lozy/danted](https://github.com/Lozy/danted) `★1.7k` - 快速安装配置 Dante Socks5 代理服务器的脚本 · Roff
- [chronoxor/CppServer](https://github.com/chronoxor/CppServer) `★1.7k` - 超高速低延迟的异步 socket 服务端与客户端 C++ 库，支持 TCP、SSL、UDP、HTTP、HTTPS、WebSocket 协议，并解决 10K 连接 · C++

## 桌面与效率工具

_桌面应用、笔记与效率增强_

- [agalwood/Motrix](https://github.com/agalwood/Motrix) `★57.3k` - 基于 aria2 与 Electron 的全能下载工具，支持 BT 和磁力链接，跨 macOS、Linux 平台 · TypeScript
- [WerWolv/ImHex](https://github.com/WerWolv/ImHex) `★55.5k` - 面向逆向工程师和程序员的十六进制编辑器，支持二进制分析、反汇编和模式匹配，采用 C++ 与 Dear ImGui 构建，自带护眼暗色主题 · C++
- [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) `★39.9k` - 免费开源的屏幕录制与演示制作工具，基于 Electron 与 PixiJS，无水印无订阅，可商用，Screen Studio 的替代品 · TypeScript _(archived)_
- [sindresorhus/quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins) `★18.8k` - 为开发者整理的 macOS Quick Look 插件清单，可快速预览代码、Markdown、JSON、压缩包等文件内容
- [TKkk-iOSer/WeChatPlugin-MacOS](https://github.com/TKkk-iOSer/WeChatPlugin-MacOS) `★14.3k` - macOS 微信功能增强插件，支持消息防撤回、自动回复、远程控制等，可搭配 Alfred Workflow 使用 · Objective-C
- [vurtun/nuklear](https://github.com/vurtun/nuklear) `★14k` - 单头文件 ANSI C 即时模式 GUI 库，兼容 C89，无需依赖，适合嵌入游戏与工具 · C _(archived)_
- [sunnyyoung/WeChatTweak](https://github.com/sunnyyoung/WeChatTweak) `★13.8k` - 命令行工具，拦截微信 macOS 客户端撤回消息并支持多开，Swift 编写，兼容 Alfred 与 Raycast · Swift
- [albertlauncher/albert](https://github.com/albertlauncher/albert) `★8k` - 基于 C++ 的快速键盘启动器，支持 Python 插件扩展，可快速搜索并启动应用 · C++
- [lc-soft/LCUI](https://github.com/lc-soft/LCUI) `★4.3k` - 用 C 语言编写的跨平台 GUI 框架，可构建桌面用户界面，支持 Windows · C
- [netnr/kms](https://github.com/netnr/kms) `★3.3k` - 基于 vlmcsd 的 KMS 激活服务，用 slmgr 命令激活 Windows 与 Office · HTML
- [zlgopen/awtk](https://github.com/zlgopen/awtk) `★3.3k` - 跨平台嵌入式 GUI 工具包，用 C 语言编写，支持 RT-Thread、LiteOS、STM32 等多种 RTOS 与芯片平台 · C
- [cnjinhao/nana](https://github.com/cnjinhao/nana) `★2.5k` - 基于现代 C++ 的跨平台 GUI 库，支持 C++11/14/17，利用模板元编程实现简洁高效的界面开发 · C++
- [mutouyun/cpp-ipc](https://github.com/mutouyun/cpp-ipc) `★2.2k` - 基于共享内存的高性能 C++17 进程间通信库，支持 Linux 与 Windows · C++
- [alxnbl/onenote-md-exporter](https://github.com/alxnbl/onenote-md-exporter) `★1.7k` - 用 C# 编写的命令行工具，将 OneNote 笔记本导出为 Markdown，兼容 Obsidian、Joplin 等笔记应用 · C#
- [taggon/highlight](https://github.com/taggon/highlight) `★379` - 为 Keynote 幻灯片提供丰富语法高亮，基于 Swift 开发，支持 RTF 输出 · Swift
- [kaiakz/lv_gui_designer](https://github.com/kaiakz/lv_gui_designer) `★79` - 基于 LittlevGL 的拖拽式 GUI 设计器，用 C 编写，可快速搭建嵌入式界面（已暂停维护） · C _(archived)_

## 系统与嵌入式

_Linux 内核、驱动、C/C++ 与嵌入式物联网_

- [nlohmann/json](https://github.com/nlohmann/json) `★50.8k` - 现代 C++ 的 header-only JSON 库，支持解析、序列化及 BSON、CBOR、JSON Patch 等格式 · C++
- [google/leveldb](https://github.com/google/leveldb) `★39.5k` - 谷歌开源的高性能键值存储库，C++ 编写，提供字符串键值的有序映射 · C++
- [aristocratos/btop](https://github.com/aristocratos/btop) `★35.1k` - 基于 C++ 的终端资源监控工具，实时显示 CPU、内存、磁盘、网络和进程状态，界面美观且高度可定制 · C++
- [nothings/stb](https://github.com/nothings/stb) `★34.9k` - 单文件公共领域 C/C++ 库集合，涵盖图像解码、字体渲染、音频处理等，即拖即用无需构建 · C
- [gabime/spdlog](https://github.com/gabime/spdlog) `★29.7k` - 高性能 C++ 日志库，支持 header-only 引入，兼容 C++11，提供快速异步与格式化输出 · C++
- [ggreer/the_silver_searcher](https://github.com/ggreer/the_silver_searcher) `★27.1k` - 用 C 编写的命令行代码搜索工具，类似 ack 但速度更快，基于 PCRE 正则匹配 · C
- [fmtlib/fmt](https://github.com/fmtlib/fmt) `★25.9k` - 现代 C++ 格式化库，以高性能和类型安全替代 printf 与 iostream，支持 chrono、浮点及跨平台输出 · C++
- [upx/upx](https://github.com/upx/upx) `★18k` - 跨平台可执行文件压缩加壳工具，支持多架构与格式，压缩率高且解压速度快 · C++
- [chenshuo/muduo](https://github.com/chenshuo/muduo) `★16.3k` - 基于 C++11 的多线程 Linux 服务器事件驱动网络库，采用 Reactor 模式，支持非阻塞 IO 与定时器 · C++
- [Tencent/rapidjson](https://github.com/Tencent/rapidjson) `★15.1k` - C++ 高性能 JSON 解析与生成库，同时提供 SAX 和 DOM 风格 API · C++
- [acaudwell/Gource](https://github.com/acaudwell/Gource) `★13.2k` - 将 Git 等版本库的提交历史渲染成动态缩放的代码城市动画，C++ 编写，支持多仓库与自定义着色 · C++
- [ShiqiYu/libfacedetection](https://github.com/ShiqiYu/libfacedetection) `★12.8k` - 开源人脸检测库，基于CNN实现，速度可达1000FPS，支持ARM平台 · C++
- [xmake-io/xmake](https://github.com/xmake-io/xmake) `★12.3k` - 基于 Lua 的跨平台构建工具，支持 C/C++、交叉编译，可替代 CMake · Lua
- [eclipse-mosquitto/mosquitto](https://github.com/eclipse-mosquitto/mosquitto) `★11.3k` - 轻量级开源 MQTT broker，支持 MQTT 5.0 与 3.1.1 协议，适用于 IoT 消息推送，用 C 编写 · C
- [jemalloc/jemalloc](https://github.com/jemalloc/jemalloc) `★11.2k` - 通用内存分配器，提供低碎片、高并发性能，支持多线程与内存剖析，广泛用于 FreeBSD、Firefox 等 · C
- [bellard/quickjs](https://github.com/bellard/quickjs) `★11.1k` - 轻量级可嵌入的 JavaScript 引擎，C 语言实现，支持 ES2020 规范，启动快、体积小 · C
- [r-lyeh/single_file_libs](https://github.com/r-lyeh/single_file_libs) `★10k` - 收录大量单文件 C/C++ 库，侧重无条款限制的宽松许可证
- [pocoproject/poco](https://github.com/pocoproject/poco) `★9.5k` - 跨平台 C++ 库，用于构建桌面、服务器、移动、IoT 和嵌入式网络应用，涵盖 HTTP、JSON、日志、数据库访问等模块 · C++
- [electronicarts/EASTL](https://github.com/electronicarts/EASTL) `★9.4k` - EA 开源的高性能 C++ STL 替代实现，针对游戏开发优化，支持 C++11 至 C++20 · C++
- [gperftools/gperftools](https://github.com/gperftools/gperftools) `★9k` - Google 高性能工具集，含 TCMalloc 内存分配器、CPU 与堆分析器，用于 C++ 程序性能调优 · C++
- [Xfennec/progress](https://github.com/Xfennec/progress) `★8.9k` - 用 C 编写的 Linux 工具，实时显示 cp、mv、dd 等 coreutils 命令的进度、速度和剩余时间 · C
- [Tencent/libco](https://github.com/Tencent/libco) `★8.7k` - 微信后台广泛使用的 C++ 协程库，自 2013 年起稳定运行于数万台机器 · C++
- [zaphoyd/websocketpp](https://github.com/zaphoyd/websocketpp) `★7.7k` - 基于C++的WebSocket客户端与服务器库，支持RFC6455协议，可跨平台运行 · C++
- [libcpr/cpr](https://github.com/libcpr/cpr) `★7.5k` - 基于 libcurl 的 C++ HTTP 客户端库，提供类似 Python Requests 的简洁 API · C++
- [orangeduck/Cello](https://github.com/orangeduck/Cello) `★7.1k` - 用 C 语言实现的高层编程库，提供动态类型、lambda 表达式和 GC 等特性，让 C 代码更接近脚本语言 · C
- [me115/design_patterns](https://github.com/me115/design_patterns) `★7.1k` - 用 C++ 图解 23 种经典设计模式，配代码示例与 UML 类图，适合入门与速查 · C++
- [rxi/microui](https://github.com/rxi/microui) `★6.9k` - 用 C 编写的微型即时模式 UI 库，代码极小、无依赖，适合嵌入游戏或工具中快速搭建界面 · C
- [peng-zhihui/HoloCubic](https://github.com/peng-zhihui/HoloCubic) `★6.7k` - 基于ESP32的伪全息透明桌面显示站，支持WiFi联网，用C语言开发 · C
- [olikraus/u8g2](https://github.com/olikraus/u8g2) `★6.7k` - 面向单色 OLED 与 LCD 的嵌入式图形库，内置多种字体，支持 Arduino 等微控制器平台 · C
- [nanomsg/nanomsg](https://github.com/nanomsg/nanomsg) `★6.3k` - C 语言编写的轻量级消息传递库，提供多种可扩展协议模式，支持进程内与跨网络通信 · C
- [memononen/nanovg](https://github.com/memononen/nanovg) `★5.7k` - 基于 OpenGL 的抗锯齿 2D 矢量绘图库，用 C 编写，适合 UI 与数据可视化 · C
- [google/bloaty](https://github.com/google/bloaty) `★5.6k` - 分析二进制文件体积构成的大小分析工具，支持 ELF、Mach-O、PE 等格式，可定位代码膨胀来源 · C++
- [forhappy/Cplusplus-Concurrency-In-Practice](https://github.com/forhappy/Cplusplus-Concurrency-In-Practice) `★5.5k` - 系统讲解 C++11 并发编程的实战教程，涵盖线程、互斥量、条件变量、原子操作与内存模型 · C++
- [google/tcmalloc](https://github.com/google/tcmalloc) `★5.4k` - Google 的高性能 C++ 内存分配库，通过线程缓存和大小类机制减少锁竞争与碎片，可替代 malloc 提升多线程程序性能 · C++
- [warmcat/libwebsockets](https://github.com/warmcat/libwebsockets) `★5.3k` - 轻量级可嵌入的 C 网络库，支持 HTTP/2、WebSocket 及 libev/libevent，适用于 FreeRTOS 等嵌入式场景 · C
- [chromiumembedded/cef](https://github.com/chromiumembedded/cef) `★4.8k` - 基于 C++ 的框架，可将 Chromium 浏览器内核嵌入其他应用，支持跨平台 · C++
- [jarro2783/cxxopts](https://github.com/jarro2783/cxxopts) `★4.8k` - 轻量级 C++ 命令行参数解析库，支持选项与位置参数，仅头文件即可使用 · C++
- [armink/EasyLogger](https://github.com/armink/EasyLogger) `★4.8k` - 超轻量级 C/C++ 日志库，ROM 占用低于 1.6K、RAM 低于 0.3K，性能高，适合嵌入式场景 · C
- [libjpeg-turbo/libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo) `★4.5k` - 基于 SIMD 加速的 JPEG 编解码库，兼容 libjpeg API，支持 x86、ARM 等平台 · C
- [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) `★4.4k` - 用树莓派 GPIO 驱动多达三条 64x64、32x32 等规格的 RGB LED 点阵屏，C++ 实现，支持多路复用 · C++
- [civetweb/civetweb](https://github.com/civetweb/civetweb) `★3.5k` - 轻量级嵌入式 C/C++ Web 服务器，支持 CGI、SSL/TLS、WebSocket 与 Lua 脚本 · C
- [fukuchi/libqrencode](https://github.com/fukuchi/libqrencode) `★3k` - 用 C 编写的高速紧凑 QR 码编码库，支持生成 PNG、EPS、SVG 等多种格式 · C
- [mbebenita/Broadway](https://github.com/mbebenita/Broadway) `★2.8k` - 将 H.264 解码器编译为 JavaScript，可在浏览器中直接播放视频 · C
- [vczh-libraries/GacUI](https://github.com/vczh-libraries/GacUI) `★2.7k` - 原生 C++ 跨平台 UI 库，支持 MVVM 数据绑定、XML 描述界面与多语言，核心与渲染器跨进程分离 · C++
- [jerryscript-project/iotjs](https://github.com/jerryscript-project/iotjs) `★2.6k` - 基于 C 语言实现的轻量级 JavaScript 物联网平台，内存占用极低，可在微控制器上运行 · C
- [PortAudio/portaudio](https://github.com/PortAudio/portaudio) `★2.2k` - 跨平台开源 C 语言库，用于实时音频输入输出 · C
- [Tencent/TscanCode](https://github.com/Tencent/TscanCode) `★2.1k` - 腾讯开源的静态代码分析工具，支持 C++、C# 和 Lua，可检测代码缺陷与安全漏洞 · C++
- [NevermindZZT/letter-shell](https://github.com/NevermindZZT/letter-shell) `★1.9k` - 嵌入式系统用的 C 语言 shell，支持命令自动补全、历史记录与权限管理，可移植到单片机 · C
- [chenshuo/recipes](https://github.com/chenshuo/recipes) `★1.9k` - C++ 代码片段合集，涵盖网络编程、多线程与性能优化等实用技巧 · C++
- [micknoise/Maximilian](https://github.com/micknoise/Maximilian) `★1.7k` - C++ 音频与音乐 DSP 库，提供合成、采样、滤波等实时音频处理功能 · C++
- [GreycLab/CImg](https://github.com/GreycLab/CImg) `★1.7k` - 轻量开源 C++ 图像处理工具库，单头文件即可集成，支持读写、滤镜、变换等操作 · C++
- [quiet/quiet](https://github.com/quiet/quiet) `★1.7k` - 用声波传输数据的 C 语言调制解调器，支持声卡和 .wav 文件，可实现超声波通信 · C
- [embox/embox](https://github.com/embox/embox) `★1.6k` - 模块化可配置的嵌入式操作系统，用C编写，支持POSIX，适用于MCU和微控制器 · C
- [MaJerle/lwrb](https://github.com/MaJerle/lwrb) `★1.5k` - 轻量级通用环形缓冲区管理库，纯 C 实现，支持 FIFO 与循环缓冲，适合嵌入式 · C
- [jeremy-rifkin/cpptrace](https://github.com/jeremy-rifkin/cpptrace) `★1.5k` - 面向 C++11 及以上的轻量可移植栈回溯库，自包含无依赖，便于调试与诊断 · C++
- [achimdoebler/UGUI](https://github.com/achimdoebler/UGUI) `★1.4k` - 面向嵌入式系统的开源 GUI 模块，用 C 语言编写，轻量小巧，适合资源受限的 MCU · C
- [nilstate/icey](https://github.com/nilstate/icey) `★1.4k` - 基于 C++20 的实时媒体栈，轻量级 libwebrtc 替代方案 · C++
- [eclipse-cyclonedds/cyclonedds](https://github.com/eclipse-cyclonedds/cyclonedds) `★1.4k` - Eclipse 基金会用 C 语言实现的高性能 DDS 中间件，支持实时数据分发与发布订阅 · C
- [eliaskosunen/scnlib](https://github.com/eliaskosunen/scnlib) `★1.3k` - 现代 C++ 的 scanf 实现，支持 ranges 与格式化输入解析 · C++
- [bittorrent/libutp](https://github.com/bittorrent/libutp) `★1.2k` - uTorrent 传输协议的 C++ 实现库，用于在 UDP 上实现可靠有序的数据传输 · C++
- [seppo0010/rlite](https://github.com/seppo0010/rlite) `★1.1k` - 自包含、无服务器、零配置、支持事务的 Redis 兼容数据库引擎，用 C 编写，堪称 Redis 界的 SQLite · C
- [justdan96/tsMuxer](https://github.com/justdan96/tsMuxer) `★1.1k` - 将 EVO、VOB、MKV、MP4 等封装重混为 TS/M2TS 的 C++ 传输流复用工具，支持 H.264、H.265、VC-1、MPEG2 视频及 AAC · C++ _(archived)_
- [cinemast/libjson-rpc-cpp](https://github.com/cinemast/libjson-rpc-cpp) `★982` - 基于 C++ 的 JSON-RPC 2.0 框架，可快速构建客户端与服务端，支持 TCP、Unix 套接字和 HTTP 传输 · C++
- [chirlu/sox](https://github.com/chirlu/sox) `★967` - 音频处理全能工具，支持格式转换、特效添加与编辑，C 语言实现 · C
- [rm-hull/luma.oled](https://github.com/rm-hull/luma.oled) `★880` - Python 驱动 SSD1306、SH1106 等常见 OLED 屏，支持 I2C 与 SPI 接口，适用于树莓派 · Python
- [MyGUI/mygui](https://github.com/MyGUI/mygui) `★853` - 轻量快速的 C++ GUI 库，接口简单灵活，适合游戏与工具界面开发 · C++
- [openxc/uds-c](https://github.com/openxc/uds-c) `★833` - 用 C 实现汽车统一诊断服务 UDS 与 OBD-II 协议的库 · C
- [pfalcon/pycopy](https://github.com/pfalcon/pycopy) `★823` - 极简省内存的 Python 方言，用 C 实现，可跑在桌面、云端、嵌入式、单片机和 IoT 设备上 · C
- [aizvorski/h264bitstream](https://github.com/aizvorski/h264bitstream) `★809` - 用 C 实现读写 H.264 视频码流的完整函数库，可检查或修改码流头部 · C
- [Ampixa/sanoTTS](https://github.com/Ampixa/sanoTTS) `★806` - 仅29.4万至140万参数的神经TTS，可在3美元芯片或浏览器中运行，在1500万参数以下级别中SCOREQ/UTMOS评分领先 · C
- [rachitiitr/modern-cpp-tricks](https://github.com/rachitiitr/modern-cpp-tricks) `★721` - 汇总 C++ 现代特性技巧，助力编程面试与算法竞赛
- [ARM-software/optimized-routines](https://github.com/ARM-software/optimized-routines) `★718` - 面向 ARM 处理器的 C 语言优化库函数实现，涵盖数学、字符串、内存等例程 · C
- [leixiaohua1020/VideoEye](https://github.com/leixiaohua1020/VideoEye) `★717` - 基于 C++ 的开源流媒体分析软件，支持实时抓包与协议解析 · C++
- [waywardgeek/sonic](https://github.com/waywardgeek/sonic) `★701` - 用C编写的轻量库，可加速或减速语音播放而不改变音调 · C
- [activesys/libcstl](https://github.com/activesys/libcstl) `★674` - C 语言通用容器库，提供 vector、list、map、set 等 STL 风格数据结构与迭代器 · C
- [gustavogenovese/curl-android-ios](https://github.com/gustavogenovese/curl-android-ios) `★653` - 为 Android 和 iOS 应用提供静态 libcurl 库，附带构建脚本，无需 Android 源码 · C
- [cesanta/slre](https://github.com/cesanta/slre) `★561` - 超轻量 C/C++ 正则表达式引擎，代码极小无依赖，适合嵌入式与资源受限环境 · C
- [rm-hull/luma.led_matrix](https://github.com/rm-hull/luma.led_matrix) `★542` - Python 驱动 MAX7219 LED 点阵与 7 段数码管及 WS2812/APA102 RGB 灯珠，支持树莓派 SPI 接口 · Python
- [crayzeewulf/libserial](https://github.com/crayzeewulf/libserial) `★496` - C++ 串口编程库，封装 Linux 下 RS-232 与 USB 串口通信，简化配置与读写操作 · C++
- [jorgen/json_struct](https://github.com/jorgen/json_struct) `★474` - 单头文件 C++ 库，用模板元编程将 JSON 直接解析为 struct 或反向序列化 · C++
- [cool2528/GDownload](https://github.com/cool2528/GDownload) `★467` - 基于 C++ 开发的全功能下载管理器 · C++
- [ireader/sdk](https://github.com/ireader/sdk) `★461` - 可移植的系统调用库，用 C 实现 AIO、socket、线程、进程、锁、事件与管道 · C
- [shichaog/WebRTC-audio-processing](https://github.com/shichaog/WebRTC-audio-processing) `★428` - 基于 WebRTC 的 C++ 音频处理库，实现回声消除、降噪与自动增益控制 · C++
- [virinext/hevcesbrowser](https://github.com/virinext/hevcesbrowser) `★387` - 用 C++ 编写的 HEVC (H.265) 码流分析工具，可解析比特流结构 · C++
- [openxc/isotp-c](https://github.com/openxc/isotp-c) `★363` - 用 C 实现 ISO-TP（ISO15765-2）CAN 协议栈，支持多帧收发与流控 · C
- [Loki-Astari/ThorsAnvil](https://github.com/Loki-Astari/ThorsAnvil) `★318` - 基于 C++20 的 Web 服务与数据库驱动库，集成 HTTP 服务器、MongoDB、Slack 及 JSON/BSON 序列化 · C++
- [raas/mbw](https://github.com/raas/mbw) `★292` - 用C语言编写的内存带宽基准测试工具，可测量顺序、随机等不同访问模式下的内存读写性能 · C
- [fanchy/fflib](https://github.com/fanchy/fflib) `★291` - 轻量级 C++ 框架，面向游戏服务端与分布式程序，封装 socket、rpc、lua、CQRS、定时器、日志及性能与内存泄漏检测工具 · C
- [hartkopp/can-isotp](https://github.com/hartkopp/can-isotp) `★289` - Linux 内核模块，实现 ISO 15765-2:2016 CAN 传输协议，自 5.10 版起已并入主线内核 · C
- [esp-arduino-libs/ESP32_Display_Panel](https://github.com/esp-arduino-libs/ESP32_Display_Panel) `★284` - 面向ESP32、ESP32-S3、ESP32-P4等芯片的显示驱动与GUI移植库，用C编写，简化屏幕适配 · C
- [xyz347/x2struct](https://github.com/xyz347/x2struct) `★265` - 支持 JSON、BSON、XML 与 C++ 结构体互转的 header-only 库，基于 C++ 模板实现 · C++
- [mikewei/shm_container](https://github.com/mikewei/shm_container) `★236` - 基于 C++11 和 SysV 共享内存的高性能服务端容器集合 · C++
- [MaJerle/lwshell](https://github.com/MaJerle/lwshell) `★216` - 面向嵌入式系统的轻量级 C 语言 shell 实现，资源占用低，便于移植 · C
- [openxc/vi-firmware](https://github.com/openxc/vi-firmware) `★211` - 为 PIC32 和 LPC1768 微控制器提供兼容 OpenXC 的车辆数据采集固件，用 C++ 编写 · C++
- [Privatehive/libONVIF](https://github.com/Privatehive/libONVIF) `★202` - 基于 gsoap 的 C++ ONVIF 库，支持 Qt 集成，用于实现网络摄像机的设备发现与控制 · C++
- [fanchy/fflua](https://github.com/fanchy/fflua) `★200` - 封装 C++ 对象注册到 Lua 的嵌入库，支持将 C++ 类与函数暴露给 Lua 调用，基于 C++ 实现 · C++
- [dimtass/DSP-Cpp-filters](https://github.com/dimtass/DSP-Cpp-filters) `★188` - 用 C++ 实现的 DSP 音频滤波器集合，涵盖低通、高通、带通等常用类型 · C++
- [Ansersion/myRtspClient](https://github.com/Ansersion/myRtspClient) `★164` - 基于 jrtplib 的 C++ RTSP 客户端，实现实时流媒体拉取与解码 · C++
- [troglobit/sysklogd](https://github.com/troglobit/sysklogd) `★121` - 面向 Linux/BSD 的 syslog 守护进程，用 syslog()/syslogp() 结构化日志 API 替代传统方案，支持 RFC3164 与 RF · C
- [roleoroleo/onvif_simple_server](https://github.com/roleoroleo/onvif_simple_server) `★94` - 用 C 编写的轻量级 ONVIF 服务器，专为资源受限设备设计 · C
- [OpenIPC/divinus](https://github.com/OpenIPC/divinus) `★81` - 基于 C 语言的多平台开源推流器，支持 OpenIPC 生态下的视频流传输 · C
- [mobius3/font-chef](https://github.com/mobius3/font-chef) `★58` - 用 C/C++ 实现的字体烘焙库，可将字形预处理为位图或纹理供游戏引擎直接使用 · C
- [nwtime/linuxptp](https://github.com/nwtime/linuxptp) `★43` - Linux 平台 IEEE 1588 精确时间协议实现，用 C 编写，支持 PTP 硬件时间戳与普通时钟、边界时钟、透明时钟 · C
- [trezor-graveyard/trezor-qrenc](https://github.com/trezor-graveyard/trezor-qrenc) `★38` - 已废弃的 Trezor 硬件钱包二维码生成器，用 C 语言编写，请勿使用 · C
- [fengbingchun/OCR_Test](https://github.com/fengbingchun/OCR_Test) `★34` - 收录多款开源 OCR 代码的 C 语言测试合集，便于对比识别效果 · C
- [VFR-maniac/opencore-amr](https://github.com/VFR-maniac/opencore-amr) `★32` - AMR-NB/WB 语音编解码库的非官方镜像，C++ 实现，源自 3GPP 自适应多速率音频标准 · C++
- [ilixi/ilixi](https://github.com/ilixi/ilixi) `★23` - 面向嵌入式 Linux 的轻量级 C++ 应用框架，集成 GUI 组件与 DirectFB 渲染 · C++
- [lindenis-org/mpp_sample](https://github.com/lindenis-org/mpp_sample) `★20` - 全志V5平台MPP多媒体框架示例代码，C语言编写，演示硬件编解码接口调用 · C
- [Corvusoft/restless](https://github.com/Corvusoft/restless) `★19` - 为 C++11 应用提供异步 RESTful 客户端能力的框架 · C++
- [codec2021/codecscope](https://github.com/codec2021/codecscope) `★18` - 基于C++的编解码器性能分析工具，可视化对比多种音视频编码格式的压缩率与速度 · C++
- [jahrulnr/esp32-picoTTS](https://github.com/jahrulnr/esp32-picoTTS) `★15` - 基于 PicoTTS 引擎的 ESP32 语音合成库，支持多核并行处理与 UTF-8 文本 · C
- [sunao2002002/mem_proc](https://github.com/sunao2002002/mem_proc) `★15` - 用C实现的内存进程管理工具，支持进程内存读写与调试 · C
- [byteman/mgcpp](https://github.com/byteman/mgcpp) `★5` - MiniGUI 的 C++ 封装实现，用面向对象方式简化嵌入式 GUI 开发 · C++
- [hevnsnt/artinchip-linux](https://github.com/hevnsnt/artinchip-linux) `★4` - 逆向 ArtInChip USB 条形屏 RSA 认证，用 Python 实现 Linux 驱动，支持网页、YouTube 和视频文件投屏 · Python

## 开发工具与 DevOps

_编辑器、Git、容器、CI/CD 与效率工具_

- [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) `★134.4k` - 基于 TypeScript 的虚拟白板，支持手绘风格图表、实时协作与端到端加密 · TypeScript
- [littlecodersh/ItChat](https://github.com/littlecodersh/ItChat) `★26.5k` - 基于 Python 的微信个人号 API，三十行代码即可定制聊天机器人，支持命令行操作 · Python
- [fangzesheng/free-api](https://github.com/fangzesheng/free-api) `★16.3k` - 汇集各类免费 API 接口服务，方便开发者快速查找调用
- [Josverl/micropython-stubber](https://github.com/Josverl/micropython-stubber) `★255` - 为不同 MicroPython 移植版生成并维护类型存根，支持 VSCode、Pylance、PyRight、Thonny、PyCharm 和 MyPy 的代码 · Python

## Python 工具

_其余 Python 脚本与工具_

- [datalab-to/marker](https://github.com/datalab-to/marker) `★40.6k` - 用 Python 将 PDF 快速高精度转换为 Markdown 和 JSON · Python
- [Diolinux/PhotoGIMP](https://github.com/Diolinux/PhotoGIMP) `★18.4k` - 为 GIMP 3+ 打造的 Photoshop 风格补丁，用 Python 调整快捷键、界面布局与工具，让 PS 用户无缝迁移 · Python
- [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) `★16.4k` - 开源 SOTA 文本转语音模型，纯 CPU 即可运行，基于 Python 实现 · Python
- [pwr-Solaar/Solaar](https://github.com/pwr-Solaar/Solaar) `★9.5k` - Linux 下管理罗技设备的 Python 工具，支持 Unifying 接收器与蓝牙连接，可配置按键、手势和电池状态 · Python
- [mesonbuild/meson](https://github.com/mesonbuild/meson) `★6.6k` - 基于 Python 的跨平台构建系统，主打速度与易用性，支持 C/C++/Rust/Java 等多语言，配置简洁无需手写 Makefile · Python
- [thunil/TecoGAN](https://github.com/thunil/TecoGAN) `★6.1k` - 基于 Python 的时序连贯 GAN，用视频超分辨率生成细节丰富且帧间稳定的高清画面，出自 SIGGRAPH 论文 · Python
- [liuwons/wxBot](https://github.com/liuwons/wxBot) `★5.3k` - 基于Python的微信机器人，已停止维护 · Python
- [gumyr/build123d](https://github.com/gumyr/build123d) `★3.5k` - 基于 OpenCascade 的 Python CAD 编程库，用代码构建 B-rep 实体模型，支持 3D 打印与导出 · Python
- [mooz/percol](https://github.com/mooz/percol) `★3.3k` - 为 UNIX 管道注入交互式过滤，用 Python 实现实时筛选命令行输出 · Python
- [zhuifengshen/DingtalkChatbot](https://github.com/zhuifengshen/DingtalkChatbot) `★1.3k` - Python 封装钉钉群自定义机器人，支持文本、链接、Markdown、ActionCard 等多种消息类型 · Python
- [rdnetto/YCM-Generator](https://github.com/rdnetto/YCM-Generator) `★904` - 为 YouCompleteMe 自动生成配置文件，用 Python 编写，省去手动配置的麻烦 · Python _(archived)_
- [taizilongxu/douban.fm](https://github.com/taizilongxu/douban.fm) `★780` - 基于 Python 的豆瓣 FM 命令行客户端，支持电台播放与频道切换 · Python
- [xcLee001/SonicVale](https://github.com/xcLee001/SonicVale) `★638` - 基于 Python 的多角色多情绪 AI 配音平台，可自动为小说、剧本、视频生成配音并导出 · Python
- [tothi/pwn-hisilicon-dvr](https://github.com/tothi/pwn-hisilicon-dvr) `★384` - 针对海思芯片DVR设备的漏洞利用工具，Python编写，含固件提取与远程代码执行 · Python
- [sr99622/libonvif](https://github.com/sr99622/libonvif) `★329` - 用 C++ 实现的 Python ONVIF 库，附带实用工具程序 · C++
- [pfalcon/pycopy-lib](https://github.com/pfalcon/pycopy-lib) `★263` - Pycopy 项目的标准库，为极简轻量级 Python 实现提供核心模块 · Python
- [2549850807/Easy_Menu](https://github.com/2549850807/Easy_Menu) `★191` - 适配所有显示设备的嵌入式菜单框架，支持可视化配置，移植简单，用 Python 开发 · Python
- [nims11/IPod-Shuffle-4g](https://github.com/nims11/IPod-Shuffle-4g) `★176` - 用 Python 管理第四代 iPod Shuffle 的歌曲与播放列表 · Python
- [youkaichao/onenote-to-markdown](https://github.com/youkaichao/onenote-to-markdown) `★69` - 用 Python 脚本把 OneNote 笔记批量导出为 Markdown 文件，便于迁移到其他笔记工具 · Python
- [danielballan/photomosaic](https://github.com/danielballan/photomosaic) `★57` - 用 Python 把大量缩略图拼成马赛克，远看呈现一张大图 · Python
- [sumary/dmusic-plugin-baidumusic](https://github.com/sumary/dmusic-plugin-baidumusic) `★48` - 为 Deepin Music Player 提供百度音乐插件，用 Python 编写，可直接搜索播放在线歌曲 · Python
- [dairoot/miloco-sdk](https://github.com/dairoot/miloco-sdk) `★44` - Python 实现的 Miloco 智能家居本地控制 SDK，支持局域网直连设备，无需云端中转 · Python
- [562590763/CADDesigner-Code](https://github.com/562590763/CADDesigner-Code) `★26` - 基于Python的CAD绘图工具，通过自然语言指令驱动AI生成设计代码，简化CAD建模流程 · Python
- [csrgxtu/Drogo](https://github.com/csrgxtu/Drogo) `★24` - 用 Python 把微信变成命令行聊天工具，让黑客在终端收发消息 · Python
- [PerpetualSmile/convert_picture_to_snowing_gif](https://github.com/PerpetualSmile/convert_picture_to_snowing_gif) `★10` - 用 Python 的 Pillow 和 pygame 为静态图片添加下雪动画并导出 GIF · Python
- [coffee-it/uargparse](https://github.com/coffee-it/uargparse) `★2` - MicroPython 的命令行参数解析库，移植自 Python 标准库 argparse，可在微控制器上使用 · Python

## 字体与设计

_字体、图标与设计资源_

- [subframe7536/maple-font](https://github.com/subframe7536/maple-font) `★29.5k` - 开源等宽编程字体，圆角设计，支持连字与 Nerd-Font 图标，中英文宽度 2:1，可细粒度自定义，适用于 IDE 和终端 · Python
- [lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai) `★26.5k` - 基于 Klee One 衍生的开源中文字体，兼顾简体繁体与日文，风格清秀易读 · Shell
- [lxgw/LxgwWenKai-Screen](https://github.com/lxgw/LxgwWenKai-Screen) `★2.2k` - 霞鹜文楷屏幕阅读版，优化字形与字重，适合电子屏幕阅读的中文开源字体
- [jonacruz89/SAWARATSUKI.ServiceLogos](https://github.com/jonacruz89/SAWARATSUKI.ServiceLogos) `★456` - 把服务 Logo 变成可爱风格的开源素材库，请勿随意 Fork

## 未分类

_尚未归类，可在 config.yaml 中通过 topics / overrides 配置分类。_

- [w7corp/easywechat](https://github.com/w7corp/easywechat) `★10.4k` - PHP 微信 SDK，封装公众号、小程序、支付、开放平台等全模块 API，开箱即用 · PHP
- [phaselden/FlipIt](https://github.com/phaselden/FlipIt) `★1.3k` - 用 C# 编写的翻页时钟屏保，模拟经典机械翻页效果 · C#
- [dieforfree/qart4j](https://github.com/dieforfree/qart4j) `★890` - 用 Java 将二维码渲染成 ASCII 字符画，支持终端直接展示 · Java
- [cxmforever/notice-board](https://github.com/cxmforever/notice-board) `★412` - 基于 mmy 的公告板项目，提供简洁的公告发布与管理功能
- [idealclover/Love-Gift](https://github.com/idealclover/Love-Gift) `★338` - 用 CoffeeScript 编写的浪漫网页礼物，献给前女友的爱心小惊喜 · CoffeeScript _(archived)_
- [xianweics/refator-code](https://github.com/xianweics/refator-code) `★87` - 基于 Martin Fowler 重构理念，系统讲解改善既有代码设计的手法与实战技巧

<!-- oh-my-awesome:end -->
