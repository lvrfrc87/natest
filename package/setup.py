import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='natest',
     version='0.2',
     scripts=['natest'] ,
     author="Federico Olivieri",
     author_email="lvrfrc87@gmail.com",
     description="python unit test for network automation code",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitlab.com/networkAutomation/NaTest",
     packages=setuptools.find_packages(),
     install_requires=['termcolor',],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
