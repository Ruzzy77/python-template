"""Pytest configuration."""
# First Party
# from aindsys.utils.fixtures import package_import


# fixtures = pytest.importorskip("aindsys.utils.fixtures", reason="Fixtures module not found.")

pytest_plugins = ["utils.fixtures"]

# PACKAGE_IMPORT = package_import.__name__
FIXT_PACKAGE_IMPORT = "package_import"
