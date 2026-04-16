file(GLOB_RECURSE SRC_FILE
    ${TOP_DIR}/csrc/activity/*.cpp
    ${TOP_DIR}/csrc/callback/*.cpp
    ${TOP_DIR}/csrc/common/*.cpp
)

file(GLOB_RECURSE REMOVE_SOURCES
    ${TOP_DIR}/csrc/common/inject/*.cpp
)

list(REMOVE_ITEM SRC_FILE ${REMOVE_SOURCES})

add_executable(dostart_chain
    ${SRC_FILE}
    main.cpp
    callback_dostart_chain.cpp
    ${TOP_DIR}/csrc/common/inject/mstx_inject.cpp
    ${TOP_DIR}/csrc/common/function_loader.cpp
    ${UT_TOP_DIR}/stub/inject/driver_inject_stub.cpp
    ${UT_TOP_DIR}/stub/inject/profapi_inject_stub.cpp
    ${UT_TOP_DIR}/stub/inject/acl_inject_stub.cpp
    ${UT_TOP_DIR}/stub/inject/hccl_inject_stub.cpp
)
 
run_test(dostart_chain)
