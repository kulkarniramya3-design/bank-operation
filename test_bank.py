from bank import bankOper

def test_deposit():
    totalbalance,updatedbalance = bankOper(200000,30000,0)

    assert totalbalance == 230000
    assert updatedbalance == 230000

def test_withdraw():
    totalbalance,updatedbalance = bankOper(100000,40000,10000)

    assert totalbalance == 140000
    assert updatedbalance == 130000

def test_anyamount():
    totalbalance,updatedbalance = bankOper(150000,0,15000)

    assert totalbalance == 150000
    assert updatedbalance == 135000