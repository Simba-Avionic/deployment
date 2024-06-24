load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")
load("//deployment/bazel:connect_tar.bzl", "connect_tar")
load("//deployment/bazel:json_megre.bzl","json_megre")
def convert(path):
    res = path.split("/")[-1].replace(".tar", "")
    return res

def _start_service_script(ctx):
    content = """ 
#!/bin/sh
################################################################################
#
#   Copyright (c) 2024 Bartosz Snieg.
#
################################################################################
#
echo "Starting components SRP EM "
/opt/em/bin/em &
echo "Simab SRP start up component script [DONE]"
"""
    return content

def _startup_script(ctx):
    content = """ 
#!/bin/sh
################################################################################
#
#   Copyright (c) 2024 Bartosz Snieg.
#
################################################################################
#
echo "Simab SRP start up script"

/opt/cpu_simba/network_interface.sh
/opt/cpu_simba/component_start_up.sh

echo "Simab SRP start up script [DONE]"

"""
    return content

def _start_service_list_impl(ctx):
    out1 = ctx.actions.declare_file("start_up.sh")
    out2 = ctx.actions.declare_file("component_start_up.sh")
    out3 = ctx.actions.declare_file("network_interface.sh")
    ctx.actions.write(output = out1, content = _startup_script(ctx))
    ctx.actions.write(output = out2, content = _start_service_script(ctx))
    # ctx.actions.write(output = out3, content = _netinterface_script(ctx))
    # out = ctx.actions.declare_file("srp_app.json")
    args = [out3.path, ctx.files.configs[0].path]

    # Action to call the script.
    ctx.actions.run(
        inputs = ctx.files.configs,
        outputs = [out3],
        arguments = args,
        executable = ctx.executable.tool,
    )
    return [DefaultInfo(files = depset([out1, out2, out3]))]

cpu_def_r = rule(
    implementation = _start_service_list_impl,
    attrs = {
        "interface_name": attr.string(),
        "configs": attr.label_list(mandatory = False, allow_files = True),
        "tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//deployment/tools/configs/local_app_generator:cpu_gen"),
        ),
    },
)

def cpu_def(name, srp_components,config, memory_structure =[]):
    configs = []
    for l in srp_components:
        # print(l)
        if ":" in l:
            configs.append(l+"_configs")
        else:
            temp = l.split("/")
            configs.append(l+":"+temp[-1].replace("/","")+"_configs")

    
    cpu_def_r(
        name = "cpu",
        configs = [config],
    )
    pkg_tar(
        name = "config_pkg",
        package_dir = "opt/cpu_simba",
        srcs = [":cpu"],
        visibility = ["//visibility:private"],
    )

    json_megre(
        name=name+"_config",
        files = configs+[config],
        visibility=["//visibility:public"]
    )
    # native.filegroup(
    #     name=name+"_components_config",
    #     srcs=configs,
    # )

    connect_tar(
            name = name,
        srcs = [":config_pkg"] + srp_components,
        visibility = ["//visibility:public"],
    )