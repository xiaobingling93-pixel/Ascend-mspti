# MindStudio-Profilier-Tools-Interface

## 简介

msPTI工具（MindStudio Profilier Tools Interface）是MindStudio针对Ascend设备提出的一套Profiling API，用户可以通过msPTI构建针对NPU应用程序的工具，用于分析应用程序的性能。

msPTI为通用场景接口，使用msPTI API开发的Profiling分析工具可以在各种框架的推理训练场景生效。

msPTI主要包括以下功能：

- Tracing：在msPTI中Tracing是指CANN应用程序执行启动CANN活动的时间戳和附加信息的收集，如CANN API、Kernel、内存拷贝等。通过了解程序运行耗时，识别CANN代码的性能问题。可以使用Activity API和Callback API收集Tracing信息。
- Profiling：在msPTI中Profiling是指单独收集一个或一组Kernel的NPU性能指标。

## 目录结构

目录如下：

```sh
└── docs                      // 文档
	└── zh                    // 中文文档
└── csrc                      // 使用C开发的一套API
└── mspti                     // 将C API的功能作为底层逻辑封装的一套Python的API
└── samples                   // 工具样例存放目录
└── scripts                   // 存放whl包构建脚本，run包编译、安装相关脚本，UT运行、覆盖率脚本等
└── test                      // 测试部分，存放UT代码
└── README.md                 // 整体仓说明文档

```

## 环境部署

### 环境和依赖

- 硬件环境请参见《[昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)》。

- 工具的使用运行需要提前获取并安装CANN开源版本，当前CANN开源版本正在发布中，敬请期待。

### 工具安装

安装msPTI工具，详情请参见《[msPTI工具安装指南](docs/zh/mspti_install_guide.md)》。

## 功能介绍

使用msPTI工具，详情请参见《[msPTI工具用户指南](docs/zh/README.md)》。

## API参考

- [msPTI C API参考](docs/zh/c_api/README.md)

  介绍msPTI工具C语言的API。

- [msPTI Python API参考](docs/zh/python_api/README.md)

  介绍msPTI工具Python语言的API。

## 免责声明

### 致msPTI使用者

- 本工具仅供调试和开发使用，使用者需自行承担使用风险，并理解以下内容：
  - 数据处理及删除：用户在使用本工具过程中产生的数据属于用户责任范畴。建议用户在使用完毕后及时删除相关数据，以防信息泄露。
  - 数据保密与传播：使用者了解并同意不得将通过本工具产生的数据随意外发或传播。对于由此产生的信息泄露、数据泄露或其他不良后果，本工具及其开发者概不负责。
  - 用户输入安全性：用户需自行保证输入的命令行的安全性，并承担因输入不当而导致的任何安全风险或损失。对于输入命令行不当所导致的问题，本工具及其开发者概不负责。
- 免责声明范围：本免责声明适用于所有使用本工具的个人或实体。使用本工具即表示您同意并接受本声明的内容，并愿意承担因使用该功能而产生的风险和责任，如有异议请停止使用本工具。
- 在使用本工具之前，请**谨慎阅读并理解以上免责声明的内容**。对于使用本工具所产生的任何问题或疑问，请及时联系开发者。

### 致数据所有者

如果您不希望您的模型或数据集等信息在msPTI中被提及，或希望更新msPTI中有关的描述，请在GitCode提交Issue，我们将根据您的Issue要求删除或更新您的相关描述。衷心感谢您对msPTI的理解和贡献。


## 安全声明

描述msPTI产品的安全加固信息、公网地址信息及通信矩阵等内容。详情请参见《[msPTI工具安全声明](./docs/zh/security_statement.md)》。

## License

msPTI产品的使用许可证，详见[LICENSE](./LICENSE)文件。

msPTI工具docs目录下的文档适用CC-BY 4.0许可证，具体请参见[LICENSE](./docs/LICENSE)。

## 贡献声明
1. **提交错误报告**：如果您在msPTI中发现了一个不存在安全问题的漏洞，请在msPTI仓库中的Issues中搜索，以防该漏洞被重复提交，如果找不到漏洞可以创建一个新的Issues。如果发现了一个安全问题，请不要将其公开，请参阅安全问题处理方式。提交错误报告时应该包含完整信息。
2. **安全问题处理**：本项目中对安全问题处理的形式，请通过邮箱通知项目核心人员确认编辑。
3. **解决现有问题**：通过查看仓库的Issues列表可以发现需要处理的问题信息，可以尝试解决其中的某个问题。
4. **如何提出新功能**：请使用Issues的Feature标签进行标记，我们会定期处理和确认开发。
5. **开始贡献：**<br>
    a. Fork本项目的仓库。<br>
    b. Clone到本地。<br>
    c. 创建开发分支。<br>
    d. 本地自测：提交前请通过所有的单元测试，包括新增的单元测试。<br>
    e. 提交代码。<br>
    f. 新建Pull Request。<br>
    g. 代码检视：您需要根据评审意见修改代码，并再次推送更新。此过程可能会有多轮。<br>
    h. 当您的PR获得足够数量的检视者批准后，Committer会进行最终审核。<br>
    i. 审核和测试通过后，CI会将您的PR合并入到项目的主干分支。

## 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交[Issues](https://gitcode.com/Ascend/mspti/issues)，我们会尽快回复。感谢您的支持。

## 致谢

msPTI由华为公司的下列部门联合贡献：

- 昇腾计算MindStudio开发部

感谢来自社区的每一个PR，欢迎贡献msPTI！