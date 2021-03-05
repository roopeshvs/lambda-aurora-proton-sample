install:
	pip install --target ./package pymysql

publish: install
	cd ./package; zip -r ../function.zip .
	zip -g function.zip app.py