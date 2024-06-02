from setuptools import setup, find_packages

# (base) brettyoung@Bretts-Air choline % python setup.py sdist bdist_wheel
# (base) brettyoung@Bretts-Air choline % twine check dist/*               

documentation = """
## Choline Command Documentation

### choline code
Launches a specified instance in Visual Studio Code. This command allows you to open and work on your project in a remote environment via VS Code.

### choline status
Runs the status command, fetching and displaying the current status of your machine or process. Use this to get real-time updates on your tasks.

### choline init
Enables the creation of a `choline.yaml` configuration file. This will typically include settings for hardware, disk space, and other environment parameters.

### choline stream
Streams data or logs to the console, providing real-time insights into your running tasks. Useful for monitoring progress.

### choline kill
Terminates the local setup of the machine. This command does not affect the remote machine but rather stops the local tasks and processes related to it.

### choline launch
Launches a new instance or task. Note that this command must be run as root.

### choline sync
Syncs your local machine with the remote machine, usually transferring files and data. Use this to keep everything up-to-date.

"""

print(documentation)

setup(
    name='choline',
    version='0.1.1',
    packages=find_packages(),
    long_description=documentation,
    long_description_content_type='text/plain',
    install_requires=[
        'paramiko',
        'scp',
        'PyYAML',
        'vastai',
	'aiohttp'
    ],

    entry_points={
        'console_scripts': [
            'choline = choline.choline:main',
        ],
    },
)
