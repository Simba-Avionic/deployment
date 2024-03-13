# load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")
# load("//deployment/bazel:start_service_list.bzl", "start_service_list")
load("//deployment/bazel:cpu_def.bzl", "cpu_def")

cpu_def(
    name = "pkg",
    cpu_name = "ec",
    interface_name = "eth0",
    ip = "192.168.10.101",
    mask = "255.255.255.0",
    srp_components = [
        "//deployment/mw/loger/dlt_fc:dlt_server",
        "//deployment/apps/example",
        "//deployment/mw/em",
        "//deployment/mw/diag/dtc:dtc_service",
        "//deployment/mw/temp:temp_service_mw",
    ],
)

filegroup(
    name = "config",
    srcs = ["platform_config.json"],
    visibility = ["//deployment/cpu:__subpackages__"],
)