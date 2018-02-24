# Set up the paths.
import os
import sys
sys.path.append(os.path.abspath('.'))

import themodule

def test_hallo():
    assert themodule.hallo() == "hallo"

def test_nohallo():
    assert themodule.hallo() != "blaat" 
