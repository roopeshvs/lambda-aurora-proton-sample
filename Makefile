install:
	pip install --target ./package pymysql

publish: install
	cd ./package; zip -r ../function.zip .
	cd ..; zip -g function.zip app.py