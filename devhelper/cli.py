import click
import os

@click.group()
def cli():
    """DevHelper CLI - Automate development tasks."""
    pass

@cli.command()
def init():
    """Initial command."""
    click.echo("Initializing DevHelper CLI!")

@cli.command()
@click.argument("language")
def generate_gitignore(language):
    """
    Generate a .gitignore file based on the provided language.
    Example: python devhelper/cli.py generate-gitignore python
    """
    templates = {
        "python": "venv/\n__pycache__/\n*.pyc\n*.pyo\n*.pyd\nbuild/\ndist/\n",
        "node": "node_modules/\n*.log\ndist/\n.env\nnpm-debug.log\n",
        "java": "target/\n*.class\n*.jar\n*.war\n*.ear\n*.log\n",
    }
    
    content = templates.get(language.lower())

    if content:
        with open(".gitignore", "w") as file:
            file.write(content)
        click.echo(f".gitignore file generated for '{language}'.")
    else:
        click.echo(f"Language '{language}' not supported. Try: python, node, java.")

@cli.command()
@click.argument("title")
@click.argument("description")
def generate_readme(title, description):
    """
    Generate a basic README.md file.
    Example: python devhelper/cli.py generate-readme "My Project" "Project Description"
    """
    content = f"# {title}\n\n{description}\n\n## Installation\n\n\n\n## Usage\n\n\n"
    with open("README.md", "w") as file:
        file.write(content)
    click.echo(f"README.md file generated with title: '{title}'.")

@cli.command()
@click.argument("license_type")
def generate_license(license_type):
    """
    Generate a standard license file.
    Options: MIT, Apache.
    Example: python devhelper/cli.py generate-license MIT
    """
    licenses = {
        "mit": "MIT License\n\nCopyright (c) 2024\n\nPermission is hereby granted, free of charge...",
        "apache": "Apache License\nVersion 2.0, January 2004\n\nLicensed under the Apache License, Version 2.0...",
    }
    
    content = licenses.get(license_type.lower())
    if content:
        with open("LICENSE", "w") as file:
            file.write(content)
        click.echo(f"LICENSE file generated with license: '{license_type.upper()}'.")
    else:
        click.echo("License not supported. Available options: MIT, Apache.")

@cli.command()
def generate_env():
    """
    Generate a basic .env file with placeholders.
    Example: python devhelper/cli.py generate-env
    """
    content = (
        "# Auto-generated .env file\n"
        "APP_NAME=my_app\n"
        "DEBUG=True\n"
        "DATABASE_URL=postgres://user:password@localhost:5432/dbname\n"
        "SECRET_KEY=change_this_key\n"
    )
    with open(".env", "w") as file:
        file.write(content)
    click.echo(".env file generated with basic placeholders.")

@cli.command()
@click.argument("service")
def generate_compose(service):
    """
    Generate a basic docker-compose.yml file.
    Options: python, node.
    Example: python devhelper/cli.py generate-compose python
    """
    templates = {
        "python": (
            "version: '3.8'\n"
            "services:\n"
            "  app:\n"
            "    build: .\n"
            "    container_name: python_app\n"
            "    ports:\n"
            "      - \"5000:5000\"\n"
            "    environment:\n"
            "      - DEBUG=True\n"
            "      - DATABASE_URL=postgres://user:password@localhost:5432/dbname\n"
        ),
        "node": (
            "version: '3.8'\n"
            "services:\n"
            "  app:\n"
            "    build: .\n"
            "    container_name: node_app\n"
            "    ports:\n"
            "      - \"3000:3000\"\n"
            "    environment:\n"
            "      - NODE_ENV=development\n"
        ),
    }
    
    content = templates.get(service.lower())
    if content:
        with open("docker-compose.yml", "w") as file:
            file.write(content)
        click.echo(f"docker-compose.yml generated for '{service}'.")
    else:
        click.echo("Service not supported. Available options: python, node.")

if __name__ == "__main__":
    cli()
