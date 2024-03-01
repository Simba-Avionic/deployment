load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "tempService",
    bin = "//mw/tempService:tempServiceMW",
    configs = [
        ":app_config",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
filegroup(
    name = "app_config",
    srcs = ["app.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)
