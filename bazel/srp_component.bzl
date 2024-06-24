load("@bazel_tools//tools/build_defs/pkg:pkg.bzl", "pkg_tar")
load("//deployment/bazel:config_gen.bzl", "config_gen")
load("//deployment/bazel:connect_tar.bzl", "connect_tar")
load("//deployment/bazel:diag_config_connector.bzl", "diag_config_connector")
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



def srp_component(name, bin, configs = [],add_configs = [], visibility = [], includes_diag=[]):

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

    connect_tar(
            name = name,
        srcs = [
            ":bin-pkg",
            ":config_files",
        ],
        visibility = visibility,
    )
    native.alias(
        name = name+"_configs",
        actual = "_configs_temp",
        visibility = ["//visibility:public"],
    )
    native.filegroup(
        name="_configs_temp",
        srcs=["diag_connect"]
    )
    config_gen(
        name = "_app_config",
        config_src = configs,
        component_name = name,
        includes = ["//deployment:Apps"],
        includes_diag = includes_diag,
    )

    diag_config_connector(
        name="diag_connect",
        files = includes_diag+configs,
    )