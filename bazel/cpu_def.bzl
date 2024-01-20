load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")

def _netinterface_script(ctx):
    content = """ 
#!/bin/sh
################################################################################
#
#   Copyright (c) 2024 Bartosz Snieg.
#
################################################################################
#
echo "Setting interface: """ + ctx.attr.interface_name + """ for """ + ctx.attr.cpu_name + """ "
echo "ip: """ + ctx.attr.ip + """"
echo "net mask """ + ctx.attr.mask + """ "
ifconfig """ + ctx.attr.interface_name + """ """ + ctx.attr.ip + """ netmask """ + ctx.attr.mask + """
echo "Interface set [DONE]"
    """
    return content
def convert(path):
    res = path.split("/")[-1].replace(".tar","")
    return res
def _start_service_script(ctx):
    t = ""
    ll= ""
    for ob in ctx.files.components:
        item = convert(ob.path)
        t = t + """
echo "Starting """ + item + """"
systemctl start /opt/""" + item + """/systemd/""" + item + """.service
echo " """ + item + """ Started "
        """
    content = """ 
#!/bin/sh
################################################################################
#
#   Copyright (c) 2024 Bartosz Snieg.
#
################################################################################
#
echo "Starting components at""" + ctx.attr.cpu_name + """ "
""" + t + """
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

sh /opt/cpu_simba/network_interface.sh
sh /opt/cpu_simba/component_start_up.sh

echo "Simab SRP start up script [DONE]"

"""
    return content

def _start_service_list_impl(ctx):
    out1 = ctx.actions.declare_file("start_up.sh")
    out2 = ctx.actions.declare_file("component_start_up.sh")
    out3 = ctx.actions.declare_file("network_interface.sh")
    ctx.actions.write(output = out1, content = _startup_script(ctx))
    ctx.actions.write(output = out2, content = _start_service_script(ctx))
    ctx.actions.write(output = out3, content = _netinterface_script(ctx))
    _startup_script(ctx)
    _start_service_script(ctx)
    _netinterface_script(ctx)

    return [DefaultInfo(files = depset([out1, out2, out3]))]

cpu_def_r = rule(
    implementation = _start_service_list_impl,
    attrs = {
        "cpu_name": attr.string(),
        "components": attr.label_list(mandatory = False, allow_files = True),
        "interface_name": attr.string(),
        "ip": attr.string(),
        "mask": attr.string(),
    },
)

def cpu_def(name, cpu_name, srp_components, interface_name, ip, mask):
    cpu_def_r(
        name = "cpu",
        cpu_name = cpu_name,
        components = srp_components,
        interface_name = interface_name,
        ip = ip,
        mask = mask,
    )
    pkg_tar(
        name = "config_pkg",
        package_dir = "opt/cpu_simba",
        srcs = [":cpu"],
        mode = "0755",
        visibility = ["//visibility:private"],
    )
    pkg_tar(
        name = name,
        deps = [":config_pkg"] + srp_components,
        mode = "0755",
        visibility = ["//visibility:private"],
    )
