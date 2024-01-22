load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "dlt_server",
    bin = "//mw/loger/dlt:dlt_server",
    configs = [
        "config.json",
        "logger.json",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

