Demo for Stencil filters

{%- filter stencil('foo') %}
This should only be included if the 'foo' pattern is applied
{%- endfilter %}
{%- filter stencil('bar') %}
This should only be included if the 'bar' pattern is applied
{%- endfilter %}
{%- filter stencil('baz') %}
This should only be included if the 'baz' pattern is applied
{%- endfilter %}
{%- filter stencil('qux') %}
This should only be included if the 'qux' pattern is applied
{%- endfilter %}
