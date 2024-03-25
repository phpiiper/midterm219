"""Test Add Command"""
import pytest
from app import App

def test_app_add_command(capfd, monkeypatch):
    """Test the 'add' command functionality"""
    inputs = iter(['add 1 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0, "The app did not exit as expected"
    out = capfd.readouterr()
    assert "6\n" in out
