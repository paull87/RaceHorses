#!/usr/bin/python3

class Horse:
    """Class that contains details of a horse."""

    def __init__(self, time, meeting, name, jockey, odds):
        """Initialise the horse class."""
        self.time = time
        self.meeting = meeting
        self.name = name
        self.jockey = jockey
        self.odds = odds

    def __repr__(self):
        return 'Horse({!r},{!r},{!r},{!r},{!r})'.format(
            self.time, self.meeting, self.name, self.jockey, self.odds)

    def display_horse(self):
        """Prints a formatted version of the horse details."""
        fmt = '{0}\n\tMeeting: {1}\n\tTime: {2}\n\tOdds: {3}'
        print(fmt.format(self.name, self.meeting, self.time, self.odds))

    def horse_format(self):
        """Returns a formatted version of the horse details."""
        fmt = '{0}\n\tMeeting: {1}\n\tTime: {2}\n\tOdds: {3}'
        return fmt.format(self.name, self.meeting, self.time, self.odds)
