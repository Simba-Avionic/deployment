load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")

pkg_tar(
    name = "config_files",
    package_dir = "/etc/simba/ota",
    srcs = ["config.json"],
    mode = "0755",
)
