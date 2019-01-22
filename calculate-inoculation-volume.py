# -*- coding: utf-8 -*-
"""
Created on 2019/01/21

@author: Triandafillou, edited by Jared Bard
"""

import numpy as np
from datetime import datetime
import argparse

lag_time = 180 #3 hour lag in minutes
doubling_time = 85 #double time in minutes

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("time1", help="The current time, in the format of 'H:MM' (24 hr)")
    parser.add_argument("time2", help="The target time, in the format of 'H:MM' (24 hr)")
    parser.add_argument("starter_od", help="The current OD of the starter, enter as a number", type=float)
    parser.add_argument("target_od", help="The target OD, enter as a number", type=float)
    parser.add_argument("total_volume", help="The volume of culture to grow in mL", type=float)
    args = parser.parse_args()

    time1 = args.time1
    time2 = args.time2
    total_volume = args.total_volume
    starter_od = args.starter_od
    target_od = args.target_od
        
    """Returns the amount of inoculation culture to add given two times t1 and t2 and two OD600s od1 and od2.
    Enter time as a string (in 24 hour format)"""
    FMT = "%H:%M"
    time_difference = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
    time_dif_min = time_difference.seconds / 60
    assert time_dif_min > lag_time

    growing_time = time_dif_min - lag_time
    number_of_doublings = time_dif_min / doubling_time
    beginning_od = args.target_od / (2**(number_of_doublings))
    volume_of_starter = (beginning_od * total_volume) / starter_od
    volume_of_media = total_volume - volume_of_starter
    print('\nTo make a {} mL culture at OD {} at {}:'.format(total_volume, target_od, time2))
    print('Add {:0.3f} uL of starter at OD {} to {:0.3f} mL of media'.format(volume_of_starter * 1000,
                                                                             starter_od,
                                                                             volume_of_media))