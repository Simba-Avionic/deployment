# load("//deployment/bazel:srp_component.bzl", "srp_component")

# srp_component(
#     name = "temp_service",
#     bin = "//mw/temp/service:temp_service_mw",
#     configs = [
#         ":config",
#     ],
#     add_configs = [
#         "config.json",
#     ],
#     visibility = ["//deployment/cpu:__subpackages__"],
# )
load("//deployment/tools/ara:adaptive_application.bzl", "ara_runtime_lib", "adaptive_application")

filegroup(
    name = "instance",
    srcs = [
        "app_config.json",
        "//deployment/system_definition/diag/jobs:temp_job",
    ],
    visibility = ["//mw/gpio_server:__subpackages__"],
)

adaptive_application(
    name = "temp_service",
    bin = "//mw/temp/service:temp_service_mw",
    model_src = ["//deployment/mw/temp:instance"],
    etcs = ["config.json"],
    visibility = ["//visibility:public"],
)

ara_runtime_lib(
    name = "ara",
    model_src = ["//deployment/mw/temp:instance"],
    visibility = ["//mw/temp/service:__subpackages__"]
)