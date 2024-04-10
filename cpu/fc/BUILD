load("//deployment/bazel:cpu_def.bzl", "cpu_def")

cpu_def(
    name = "pkg",
    config = ":config",
    srp_components = [
        "//deployment/mw/loger/dlt_fc/fc:dlt_server",
        "//deployment/apps/example2/example",
        "//deployment/mw/em",
        "//deployment/mw/gpio",
    ],
)

filegroup(
    name = "config",
    srcs = ["platform_config.json"],
    visibility = ["//deployment/cpu:__subpackages__"],
)
