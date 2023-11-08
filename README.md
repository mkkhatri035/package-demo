# Demo Python Package
This is the demo structure for creating the python packages.

## Development
All the files for the development of the module are in module Folder.
1.) Update the demo_module folder with your module name

2.) Update the `__init__.py` file for your module name and import required functions or classes

3.) Update README.md file for description of the package. 

4.) Update the dependencies in the setup.py file and you are ready to go and Author name.

**Note** For Maintaining the documentation format consistent, I prefer using pre-commit.

### Checklist before making wheel file

- [ ] Module name updated
- [ ] Module version updated
- [ ] Required Modules and Sub-modules have `__init__.py` file with documentation
- [ ] Code Documentation is correct

### Run this command after setting everything
python setup.py sdist bdist_wheel

## Testing

To test the module, follow the following steps:

1.) Create the virtual environment in conda or venv. For this venv has been used with Python 3.10. You can use my venv attached with this repository, just update `$(cygpath "C:\Users\User1\Downloads\projects\package-demo\env")` to your currect path in bin\activate file.

2.) Locate your wheel file or module directory.

3.) Activate your virtual Environment.

4.) In terminal locate the module directory.

5.) Perform install, Either `pip install -e .` for module directory path OR `pip install *.whl` for wheel file.

6.) Now just do `import demo_module` as noraml in your virtual environment. As done in testing folder.