#TEST FOR MODULE TIMETOOLS.PY

#LET'S IMPORT MODULE TO BE TESTED
import timetools

#UNIT TESTS DEFINITIONS
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    