from distutils.core import setup

def main():
    setup(
        name='tuneease',
        packages=['backend'],
        version='0.0.1',
        license='MIT',
        description='Generate music with AI',
        author='Pranit Shah',
        author_email='ppshah2023@gmail.com',
        url='https://www.pranitshah.cyou/musetune',
        download_url='https://github.com/Pshah2023/TuneEase/releases/tag/0.1.0',
        keywords=['music', 'AI', 'getmusic'],
        install_requires=[
            'torch==2.0.1',
            'torchaudio==2.0.2',
            'torchvision==0.15.2',
            'absl-py==1.4.0',
            'blinker==1.6.2',
            'cachetools==5.3.1',
            'certifi==2023.7.22',
            'chardet==5.2.0',
            'charset-normalizer==3.2.0',
            'colorama==0.4.6',
            'contourpy==1.1.0',
            'cycler==0.11.0',
            'einops==0.6.1',
            'Flask==2.3.2',
            'Flask-Cors==4.0.0',
            'fonttools==4.42.0',
            'fsspec==2023.6.0',
            'google-auth==2.22.0',
            'google-auth-oauthlib==1.0.0',
            'grpcio==1.57.0',
            'huggingface-hub==0.16.4',
            'idna==3.4',
            'itsdangerous==2.1.2',
            'Jinja2==3.1.2',
            'joblib==1.3.2',
            'jsonpickle==3.0.2',
            'kiwisolver==1.4.4',
            'Markdown==3.4.4',
            'MarkupSafe==2.1.3',
            'matplotlib==3.7.2',
            'miditoolkit==0.1.16',
            'mido==1.3.0',
            'more-itertools==10.1.0',
            'music21==8.3.0',
            'numpy==1.23.5', # this version is crucial for it to work out of the box
            'oauthlib==3.2.2',
            'packaging==23.1',
            'Pillow==10.0.0',
            'protobuf==4.24.0',
            'pyasn1==0.5.0',
            'pyasn1-modules==0.3.0',
            'pyparsing==3.0.9',
            'python-dateutil==2.8.2',
            'PyYAML==6.0.1',
            'regex==2023.8.8',
            'requests==2.31.0',
            'requests-oauthlib==1.3.1',
            'rsa==4.9',
            'safetensors==0.3.2',
            'scipy==1.11.1',
            'six==1.16.0',
            'tensorboard==2.14.0',
            'tensorboard-data-server==0.7.1',
            'tokenizers==0.13.3',
            'tqdm==4.66.1',
            'transformers==4.31.0',
            'typing_extensions==4.7.1',
            'urllib3==1.26.16',
            'webcolors==1.13',
            'Werkzeug==2.3.7',
        ],
        include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Artistic Software',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
        entry_points={
            'console_scripts': [
                'tuneease = backend.tuneease:tuneease'
            ]
        },

    )

if __name__ == "__main__":
    main()