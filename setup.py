import setuptools

setuptools.setup(
    name="weeb_classifier",
    version="0.0.1",
    author="Kristian Nymann Jakobsen",
    author_email="kristian@nymann.dev",
    description="Weeb image classification.",
    url="https://github.com/nymann/ai",
    packages=setuptools.find_packages(),
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["tensorflow", "matplotlib", "Pillow"],
    extras_require={
        'lint': [
            "pylint",
            "coverage"
        ]
    },
    package_data={'weeb_classifier': ['weeb_model/saved_model.pb']},
    entry_points={
        'console_scripts': [
            'weeb=weeb_classifier.console_scripts.__main__:solve',
            'weeb-train=weeb_classifier.console_scripts.__main__:train',
        ]
    },
)
