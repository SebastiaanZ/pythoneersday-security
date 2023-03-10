import pathlib


def get_fixture_files(base_dir: pathlib.Path) -> list[str]:
    apps_dir = base_dir / "apps"
    return [fixture.name for fixture in apps_dir.glob("**/fixtures/*.json")]
