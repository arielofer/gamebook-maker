from gamebook.terminal_output import TerminalOutput
from gamebook.scene import Scene


def test_is_content_recieved():
    example_desc = "this is an example scene"
    content_error = "no content recieved"

    example_scene = Scene("exapmle scene",
                          desc=example_desc,
                          options=[])

    empty_scene = Scene("", "", options=[])

    output_instance = TerminalOutput()

    assert output_instance.output(example_scene.show_desc()) ==\
        print(example_desc)
    assert output_instance.output(empty_scene.get_name()) ==\
        print(content_error)
