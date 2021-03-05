install:
	pip install --target ./package pymysql

publish: install
	zip -r function.zip ./package
	zip -g function.zip app.py