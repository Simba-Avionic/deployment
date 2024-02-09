load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "example",
    bin = "//apps/example",
    configs = [
        "config.json",
        "logger.json",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

