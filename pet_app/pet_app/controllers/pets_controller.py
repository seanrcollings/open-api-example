from dataclasses import dataclass
import enum

from litestar import Controller, get, post, delete, patch
from litestar.partial import Partial


class PetSpecies(enum.Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"


@dataclass
class Pet:
    id: int
    name: str
    species: PetSpecies
    breed: str


pets = [
    Pet(id=1, name="Fido", species=PetSpecies.DOG, breed="Labrador"),
    Pet(id=2, name="Garfield", species=PetSpecies.CAT, breed="Tabby"),
    Pet(id=3, name="Tweety", species=PetSpecies.BIRD, breed="Canary"),
]


class PetsController(Controller):
    path = "/pets"
    tags = ["pets"]

    @get()
    async def list_pets(self) -> list[Pet]:
        return pets

    @get(path="/{pet_id:int}")
    async def get_pet(self, pet_id: int) -> Pet:
        return [pet for pet in pets if pet.id == pet_id][0]

    @post()
    async def create_pet(self, data: Pet) -> Pet:
        ...

    @patch(path="/{pet_id:int}")
    async def partial_update_pet(self, pet_id: int, data: Partial[Pet]) -> Pet:
        ...

    @delete(path="/{pet_id:int}")
    async def delete_pet(self, pet_id: int) -> None:
        ...
