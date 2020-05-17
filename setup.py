from setuptools import setup

setup(
    name='fork_new',
    version='0.1',
    py_modules=['fork_new', 'sample'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fork_new=fork_new:cli
    ''',
)