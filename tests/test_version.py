"""Unit tests for __version__.py."""

import learning  # noqa


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(learning, "__version__")
    assert learning.__version__ != "0.0.0"
