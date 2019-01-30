import setuptools

setuptools.setup(
    name='space_control',
    version='0.0.1',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'remove_spaces=space_control.remove_spaces:remove_spaces',
            'build=space_control.add_spaces:build',
            'add_spaces=space_control.add_spaces:add_spaces',
            'analise=space_control.performance:analise'
        ]
    }
)
