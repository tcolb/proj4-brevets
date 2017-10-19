"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

opening_table = {"100": 34, "200": 34, "300": 32, "400": 32, "500": 30,
                 "600": 30, "700": 28, "800": 28, "900": 28}

closing_table = {"100": 15, "200": 15, "300": 15, "400": 15, "500": 15,
                 "600": 15, "700": 11.428, "800": 11.428, "900": 11.428}


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    rounded_dist = int(math.ceil(float(control_dist_km) / 100.0) * 100)

    calc_time = float(control_dist_km) / float(opening_table[str(rounded_dist)])

    arrow_date = arrow.get(brevet_start_time)

    arrow_some = arrow_date.shift(hours=+calc_time)

    return arrow_some.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    rounded_dist = int(math.ceil(float(control_dist_km) / 100.0) * 100)

    calc_time = float(control_dist_km) / float(closing_table[str(rounded_dist)])

    arrow_date = arrow.get(brevet_start_time)

    arrow_some = arrow_date.shift(hours=+calc_time)

    return arrow_some.isoformat()
