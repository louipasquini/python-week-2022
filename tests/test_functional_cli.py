from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "Pilsen", "--flavor=5", "--image=8", "--cost=10"]
    )
    assert result.exit_code == 0
    assert "Beer added to database" in result.stdout
