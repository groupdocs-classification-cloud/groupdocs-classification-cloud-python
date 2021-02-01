![](https://img.shields.io/badge/api-v1.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-classification-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-classification-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-classification-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-classification-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-classification-cloud/groupdocs-classification-cloud-python)](https://github.com/groupdocs-classification-cloud/groupdocs-classification-cloud-python/blob/master/LICENSE)

# Python SDK for GroupDocs.Classification Cloud REST API

This repository contains GroupDocs.Classification Cloud SDK for Python source code. This SDK allows you to work with GroupDocs.Classification Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

# Classification Processing Features
- Perform raw text classification.
- Perform document classification for the supported file formats.
- Perform multilingual sentiment analysis (binary or 3-classes) in English, Chinese, Spanish, and German.



## New Features & Enhancements Version 20.11

- Batch text classification was added to API. Now up to 10 texts can be classified in one request.
- Sentiment3 taxonomy (Negative/Neutral/Positive) is supported now.

## Supported Document Formats

- Microsoft Word: DOC, DOCX, DOCM, DOT, DOTX, DOTM
- OpenOffice: ODT, OTT
- Portable: PDF
- Other: RTF, TXT

### Supported IAB-2 Taxonomy

- Automotive,
- Books_and_Literature,
- Business_and_Finance,
- Careers,
- Education,
- Events_and_Attractions,
- Family_and_Relationships,
- Fine_Art,
- Food_&_Drink,
- Healthy_Living,
- Hobbies_&_Interests,
- Home_&_Garden,
- Medical_Health,
- Movies,
- Music_and_Audio,
- News_and_Politics,
- Personal_Finance,
- Pets,
- Pop_Culture,
- Real_Estate,
- Religion_&_Spirituality,
- Science,
- Shopping,
- Sports,
- Style_&_Fashion,
- Technology_&_Computing,
- Television,
- Travel,
- Video_Gaming

### Supported Documents Taxonomy

- ADVE - advertisements, brochures.
- Email
- Form
- Letter
- Memo - memorandums.
- News - articles, including news articles.
- Invoice
- Report
- Resume
- Scientific - scientific papers.
- Other - the other classes of documents or cases where the classifier is not sure.

### Sentiment Taxonomy

- Negative
- Positive
-
### Sentiment3 Taxonomy`

- Negative
- Neutral
- Positive
See [API Reference](https://apireference.groupdocs.cloud/classification/) for full API specification.

## How to use the SDK?

The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [PyPi](https://pypi.org/project/groupdocs-classification-cloud/) (recommended). For more details, please visit our [documentation website](https://docs.groupdocs.cloud/classification/).

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
Please put your credentials into [Configuration](groupdocsclassificationcloud/configuration.py).

## Dependencies
- Python 2.7 and 3.4+
- referenced packages (see [here](setup.py) for more details)

## GroupDocs.Classification Cloud Resources

[Home](https://www.groupdocs.cloud/) | [Docs](https://docs.groupdocs.cloud/classification/) | [Demos](https://products.groupdocs.app/classification/family) | [API Reference](https://apireference.groupdocs.cloud/classification/) | [Blog](https://blog.groupdocs.cloud/category/classification/) | [Free Support](https://forum.groupdocs.cloud/c/classification) | [Free Trial](https://purchase.groupdocs.cloud/trial)
