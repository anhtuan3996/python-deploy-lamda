# python-deploy-lamda


## Step 1: install package in current dir
```
pip3 install requests -t .
```
## Step 2: zip folder
```
zip -r filezip.zip .
```
## Step 3 : using aws cli upload file zip
```
aws lambda update-function-code --function-name FUNCTION_NAME --zip-file fileb://filezip.zip
```
