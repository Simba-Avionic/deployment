

def _impl(ctx):
    # The list of arguments we pass to the script.
    out = ctx.actions.declare_file("web_config.json")
    args = [out.path] + [f.path for f in ctx.files.files]

    # Action to call the script.
    ctx.actions.run(
        inputs = ctx.files.files,
        outputs = [out],
        arguments = args,
        executable = ctx.executable.tool,
    )
    return [DefaultInfo(files = depset([out]))]

web_config = rule(
    implementation = _impl,
    attrs = {
        "files": attr.label_list(mandatory = False, allow_files = True),
        "tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//deployment/tools/web_config"),
        ),
    },
)