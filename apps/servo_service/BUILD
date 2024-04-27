load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "servoService",
    bin = "//services/ServoService",
    configs = [
        ":app_config"
    ],
    add_configs = [
        "config.json",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

filegroup(
    name = "app_config",
    srcs = ["app.json"],
    visibility = ["//deployment/apps:__subpackages__"],
)
