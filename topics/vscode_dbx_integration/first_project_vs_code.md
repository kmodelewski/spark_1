# Setting first project

1. Install UV https://docs.astral.sh/uv/#highlights
2. Check version of databricks connect sdk: https://pypi.org/project/databricks-connect/
```bash
uv init --python 3.12
```
3. Add to pyproject.toml you additional libraries

```yml title='pyproject.toml'
[project]
name = "spark-1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = ['databricks-connect', 'pyspark>=4.0.0']
```

4. Run uv sync command
```bash
uv sync
```
*So far we have configured python project with virtual environment (with .venv file). Now we need to configure databricks asset bundle*

5. Click in vs code - create configuration from databricks extension
This step creates databricks.yml and .databricks directory.

6. Add to .gitignore files/directories we would like to not sync with remote git repository
