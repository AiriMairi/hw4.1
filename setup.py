import setuptools

with open('readme.md') as file:
    readme_desc = file.read()

setuptools.setup(
    name='taromaro',
    version='0.2',
    author='Airi',
    author_email='airinalatipova@yandex.ru',
    description='With this package you can find out the answer to any question',
    long_description=readme_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/AiriMairi/hw4.1',
    packages=['taromaro'],
    install_requires=['logging'],
    python_requires='>=3.6'
)
