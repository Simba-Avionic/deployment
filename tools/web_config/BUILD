py_binary(
    name = "web_config",
    srcs = ["web_config.py"],
    data = [],
    visibility = ["//visibility:public"],
    deps = [],
)

py_binary(
    name = "diag_connector",
    srcs = ["diag_connector.py"],
    visibility = ["//visibility:public"],
    deps = [
        "//deployment/tools/configs/diag:diag_jobs",
        "//deployment/tools/configs/dtc_gen:dtc_lib",
    ],
)
