load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "i2c_service",
    bin = "//mw/i2c_service",
    configs = [
        ":config",
    ],
    add_configs = [
        "config.json",
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
