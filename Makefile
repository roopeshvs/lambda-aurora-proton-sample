install:
	pip install --target ./package pymysql

publish: install
	zip -r ../my-deployment-package.zip ./package
	zip -g my-deployment-package.zip app.py