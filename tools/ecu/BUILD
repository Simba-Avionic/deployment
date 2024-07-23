load("//deployment/bazel:flash_ecu.bzl", "flash_ecu")
load("//deployment/bazel:docker_flash_ecu.bzl", "docker_flash_ecu")

flash_ecu(
    name = "flash_ec",
    file = ["//deployment/cpu/ec:pkg"],
    ip = "192.168.10.101",
    user_name = "root",
)

flash_ecu(
    name = "flash_fc",
    file = ["//deployment/cpu/fc:pkg"],
    ip = "192.168.10.102",
    user_name = "root",
)

docker_flash_ecu(
    name = "sim_flash_fc",
    file = ["//deployment/cpu/fc:pkg"],
    ip = "192.168.10.102",
    user_name = "root",
)
docker_flash_ecu(
    name = "sim_flash_ec",
    file = ["//deployment/cpu/ec:pkg"],
    ip = "192.168.10.101",
    user_name = "root",
)