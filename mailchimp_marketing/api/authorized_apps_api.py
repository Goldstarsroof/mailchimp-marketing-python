# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.23
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class AuthorizedAppsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, **kwargs):  # noqa: E501
        """List authorized apps  # noqa: E501

        Get a list of an account's registered, connected applications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List authorized apps  # noqa: E501

        Get a list of an account's registered, connected applications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'exclude_fields', 'count', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'count' in params and params['count'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling ``, must be a value less than or equal to `1000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/authorized-apps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get(self, app_id, **kwargs):  # noqa: E501
        """Get authorized app info  # noqa: E501

        Get information about a specific authorized application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: The unique id for the connected authorized application. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: InlineResponse2001Apps
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_with_http_info(app_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(app_id, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, app_id, **kwargs):  # noqa: E501
        """Get authorized app info  # noqa: E501

        Get information about a specific authorized application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_with_http_info(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: The unique id for the connected authorized application. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: InlineResponse2001Apps
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['app_id'] = params['app_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/authorized-apps/{app_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001Apps',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def link(self, client_details, **kwargs):  # noqa: E501
        """Link application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.link(client_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClientDetails client_details: Use this endpoint to link your application and retrieve OAuth2-based credentials. This is useful if you can't implement the OAuth2 flow but still want to associate calls with your application. (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.link_with_http_info(client_details, **kwargs)  # noqa: E501
        else:
            (data) = self.link_with_http_info(client_details, **kwargs)  # noqa: E501
            return data

    def link_with_http_info(self, client_details, **kwargs):  # noqa: E501
        """Link application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.link_with_http_info(client_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClientDetails client_details: Use this endpoint to link your application and retrieve OAuth2-based credentials. This is useful if you can't implement the OAuth2 flow but still want to associate calls with your application. (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_details' is set
        if ('client_details' not in params or
                params['client_details'] is None):
            raise ValueError("Missing the required parameter `client_details` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client_details' in params:
            body_params = params['client_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/authorized-apps', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
