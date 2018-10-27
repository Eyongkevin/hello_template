class BaseCongig(object):
	'''
	Base config class
	'''
	DEBUG = True
	TESTING = False
class ProductionConfig(BaseCongig):
	"""
	Production specific config
	"""
	DEBUG = False
class DevelopmentConfig(BaseCongig):
	"""
	Development environment specific configuration
	"""
	DEBUG = True
	TESTING = True
