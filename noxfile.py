import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
@nox.parametrize("jinja2", ["2.11.3", "3.1.1"])
def unit_tests(session, jinja2):
    session.install(".")
    session.install(f"jinja2=={jinja2}")
    session.run("pytest")
