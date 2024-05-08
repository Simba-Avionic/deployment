load("//deployment/bazel:srp_component.bzl", "srp_component")

srp_component(
    name = "diag_ota",
    add_configs = [
        "config.json",
        "//libdoip/examples:example_server",
    ],
    bin = "//apps/diag_ota/code:diag_ota",
    configs = [
        ":app_config",
    ],
    includes_diag = [
        "//deployment/system_definition/diag/jobs:read_vin_job",
        "//deployment/system_definition/diag/jobs:start_rid",
        "//deployment/system_definition/diag/jobs:hard_restart",
    ],
    visibility = ["//deployment/cpu:__subpackages__"],
)

filegroup(
    name = "app_config",
    srcs = ["app.json"],
    visibility = ["//deployment/apps:__subpackages__"],
)
