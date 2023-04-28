#TEST FOR MODULE TIMETOOLS.PY

#LET'S IMPORT MODULE TO BE TESTED
import timetools

#UNIT TESTS DEFINITIONS
# Test if datediff function calculates correct and absolute values
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

# Test if timediff function calculates correct and absolute values
def test_timediff():
    assert timetools.timediff(('11:30:15', '10:10:05'), 4) == 1.3361
    assert timetools.timediff(('10:10:05', '11:30:15'), 4) == 1.3361