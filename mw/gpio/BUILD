load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "gpio",
    bin = "//mw/gpio_server:gpio_service",
    configs = [
        ":config",
    ],
    add_configs = [
        "//deployment/mw/gpio:configs"
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
filegroup(
    name = "config",
    srcs = [
        "app.json",
        ],
    visibility = ["//deployment/mw:__subpackages__"],
)
filegroup(
    name = "configs",
    srcs = ["config.json"],
    visibility = ["//visibility:public"],
)