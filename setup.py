from distutils.core import setup

setup(
    name = "ApprovalTests",
    version = '0.0.1',
    author='Chris Lucian;Llewellyn Falco;Jim Counts',
    author_email='somebody@one.of.us.com',
    packages=['approvaltests','approvaltests.test'],
    url='http://www.approvaltests.com',
    license='LICENSE.txt',
    description='Test verification library.',
    long_description=open('README.txt').read(),

)
