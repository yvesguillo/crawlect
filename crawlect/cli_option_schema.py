#! /usr/bin/env python3

def cli_option_schema(parser):
    """Introspect given ArgumentParser and return an CLI options schema."""

    schema = []

    for group in parser._action_groups:
        group_name = group.title

        for param in group._group_actions:
            # Skip positional args.
            if param.option_strings:
                entry = {
                    "group": str(group_name) if group_name else "",
                    "flags": param.option_strings if param.option_strings else "",
                    "type": str(param.type) if param.type else "",
                    "default": str(param.default) if param.default else "",
                    "required": str(param.required) if param.required else "",
                    "metavar": str(param.metavar) if param.metavar else "",
                    "help": str(param.help.strip()) if param.help else "",
                }
                schema.append(entry)

    return schema
