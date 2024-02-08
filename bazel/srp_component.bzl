load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")

def _component_system_d(ctx):
    out = ctx.actions.declare_file("srp_app.json")
    ctx.actions.write(
        output = out,
        content = """
{
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

def srp_component(name, bin, prio = 0, wait_time = 0, configs = [], start_parms = "", startup_prio = "0", startup_after_delay = "0", visibility = []):
    component_app(
        name = "srp_config",
        app_name = name,
        parms = start_parms,
        startup_prio = startup_prio,
        startup_after_delay = startup_after_delay,
    )

    pkg_tar(
        name = "config_files",
        package_dir = "opt/" + name + "/etc",
        srcs = [":srp_config"] + configs,
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
