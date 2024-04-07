from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    description='MCQ generator',
    author='Sanchit Setia',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2',
        'langchain-google-genai'
    ],
)
