load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "em",
    bin = "//mw/em/code:em",
    configs = [
        "config.json",
        "logger.json",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
