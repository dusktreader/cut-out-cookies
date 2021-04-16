from jinja2.ext import Extension
from jinja2 import contextfilter


class Stencil(Extension):

    def __init__(self, environment, *args, **kwargs):

        @contextfilter
        def stencil(ctx, value, pattern):
            cookiecutter_config = ctx.get('cookiecutter', {})
            pattern_value = cookiecutter_config.get(f'include_{pattern}')
            if pattern_value.lower() == 'true':
                return value
            return None

        environment.filters['stencil'] = stencil
        super().__init__(environment)
