import jinja2
import pytest
import snick


class TestStencil:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.jinja_env = jinja2.Environment(extensions=["cutout.Stencil"])

    def test_stencil__returns_original_string_if_tag_is_included_in_context(self):
        template = self.jinja_env.from_string("""{{'test.py'|stencil('foo')}}""")
        assert template.render(cookiecutter=dict(include_foo=True)) == "test.py"

    def test_stencil__returns_None_if_tag_is_not_included_in_context(self):
        template = self.jinja_env.from_string("""{{'test.py'|stencil('foo')}}""")
        assert template.render(cookiecutter=dict(include_foo=False)) == ""

    def test_stencil__handles_filter_block_correctly(self):
        template = self.jinja_env.from_string(
            snick.dedent(
                """
                Some Text that should always be included
                {%- filter stencil('foo') %}
                Some Text that should only be included with foo
                {%- endfilter %}
                """
            )
        )
        assert template.render(cookiecutter=dict(include_foo=True)) == snick.dedent(
            """
            Some Text that should always be included
            Some Text that should only be included with foo
            """
        )
        assert template.render(cookiecutter=dict(include_foo=False)) == snick.dedent(
            """
            Some Text that should always be included
            """
        )

    def test_stencil_path__returns_None_if_tag_is_not_included(self):
        template = self.jinja_env.from_string("""{{'test.py'|stencil_path('foo')}}""")
        assert template.render(cookiecutter=dict(include_foo=False)) == "None"

    def test_stencil_path__is_equivalent_of_stencil_and_null(self):
        template1 = self.jinja_env.from_string("""{{'test.py'|stencil('foo')|null}}""")
        template2 = self.jinja_env.from_string("""{{'test.py'|stencil_path('foo')}}""")
        assert (
            template1.render(
                cookiecutter=dict(include_foo=False),
            )
            == template2.render(
                cookiecutter=dict(include_foo=False),
            )
            == "None"
        )
