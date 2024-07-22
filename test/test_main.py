import io
import sys
import pytest
from contextlib import redirect_stdout
from main.hanoi import hanoi

def test_hanoi_output():
    # Capture stdout to check the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Test with 3 disks
    hanoi.hanoi(3, 'A', 'C', 'B')

    # Reset redirection
    sys.stdout = sys.__stdout__

    # Expected output for 3 disks
    expected_output = """\
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
"""

    # Compare captured output with expected output
    assert captured_output.getvalue() == expected_output
