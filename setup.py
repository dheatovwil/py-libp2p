import setuptools


classifiers = [
    (
        "Programming Language :: Python :: %s" % version
    )
    for version in ["3.7"]
]


setuptools.setup(
    name="libp2p",
    description="libp2p implementation written in python",
    version="0.0.1",
    license="MIT/APACHE2.0",
    platforms=["unix", "linux", "osx"],
    classifiers=classifiers,
    install_requires=[
        "pycryptodome",
        "click",
        "base58",
        "pymultihash",
        "multiaddr",
        "multistream_select"
    ],
    packages=["libp2p"],
    zip_safe=False,
)
