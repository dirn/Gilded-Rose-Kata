# Gilded Rose Kata

This is an implementation of the Gilded Rose Kata. It is based on the RailsConf
2014 talk [All the Little Things by Sandi Metz][sandi].

The code is written in Python. I've done my best to implement the tests
referenced in the talk. The `main` branch is set to the original implementation
of the `GildedRose` class. If you'd like to play along with Sandi's talk, start
there. To get started, run the following

```sh
    pip install -r requirements.txt
    pre-commit install
```

[pre-commit] is used to handle some linting and fixing.

The tests can be run by invoking [tox].

```sh
    tox
```

My final version (modelled after the talk) can be found in the `refactored`
branch. It contains separate commits for each stage in the refactoring.

[pre-commit]: https://pre-commit.com
[sandi]: https://www.youtube.com/watch?v=8bZh5LMaSmE
[tox]: https://tox.readthedocs.io
