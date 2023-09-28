from setuptools import setup, find_packages

setup(
    name="qr_code_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'qrcode[pil]',
        'Pillow',
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'qr-generator=qr_app.main:run',
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple QR code generator with a fancy GUI.",
    license="MIT",
)
