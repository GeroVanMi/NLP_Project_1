python3 -m build
# TODO: It would be better to upload to the test instance of PyPI instead of to the live version:
twine upload dist/*
