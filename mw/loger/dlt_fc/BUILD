load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "dlt_server",
    bin = "//mw/logger/code:dlt_server",
    configs = [
        "config.json",
        "logger.json",
    ],
    startup_prio = "10",
    visibility = ["//deployment/cpu:__subpackages__"],
)

