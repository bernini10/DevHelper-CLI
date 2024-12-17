from click.testing import CliRunner
from devhelper.cli import cli

def test_generate_license_mit():
    runner = CliRunner()
    result = runner.invoke(cli, ['generate-license', 'MIT'])
    assert result.exit_code == 0
    assert "LICENSE file generated with license: 'MIT'." in result.output
