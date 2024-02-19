load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "em",
    bin = "//mw/em/code:em",
    configs = [
        ":config",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
filegroup(
    name = "config",
    srcs = ["app.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)
