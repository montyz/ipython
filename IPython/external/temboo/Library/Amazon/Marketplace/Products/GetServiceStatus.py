# -*- coding: utf-8 -*-

###############################################################################
#
# GetServiceStatus
# This is the standard method following MWS API GetServiceStatus standard. It can return a GREEN, GREEN_I, YELLOW or RED status.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetServiceStatus(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetServiceStatus Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetServiceStatus, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Products/GetServiceStatus')


    def new_input_set(self):
        return GetServiceStatusInputSet()

    def _make_result_set(self, result, path):
        return GetServiceStatusResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetServiceStatusChoreographyExecution(session, exec_id, path)

class GetServiceStatusInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetServiceStatus
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetServiceStatusInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetServiceStatusInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetServiceStatusInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetServiceStatusInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetServiceStatusInputSet, self)._set_input('Endpoint', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetServiceStatusInputSet, self)._set_input('ResponseFormat', value)

class GetServiceStatusResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetServiceStatus Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_Status(self):
        """
        Retrieve the value for the "Status" output from this Choreo execution. ((string) The service status parsed from the Amazon response.)
        """
        return self._output.get('Status', None)

class GetServiceStatusChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetServiceStatusResultSet(response, path)
