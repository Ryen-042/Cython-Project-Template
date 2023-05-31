.PHONY: compile clean-build clean compile-force compile-profile install publish-pypi ruff flake8 cython-lint lint

.DEFAULT_GOAL := compile;


# For some reason, the globstar (eg, **/*.py) is broken in windows. This is a workaround.
# Source: https://stackoverflow.com/questions/2483182/recursive-wildcards-in-gnu-make
# Other: https://dev.to/blikoor/customize-git-bash-shell-498l
rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

compile:
	@echo "Compiling...";
	python setup.py build_ext --inplace;
	@echo "Done.";

clean-build:
	@echo "Removing the build related directories...";
	rm -rf build dist  [package_name].egg-info; # Change the package name here.
	rm -rf $(call rwildcard,.,*__pycache__);
	@echo "Done.";

clean: clean-build
	@echo "Removing the '.pyd', '.c' files, and the 'build' directory...";
	rm -rf src/extensions/**/*.pyd src/extensions/**/*.c;
	@echo "Done.";

compile-force:
	@echo "Forcing recompilation...";
	python setup.py build_ext --inplace --force;
	@echo "Done.";

compile-profile:
	@echo "Recompiling with profiling enabled...";
	python setup.py build_ext --inplace --force --profile;
	@echo "Done.";

install: clean-build
	@echo "Installing package from local...";
	pip uninstall [package_name] -y; # Change the package name here.
	pip install -e .;
	@echo "Done.";

publish-pypi:
	@echo "Publishing to PyPI...";
	python setup.py sdist bdist_wheel;
	twine upload dist/*;
	@echo "Done.";

ruff:
	@echo "Linting Python files...";
	-ruff .;
	@echo "Done.";

flake8:
	@echo "Linting Python files...";
	-flake8 --color always;
	@echo "Done.";

cython-lint:
	@echo "Linting Cython files...";
	-cython-lint src/extensions/**/*.pyx --ignore W293,E501,E266,E265,E261,E221,E128,E127;
	@echo "Done.";

lint: ruff flake8 cython-lint;
