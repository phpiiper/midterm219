"""Test the app functionality"""
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that file is deleted"""
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0, "The app did not exit as expected"

def test_menu_command(capfd,monkeypatch):
    """Test menu command"""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    assert "\nList of Commands: \n" in capfd.readouterr().out


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
