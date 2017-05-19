# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:26:10 2017

@author: Triandafillou
"""

import numpy as np
from datetime import datetime
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("time1", help="The first (earlier) time reading, in the format of 'H:MM' (24 hr)")
    parser.add_argument("time2", help="The second (later) time reading, in the format of 'H:MM' (24 hr)")
    parser.add_argument("od1", help="The first (earlier) OD reading, enter as a number", type=float)
    parser.add_argument("od2", help="The second (later) OD reading, enter as a number", type=float)
    parser.add_argument("--units", help="The time units desired; default is minutes, enter 'hour' for hours",
                        default="min")
    args = parser.parse_args()
    #print(args.od1 / 2)

    """Returns the doubling time of a culture given two times t1 and t2 and two OD600s od1 and od2.
    Enter time as a string (in 24 hour format)"""
    assert args.od1 < args.od2
    FMT = "%H:%M"
    time_difference = datetime.strptime(args.time2, FMT) - datetime.strptime(args.time1, FMT)
    assert time_difference.seconds > 0
    if args.units == "min":
        doubling_time = (time_difference.seconds/60) / np.log2(args.od2 / args.od1)
        print("Doubling time is {} minutes".format(doubling_time))
    elif args.units == "hour":
        doubling_time = (time_difference.seconds/3600) / np.log2(args.od2 / args.od1)
        print("Doubling time is {} hours".format(doubling_time))
    else:
        print("Unit type not recognized, please enter min or hour")
            