from gamebook.terminal_output import TerminalOutput
from gamebook.scene import Scene
import pytest


def test_is_content_recieved():
    example_desc = "this is an example scene"

    example_scene = Scene("exapmle scene",
                          desc=example_desc,
                          options=[])

    output_instance = TerminalOutput()

    assert output_instance.output(example_scene.show_desc()) ==\
        print(example_desc)


def test_content_is_empty_error():
    output_instance = TerminalOutput()

    content_error = "no content recieved"
    empty_scene = Scene("", "", options=[])

    with pytest.raises(ValueError) as error_text:
        assert output_instance.output(empty_scene.get_name())
    assert str(error_text.value) == content_error
