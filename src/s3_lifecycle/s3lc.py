import boto3
import json
from botocore.exceptions import ClientError


class S3LifeCycle():
    def __init__(self, *args, **kwargs):
        bucket = kwargs["bucket"]
        # prefix = kwargs["prefix"]
        # rule_name = kwargs["rule_name"]
        # transition_days = kwargs["transition_days"]
        # storage_class = kwargs["storage_class"]

        s3 = boto3.resource("s3")
        self.bucket_lc_config = s3.BucketLifecycleConfiguration(bucket)

        # rules = self._get_rules()
        # rule = self._create_rule(
        #     prefix=prefix,
        #     rule_name=rule_name,
        #     transition_days=transition_days,
        #     storage_class=storage_class
        # )
        # rules.append(rule)
        # self._put_rules(rules)


    def get_rules(self) -> list:
        rules = []
        try:
            rules = self.bucket_lc_config.rules
        except ClientError as e:
            if e.response["Error"]["Code"] == "NoSuchLifecycleConfiguration":
                return rules
            else:
                raise e
        return rules

    def create_rule(self, prefix: str = None, rule_name: str = None,
        transition_days: int = None, storage_class: str = None) -> dict:

        return {
            "ID": rule_name,
            "Filter": {
                "Prefix" : prefix
            },
            "Status": "Enabled",
            "Transitions": [
                {
                    "Days": transition_days,
                    "StorageClass" : storage_class
                }
            ]
        }

    def put_rules(self, rules: dict = None) -> dict:
        response = self.bucket_lc_config.put(
            LifecycleConfiguration={
                "Rules" : rules
            }
        )
        return response
