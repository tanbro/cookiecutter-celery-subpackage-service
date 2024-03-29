# cookiecutter-celery-subpackage-service

This is a [cookiecutter][] template for a [python][] project that:

> - is a [celery][] worker, with [tasks][] in it.
> - is a sub-package, and it's parent namespace has multiple other similar [celery][] worker sub-packages.

The whole projects is like:

```sh
.
├── README.md
├── ...
│
├── myproject-services-subpack1
│   ├── README.md
│   ├── setup.cfg
│   ├── setup.py
│   ├── tests/
│   └── src
│       └── myproject
│           └── services
│               └── subpack1
│                   ├── app.py
│                   ├── __init__.py
│                   └── tasks.py
│
├── myproject-services-subpack2
│   ├── README.md
│   ├── setup.cfg
│   ├── setup.py
│   ├── tests/
│   └── src
│       └── myproject
│           └── services
│               └── subpack2
│                   ├── __init__.py
│                   ├── app.py
│                   └── tasks.py
│
├── myproject-other-module
│   ├── README.md
│   ├── setup.py
│   └── myproject
│       └── other
│           └── module.py
│
└── ...
```

`myproject-services-subpackN` are the sub-packages generated by this template.

## Generate

In your project's working directory, run:

```bash
cookiecutter cookiecutter-celery-subpackage-service
```

When generated:

- `Hello world` [celery][] [tasks][] defined in `tasks.py`
- [celery][] application variable `app` defined in `app.py`

## Requires

This [cookiecutter][] template can be used on either [Python]`2` or [Python]`3`, with [cookiecutter][]`>=1.5`.
But the sub-package generated by the template requires:

- [Python][]`>=3.5`
- [setuptools][]`>=40.1.0`
- [Celery][]`>=4.3`

> ❗ **Attention**:
>
> Since [setuptools][]`>=40.1.0` required, an update might be necessary on your development environment before any action to the sub-package's [setuptools][]:
>
> ```bash
> pip install -U setuptools
> ```

## Develop

Install the sub-package in *develop mode* into your parent project's environment:

```bash
cd myproject-services-subpack1
python setup.py develop
```

[cookiecutter]: https://github.com/audreyr/cookiecutter "A command-line utility that creates projects from cookiecutters (project templates)"
[Python]: https://python.org/
[celery]: http://www.celeryproject.org/ "Distributed Task Queue"
[tasks]: http://docs.celeryproject.org/en/latest/userguide/tasks.html "Tasks are the building blocks of Celery applications"
[setuptools]: https://packaging.python.org/key_projects/#easy-install "setuptools (which includes easy_install) is a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions, especially ones that have dependencies on other packages."
