import pytest
from main import *
from main import Error # nom du fichier

# test unitaire
def test_div():
	assert divide(1,2) == 0.5

def test_raise():
	with pytest.raises(Error):
		divide(1,0)

def test_multi():
	with pytest.raises(Error):
		multiply(3,5) == 15
