import pytest
from main import divide, Error, soustr # nom du fichier

# test unitaire
def test_div():
	assert divide(1,2) == 0.5

def test_raise():
	with pytest.raises(Error):
		divide(1,0)

def test_soustr():
	assert soustr(2,1) == 1
