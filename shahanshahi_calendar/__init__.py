
# Third party modules
import jdatetime


class ImperialDate:
    def __init__(self, year, month, day, locale=None):
        # TODO: Apply a better solution to handle this and support dates before 1180.
        # Handle year complexity in out of range cases
        if year <= 1180: 
            raise ValueError(f"Imperial year must be at least {1181}, got {year}")
        # Internally store Jalali date (Imperial year minus 1180)
        self._jalali_date = jdatetime.date(year - 1180, month, day, locale=locale)


class ImperialDateTime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        # jdatetime.datetime does NOT support 'locale'
        self._jalali_dt = jdatetime.datetime(
            year - 1180, month, day, hour, minute, second, microsecond, tzinfo=tzinfo
        )
