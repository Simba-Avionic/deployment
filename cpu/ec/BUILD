load("//deployment/bazel:cpu_def.bzl", "cpu_def")

cpu_def(
    name = "pkg",
    config = ":config",
    etcs = [
        "diag_config.json",
        "logger_config.json",
    ],
    srp_components = [
        # "//deployment/mw/loger/dlt_fc:dlt_server",
        # "//deployment/apps/example",
        # "//deployment/mw/em",
        # "//deployment/mw/gpio",
        # "//deployment/mw/temp:temp_service",
        # "//deployment/apps/env_service",
        # "//deployment/apps/prim_service",
        # "//deployment/apps/diag_ota/ec:diag_ota",
        # "//deployment/apps/servo_service:servoService",
        # # "//deployment/mw/diag/dtc:dtc_service",
        # "//deployment/mw/i2c:i2c_service",
        "//deployment/example_adaptive/ExampleApp",
        "//deployment/example_adaptive/ExampleApp2",
        "//deployment/platform/em",
        "//deployment/platform/logger",
        "//deployment/platform/diag_demon",
    ],
)

filegroup(
    name = "config",
    srcs = ["platform_config.json"],
    visibility = ["//deployment/cpu:__subpackages__"],
)
