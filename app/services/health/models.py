from typing import Optional

from pydantic import BaseModel

class Check(BaseModel):
  success: bool
  title: str
  error_msg: Optional[str]

class Health(BaseModel):
  alive: Check 