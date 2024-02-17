load("//deployment/bazel:srp_component.bzl", "srp_component")
load("//deployment/bazel:config_gen.bzl", "config_gen")

srp_component(
    name = "em",
    app_id = "0x0102",
    bin = "//mw/em/code:em",
    configs = [
        "logger.json",
    ],
    diag_enable = True,
    visibility = ["//deployment/cpu:__subpackages__"],
)
filegroup(
    name = "config",
    srcs = ["app.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)
config_gen(
    name = "test",
    config_src = [":config"],
    includes = ["//deployment:Apps"],
)
