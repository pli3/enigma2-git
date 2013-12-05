from Components.Converter.Converter import Converter
from Components.Element import cached
from Components.config import config
from Tools.GetEcmInfo import GetEcmInfo 
from Poll import Poll


class CryptoInfo(Poll, Converter, object):
	def __init__(self, type):
		Converter.__init__(self, type)
		Poll.__init__(self)

		self.type = type
		self.active = False
# iq - [
#		self.visible = config.usage.show_cryptoinfo.value
		self.visible = config.usage.show_cryptoinfo.value != "off"
# ]
		self.textvalue = ""
		self.poll_interval = 1000
		self.poll_enabled = True
		self.ecmdata = GetEcmInfo()
		
	@cached
	def getText(self):
# iq - [
#		if not config.usage.show_cryptoinfo.value:
		if config.usage.show_cryptoinfo.value == "off":
# ]
			self.visible = False
			data = ''
		else:
			self.visible = True
			if self.type == "VerboseInfo":
				data = self.ecmdata.getEcmData()[0]
			else:
				data = self.ecmdata.getInfo(self.type)
		return data
	text = property(getText)
