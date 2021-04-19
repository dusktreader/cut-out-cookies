# A jinja2 extension for optionally including files in cookiecutter templates

It's a well known and documented issue that cookiecutter does not support
conditionally included files and directories. See
[this post on github](https://github.com/cookiecutter/cookiecutter/issues/723).

This package unlocks that feature with simple jinja2 filters that can be
applied to:
* optional file inclusion
* optional directory inclusion
* optional inclusion of blocks within templates
* optional inclusion of in-line text


## Setup

This assumes that you have cookiecutter installed already and have a project
that you are building into a template. This also assumes you are managing
your environment in your preferred way.

First, install `cut-out-cookies`:
```bash
$ pip install cut-out-cookies
```
If you are using poetry, pipenv, flit, etc you will need to convert the
command for your setup.

Add the extension to your `cookiecutter.json` file like so:
```json
{
    "full_name": "Tucker Beck",
    "email": "tucker.beck@gmail.com",
    "project_name": "Sugar Cookies Project",
    "version": "0.1.0",
    "_extensions": ["cutout.Stencil"]
}
```
The only important line here is where the extension is being added. The
reset is just for example context.

Next, you should add some 'patterns' to your `cookiecutter.json` that you
will use to 'decorate' your optional cookies with:
```json
{
    "full_name": "Tucker Beck",
    "email": "tucker.beck@gmail.com",
    "project_name": "Sugar Cookies Project",
    "version": "0.1.0",
    "_extensions": ["cutout.Stencil"],
    "include_sprinkles": false,
    "include_frosting": false
}
```
This indicates that, by default, any cookies decorated with 'sprinkles' or
'frosting' should not be included in the generated project. The user will
now be prompted if they want to include the optional features 'sprinkles'
and 'frosting'

Finally, due to [this issue on the cookiecutter github repo](https://github.com/cookiecutter/cookiecutter/issues/1518)
you will need to install a post-gen project hook to cleanup the directories
that you intend to omit. Add a `hooks` directory in your template with a
file called `post_gen_project.py`. That file needs to contain this:
```python
from cutout import cleanup

cleanup()
```

That's it. You should be ready to make some cookies now!


## Using cut-out-cookies stencils

For a case study, let's suppose you are building a project stencil called
'Sugar Cookies' that starts out looking like this:
```
sugar-cookies/
├── cookiecutter.json
└── {{cookiecutter.project_name}}
    └── README.md
```


### Optionally including a file

To indicate that a file should only be included if a certain pattern is
included, you use the `stencil` filter in its template filename.

Let's create a file called 'tasty.py' that should only be included if the
'sprinkles' pattern is applied. To do that, we'll apply the `stencil`
filter like so:
```
examples/
├── cookiecutter.json
└── {{cookiecutter.project_name}}
    ├── README.md
    └── {{'tasty.py'|stencil('sprinkles')}}
```

Now if the `include_sprinkles` setting is enabled in cookiecutter, the rendered
project will have a file called `tasty.py`. If it is not enabled, the `tasty.py`
source file will be omitted altogether


### Optionally including a directory

To indicate that a directory should only be included if a certain pattern is
included, you use the `stencil_path` filter in its name. Unfortunately, the
`stencil` filter cannot be used for directories due to
[this issue](https://github.com/cookiecutter/cookiecutter/issues/1518). The
`stencil_path` causes non-matching directories to be renamed to 'None'. Then,
a post-gen hook can be used to remove these directories. This approach is a
bit of a hack, but until the mentioned issue is fixed, we've tried to make it
as painless as possible by including a `cleanup` function that can be easily
added to a `post_gen_project` hook.

Let's create a diretory called 'batch' that should only be included if the
'frosting' pattern is included. To do that, we'll apply the `stencil_path` filter
like so:
```
examples/
├── cookiecutter.json
├── hooks/
│   └── post_gen_project.py
└── {{cookiecutter.project_name}}
    ├── README.md
    └── {{'batch'|stencil_path('frosting')}}
        ├── star_shaped.py
        └── heart_shaped.py
```

Now if the `include_frosting` setting is enabled in cookiecutter, the rendered
project will have a directory called `batch` that includes two file called
`star_shaped.py` and `heart_shaped.py`. If it is not enabled, the directory will
be named 'None' in the generated project. If you have the `post_gen_project` hook
defined like this:

```python
from cutout import cleanup
cleanup()
```

Then the non-matching directories will be removed after project generation.


### Optionally include a block of text

To indicate that a block of text should only be included if a cerain pattern
is included, you use the `stencil` filter block like so:
```
This text will always be included
{%- filter stencil('glitter') }
This text will only be inlcuded if the glitter pattern is included in the
cookiecutter config
{% endfilter %}
```


### Optionally include text inline

To indicate that a bit  of in-line text should only be included if a cerain pattern
is included, you use the `stencil` filter like so:
```
This text includes {{ 'whipped cream' | stencil('creamy') }} frosting
```
The text above will only include 'whipped cream' if the `creamy` pattern in included
