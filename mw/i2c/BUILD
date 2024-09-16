load("//deployment/tools/ara:adaptive_application.bzl", "adaptive_application")

filegroup(
    name = "instance",
    srcs = [
        "app_config.json",
    ],
    visibility = ["//mw/i2c_service:__subpackages__"],
)

adaptive_application(
    name = "i2cMWService",
    bin = "//mw/i2c_service:i2cService",
    model_src = ["//deployment/mw/i2c:instance"],
    visibility = ["//visibility:public"],
)


# load("//deployment/bazel:srp_component.bzl", "srp_component")

# srp_component(
#     name = "i2c_service",
#     bin = "//mw/i2c_service",
#     configs = [
#         ":config",
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
