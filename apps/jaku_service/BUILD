load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "jaku_service",
    bin = "//apps/jaku_service",
    configs = [
        ":app_config"
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

filegroup(
    name = "app_config",
    srcs = ["app.json"],
    visibility = ["//deployment/apps:__subpackages__"],
)
