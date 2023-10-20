import pytest
import main # nom du fichier

# test unitaire
def test_div(cal):
	assert divide(1,2) == 0.5

def test_raise(cal):
	with pytest.raises(Error):
		divide(1,0)
