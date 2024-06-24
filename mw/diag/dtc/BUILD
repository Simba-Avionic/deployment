load("//deployment/bazel:srp_component.bzl", "srp_component")
load("//deployment/bazel:dtc_gen.bzl", "dtc_support_list")

srp_component(
    name = "dtc_service",
    add_configs = [":dtc_config"],
    bin = "//mw/diag/dtc:dtc_service",
    configs = [
        ":config",
    ],
    includes_diag = [
        "//deployment/system_definition/diag/jobs:dtc_jobs",
        "//deployment/system_definition/diag/dtc:Incorrect_dtc_config",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

filegroup(
    name = "config",
    srcs = ["app.json"],
    visibility = ["//deployment/mw:__subpackages__"],
)

dtc_support_list(
    name = "dtc_config",
    includes = [
        "//deployment/system_definition/diag/dtc:Example_dtc",
        "//deployment/system_definition/diag/dtc:Incorrect_dtc_config",
    ],
)
