import setuptools

setuptools.setup(
    name='word_change',
    version='0.0.1',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'create=word_change.createdb:create'
            'generator=word_change.createdb:generator'
            'printdb=word_change.createdb:printdb'
            'creator=word_change.parser:creator'
            'replace_latex=word_change.parser:replace_latex'
            'spotlight_latex=word_change.parser:spotlight_latex'
            'replace=word_change.parser:replace'
            'spotlight=word_change.parser:spotlight'
        ]
    }
)
