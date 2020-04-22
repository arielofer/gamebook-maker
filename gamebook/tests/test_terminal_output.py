from gamebook.terminal_output import TerminalOutput
from gamebook.scene import Scene

def test_is_content_recieved():
    example_scene=Scene("exapmle scene","this is an example scene",options=[])
    empty_scene=Scene("","",options=[])

    output_instance = TerminalOutput()
    
    assert output_instance.output(example_scene.show_desc()) == "this is an example scene"
    assert output_instance.output(empty_scene.get_name()) == "no content recieved"