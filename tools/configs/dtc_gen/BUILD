py_binary(
    name = "dtc_gen",
    srcs = ["dtc_gen.py"],
    imports = ["."],
    visibility = ["//visibility:public"],
    deps = [
        "//deployment/tools/configs/diag:diag_jobs",
        "//deployment/tools/configs/dtc_gen:dtc_lib",
    ],
)

py_library(
    name = "dtc_lib",
    srcs = ["dtc.py"],
    visibility = ["//visibility:public"],
)
