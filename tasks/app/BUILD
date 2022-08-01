python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
)

pex_binary(
    name="debug",
    entry_point="debug.py",
)

file(
    name="config",
    source="config.json",
)

relocated_files(
    name="relocated_config",
    files_targets=["tasks/app:config"],
    src="tasks/app",
    dest="",
)

archive(
    name="app_with_config",
    packages=[":main"],
    files=[":relocated_config"],
    format="zip"
)
