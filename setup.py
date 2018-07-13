from setuptools import setup, find_packages

setup(
    name='django-fperms-iscore',
    version='0.0.1',
    description='Perms for IS core library',
    author='Petr Olah',
    author_email='djangoguru@gmail.com',
    url='https://github.com/druids/django-fperms-iscore',
    package_dir={
        'fperms_iscore': 'fperms_iscore',
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-fperms==0.4.2',
        #'django-is-core==2.11.1',
    ],
    license='MIT',
    zip_safe=False,
    keywords='django-fperms-iscore',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
