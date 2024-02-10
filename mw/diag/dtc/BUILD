load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    app_id = "0x0101",
    diag_enable = True, 
    name = "dtc_service",
    bin = "//mw/diag/dtc:dtc_service",
    configs = [
        "logger.json",
    ],
    startup_prio = "8",
    visibility = ["//deployment/cpu:__subpackages__"],
)
