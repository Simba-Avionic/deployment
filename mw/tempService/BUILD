load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "tempService",
    bin = "//mw/temp/service:temp_service_mw",
    configs = [
        ":app_config",
    ],
    add_configs = [
    "temp_config.json",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
filegroup(
    name = "app_config",
    srcs = ["app.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)
