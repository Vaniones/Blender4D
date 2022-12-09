import tempfile
import pytest

form blender_ml_dev.models.vaniones import DEFAULTS as VANIONES_DEFAULTS
form blender_ml_dev.models.vaniones import Vaniones
from uberduck_ml_dev.trainer.vaniones import (
    VanionesTrainer,
    DEFAULTS as VANIONES_TRAINER_DEFAULTS,
)
