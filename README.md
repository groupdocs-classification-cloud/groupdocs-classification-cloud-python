# groupdocs-classification-cloud-sdk-py
This repository contains GroupDocs.Classification Cloud (https://products.groupdocs.cloud/classification) SDK for Python source code. This SDK allows you to work with GroupDocs.Classification Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

# Key Features
* Classification of texts
* Classification of documents

See [API Reference](https://apireference.groupdocs.cloud/classification/) for full API specification.

## How to use the SDK?
The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [PyPi](https://pypi.org/project/groupdocsclassificationcloud) (recommended). For more details, please visit our [documentation website](https://docs.groupdocs.cloud/display/classification/Available+SDKs).

### Prerequisites

To use GroupDocs.Classification Cloud Python SDK you need to register an account with [GroupDocs Cloud](https://www.groupdocs.cloud/) and lookup/create App Key and SID at [Cloud Dashboard](https://dashboard.groupdocs.cloud/#/apps). There is free quota available. For more details, see [GroupDocs Cloud Pricing](https://purchase.groupdocs.cloud/pricing).

## Installation & Usage
### pip install groupdocsclassificationcloud

If the python package is hosted on Github, you can install directly from Github

```sh
pip install groupdocsclassificationcloud
```
(you may need to run `pip` with root permission: `sudo pip install groupdocsclassificationcloud`)

Then import the package:
```python
import groupdocsclassificationcloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import groupdocsclassificationcloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import os
from groupdocsclassificationcloud.configuration import Configuration
from groupdocsclassificationcloud.apis.classification_api import ClassificationApi, classify_request
from groupdocsclassificationcloud.models import BaseRequest


class Classification(object):
    APP_SID = '' # Put your appSid here
    APP_KEY = '' # Put your appKey here

    def __init__(self):
        self.classification_api = ClassificationApi(configuration=Configuration(Classification.APP_SID,
                                                                                Classification.APP_KEY))

    # Classify text with IAB-2 taxonomy (Default)
    def classify_raw_text(self):
        request = classify_request(BaseRequest("Try text classification"))

        result = self.classification_api.classify(request)
        print("Result {}".format(result))


classification = Classification()
classification.classify_raw_text()

```

[Test](test/) contain various examples of using the SDK.
Please put your credentials into [Configuration](groupdocsclassificationcloud/configuration.py) or use Settings/servercreds.json file:
{
  "BaseUrl":"https://api.groupdocs.cloud",
  "AppSid":"Your App Sid",
  "AppKey":"Your App Key"
}

## Dependencies
- Python 2.7 and 3.4+
- referenced packages (see [here](setup.py) for more details)

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.groupdocs.cloud/c/classification).
