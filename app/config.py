class Config:
    """
    General configuration parent class
    """

    class prodConfig(Config):
        """
        Production configuration child class
        """

    class DevConfig(Config):
        """
        Development configuraion class
        """

        DEBUG = True