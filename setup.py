from setuptools import setup

setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de jemplo",
    author="Laura",
    author_email="hola@laura.com",
    url="http://www.laura.net",
    packages=['paquete','paquete.hola','paquete.adios'],
    scripts=[]
)

