install:
	pip install --target ./package pymysql

publish: install
	cd package
	zip -r ../my-deployment-package.zip .
	cd ..
	zip -g my-deployment-package.zip lambda_function.py