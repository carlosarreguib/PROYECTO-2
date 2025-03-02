def predict_price(rooms=None,
                  bathroom=None,
                  lift=None,
                  terrace=None,
                  square_meters=None,
                  real_state=None,
                  neighborhood=None):
    """ Predictor for price from model/67a260e854e70fb808f11be1

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (square_meters is None):
        return 1223.33555
    if (square_meters > 113):
        if (square_meters > 151):
            if (square_meters > 186):
                if (neighborhood is None):
                    return 2558.40574
                if (neighborhood == 'Horta- Guinardo'):
                    return 2217.27273
                if (neighborhood != 'Horta- Guinardo'):
                    if (lift is None):
                        return 2574.51073
                    if (lift == 'True'):
                        if (square_meters > 242):
                            return 2741.46341
                        if (square_meters <= 242):
                            if (rooms is None):
                                return 2561.60234
                            if (rooms > 5):
                                return 2271.61538
                            if (rooms <= 5):
                                return 2585.46203
                    if (lift == 'False'):
                        return 2353.66667
            if (square_meters <= 186):
                if (bathroom is None):
                    return 2207.78218
                if (bathroom > 2):
                    if (rooms is None):
                        return 2358.6988
                    if (rooms > 4):
                        if (rooms > 5):
                            if (real_state is None):
                                return 1740
                            if (real_state == 'flat'):
                                return 2100
                            if (real_state != 'flat'):
                                return 1200
                        if (rooms <= 5):
                            return 2180.30435
                    if (rooms <= 4):
                        return 2456.95652
                if (bathroom <= 2):
                    if (square_meters > 177):
                        return 2321.73469
                    if (square_meters <= 177):
                        if (terrace is None):
                            return 2045.68783
                        if (terrace == 'True'):
                            return 2170.30435
                        if (terrace == 'False'):
                            return 1974.03333
        if (square_meters <= 151):
            if (square_meters > 128):
                if (bathroom is None):
                    return 1937.33959
                if (bathroom > 2):
                    if (rooms is None):
                        return 2186.96753
                    if (rooms > 4):
                        return 1935.19231
                    if (rooms <= 4):
                        return 2238.10938
                if (bathroom <= 2):
                    if (rooms is None):
                        return 1858.07629
                    if (rooms > 3):
                        if (square_meters > 141):
                            return 1853.7125
                        if (square_meters <= 141):
                            return 1598.6259
                    if (rooms <= 3):
                        if (square_meters > 134):
                            if (bathroom > 1):
                                if (real_state is None):
                                    return 2106.88816
                                if (real_state == 'attic'):
                                    return 2490.90909
                                if (real_state != 'attic'):
                                    return 2076.92908
                            if (bathroom <= 1):
                                return 1693.58824
                        if (square_meters <= 134):
                            return 1872.40206
            if (square_meters <= 128):
                if (rooms is None):
                    return 1628.50676
                if (rooms > 3):
                    if (square_meters > 119):
                        if (bathroom is None):
                            return 1542.11392
                        if (bathroom > 2):
                            return 1886
                        if (bathroom <= 2):
                            return 1506.04196
                    if (square_meters <= 119):
                        return 1306.86076
                if (rooms <= 3):
                    if (terrace is None):
                        return 1738.53521
                    if (terrace == 'False'):
                        if (real_state is None):
                            return 1665.95851
                        if (real_state == 'apartment'):
                            return 1997.8
                        if (real_state != 'apartment'):
                            if (square_meters > 118):
                                return 1692.48438
                            if (square_meters <= 118):
                                return 1505.10843
                    if (terrace == 'True'):
                        return 1891.96491
    if (square_meters <= 113):
        if (bathroom is None):
            return 1118.05644
        if (bathroom > 1):
            if (real_state is None):
                return 1360.48023
            if (real_state == 'apartment'):
                if (lift is None):
                    return 1957.46089
                if (lift == 'True'):
                    if (square_meters > 76):
                        return 1884.7381
                    if (square_meters <= 76):
                        return 1476.85417
                if (lift == 'False'):
                    if (neighborhood is None):
                        return 2086.56637
                    if (neighborhood == 'Eixample'):
                        return 2235.19101
                    if (neighborhood != 'Eixample'):
                        if (rooms is None):
                            return 1990.0146
                        if (rooms > 1):
                            return 2030.97638
                        if (rooms <= 1):
                            if (square_meters > 52):
                                return 1312.25
                            if (square_meters <= 52):
                                return 2100
            if (real_state != 'apartment'):
                if (square_meters > 76):
                    if (square_meters > 98):
                        if (rooms is None):
                            return 1455.38773
                        if (rooms > 3):
                            if (bathroom > 2):
                                return 1757.72727
                            if (bathroom <= 2):
                                return 1306.3012
                        if (rooms <= 3):
                            if (rooms > 1):
                                if (rooms > 2):
                                    if (square_meters > 103):
                                        if (bathroom > 2):
                                            return 2198.33333
                                        if (bathroom <= 2):
                                            if (neighborhood is None):
                                                return 1562.96067
                                            if (neighborhood == 'Sant Martí'):
                                                return 1787.77273
                                            if (neighborhood != 'Sant Martí'):
                                                if (neighborhood == 'Sants-Montjuïc'):
                                                    return 1165
                                                if (neighborhood != 'Sants-Montjuïc'):
                                                    return 1545.90667
                                    if (square_meters <= 103):
                                        if (square_meters > 100):
                                            return 1292.875
                                        if (square_meters <= 100):
                                            if (neighborhood is None):
                                                return 1484.75862
                                            if (neighborhood == 'Ciutat Vella'):
                                                return 2606.66667
                                            if (neighborhood != 'Ciutat Vella'):
                                                return 1444.69048
                                if (rooms <= 2):
                                    return 1641.01709
                            if (rooms <= 1):
                                return 1072.15385
                    if (square_meters <= 98):
                        if (real_state == 'flat'):
                            if (bathroom > 2):
                                return 1640.5
                            if (bathroom <= 2):
                                if (rooms is None):
                                    return 1296.61703
                                if (rooms > 3):
                                    if (neighborhood is None):
                                        return 1227.86601
                                    if (neighborhood == 'Sarria-Sant Gervasi'):
                                        return 1406.11111
                                    if (neighborhood != 'Sarria-Sant Gervasi'):
                                        return 1194.83824
                                if (rooms <= 3):
                                    if (terrace is None):
                                        return 1317.55933
                                    if (terrace == 'False'):
                                        if (square_meters > 89):
                                            if (neighborhood is None):
                                                return 1357.66756
                                            if (neighborhood == 'Gràcia'):
                                                return 1172.08333
                                            if (neighborhood != 'Gràcia'):
                                                return 1370.4298
                                        if (square_meters <= 89):
                                            if (rooms > 1):
                                                if (lift is None):
                                                    return 1260.23586
                                                if (lift == 'True'):
                                                    return 1280.0751
                                                if (lift == 'False'):
                                                    return 1171.39823
                                            if (rooms <= 1):
                                                return 1021.85185
                                    if (terrace == 'True'):
                                        if (rooms > 2):
                                            if (lift is None):
                                                return 1327.90404
                                            if (lift == 'True'):
                                                return 1355.05848
                                            if (lift == 'False'):
                                                return 1155.92593
                                        if (rooms <= 2):
                                            return 1567.16981
                        if (real_state != 'flat'):
                            if (rooms is None):
                                return 1643.5
                            if (rooms > 2):
                                if (bathroom > 2):
                                    if (square_meters > 84):
                                        return 1500
                                    if (square_meters <= 84):
                                        return 2600
                                if (bathroom <= 2):
                                    return 1340.22222
                            if (rooms <= 2):
                                return 1946.10526
                if (square_meters <= 76):
                    if (bathroom > 2):
                        if (rooms is None):
                            return 1651.42308
                        if (rooms > 3):
                            return 2525
                        if (rooms <= 3):
                            return 1492.59091
                    if (bathroom <= 2):
                        if (square_meters > 52):
                            if (lift is None):
                                return 1172.55441
                            if (lift == 'True'):
                                if (rooms is None):
                                    return 1204.13542
                                if (rooms > 2):
                                    if (square_meters > 60):
                                        return 1122.56028
                                    if (square_meters <= 60):
                                        return 1288.15625
                                if (rooms <= 2):
                                    if (square_meters > 68):
                                        if (real_state == 'attic'):
                                            return 2240
                                        if (real_state != 'attic'):
                                            if (neighborhood is None):
                                                return 1351.94578
                                            if (neighborhood == 'Sant Martí'):
                                                if (square_meters > 73):
                                                    return 1165.83333
                                                if (square_meters <= 73):
                                                    return 1701.26667
                                            if (neighborhood != 'Sant Martí'):
                                                return 1323.51035
                                    if (square_meters <= 68):
                                        if (terrace is None):
                                            return 1153.86631
                                        if (terrace == 'True'):
                                            return 1373
                                        if (terrace == 'False'):
                                            return 1108.62581
                            if (lift == 'False'):
                                if (square_meters > 73):
                                    return 1188.02381
                                if (square_meters <= 73):
                                    if (neighborhood is None):
                                        return 1034.99371
                                    if (neighborhood == 'Sarria-Sant Gervasi'):
                                        return 1238.6875
                                    if (neighborhood != 'Sarria-Sant Gervasi'):
                                        return 1012.2028
                        if (square_meters <= 52):
                            return 921.82759
        if (bathroom <= 1):
            if (real_state is None):
                return 1020.50702
            if (real_state == 'apartment'):
                if (square_meters > 43):
                    if (lift is None):
                        return 1532.87162
                    if (lift == 'True'):
                        if (square_meters > 61):
                            if (rooms is None):
                                return 1448.95455
                            if (rooms > 1):
                                return 1374.60976
                            if (rooms <= 1):
                                return 1621.49057
                        if (square_meters <= 61):
                            if (square_meters > 49):
                                return 1277.17901
                            if (square_meters <= 49):
                                return 1110.42222
                    if (lift == 'False'):
                        if (neighborhood is None):
                            return 1681.78614
                        if (neighborhood == 'Ciutat Vella'):
                            return 1488.27273
                        if (neighborhood != 'Ciutat Vella'):
                            if (terrace is None):
                                return 1742.76302
                            if (terrace == 'False'):
                                if (neighborhood == 'Horta- Guinardo'):
                                    return 1431.6
                                if (neighborhood != 'Horta- Guinardo'):
                                    if (square_meters > 61):
                                        return 1894.17483
                                    if (square_meters <= 61):
                                        if (rooms is None):
                                            return 1723.50254
                                        if (rooms > 2):
                                            return 1323.72727
                                        if (rooms <= 2):
                                            return 1747.14516
                            if (terrace == 'True'):
                                return 1258
                if (square_meters <= 43):
                    if (lift is None):
                        return 1066.29225
                    if (lift == 'True'):
                        return 816.72
                    if (lift == 'False'):
                        if (rooms is None):
                            return 1155.85167
                        if (rooms > 0):
                            if (neighborhood is None):
                                return 1192.47668
                            if (neighborhood == 'Ciutat Vella'):
                                return 1079.55405
                            if (neighborhood != 'Ciutat Vella'):
                                return 1262.69748
                        if (rooms <= 0):
                            return 714.0625
            if (real_state != 'apartment'):
                if (square_meters > 58):
                    if (square_meters > 74):
                        if (rooms is None):
                            return 1118.86753
                        if (rooms > 2):
                            if (square_meters > 82):
                                if (square_meters > 106):
                                    return 1337.07143
                                if (square_meters <= 106):
                                    if (rooms > 4):
                                        return 2300
                                    if (rooms <= 4):
                                        return 1104.9542
                            if (square_meters <= 82):
                                if (square_meters > 79):
                                    return 1054.66802
                                if (square_meters <= 79):
                                    return 979.75278
                        if (rooms <= 2):
                            if (square_meters > 107):
                                return 1576.08696
                            if (square_meters <= 107):
                                if (real_state == 'attic'):
                                    return 1479.73684
                                if (real_state != 'attic'):
                                    if (neighborhood is None):
                                        return 1168.87322
                                    if (neighborhood == 'Gràcia'):
                                        return 1350.60256
                                    if (neighborhood != 'Gràcia'):
                                        if (terrace is None):
                                            return 1148.4777
                                        if (terrace == 'False'):
                                            return 1123.3421
                                        if (terrace == 'True'):
                                            return 1230.51534
                    if (square_meters <= 74):
                        if (rooms is None):
                            return 996.83499
                        if (rooms > 2):
                            if (square_meters > 68):
                                return 950.4023
                            if (square_meters <= 68):
                                return 886.75643
                        if (rooms <= 2):
                            if (lift is None):
                                return 1045.36059
                            if (lift == 'True'):
                                if (real_state == 'attic'):
                                    return 1302.16667
                                if (real_state != 'attic'):
                                    if (square_meters > 64):
                                        if (neighborhood is None):
                                            return 1105.66308
                                        if (neighborhood == 'Sarria-Sant Gervasi'):
                                            return 1193.62385
                                        if (neighborhood != 'Sarria-Sant Gervasi'):
                                            if (terrace is None):
                                                return 1087.94085
                                            if (terrace == 'True'):
                                                return 1197.36274
                                            if (terrace == 'False'):
                                                if (rooms > 0):
                                                    return 1056.35185
                                                if (rooms <= 0):
                                                    return 1443
                                    if (square_meters <= 64):
                                        if (rooms > 0):
                                            return 1021.89344
                                        if (rooms <= 0):
                                            return 1311
                            if (lift == 'False'):
                                if (square_meters > 63):
                                    if (terrace is None):
                                        return 1013.87987
                                    if (terrace == 'False'):
                                        return 988.14559
                                    if (terrace == 'True'):
                                        return 1156.78723
                                if (square_meters <= 63):
                                    return 919.84667
                if (square_meters <= 58):
                    if (square_meters > 43):
                        if (real_state == 'attic'):
                            return 1104.19048
                        if (real_state != 'attic'):
                            if (square_meters > 50):
                                if (rooms is None):
                                    return 914.96637
                                if (rooms > 2):
                                    return 845.6
                                if (rooms <= 2):
                                    if (lift is None):
                                        return 928.58716
                                    if (lift == 'True'):
                                        return 950.33896
                                    if (lift == 'False'):
                                        return 892.40816
                            if (square_meters <= 50):
                                if (lift is None):
                                    return 856.80569
                                if (lift == 'True'):
                                    return 879.25232
                                if (lift == 'False'):
                                    return 821.35208
                    if (square_meters <= 43):
                        if (square_meters > 29):
                            if (terrace is None):
                                return 768.93893
                            if (terrace == 'False'):
                                return 754.04124
                            if (terrace == 'True'):
                                return 850.92908
                        if (square_meters <= 29):
                            return 637.12088
