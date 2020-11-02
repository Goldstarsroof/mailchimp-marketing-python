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


class ReportingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def get_facebook_ads_report_all(self, **kwargs):  # noqa: E501
        """List facebook ads reports  # noqa: E501

        Get reports of Facebook ads.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facebook_ads_report_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :param str sort_field: Returns files sorted by the specified field.
        :param str sort_dir: Determines the order direction for sorted results.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facebook_ads_report_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_facebook_ads_report_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_facebook_ads_report_all_with_http_info(self, **kwargs):  # noqa: E501
        """List facebook ads reports  # noqa: E501

        Get reports of Facebook ads.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facebook_ads_report_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :param str sort_field: Returns files sorted by the specified field.
        :param str sort_dir: Determines the order direction for sorted results.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'exclude_fields', 'count', 'offset', 'sort_field', 'sort_dir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facebook_ads_report_all" % key
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
        if 'sort_field' in params:
            query_params.append(('sort_field', params['sort_field']))  # noqa: E501
        if 'sort_dir' in params:
            query_params.append(('sort_dir', params['sort_dir']))  # noqa: E501

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
            '/reporting/facebook-ads', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_facebook_ad_report(self, outreach_id, **kwargs):  # noqa: E501
        """Get facebook ad report  # noqa: E501

        Get report of a Facebook ad.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facebook_ad_report(outreach_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outreach_id: The outreach id. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facebook_ad_report_with_http_info(outreach_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facebook_ad_report_with_http_info(outreach_id, **kwargs)  # noqa: E501
            return data

    def get_facebook_ad_report_with_http_info(self, outreach_id, **kwargs):  # noqa: E501
        """Get facebook ad report  # noqa: E501

        Get report of a Facebook ad.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facebook_ad_report_with_http_info(outreach_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outreach_id: The outreach id. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['outreach_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facebook_ad_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'outreach_id' is set
        if ('outreach_id' not in params or
                params['outreach_id'] is None):
            raise ValueError("Missing the required parameter `outreach_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'outreach_id' in params:
            path_params['outreach_id'] = params['outreach_id']  # noqa: E501

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
            '/reporting/facebook-ads/{outreach_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_facebook_ad_product_activity_report(self, outreach_id, **kwargs):  # noqa: E501
        """List facebook ecommerce report  # noqa: E501

        Get breakdown of product activity for an outreach.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facebook_ad_product_activity_report(outreach_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outreach_id: The outreach id. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :param str sort_field: Returns files sorted by the specified field.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facebook_ad_product_activity_report_with_http_info(outreach_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facebook_ad_product_activity_report_with_http_info(outreach_id, **kwargs)  # noqa: E501
            return data

    def get_facebook_ad_product_activity_report_with_http_info(self, outreach_id, **kwargs):  # noqa: E501
        """List facebook ecommerce report  # noqa: E501

        Get breakdown of product activity for an outreach.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facebook_ad_product_activity_report_with_http_info(outreach_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outreach_id: The outreach id. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :param str sort_field: Returns files sorted by the specified field.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['outreach_id', 'fields', 'exclude_fields', 'count', 'offset', 'sort_field']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facebook_ad_product_activity_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'outreach_id' is set
        if ('outreach_id' not in params or
                params['outreach_id'] is None):
            raise ValueError("Missing the required parameter `outreach_id` when calling ``")  # noqa: E501

        if 'count' in params and params['count'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling ``, must be a value less than or equal to `1000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'outreach_id' in params:
            path_params['outreach_id'] = params['outreach_id']  # noqa: E501

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
        if 'sort_field' in params:
            query_params.append(('sort_field', params['sort_field']))  # noqa: E501

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
            '/reporting/facebook-ads/{outreach_id}/ecommerce-product-activity', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_landing_page_reports_all(self, **kwargs):  # noqa: E501
        """List landing pages reports  # noqa: E501

        Get reports of landing pages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_landing_page_reports_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_landing_page_reports_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_landing_page_reports_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_landing_page_reports_all_with_http_info(self, **kwargs):  # noqa: E501
        """List landing pages reports  # noqa: E501

        Get reports of landing pages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_landing_page_reports_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :return: InlineResponse20012
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
                    " to method get_landing_page_reports_all" % key
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
            '/reporting/landing-pages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_landing_page_report(self, outreach_id, **kwargs):  # noqa: E501
        """Get landing page report  # noqa: E501

        Get report of a landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_landing_page_report(outreach_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outreach_id: The outreach id. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: LandingPageReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_landing_page_report_with_http_info(outreach_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_landing_page_report_with_http_info(outreach_id, **kwargs)  # noqa: E501
            return data

    def get_landing_page_report_with_http_info(self, outreach_id, **kwargs):  # noqa: E501
        """Get landing page report  # noqa: E501

        Get report of a landing page.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_landing_page_report_with_http_info(outreach_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outreach_id: The outreach id. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: LandingPageReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['outreach_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_landing_page_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'outreach_id' is set
        if ('outreach_id' not in params or
                params['outreach_id'] is None):
            raise ValueError("Missing the required parameter `outreach_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'outreach_id' in params:
            path_params['outreach_id'] = params['outreach_id']  # noqa: E501

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
            '/reporting/landing-pages/{outreach_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LandingPageReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
