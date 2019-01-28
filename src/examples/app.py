#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Amazon S3 API
# Copyright (c) 2008-2019 Hive Solutions Lda.
#
# This file is part of Hive Amazon S3 API.
#
# Hive Amazon S3 API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Amazon S3 API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Amazon S3 API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2019 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os

import appier

from . import base

class S3App(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "s3",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.buckets()

    @appier.route("/buckets", "GET")
    def buckets(self):
        api = self.get_api()
        buckets = api.list_buckets()
        return buckets

    @appier.route("/buckets/<str:bucket>/create/<str:message>", "GET")
    def create_object(self, bucket, message):
        name = self.field("name", "hello")
        api = self.get_api()
        message = appier.legacy.bytes(
            message,
            encoding = "utf-8",
            force = True
        )
        contents = api.create_object(bucket, name, message)
        return contents

    @appier.route("/buckets/<str:bucket>/upload", "GET")
    def upload_object(self, bucket):
        api = self.get_api()
        path = self.field("path", mandatory = True)
        name = self.field("name", None)
        name = name or os.path.basename(path)
        contents = api.create_file_object(bucket, name, path)
        return contents

    def get_api(self):
        api = base.get_api()
        return api

if __name__ == "__main__":
    app = S3App()
    app.serve()
else:
    __path__ = []
