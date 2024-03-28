"""Test the calculator's extra functions"""
import os
import pytest
import pandas as pd
from app import App

def test_clear_history(capfd,monkeypatch):
    """Test that file clears"""
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0, "The app did not exit as expected"
    csv_file_path = app.get_environment_variable("DATADIRNAME","./data") + "/" + app.get_environment_variable("HISTORYFILENAME")
    assert pd.read_csv(csv_file_path).empty

def test_delete_history(capfd,monkeypatch):
    """Test that file is deleted"""
    inputs = iter(['delete', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0, "The app did not exit as expected"
    csv_file_path = app.get_environment_variable("DATADIRNAME","./data") + "/" + app.get_environment_variable("HISTORYFILENAME")
    assert os.path.exists(csv_file_path) is False
def test_history_calculator(capfd,monkeypatch):
    """Test that file saves and views operations correctly"""
    inputs = iter(['add 1 2', 'history','exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0, "The app did not exit as expected"
    out = capfd.readouterr().out
    assert "\n3\nCalc History:\nOperation, Values\n" in out
    assert "add" in out
    assert "['1', '2']" in out
