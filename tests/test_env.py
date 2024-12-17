from click.testing import CliRunner
from devhelper.cli import cli

def test_generate_env():
    runner = CliRunner()
    result = runner.invoke(cli, ['generate-env'])
    assert result.exit_code == 0
    assert ".env file generated with basic placeholders." in result.output
