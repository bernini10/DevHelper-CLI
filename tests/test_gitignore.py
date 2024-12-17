from click.testing import CliRunner
from devhelper.cli import cli

def test_generate_gitignore_python():
    runner = CliRunner()
    result = runner.invoke(cli, ['generate-gitignore', 'python'])
    assert result.exit_code == 0
    assert ".gitignore file generated for 'python'." in result.output
