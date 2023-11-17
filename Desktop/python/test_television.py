from television import Television
import pytest

class Test_Class:
    def test_init(self):
        tv_1 = Television()
        # test variables
        assert tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        # turn on tv
        tv_2 = Television()
        tv_2.power()
        assert tv_2.__str__() == 'Power = True, Channel = 0, Volume = 0'
        # turn off tv
        tv_2.power()
        assert tv_2.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_muted(self):
        tv_3 = Television()
        # turn on tv, volume up one, then mute
        tv_3.power()
        tv_3.volume_up()
        tv_3.mute()
        assert tv_3.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # unmute tv
        tv_3.mute()
        assert tv_3.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # turn off and mute
        tv_3.power()
        tv_3.mute()
        assert tv_3.__str__() == 'Power = False, Channel = 0, Volume = 1'
        # keep off and unmute
        tv_3.mute()
        assert tv_3.__str__() == 'Power = False, Channel = 0, Volume = 1'


    def test_channel_up(self):
        tv_4 = Television()
        # keep off and channel up one
        tv_4.channel_up()
        assert tv_4.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # turn on and channel up one
        tv_4.power()
        tv_4.channel_up()
        assert tv_4.__str__() == 'Power = True, Channel = 1, Volume = 0'
        # keep on and channel up past max
        tv_4.channel_up()
        tv_4.channel_up()
        tv_4.channel_up()
        assert tv_4.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        tv_5 = Television()
        # keep off and channel down one
        tv_5.channel_down()
        assert tv_5.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # turn on and channel down past min
        tv_5.power()
        tv_5.channel_down()
        assert tv_5.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        tv_6 = Television()
        # keep off and volume up
        tv_6.volume_up()
        assert tv_6.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # turn on and volume up
        tv_6.power()
        tv_6.volume_up()
        assert tv_6.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # keep on, mute, then volume up
        tv_6.mute()
        tv_6.volume_up()
        assert tv_6.__str__() == 'Power = True, Channel = 0, Volume = 2'
        # keep on and go past max volume
        tv_6.volume_up()
        assert tv_6.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        tv_7 = Television()
        # keep off and decrease volume
        tv_7.volume_down()
        assert tv_7.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # turn on and decrease volume (must raise to max first)
        tv_7.power()
        tv_7.volume_up()
        tv_7.volume_up()
        tv_7.volume_down()
        assert tv_7.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # keep on, mute, and decrease
        tv_7.mute()
        tv_7.volume_down()
        assert tv_7.__str__() == 'Power = True, Channel = 0, Volume = 0'
        # keep on and go past minimum volume
        tv_7.volume_down()
        assert tv_7.__str__() == 'Power = True, Channel = 0, Volume = 0'


























