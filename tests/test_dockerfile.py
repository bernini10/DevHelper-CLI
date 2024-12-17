from click.testing import CliRunner
from devhelper.cli import cli

def test_generate_compose_python():
    runner = CliRunner()
    result = runner.invoke(cli, ['generate-compose', 'python'])
    assert result.exit_code == 0
    assert "docker-compose.yml generated for 'python'." in result.output

    with open("docker-compose.yml", "r") as file:
        content = file.read()
        assert "container_name: python_app" in content

def test_generate_compose_node():
    runner = CliRunner()
    result = runner.invoke(cli, ['generate-compose', 'node'])
    assert result.exit_code == 0
    assert "docker-compose.yml generated for 'node'." in result.output

    with open("docker-compose.yml", "r") as file:
        content = file.read()
        assert "container_name: node_app" in content
