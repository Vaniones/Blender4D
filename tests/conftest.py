import tempfile
import pytest

from blender_ml_dev.models.vaniones import DEFAULTS as VANIONES_DEFAULTS
from blender_ml_dev.models.vaniones import Vaniones
from blender_tests_ml_dev.trainer.vaniones import (
    VanionesTrainer,
    DEFAULTS as VANIONES_TRAINER_DEFAULTS,
)
