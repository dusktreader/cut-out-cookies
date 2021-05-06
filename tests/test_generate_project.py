from cookiecutter.main import cookiecutter as bake
from cutout.constants import STENCIL_PATH_PREFIX


class TestBuild:
    def test_build__with_defaults(self, tmp_path):
        bake("examples", output_dir=tmp_path, no_input=True)
        build_path = tmp_path / "cut-out-test"
        assert build_path.exists()
        assert not (build_path / "foo.py").exists()
        assert not (build_path / "bar.py").exists()
        assert (build_path / "boring.py").exists()
        assert "I am source code in boring.py" in (build_path / "boring.py").read_text()
        assert (
            "This should only be included if the 'qux' pattern is applied" not in (build_path / "boring.py").read_text()
        )
        assert not (build_path / "baz").exists()
        assert not (build_path / "garply").exists()
        assert len(list(build_path.glob(f"**/{STENCIL_PATH_PREFIX}*"))) == 0
        assert "foo" not in (build_path / "README.md").read_text()
        assert "bar" not in (build_path / "README.md").read_text()
        assert "baz" not in (build_path / "README.md").read_text()
        assert "qux" not in (build_path / "README.md").read_text()

    def test_build__including_foo(self, tmp_path):
        bake("examples", output_dir=tmp_path, no_input=True, extra_context=dict(include_foo=True))
        build_path = tmp_path / "cut-out-test"
        assert build_path.exists()
        assert (build_path / "foo.py").exists()
        assert not (build_path / "bar.py").exists()
        assert (build_path / "boring.py").exists()
        assert "I am source code in boring.py" in (build_path / "boring.py").read_text()
        assert (
            "This should only be included if the 'qux' pattern is applied" not in (build_path / "boring.py").read_text()
        )
        assert not (build_path / "baz").exists()
        assert not (build_path / "garply").exists()
        assert len(list(build_path.glob(f"**/{STENCIL_PATH_PREFIX}*"))) == 0
        assert "foo" in (build_path / "README.md").read_text()
        assert "bar" not in (build_path / "README.md").read_text()
        assert "baz" not in (build_path / "README.md").read_text()
        assert "qux" not in (build_path / "README.md").read_text()

    def test_build__including_bar(self, tmp_path):
        bake("examples", output_dir=tmp_path, no_input=True, extra_context=dict(include_bar=True))
        build_path = tmp_path / "cut-out-test"
        assert build_path.exists()
        assert not (build_path / "foo.py").exists()
        assert (build_path / "bar.py").exists()
        assert (build_path / "boring.py").exists()
        assert "I am source code in boring.py" in (build_path / "boring.py").read_text()
        assert (
            "This should only be included if the 'qux' pattern is applied" not in (build_path / "boring.py").read_text()
        )
        assert not (build_path / "baz").exists()
        assert not (build_path / "garply").exists()
        assert len(list(build_path.glob(f"**/{STENCIL_PATH_PREFIX}*"))) == 0
        assert "foo" not in (build_path / "README.md").read_text()
        assert "bar" in (build_path / "README.md").read_text()
        assert "baz" not in (build_path / "README.md").read_text()
        assert "qux" not in (build_path / "README.md").read_text()

    def test_build__including_baz(self, tmp_path):
        bake("examples", output_dir=tmp_path, no_input=True, extra_context=dict(include_baz=True))
        build_path = tmp_path / "cut-out-test"
        assert build_path.exists()
        assert not (build_path / "foo.py").exists()
        assert not (build_path / "bar.py").exists()
        assert (build_path / "boring.py").exists()
        assert "I am source code in boring.py" in (build_path / "boring.py").read_text()
        assert (
            "This should only be included if the 'qux' pattern is applied" not in (build_path / "boring.py").read_text()
        )
        assert (build_path / "baz").exists()
        assert not (build_path / "garply").exists()
        assert len(list(build_path.glob(f"**/{STENCIL_PATH_PREFIX}*"))) == 0
        assert "foo" not in (build_path / "README.md").read_text()
        assert "bar" not in (build_path / "README.md").read_text()
        assert "baz" in (build_path / "README.md").read_text()
        assert "qux" not in (build_path / "README.md").read_text()

    def test_build__including_qux(self, tmp_path):
        bake("examples", output_dir=tmp_path, no_input=True, extra_context=dict(include_qux=True))
        build_path = tmp_path / "cut-out-test"
        assert build_path.exists()
        assert not (build_path / "foo.py").exists()
        assert not (build_path / "bar.py").exists()
        assert (build_path / "boring.py").exists()
        assert "I am source code in boring.py" in (build_path / "boring.py").read_text()
        assert "This should only be included if the 'qux' pattern is applied" in (build_path / "boring.py").read_text()
        assert not (build_path / "baz").exists()
        assert not (build_path / "garply").exists()
        assert len(list(build_path.glob(f"**/{STENCIL_PATH_PREFIX}*"))) == 0
        assert "foo" not in (build_path / "README.md").read_text()
        assert "bar" not in (build_path / "README.md").read_text()
        assert "baz" not in (build_path / "README.md").read_text()
        assert "qux" in (build_path / "README.md").read_text()
