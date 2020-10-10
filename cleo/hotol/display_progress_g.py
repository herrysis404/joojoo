import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import math
import os
import time

from cleo import (
    FINISHED_PROGRESS_STR,
    UN_FINISHED_PROGRESS_STR,
    EDIT_SLEEP_TIME_OUT
)


async def progress_for_pyrogram_g(
    current,
    total,
    ud_type,
    message,
    start
):
    """ generic progress display for Telegram Upload / Download status """
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = (time_to_completion) / 1000

        elapsed_time = get_readable_time(seconds=elapsed_time)
        estimated_total_time = get_readable_time(seconds=estimated_total_time)

        progress = "\n{0}{1} \n\nProgress   : {2}%\n".format(
            ''.join([FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 6.6666667))]),
            ''.join([UN_FINISHED_PROGRESS_STR for i in range(15 - math.floor(percentage / 6.6666667))]),
            round(percentage, 2))

        tmp = progress + "Total       : {0} of {1}\nSpeed        : {2}/s\nETA            : {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                "{}\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def humanbytes(size: int) -> str:
    """ converts bytes into human readable format """
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    number = 0
    dict_power_n = {
        0: " ",
        1: "Ki",
        2: "Mi",
        3: "Gi",
        4: "Ti"
    }
    while size > power:
        size /= power
        number += 1
    return str(round(size, 2)) + " " + dict_power_n[number] + 'B'


def time_formatter(milliseconds: int) -> str:
    """ converts seconds into human readable format """
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days} d '
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours} h '
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes} m '
    seconds = int(seconds)
    result += f'{seconds} s '
    return result

#def get_readable_time(milliseconds: int) -> str:
#    result = ''
#
 #   (days, remainder) = divmod(seconds, 86400000)
  #  days = int(days)
  #  if days != 0:
#        result += f'{days}d'

 #   (hours, remainder) = divmod(remainder, 3600000)
  #  hours = int(hours)
   # if hours != 0:
   #     result += f'{hours}h'
#
 #   (minutes, remainder) = divmod(remainder, 60000)
  #  minutes = int(minutes)
   # if minutes != 0:
    #    result += f'{minutes}m'

#    (seconds, milliseconds) = divmod(remainder, 1000)
 #   seconds = int(seconds)
  #  if seconds != 0:
  #      result += f'{seconds}s'
  #  milliseconds = int(milliseconds)
  #  result += f'{milliseconds}ms'
  #  return result
