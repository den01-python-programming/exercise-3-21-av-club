import pytest
import src.exercise

def test_exercise():
    input_values = ["java is a programming language","navy blue shirt","","Do you have a favourite flavour","was it a cat?","bye",""]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["","java","","navy","","","have","favourite","flavour","","",""]
