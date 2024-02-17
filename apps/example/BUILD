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

filegroup(
    name = "app_config",
    srcs = ["app.json","app2.json"],
    visibility = ["//deployment/apps:__subpackages__"],
)
