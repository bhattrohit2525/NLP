# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:27:04 2021

@author: User
"""
from pydantic import BaseModel

class HateSpeech(BaseModel):
    text: str