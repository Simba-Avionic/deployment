def _dtc_support_list_impl(ctx):
    # The list of arguments we pass to the script.
    out = ctx.actions.declare_file("dtc_support_list.json")
    args = [out.path]
    for i in ctx.files.includes:
        args.append(i.path)

    # Action to call the script.
    ctx.actions.run(
        inputs = ctx.files.includes,
        outputs = [out],
        arguments = args,
        executable = ctx.executable.tool,
    )
    return [DefaultInfo(files = depset([out]))]

dtc_support_list = rule(
    implementation = _dtc_support_list_impl,
    attrs = {
        "includes": attr.label_list(mandatory = False, allow_files = True),
        "tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//deployment/tools/configs/dtc_gen"),
        ),
    },
)