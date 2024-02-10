load("//deployment/bazel:flash_ecu.bzl", "flash_ecu")
load("//deployment/bazel:flash_ecu.bzl", "flash_bbb_ecu")

flash_ecu(
    name = "flash_ec",
    file = ["//deployment/cpu/ec:pkg"],
    ip = "192.168.10.101",
    user_name = "root",
)


flash_bbb_ecu(
    name = "flash_bbb_ec",
    file = ["//deployment/cpu/ec:pkg"],
    ip = "192.168.10.101",
    user_name = "root",
)