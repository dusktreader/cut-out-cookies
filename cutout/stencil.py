import jinja2
import jinja2.ext


class Stencil(jinja2.ext.Extension):
    def __init__(self, environment, *args, **kwargs):
        @jinja2.contextfilter
        def stencil(ctx, value, pattern):
            cookiecutter_config = ctx.get("cookiecutter", {})
            included = cookiecutter_config.get(f"include_{pattern}")
            if isinstance(included, str):
                included = included.lower() == "true"
            return value if included else ""

        def null(value):
            return None if value == "" else value

        @jinja2.contextfilter
        def stencil_path(ctx, value, pattern):
            return null(stencil(ctx, value, pattern))

        environment.filters["stencil"] = stencil
        environment.filters["null"] = null
        environment.filters["stencil_path"] = stencil_path
        super().__init__(environment)
