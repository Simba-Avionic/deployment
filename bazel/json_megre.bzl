def _impl(ctx):
    # The list of arguments we pass to the script.
    out = ctx.actions.declare_file("merged_json.json")
    args = [out.path] + [f.path for f in ctx.files.files]

    # Action to call the script.
    ctx.actions.run(
        inputs = ctx.files.files,
        outputs = [out],
        arguments = args,
        executable = ctx.executable.tool,
    )
    return [DefaultInfo(files = depset([out]))]

json_megre = rule(
    implementation = _impl,
    attrs = {
        "files": attr.label_list(mandatory = False, allow_files = True),
        "tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//deployment/tools/other:json_megre"),
        ),
    },
)