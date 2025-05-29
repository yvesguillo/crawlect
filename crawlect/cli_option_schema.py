#! /usr/bin/env python3

def cli_option_schema(parser, ignore = []):
    """Introspect given ArgumentParser and return an CLI options schema."""

    schema = []

    for group in parser._action_groups:
        group_name = group.title

        for param in group._group_actions:
            # Skip unwanted args.
            if param.option_strings and not any(opt in param.option_strings for opt in ignore):
                entry = {
                    "group":    group_name or "",
                    "flags":    list(param.option_strings),
                    "type":     param.type.__name__ if param.type else "",
                    "choices":  list(param.choices) if param.choices else [],
                    "default":  str(param.default) if param.default is not None else "",
                    "required": param.required if param.required is not None else False,
                    "metavar":  getattr(param, "metavar", "") or getattr(param, "dest", ""),
                    "help":     param.help.strip() if param.help else ""
                }
                schema.append(entry)

    return schema
