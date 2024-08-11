load("//deployment/tools/ara:adaptive_application.bzl", "adaptive_application", "ara_runtime_lib", "ara_someip_lib")

ara_runtime_lib(
    name = "ara",
    model_src = ["//deployment/example_adaptive/ExampleApp:instance"],
)

ara_someip_lib(
    name = "someip_lib",
    model_src = ["//deployment/example_adaptive/ExampleApp:instance"],
)

filegroup(
    name = "instance",
    srcs = [
        "example_app.json",
        "example_data_type.json",
        "example_service.json",
        "//deployment/system_definition/diag/dtc:Example_dtc",
        "//deployment/system_definition/diag/jobs:read_vin_job",
    ],
    visibility = ["//example_adaptive/ExampleApp/code:__subpackages__"],
)

adaptive_application(
    name = "ExampleApp",
    bin = "//example_adaptive/ExampleApp/code/application:ExampleApp",
    model_src = ["//deployment/example_adaptive/ExampleApp:instance"],
    visibility = ["//visibility:public"],
)
