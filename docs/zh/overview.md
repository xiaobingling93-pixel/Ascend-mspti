# 简介

msPTI工具（MindStudio Profiler Tools Interface）是MindStudio针对Ascend设备提出的一套Profiling API，用户可以通过msPTI构建针对NPU应用程序的工具，用于分析应用程序的性能。

msPTI为通用场景接口，使用msPTI API开发的Profiling分析工具可以在各种框架的推理训练场景生效。

msPTI主要包括以下功能：

- Tracing：在msPTI中Tracing是指CANN应用程序执行启动CANN活动的时间戳和附加信息的收集，如CANN API、Kernel、内存拷贝等。通过了解程序运行耗时，识别CANN代码的性能问题。可以使用Activity API和Callback API收集Tracing信息。
- Profiling：在msPTI中Profiling是指单独收集一个或一组Kernel的NPU性能指标。
