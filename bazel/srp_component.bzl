load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")
load("//deployment/bazel:config_gen.bzl", "config_gen")
def _component_system_d(ctx):
    l = ""
    if (ctx.attr.diag_enable):
        l = l + """
    "diag_id":""" + "{}".format(int(ctx.attr.app_id,16)) + ""","""
    out = ctx.actions.declare_file("srp_app.json")
    ctx.actions.write(
        output = out,
        content = """
{
    """ + l + """
    "bin_path":"/opt/""" + ctx.attr.app_name + """/bin/""" + ctx.attr.app_name + """\",
    "parms":\"""" + ctx.attr.parms + """\",
    "startup_prio":""" + ctx.attr.startup_prio + """,
    "startup_after_delay":""" + ctx.attr.startup_after_delay + """
}
    """,
    )
    return [DefaultInfo(files = depset([out]))]

component_app = rule(
    implementation = _component_system_d,
    attrs = {
        "app_name": attr.string(),
        "parms": attr.string(),
        "startup_prio": attr.string(),
        "app_id": attr.string(),
        "diag_enable": attr.bool(),
        "startup_after_delay": attr.string(),
    },
)

def _impl(ctx):
    # The list of arguments we pass to the script.
    out = ctx.actions.declare_file(ctx.attr.out_name)
    args = [out.path] + [f.path for f in ctx.files.src]

    # Action to call the script.
    ctx.actions.run(
        inputs = ctx.files.src,
        outputs = [out],
        arguments = args,
        executable = ctx.executable.tool,
    )
    return [DefaultInfo(files = depset([out]))]

rename = rule(
    implementation = _impl,
    attrs = {
        "src": attr.label_list(mandatory = False, allow_files = True),
        "out_name": attr.string(),
        "tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//deployment/bazel:rename_sh"),
        ),
    },
)

def srp_component(name, bin, configs = [],add_configs = [], visibility = []):

    pkg_tar(
        name = "config_files",
        package_dir = "opt/" + name + "/etc",
        srcs = [":_app_config"]+add_configs,
        # mode = "0777",
        visibility = ["//visibility:private"],
    )

    pkg_tar(
        name = "bin-pkg",
        package_dir = "opt/" + name + "/bin",
        srcs = [
            ":out_bin",
        ],
        # mode = "0777",
        visibility = ["//visibility:private"],
    )

    rename(
        name = "out_bin",
        out_name = name,
        src = [bin],
        visibility = ["//visibility:private"],
    )

    pkg_tar(
        name = name,
        deps = [
            ":config_files",
            ":bin-pkg",
        ],
        # mode = "0777",
        visibility = visibility,
    )

    config_gen(
        name = "_app_config",
        config_src = configs,
        component_name = name,
        includes = ["//deployment:Apps"],
    )