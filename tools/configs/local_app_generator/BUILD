py_binary(
    name = "generator",
    srcs = ["generator.py"],
    deps=["//deployment/tools/configs/local_app_generator/lib"],
    data=["//deployment/tools/configs/local_app_generator:example"],
    visibility = ["//visibility:public"],
)
filegroup(
    name = "example",
    srcs = ["example.json"],
)