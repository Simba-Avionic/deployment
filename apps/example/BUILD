load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")

pkg_tar(
    name = "config_files",
    package_dir = "/etc/simba/example",
    srcs = ["config.json"],
    mode = "0755",
)

pkg_tar(
    name = "bin",
    package_dir = "/bin/simba/example",
    srcs = ["//apps/example:router"],
    mode = "0755",
)

pkg_tar(
    name = "pkg",
    deps = ["//deployment/apps/example:config_files","//deployment/apps/example:bin"],
)