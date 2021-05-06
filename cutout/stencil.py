import jinja2
import jinja2.ext
from cutout.constants import STENCIL_PATH_PREFIX


class Stencil(jinja2.ext.Extension):
    counter = 0

    def __init__(self, environment, *args, **kwargs):
        @jinja2.contextfilter
        def stencil(ctx, value, pattern):
            cookiecutter_config = ctx.get("cookiecutter", {})
            included = cookiecutter_config.get(f"include_{pattern}")
            if isinstance(included, str):
                included = included.lower() == "true"
            return value if included else ""

        @jinja2.contextfilter
        def stencil_path(ctx, value, pattern):
            rendered_value = stencil(ctx, value, pattern)
            if rendered_value == "":
                self.counter += 1
                return f"{STENCIL_PATH_PREFIX}{value}"
            return rendered_value

        environment.filters["stencil"] = stencil
        environment.filters["stencil_path"] = stencil_path
        super().__init__(environment)
