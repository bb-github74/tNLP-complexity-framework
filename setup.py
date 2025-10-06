from setuptools import setup, find_packages

setup(
  name = 'tnlp',
  version = '0.1.0',
  packages = find_packages(),
  install_requires = [
    'spacy>=3.0',
    'pandas',
    'numpy',
    'scikit-learn',
  ],
  author='Bat Baasan',
  description='tNLP: Modifier-aware framework for sentence complexity',
  keywords='nlp linguistics sentence-complexity modifiers svo',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
  ]
)
