# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="GroupDocs" file="classification_api.py">
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
# -----------------------------------------------------------------------------------


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from groupdocsclassificationcloud.rest import ApiException
from groupdocsclassificationcloud.api_client import ApiClient


class ClassificationApi(object):
    """
    GroupDocs.Classification for Cloud API

    :param api_client: an api client to perfom http requests
    :param configuration: an api client configuration
    """
    def __init__(self, api_client=None, configuration=None):
        if api_client is None:
            api_client = ApiClient(configuration)
        self.api_client = api_client
        self.__request_token()

    def classify(self, request, **kwargs):  # noqa: E501
        """Classifies text or document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request BaseRequest : Raw text to classify or document's info. (required)
        :param best_classes_count str : Count of the best classes to return.
        :param taxonomy str : Taxonomy to use for classification.
        :param precision_recall_balance str : Balance between precision and recall: precision, recall or empty (for default).
        :param storage str : Storage name
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.classify_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.classify_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def classify_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classifies text or document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request classify_request object with parameters
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method classify" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if request.request is None:
            raise ValueError("Missing the required parameter `request` when calling `classify`")  # noqa: E501

        collection_formats = {}
        path = '/classification/classify'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('BestClassesCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('BestClassesCount' + '}'), request.best_classes_count if request.best_classes_count is not None else '')
        else:
            if request.best_classes_count is not None:
                query_params.append((self.__downcase_first_letter('BestClassesCount'), request.best_classes_count))  # noqa: E501
        if self.__downcase_first_letter('Taxonomy') in path:
            path = path.replace('{' + self.__downcase_first_letter('Taxonomy' + '}'), request.taxonomy if request.taxonomy is not None else '')
        else:
            if request.taxonomy is not None:
                query_params.append((self.__downcase_first_letter('Taxonomy'), request.taxonomy))  # noqa: E501
        if self.__downcase_first_letter('PrecisionRecallBalance') in path:
            path = path.replace('{' + self.__downcase_first_letter('PrecisionRecallBalance' + '}'), request.precision_recall_balance if request.precision_recall_balance is not None else '')
        else:
            if request.precision_recall_balance is not None:
                query_params.append((self.__downcase_first_letter('PrecisionRecallBalance'), request.precision_recall_balance))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.request is not None:
            body_params = request.request
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClassificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_supported_file_formats(self, request, **kwargs):  # noqa: E501
        """Retrieves list of supported file formats.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: FormatCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_supported_file_formats_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_supported_file_formats_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_supported_file_formats_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_supported_file_formats_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_supported_file_formats_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of supported file formats.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_supported_file_formats_request object with parameters
        :return: FormatCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supported_file_formats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/classification/formats'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormatCollection',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Helper method to convert first letter to downcase
    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return s
        else:
            return s[0].lower() + s[1:]

    def __request_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        config.api_version = ''
        request_url = "connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.api_key['Authorization'] = access_token
        self.api_client.configuration.api_version = api_version