#  Copyright 2022 The CDEvents Authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  SPDX-License-Identifier: Apache-2.0
"""CDEvents base types."""
from dataclasses import dataclass
from typing import Dict, TypeVar, Union, Any

from cdevents.context import Context
from cdevents.subject import Subject


SPEC_VERSION = "0.1.0"


@dataclass
class CDEvent:
    """Base class for CDEvents."""

    context: Context
    """Context."""

    subject: Subject
    """Subject."""

    custom_data: Union[Dict, str, None]
    """Custom data for event."""

    custom_data_content_type: str
    """Type identifier for custom data."""