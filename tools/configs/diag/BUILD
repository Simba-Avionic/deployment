py_library(
    name = "diag_jobs",
    srcs = ["diag_job.py"],
)

py_binary(
    name = "app_diag_gen",
    srcs = ["app_diag_gen.py"],
    imports = ["."],
    visibility = ["//visibility:public"],
    deps = ["//deployment/tools/configs/diag:diag_jobs"],
)
