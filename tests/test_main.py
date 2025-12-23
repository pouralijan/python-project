from python_project.main import hello_world


def test_hello_world() -> None:
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"  # noqa: S101


def test_hello_world_not_empty() -> None:
    """Test that hello_world returns a non-empty string."""
    result = hello_world()
    assert isinstance(result, str)  # noqa: S101
    assert len(result) > 0  # noqa: S101
