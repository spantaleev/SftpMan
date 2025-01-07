"""
SftpMan
=======

⚠️ **Warning**: This CLI application and library has been rewritten in Rust. See https://github.com/spantaleev/sftpman-rs. This old Python-based software is no longer maintained.

SftpMan is a command-line application (with a GUI frontend packaged separately) that makes it easy to setup and mount SSHFS/SFTP file systems.

It allows you to define all your SFTP systems and easily mount/unmount them.

A GTK frontend is available, named sftpman-gtk.
"""

from setuptools import setup

setup(
    name = "sftpman",
    version = '1.3.1',
    description = "A command-line application that helps you mount SFTP file systems.",
    long_description = __doc__,
    author = "Slavi Pantaleev",
    author_email = "slavi@devture.com",
    url = "https://github.com/spantaleev/sftpman-python",
    keywords = ["sftp", "ssh", "sshfs"],
    license = "GPL v3",
    packages = ['sftpman'],
    entry_points="""
    [console_scripts]
    sftpman = sftpman.launcher:main
    """,
    zip_safe = False,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Unix",
        "Topic :: Communications :: File Sharing",
        "Topic :: Internet",
        "Topic :: Internet :: File Transfer Protocol (FTP)",
        "Topic :: System :: Networking",
        "Topic :: Utilities"
    ]
)
