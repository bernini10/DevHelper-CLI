from click.testing import CliRunner
from devhelper.cli import cli

def test_cli_init():
    runner = CliRunner()
    result = runner.invoke(cli, ['init'])
    assert result.exit_code == 0
    assert "Initializing DevHelper CLI!" in result.output
