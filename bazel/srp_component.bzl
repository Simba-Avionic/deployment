load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")
load("//deployment/bazel:config_gen.bzl", "config_gen")

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