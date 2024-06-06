load("//deployment/bazel:cpu_def.bzl", "cpu_def")

cpu_def(
    name = "pkg",
    config = ":config",
    srp_components = [
        "//deployment/mw/loger/dlt_fc:dlt_server",
        "//deployment/apps/example",
        "//deployment/mw/em",
        "//deployment/mw/gpio",
        "//deployment/mw/temp:temp_service",
        "//deployment/apps/env_service",
        "//deployment/apps/prim_service",
        "//deployment/apps/diag_ota/ec:diag_ota",
        "//deployment/apps/servo_service:servoService",
        # "//deployment/mw/diag/dtc:dtc_service",
        "//deployment/mw/i2c:i2c_service",
        "//deployment/apps/logger_service",
    ],
)

filegroup(
    name = "config",
    srcs = ["platform_config.json"],
    visibility = ["//deployment/cpu:__subpackages__"],
)
