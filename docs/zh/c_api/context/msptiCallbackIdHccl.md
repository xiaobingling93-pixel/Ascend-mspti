# msptiCallbackIdHccl<a name="ZH-CN_TOPIC_0000002049465541"></a>

msptiCallbackIdHccl为[msptiEnableCallback](msptiEnableCallback.md)调用的枚举类。只有在枚举类中定义的函数才可以被callback api追踪。这些枚举在全局中唯一，定义如下：

```cpp
typedef enum {
	MSPTI_CBID_HCCL_ALLREDUCE = 1,//表示跟踪函数为HccAllReduce
	MSPTI_CBID_HCCL_BROADCAST = 2,//表示跟踪函数为HccBoardCast
	//其他枚举值与上述例子类似，不再赘述
} msptiCallbackIdHccl;
```

