# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
for a in range(1, 10):
    for b in range(10):
        for c in range(6):
            for d in range(4):
                for e in range(3):
                    for f in range(3):
                        for g in range(2):
                            for h in range(2):
                                for k in range(2):
                                    for l in range(2):
                                        if a + b + c + d + f + g + h + k + l + e == 10:
                                            dize = [a, b, c, d, e, f, g, h, k, l]
                                            status = True
                                            for i in range(10):
                                                if dize[i] == dize.count(i):
                                                    continue
                                                status = False
                                                break
                                            if status:
                                                print("".join(str(sifre) for sifre in dize))