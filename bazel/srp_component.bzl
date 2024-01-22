load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")

def _component_system_d(ctx):
    out = ctx.actions.declare_file(ctx.attr.component_name + ".service")
    ctx.actions.write(
        output = out,
        content = """
[Unit]
Description=Simba srp app: """ + ctx.attr.component_name + """
StartLimitIntervalSec=2
StartLimitBurst=2
After=srp_start.service

[Service]
ExecStart=/opt/""" + ctx.attr.component_name + "/bin/" + ctx.attr.component_name + """
StandardOutput=journal
StandardError=journal
SyslogIdentifier=""" + ctx.attr.component_name + """
Restart=on-failure
RestartSec=5
Type=notify

[Install]
WantedBy=multi-user.target
        """,
    )
    return [DefaultInfo(files = depset([out]))]

component_system_d = rule(
    implementation = _component_system_d,
    attrs = {
        "component_name": attr.string(),
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
        "src":  attr.label_list(mandatory = False, allow_files = True),
        "out_name": attr.string(),
        "tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//deployment/bazel:rename_sh"),
        ),
    },
)


def srp_component(name, bin, prio = 0, wait_time = 0 ,configs = [], visibility = []):
    pkg_tar(
        name = "config_files",
        package_dir = "opt/" + name + "/etc",
        srcs = configs,
        mode = "0777",
        visibility = ["//visibility:private"],
    )

    pkg_tar(
        name = "bin-pkg",
        package_dir = "opt/" + name + "/bin",
        srcs = [
            ":out_bin"
        ],
        mode = "0777",
        visibility = ["//visibility:private"],
    )

    rename(
        name="out_bin",
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
        mode = "0777",
        visibility = visibility,
    )
