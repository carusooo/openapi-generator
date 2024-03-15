# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, conlist
from petstore_api.models.tag import Tag

class ArrayOfArrayOfModel(BaseModel):
    """
    ArrayOfArrayOfModel
    """
    another_property: Optional[conlist(conlist(Tag))] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["another_property"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ArrayOfArrayOfModel:
        """Create an instance of ArrayOfArrayOfModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in another_property (list of list)
        _items = []
        if self.another_property:
            for _item in self.another_property:
                if _item:
                    _inner_items = []
                    for _inner_item in _item:
                        if _inner_item is not None:
                            if hasattr(_inner_item, "to_dict") and callable(_inner_item.to_dict):
                                _inner_items.append(_inner_item.to_dict())
                            else:
                                _inner_items.append(_inner_item)
                    _items.append(_inner_items)
            _dict['another_property'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArrayOfArrayOfModel:
        """Create an instance of ArrayOfArrayOfModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ArrayOfArrayOfModel.parse_obj(obj)

        _obj = ArrayOfArrayOfModel.parse_obj({
            "another_property": [
                    [Tag.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj.get("another_property")
                ] if obj.get("another_property") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


