# coding: utf-8
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="base_test_context.py">
#   Copyright (c) 2019 GroupDocs.Classification for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
#

import os
import json
import unittest
import warnings
import asposestoragecloud
from groupdocsclassificationcloud import ClassificationApi, Configuration
import six


class BaseTestContext(unittest.TestCase):

    def setUp(self):
        root_path = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
        self.local_test_folder = os.path.join(root_path, 'TestData')
        self.remote_test_folder = os.path.join('Temp', 'SdkTests', 'python')
        self.local_common_folder = os.path.join(self.local_test_folder, 'Common')
        with open(os.path.join(root_path, 'Settings', 'servercreds.json')) as f:
            creds = json.loads(f.read())

        self.classification_api = ClassificationApi(configuration=Configuration(creds['AppSid'],
                                                                                creds['AppKey'],
                                                                                creds['BaseUrl']))

        storage_configuration = asposestoragecloud.Configuration()
        storage_configuration.base_url = creds['BaseUrl'] + '/v1.1'
        storage_configuration.host = creds['BaseUrl']

        storage_api_client = asposestoragecloud.ApiClient(
            apiKey=creds['AppKey'],
            appSid=creds['AppSid'],
            configuration=storage_configuration)

        self.storage_api = asposestoragecloud.StorageApi(storage_api_client)
        if six.PY3:
            warnings.simplefilter("ignore", ResourceWarning)
