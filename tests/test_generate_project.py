from cookiecutter.main import cookiecutter as bake


class TestBuild:

    def test_build__with_defaults(self, tmp_path):
        bake('examples', output_dir=tmp_path, no_input=True)
        build_path = tmp_path / 'cut-out-test'
        assert build_path.exists()
        assert not (build_path / 'foo.py').exists()
        assert not (build_path / 'bar.py').exists()
        assert (build_path / 'boring.py').exists()
        assert "I am source code in boring.py" in (build_path / 'boring.py').read_text()
        assert "This should only be included if the 'qux' pattern is applied" not in (build_path / 'boring.py').read_text()
        assert not (build_path / 'baz').exists()
