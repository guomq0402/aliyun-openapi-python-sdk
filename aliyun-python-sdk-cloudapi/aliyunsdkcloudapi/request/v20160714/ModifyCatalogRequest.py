# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ModifyCatalogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'ModifyCatalog','apigateway')

	def get_CatalogId(self):
		return self.get_query_params().get('CatalogId')

	def set_CatalogId(self,CatalogId):
		self.add_query_param('CatalogId',CatalogId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_CatalogName(self):
		return self.get_query_params().get('CatalogName')

	def set_CatalogName(self,CatalogName):
		self.add_query_param('CatalogName',CatalogName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)