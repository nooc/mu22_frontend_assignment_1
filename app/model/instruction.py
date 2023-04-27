from typing import Optional
from pydantic import BaseModel


class InstructionBase(BaseModel):
    text:str

class Instruction(InstructionBase):
    recipe_id:Optional[int] = None

class InstructionDb(Instruction):
    id:Optional[int] = None
