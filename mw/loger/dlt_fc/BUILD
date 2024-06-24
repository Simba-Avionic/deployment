load("//deployment/bazel:srp_component.bzl", "srp_component")
srp_component(
    name = "dlt_server",
    bin = "//mw/logger/code:dlt_server",
    configs = [
        ":config",
    ],
    add_configs = [
    "//deployment/mw/loger/dlt_fc:temp_configs",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
filegroup(
    name = "config",
    srcs = ["app.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)
filegroup(
    name = "temp_configs",
    srcs = ["config.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)