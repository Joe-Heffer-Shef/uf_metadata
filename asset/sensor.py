import os.path
import datetime
import logging

LOGGER = logging.getLogger(__name__)


class Sensor(Asset):
    """
    A sensor registered to the Urban Flows Observatory
    """

    def __init__(self, sensor_id, family, detectors: list, provider: dict = None, serial_number=None,
                 energy_supply=None, freq_maintenance=None, s_type=None, data_acquisition_interval=None,
                 first_date=None, datoz18_handle=None, desc_url=None, iot_import_ip=None, iot_import_port=None,
                 iot_import_token=None, iot_import_username=None, iot_import_password=None, iot_export_ip=None,
                 iot_export_port=None, iot_export_token=None, iot_export_username=None, iot_export_password=None):
        """
        Sensor usage example:

        sensor = Sensor(
            sensor_id='my_sensor_01',
            family='AirQualityGizmo 9000',
            detectors=[
                dict(name='xxx'|unit='xxx'|epsilon='xxx'),
                dict(name='xxx'|unit='xxx'|epsilon='xxx'),
                dict(name='xxx'|unit='xxx'|epsilon='xxx'),
            ]
        )

        :param sensor_id: Unique identifier
        :param family: The group or category of device
        :param detectors: Measurement capabilities of the device
        :type detectors: list[dict]
        :param provider:
        :param serial_number:
        :param energy_supply:
        :param freq_maintenance:
        :param s_type:
        :param data_acquisition_interval:
        :param first_date: The sensor has been operational since this time
        :param datoz18_handle:
        :param desc_url:
        :param iot_import_ip:
        :param iot_import_port:
        :param iot_import_token:
        :param iot_import_username:
        :param iot_import_password:
        :param iot_export_ip:
        :param iot_export_port:
        :param iot_export_token:
        :param iot_export_username:
        :param iot_export_password:
        """

        self.id = sensor_id
        self._provider = provider
        self.serial_number = serial_number
        self.energy_supply = energy_supply
        self.freq_maintenance = freq_maintenance
        self.s_type = s_type
        self.family = family
        self.data_acquisition_interval = data_acquisition_interval
        self.first_date = first_date
        self.datoz18_handle = datoz18_handle
        self._detectors = detectors
        self.desc_url = desc_url

        # Internet of Things

        # Import
        self.iot_import_ip = iot_import_ip
        self.iot_import_port = iot_import_port
        self.iot_import_token = iot_import_token
        self.iot_import_username = iot_import_username
        self.iot_import_password = iot_import_password

        # Export
        self.iot_export_ip = iot_export_ip
        self.iot_export_port = iot_export_port
        self.iot_export_token = iot_export_token
        self.iot_export_username = iot_export_username
        self.iot_export_password = iot_export_password

    def __iter__(self):
        yield 'sensorid', self.id
        yield 'provider', self.provider
        yield 'serialnumber', self.serial_number
        yield 'energysupply', self.energy_supply
        yield 'freqmaintenance', self.freq_maintenance
        yield 'sType', self.s_type
        yield 'family', self.family
        yield 'data-acquisition-interval[min]', self.data_acquisition_interval
        yield 'firstdate', self.first_date
        yield 'datoz18-handle', self.datoz18_handle
        yield from self.detectors
        yield 'desc-url', self.desc_url

        # IoT
        yield 'iot-import-IP', self.iot_import_ip
        yield 'iot-import-port', self.iot_import_port
        yield 'iot-import-token', self.iot_import_token
        yield 'iot-import-usrname', self.iot_import_username
        yield 'iot-import-pwd', self.iot_import_password

        yield 'iot-export-IP', self.iot_export_ip
        yield 'iot-export-port', self.iot_export_port
        yield 'iot-export-token', self.iot_export_token
        yield 'iot-export-usrname', self.iot_export_username
        yield 'iot-export-pwd', self.iot_export_password

    @property
    def detectors(self) -> iter:
        for detector in self._detectors:
            yield 'detector', self.concat_dict(detector)

    @property
    def provider(self):
        return self.concat_dict(self._provider)
