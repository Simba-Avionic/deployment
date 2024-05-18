load("//deployment/bazel:flash_ecu.bzl", "flash_ecu")

flash_ecu(
    name = "flash_ec",
    file = ["//deployment/cpu/ec:pkg"],
    ip = "192.168.11.101",
    user_name = "root",
)

flash_ecu(
    name = "flash_fc",
    file = ["//deployment/cpu/fc:pkg"],
    ip = "192.168.10.102",
    user_name = "root",
)
flash_ecu(
    name = "flash_sim_ec",
    file = ["//deployment/cpu/ec_sim:pkg"],
    ip = "192.168.11.101",
    user_name = "root",
)
flash_ecu(
    name = "flash_sim_fc",
    file = ["//deployment/cpu/fc_sim:pkg"],
    ip = "192.168.11.102",
    user_name = "root",
)