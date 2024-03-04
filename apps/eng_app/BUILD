load("//deployment/bazel:config_gen.bzl", "bs_someip_gen")
filegroup(
    name = "app_config",
    srcs = ["app.json"],
    visibility = ["//deployment/apps:__subpackages__"],
)

bs_someip_gen(
    name="config",
    config_src = [":app_config"],
    includes = ["//deployment:Apps"],
    )