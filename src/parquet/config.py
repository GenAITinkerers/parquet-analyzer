"""
This module defines the configuration for the anomaly detection package.
It uses Pydantic to manage configuration parameters and reads from environment
files. Keep the environment variables in a file named `.envjson` or `.env`
in the parent directory. This file is used to define configuration parameters
for the anomaly detection package. It includes parameters for the Isolation
Forest algorithm and can be extended with additional configuration 
variables as needed.

create instance of Config class to access configuration parameters.
execute `get_config()` to load the configuration from environment variables.
The git_config function caches the configuration to avoid reloading 
it multiple times. This uses caching to ensure that the configuration
is loaded only once, improving performance.
the same instance of Config is returned every time get_config() is called.
"""


import json
from functools import lru_cache
from pathlib import Path

# from pydantic import BaseSettings
from pydantic import BaseModel
from pydantic_settings import BaseSettings

ENV_JSON_FILE = Path(__file__).parents[2] / ".envjson"
DOTENV_FILE = Path(__file__).parents[2] / ".env"


class ConfigParametersAutoEncoder(BaseModel):
    """
    This class defines the configuration parameters for Autoencoder.
    It can be extended with additional configuration variables as needed.
    """
    
    # Define Autoencoder specific parameters here
    input_dim: int = 784  # Example default value for input dimension
    encoding_dim: int = 32  # Example default value for encoding dimension
    epochs: int = 50  # Example default value for number of training epochs
    batch_size: int = 64  # Example default value for batch size
    learning_rate: float = 0.001  # Example default value for learning rate

class ConfigParametersIsolationForest(BaseModel):
    """
    This class defines the configuration parameters for Isolation Forest.
    It can be extended with additional configuration variables as needed.
    """
    
    n_estimators: int = 100  # Default value
    max_samples: int | float | str = "auto"  # Default value
    contamination: float | str = 0.01  # Default value
    max_features: int | float = 1.0  # Default value

    def to_model_dict(self) -> dict:
        """
        Convert the configuration parameters to a dictionary.
        """
        # Ensure the specified keys exist in the model
        valid_keys = {"n_estimators", "max_samples", "contamination", "max_features"}
        existing_keys = valid_keys.intersection(self.__fields__.keys())  # Check against model fields
        return self.dict(include=existing_keys)

class Config(BaseSettings):
    """
    This config will automatically read in the environment variables that have the same name as its class variables.

    Pydantic will automatelly parse and validate the passed environment variables.
    """
    
    # Define class variables with default values and types
    LOGLEVEL: str = "INFO"
    CONFIG_AUTO_ENCODER: ConfigParametersAutoEncoder = ConfigParametersAutoEncoder()
    CONFIG_ISOLATION_FOREST: ConfigParametersIsolationForest = ConfigParametersIsolationForest()




    # Additional configuration variables can be added here


@lru_cache()
def get_config() -> Config:
    """Returns the same Config wherever this is called thanks to the cache.

    Priority of environment variables: 1. ENV_JSON_FILE 2. DOTENV_FILE 3. os.environ
    """
    env_json = {}
    try:
        with open(ENV_JSON_FILE, "r", encoding="utf-8") as fp:
            env_json = json.load(fp)
    except FileNotFoundError:
        pass

    return Config(_env_file=DOTENV_FILE, **env_json)

if __name__ == "__main__":
    # If this module is run directly, print the configuration
    CONFIG = get_config()
    print("Config loaded successfully.")
    # print(f"AutoEncoder Config: {CONFIG.CONFIG_AUTO_ENCODER}")
    # You can access other configuration parameters similarly
