from click.testing import CliRunner
from devhelper.cli import cli

def test_generate_readme():
    runner = CliRunner()
    result = runner.invoke(cli, ['generate-readme', 'My Project', 'Project Description'])
    assert result.exit_code == 0
    assert "README.md file generated with title: 'My Project'." in result.output
