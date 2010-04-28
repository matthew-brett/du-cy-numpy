from numpy.distutils.core import setup

import lisandro_monkey
#import matthew_monkey

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.add_extension('cytest', ['cytest.pyx'])
    return config


setup(configuration = configuration)

