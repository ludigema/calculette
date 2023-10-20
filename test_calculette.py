import pytest
from main import sum, divide, Error # nom du fichier

# test unitaire
def test_div():
	assert divide(1,2) == 0.5

def test_raise():
	with pytest.raises(Error):
		divide(1,0)

def test_sum():
	assert sum(4,9) == 13