from dataclasses import dataclass

from pathlib import Path
from extensions.configuration import read_configs_to_dataclass, hosting_environment
from extensions.opentelemetry.config import configure_logging


BASE_DIR = Path(__file__).parent

@dataclass
class Config:
    logging_level: str
    dummy_secret: str

config = read_configs_to_dataclass(Config, BASE_DIR)



configure_logging(
   enable_otel=hosting_environment.is_production(),
   level=config.logging_level
)