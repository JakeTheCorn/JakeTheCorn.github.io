pip install coverage
coverage run -m unittest discover --pattern='*_tests.py'
coverage html --omit="*file*,*console*,*_tests.py"
