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
class CreateAllEcsWhiteListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'CreateAllEcsWhiteList','jarvis')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SrcIP(self):
		return self.get_query_params().get('SrcIP')

	def set_SrcIP(self,SrcIP):
		self.add_query_param('SrcIP',SrcIP)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_SourceCode(self):
		return self.get_query_params().get('SourceCode')

	def set_SourceCode(self,SourceCode):
		self.add_query_param('SourceCode',SourceCode)