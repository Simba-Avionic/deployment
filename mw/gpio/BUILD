# load("//deployment/bazel:srp_component.bzl", "srp_component")

# srp_component(
#     name = "gpio",
#     bin = "//mw/gpio_server:gpio_service",
#     configs = [
#         ":config",
#     ],
#     add_configs = [
#         "config.json",
#     ],
#     visibility = ["//deployment/cpu:__subpackages__"],
# )
# filegroup(
#     name = "config",
#     srcs = [
#         "app.json",
#         ],
#     visibility = ["//deployment/mw:__subpackages__"],
# )

load("//deployment/tools/ara:adaptive_application.bzl", "adaptive_application")

filegroup(
    name = "instance",
    srcs = [
        "app_config.json",
        "//deployment/system_definition/diag/jobs:gpio_mw_job",
    ],
    visibility = ["//mw/gpio_server:__subpackages__"],
)

adaptive_application(
    name = "gpio_service",
    bin = "//mw/gpio_server:gpio_service",
    model_src = ["//deployment/mw/gpio:instance"],
    etcs = ["config.json"],
    visibility = ["//visibility:public"],
)