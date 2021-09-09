"""
Author : Venkatesan Madappan
Test Automation Framework
"""
import logging
import os
import os.path
import sys
import datetime

from Device.nrfboard import NrfBoard
from Template.logmodule import Log
from config.configmodule import ConfigModule


class TestBase:
    """
    Base Test Class
    """
    log_file_name = None
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))

    def __init__(self):
        filename = os.path.join(os.getcwd(), './config/deviceconfig.json')
        self.config_module = ConfigModule(filename)
        self.config_module.get_config_parameters()
        logfile = os.path.join(os.getcwd(), TestBase.log_file_name)
        self.logger = Log(logfile)
        if self.config_module.config_data["log_message_to_console"] == "YES":
            self.logger = logging.getLogger()
            stdout_handler = logging.StreamHandler(sys.stdout)
            self.logger.addHandler(stdout_handler)
        if self.config_module.config_data["Board"] == "NRF5340":
            self.dut = NrfBoard()
        else:
            assert True, "Unknown Device, unable to create device Object"
        self.logger.info("TestCase Base")

    def run(self):
        """
        Generic Method to run the test
        :return:
        """
        self.dut.create_device_and_transport(self.config_module.config_data)
        self.logger.info("Run the Test Case")

    @staticmethod
    def wait_for_advertisement():
        print("*" * 30, end='\n')
        input('("Press any key than Press Enter") to Start Advertisement on the NRF Board')

    def cleanup(self):
        """
        Clean up method
        :return: None
        """
        self.dut.cleanup()


if __name__ == "__main__":
    print("Test Framework Main Test base")
