<h1 align="center">MindStudio Profiler Tools Interface</h1>

<div align="center">
  <p><b>昇腾 Profiling 工具接口</b></p>

[📖 用户指南](./docs/zh/README.md) |
[🛠️ 安装指南](./docs/zh/mspti_install_guide.md) |
[📚 API 参考](./docs/zh/c_api/README.md) |
[🌐 软件下载](https://gitcode.com/Ascend/mspti/releases)

</div>

<br>

## 📢 最新消息

* [2026.02.06]：版本说明新增 `26.0.0-alpha.1` 发布记录，兼容 CANN `> 8.5.0`，详情请参见 [《版本说明》](./docs/zh/release_notes.md)。

## 📌 简介

msPTI（MindStudio Profiler Tools Interface）是面向 Ascend 设备的 Profiling API 集合，帮助开发者为 NPU 应用构建性能采集与分析工具，适用于推理与训练场景。

msPTI 主要提供以下能力：

- `Tracing`：采集 CANN API、Kernel、内存拷贝、通信、打点等时间戳及附加信息，用于定位执行链路中的性能瓶颈。
- `Profiling`：单独采集一个或一组 Kernel 的 NPU 性能指标，支撑计算与通信分析。

## 🔍 目录结构

```text
├─docs
│  └─zh                  # 中文文档、安装指南、版本说明、安全声明、API 参考
├─csrc                   # C/C++ 核心实现
│  ├─activity            # Activity 数据采集与解析
│  ├─callback            # Callback 订阅与回调管理
│  ├─common              # 公共基础能力
│  └─include             # msPTI C API 头文件
├─mspti                  # Python 封装
│  ├─monitor             # Kernel / HCCL / MSTX Monitor
│  └─csrc                # Python 扩展绑定实现
├─samples                # C++ / Python 样例
├─scripts                # 构建、打包、安装、测试脚本
├─test                   # UT / ST 测试代码
├─CMakeLists.txt         # C++ 构建入口
└─README.md              # 仓库总览
```

## 📖 功能介绍

| 模块 | 功能简介 | 资料入口 |
| --- | --- | --- |
| `Activity API` | 采集 API、Kernel、Memory、HCCL、Marker、External Correlation 等活动数据，用于构建 Tracing / Profiling 工具。 | [C API 参考](./docs/zh/c_api/README.md) |
| `Callback API` | 订阅 Runtime / HCCL 回调，在 API 调用前后执行自定义逻辑或关联采集数据。 | [C API 参考](./docs/zh/c_api/README.md) |
| `Python API` | 提供 `KernelMonitor`、`HcclMonitor`、`MstxMonitor` 等接口，快速接入 Python 场景分析能力。 | [Python API 参考](./docs/zh/python_api/README.md) |
| `样例集` | 覆盖 callback、activity、correlation、HCCL、Python monitor 等典型场景，便于快速上手。 | [样例说明](./samples/README.md) / [用户指南](./docs/zh/README.md) |

## 🛠️ 安装指南

msPTI 运行依赖配套版本的 CANN 环境。安装 msPTI 前，请先完成以下环境准备：

- 硬件环境请参见《[昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)》。
- 软件环境请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/softwareinst/instg/instg_quick.html?Mode=PmIns&InstallType=local&OS=openEuler&Software=cannToolKit)》安装配套版本的 CANN Toolkit 开发套件包和 ops 算子包。

完成上述准备后，可通过以下两种方式安装 msPTI：

- 方式一：从 [releases 页面](https://gitcode.com/Ascend/mspti/releases) 下载预构建的 `run` 包，执行 MD5 校验后安装。
- 方式二：从源码仓执行 `bash scripts/build.sh [<version>]` 先构建 `run` 包，再安装。

完整环境准备、两种安装方式的详细步骤、安装参数与示例命令请参见 [《msPTI 工具安装指南》](./docs/zh/mspti_install_guide.md)。

## 🚀 快速入门

建议按照“安装工具 -> 配置环境 -> 运行样例”的顺序完成快速体验：

1. 完成工具安装。

   请先参见 [《msPTI 工具安装指南》](./docs/zh/mspti_install_guide.md)，通过“下载 `run` 包安装”或“源码构建 `run` 包后安装”任一方式完成安装。

2. 配置 CANN 环境变量。

   ```bash
   source ${install_path}/set_env.sh
   ```

3. 进入样例目录并执行脚本。

   ```bash
   cd ${install_path}/tools/mspti/samples/callback_domain
   bash sample_run.sh
   ```

其中 `${install_path}` 需要替换为 CANN 的安装路径，例如 `/usr/local/Ascend/cann`。

`samples` 目录下各样例的适用场景、能力说明与补充说明，请参见 [《samples 样例说明》](./samples/README.md)。

## 📝 相关说明

- [《版本说明》](./docs/zh/release_notes.md)
- [《C API 参考》](./docs/zh/c_api/README.md)
- [《Python API 参考》](./docs/zh/python_api/README.md)
- [《安全声明》](./docs/zh/security_statement.md)
- [LICENSE](./LICENSE)
- [Third_Party_Open_Source_Software_Notice](./Third_Party_Open_Source_Software_Notice)
- 欢迎通过 [Issues](https://gitcode.com/Ascend/mspti/issues) 和 Pull Request 参与贡献；提交前请完成本地自测并确保新增能力带有必要测试。

## 💬 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交 [Issues](https://gitcode.com/Ascend/mspti/issues)，我们会尽快回复。感谢你的支持。

## 🤝 致谢

msPTI 由华为昇腾计算 MindStudio 开发部贡献，感谢来自社区的每一个 PR，欢迎持续参与共建。

## 关于 MindStudio 团队

MindStudio 团队围绕昇腾开发场景持续建设训练、推理、性能分析等工具链能力。更多信息请访问 [昇腾社区](https://www.hiascend.com/developer/software/mindstudio) 和 [昇腾论坛](https://www.hiascend.com/forum/)。
