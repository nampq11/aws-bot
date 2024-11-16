from os import path

import aws_cdk as cdk
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_lambda_python_alpha as python

class ApiStack(cdk.Stack):
    def __init__(self, scope: cdk.App, contruct_id: str, **kwargs) -> None:
        super().__init__(scope, contruct_id, **kwargs)

        lambda_function = python.PythonFunction(
            self,
            "Function",
            entry=path.join(path.dirname(__file__), 'app'),
            runtime=lambda_.Runtime.PYTHON_3_11,
            index="main.py",
        )

        api = apigateway.LambdaRestApi(
            self,
            "API",
            handler=lambda_function
        )