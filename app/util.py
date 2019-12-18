import datetime
from dateutil.parser import parse
import pytz
import re

def main():
    """Main entry point for normalize utility.
    """

    # print(NormalizeDuration("1:23:32.123"))
    pass

def NormalizeDuration(originalvalue_str):
    """Normalize Duration value from input string.

    Requirements: columns are in HH:MM:SS.MS format (where MS is milliseconds); please convert them to the 
    total number of seconds expressed in floating point format
    """
    try:
        iscorrectformat, result_str = __check_formatting(originalvalue_str)
        if (iscorrectformat):
            time_parts = [int(x) for x in re.split('[:.]', result_str)]
            td = datetime.timedelta(hours = time_parts[0], minutes = time_parts[1], seconds = time_parts[2], milliseconds = time_parts[3])
            return True, td.total_seconds()
        else:
            return False, result_str
    except Exception as err:
        return False, err

def NormalizeFullName(originalvalue_str):
    """Normalize the Full Name value.

    Requirements: column should be converted to uppercase.
    """
    try:
        iscorrectformat, result_str = __check_formatting(originalvalue_str)
        if (iscorrectformat):
            upper_str = result_str.upper()
            return True, upper_str
        else:
            return False, result_str
    except Exception as err:
        return False, err

def NormalizeText(originalvalue_str):
    """Normalize general text values.

    Requirements: Check UTF-8 formatting. * Be careful, there may be commas in these values. * Be sure to 
    preserve formatting as much as possible.
    """
    try:
        iscorrectformat, result_str = __check_formatting(originalvalue_str)
        if (iscorrectformat):
            return True, result_str
        else:
            return False, result_str
    except Exception as err:
        return False, err

def NormalizeTimeStamp(originalvalue_str):
    """Normalize datetime timestamp values.

    Requirements: column should be formatted in ISO-8601 format; column should be assumed to be in US/Pacific 
    time; please convert it to US/Eastern
    """
    try:
        iscorrectformat, result_str = __check_formatting(originalvalue_str)
        if (iscorrectformat):
            date_obj = parse(result_str)
            pac_tz = pytz.timezone('US/Pacific')
            ea_tz = pytz.timezone('US/Eastern')
            pac_date_obj = pac_tz.localize(date_obj)
            ea_date_obj = pac_date_obj.astimezone(ea_tz)
            return True, ea_date_obj.isoformat()
        else:
            return None, result_str
    except Exception as err:
        return False, err

def NormalizeZip(originalvalue_str):
    """Normalize Zip Code values.

    Requirements: codes should be formatted as 5 digits. If there are less than 5 digits, assume 0 as the prefix.
    """
    try:
        iscorrectformat, result_str = __check_formatting(originalvalue_str)
        if (iscorrectformat):
            padded_str = result_str.rjust(5, '0')
            return True, padded_str
        else:
            return False, result_str
    except Exception as err:
        return False, err

def __check_formatting(input_str):
    """Check UTF-8 formatting for each input string.

    Encode input string to bytes and then decode back to string using UTF-8 encoding.
    """
    try:
        input_bytes = input_str.encode('utf-8', 'replace') 
        output_str = input_bytes.decode('utf-8')
        return True, output_str
    except UnicodeError:
        return False, 'Input String Failed Format Check'

if __name__ == '__main__':
    """Call main function if this is the primary point of entry
    """
    main()
