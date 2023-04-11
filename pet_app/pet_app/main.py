from litestar import Litestar

from pet_app.controllers.pets_controller import PetsController

app = Litestar([PetsController])
