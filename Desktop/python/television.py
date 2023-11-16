class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method that sets instance variables
        '''
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method that sets power variable to opposite of current value
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        Method that sets muted variable to opposite of current value
        '''
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self) -> None:
        '''
        Method that increases channel by one unless at maximum channel, then will go down to minimum channel
        '''
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1
    def channel_down(self) -> None:
        '''
        Method that decreases channel by one unless at minimum channel, then will go up to maximum channel
        '''
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1
    def volume_up(self) -> None:
        '''
        Method that increases volume by one unless at maximum volume, then will stay at maximum volume
        '''
        if self.__volume != self.MAX_VOLUME:
            self.__volume += 1
        else:
            self.__volume = self.MAX_VOLUME
    def volume_down(self) -> None:
        '''
        Method that decreases volume by one unless at minimum volume, then will stay at minimum volume
        '''
        if self.__volume != self.MIN_VOLUME:
            self.__volume -= 1
        else:
            self.__volume = self.MIN_VOLUME

    def __str__(self) -> str:
        '''
        Method that returns a string with the power, channel, and volume variables.
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'




