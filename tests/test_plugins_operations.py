"""Test Operation Commands"""
import pytest
from app import App

COMMANDS = [
        ('add 1 2 3', '6'),
        ('add 1 c', 'InvalidOperation'),
        ('divide 6 2', '3'),
        ('divide 6 0', 'ZeroDivisionError'),
        ('divide 6 b', 'InvalidOperation'),
        ('multiply 1 2 3', '6'),
        ('multiply 1 b c', 'InvalidOperation'),
        ('subtract 1 2 3', '-4'),
        ('subtract 1 b c', 'InvalidOperation'),
    ]
def test_operation_commands(capfd, monkeypatch):
    """Tests operations"""
    for command, expected_output in COMMANDS:
        inputs = iter([command, 'exit'])
        # pylint: disable=cell-var-from-loop
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        app = App()
        with pytest.raises(SystemExit) as e:
            app.start()
        assert e.value.code == 0, "The app did not exit as expected"
        out = capfd.readouterr().out
        assert expected_output in out
