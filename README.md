# S3 Object Life Cycle CLI

## Description
This tool is a CLI to set Amazon S3 object life cycle policy.

## Prerequisite
1. Required python3 (>3.6)
2. AWS CLI credentials default settings  
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html


## Setup
1. Clone this repository.
2. Install dependencies.
```
pip3 install -r requirements.txt
```
3. Check if it works.
```
./bin/s3lc --help
```  

Then if you get following, installation done.
```
usage: s3lc [-h] -b BUCKET -p PREFIX -n RULE_NAME -d TRANSITION_DAYS -s
            {GLACIER,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,DEEP_ARCHIVE}

S3 Object Lifecycle configuration CLI.

optional arguments:
  -h, --help            show this help message and exit
  -b BUCKET, --bucket BUCKET
                        S3 Bucket Name
  -p PREFIX, --prefix PREFIX
                        S3 prefix name to apply life cycle rule.
  -n RULE_NAME, --rule-name RULE_NAME
                        S3 object life cycle rule name. ex) logs. Note: This
                        must be unique in the S3 bucket.
  -d TRANSITION_DAYS, --transition-days TRANSITION_DAYS
                        Indicates the number of days after creation when
                        objects are transitioned to the specified storage
                        class.
  -s {GLACIER,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,DEEP_ARCHIVE}, --storage-class {GLACIER,STANDARD_IA,ONEZONE_IA,INTELLIGENT_TIERING,DEEP_ARCHIVE}
                        The storage class to which you want the object to
                        transition.
```

## Usage
You want life cycle policy on your S3 bucket ```my-lc-bucket``` with prefix ```my-lc-prefix```, and transition days is 90 days to transfer objects on the prefix to storage class ```Deep Archive```. Don't forget name your rule ```my-lc-rule-1```

```
./bin/s3lc -b my-lc-bucket -p my-lc-prefix/ -n my-lc-rule-1 -d 90 -s DEEP_ARCHIVE
```

