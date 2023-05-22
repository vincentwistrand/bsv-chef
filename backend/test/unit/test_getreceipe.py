import sys
sys.path.append('src')
import pytest
from src.controllers.receipecontroller import ReceipeController
from src.util.calculator import calculate_readiness

@pytest.fixture
def sut():
    mockedDAO = mock.MagicMock()
    mockedDAO.find.return_value = None
    mockedsut = ReceipeController(dao=mockedDAO)
    return mockedsut

# add your test case implementation here
@pytest.mark.unit
def test_get_receipe_readiness_below_available(sut):
    #user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}, {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}]
    with patch('src.controllers.receipecontroller.calculator') as calculator:
        calculator.return_value = 0.05
        readiness = sut.get_receipe_readiness({"diets": ["normal", "vegetarian"]}, {}, {"name": "vegetarian"})
        assert readiness == 0.05

# add your test case implementation here
@pytest.mark.unit
def test_get_receipe_readiness_below_notavailable(sut):
    #user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}, {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}]
    with patch('src.controllers.receipecontroller.calculator') as calculator:
        calculator.return_value = 0.05
        readiness = sut.get_receipe_readiness({"diets": ["normal", "vegetarian"]}, {}, {"name": "vegan"})
        assert readiness == 0.05

# add your test case implementation here
@pytest.mark.unit
def test_get_receipe_readiness_above_available(sut):
    #user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}, {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}]
    with patch('src.controllers.receipecontroller.calculator') as calculator:
        calculator.return_value = 0.15
        readiness = sut.get_receipe_readiness({"diets": ["normal", "vegetarian"]}, {}, {"name": "vegetarian"})
        assert readiness == 0.05

# add your test case implementation here
@pytest.mark.unit
def test_get_receipe_readiness_above_notavailable(sut):
    #user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}, {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}]
    with patch('src.controllers.receipecontroller.calculator') as calculator:
        calculator.return_value = 0.15
        readiness = sut.get_receipe_readiness({"diets": ["normal", "vegetarian"]}, {}, {"name": "vegan"})
        assert readiness == 0.05
        