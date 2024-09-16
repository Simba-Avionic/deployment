# load("//deployment/bazel:srp_component.bzl", "srp_component")

# srp_component(
#     name = "servoService",
#     bin = "//apps/ServoService",
#     configs = [
#         ":app_config"
#     ],
#     add_configs = [
#         "config.json"
#     ],
#     visibility = ["//deployment/cpu:__subpackages__"],
# )

# filegroup(
#     name = "app_config",
#     srcs = ["app.json"],
#     visibility = ["//deployment/apps:__subpackages__"],
# )

load("//deployment/tools/ara:adaptive_application.bzl", "adaptive_application")

filegroup(
    name = "instance",
    srcs = [
        "app_config.json",
        "//deployment/system_definition/diag/jobs:servo_status_job",
        "//deployment/system_definition/diag/jobs:vent_servo_status_job",
    ],
    visibility = ["//apps/ServoService:__subpackages__"],
)

adaptive_application(
    name = "servoService",
    bin = "//apps/ServoService",
    model_src = ["//deployment/apps/servo_service:instance"],
    etcs = ["config.json"],
    visibility = ["//visibility:public"],
)

