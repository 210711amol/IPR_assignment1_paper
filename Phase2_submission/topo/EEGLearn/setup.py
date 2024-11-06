from distutils.core import setup

setup(
    name='EEGLearn',
    version='1.11',
    packages=['eeglearn'],
    install_requires=['numpy==1.23.4', 'scipy==1.9.3', 'scikit-learn==1.1.2', 'theano==1.0.5',
                      'lasagne @ git+https://github.com/Lasagne/Lasagne.git#egg=lasagne=0.2.dev1'],
    url='https://github.com/pbashivan/EEGLearn',
    license='GNU GENERAL PUBLIC LICENSE',
    author='Pouya Bashivan',
    description='Representation learning from EEG'
)
