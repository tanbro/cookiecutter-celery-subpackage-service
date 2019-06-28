# cookiecutter-celery-subpackage-service

This is a [cookiecutter][] template for a project that:

> - is a [celery][] woker, with [tasks][] in it.
> - is a sub-package of the parent project, and the parent project has multiple other similar sub-packages.

The whole projects is like:

```sh
.
├── README.md
├── ...
│
├── myproject-services-subpack1
│   ├── README.md
│   ├── setup.py
│   ├── setup.cfg
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
│   ├── setup.py
│   ├── setup.cfg
│   ├── tests/
│   └── src
│       └── myproject
│           └── services
│               └── subpack2
│                   ├── __init__.py
│                   ├── app.py
│                   └── tasks.py
│
├── myproject-othermodule
│   ├── README.md
│   └─── setup.py
│        └── myproject
│            └── othermodule.py
│
└── ...
```

## Generate

In your project's working directory, run:

```bash
cookiecutter cookiecutter-celery-subpackage-service
```

When generated:

- `Hello world` [celery][] [tasks][] is defined in `tasks.py`
- [celery][] application variable `app` is defined in `app.py`

## Develop

Install the sub-package in *develop mode* on your parent project's environment:

```bash
cd myproject-services-subpack1
python setup.py develop
```

[cookiecutter]: https://github.com/audreyr/cookiecutter "A command-line utility that creates projects from cookiecutters (project templates)"
[celery]: http://www.celeryproject.org/ "Distributed Task Queue"
[tasks]: http://docs.celeryproject.org/en/latest/userguide/tasks.html "Tasks are the building blocks of Celery applications"
