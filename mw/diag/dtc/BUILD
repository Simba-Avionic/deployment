load("//deployment/bazel:srp_component.bzl", "srp_component")
load("//deployment/bazel:dtc_gen.bzl", "dtc_support_list")

srp_component(
    name = "dtc_service",
    bin = "//mw/diag/dtc:dtc_service",
    configs = [
        ":config",
    ],
    add_configs = [":dtc_config",],
    includes_diag = [
        "//deployment/system_definition/diag/jobs:dtc_jobs",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

filegroup(
    name = "config",
    srcs = ["app.json",],
    visibility = ["//deployment/mw:__subpackages__"],
)

dtc_support_list(
    name = "dtc_config",
    includes = ["//deployment/system_definition/diag/dtc:Example_dtc"],
)
