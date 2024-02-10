load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    app_id = "0x0102",
    diag_enable = True, 
    name = "em",
    bin = "//mw/em/code:em",
    configs = [
        "logger.json",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)
