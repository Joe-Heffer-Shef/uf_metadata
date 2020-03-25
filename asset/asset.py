"""
Classes for generating configuration files for the Urban Flows Observatory Asset Manager
"""

import os.path
import datetime
import logging

LOGGER = logging.getLogger(__name__)


class Asset:
    """
    A physical asset registered to the Urban Flows Observatory
    """
    
    def __str__(self):
        """Build asset configuration file"""

        lines = list()

        lines.append('begin.asset')

        # Build key-value pairs
        lines.extend(("{}={}".format(key, value if value else '') for key, value in self))

        lines.append('end.asset')

        # Line break at end-of-file
        lines.append('')

        return '\n'.join(lines)

    def __iter__(self):
        """Generate key-value pairs for output to configuration files"""
        raise NotImplementedError

    @property
    def subdir(self) -> str:
        parts = ['assets', "{}s".format(self.__class__.__name__.casefold())]
        
        subdir = os.path.join(*parts)
        
        os.makedirs(subdir, exist_ok=True)
        
        return subdir

    @property
    def filename(self) -> str:
        return '{}.txt'.format(self.id)

    @property
    def path(self) -> str:
        """File path"""
        return os.path.join(self.subdir, self.filename)

    def save(self):
        """Serialise asset configuration file"""
        with open(self.path, 'w+') as file:
            file.write(str(self))

            LOGGER.info("Wrote '%s'", file.name)

    @staticmethod
    def concat_dict(d: dict) -> str:
        """
        Build a string with this format from a dictionary e.g.

        dict(id='xx'|contact='xx'|tel='xxx')

        becomes

        id:xx|contact:xx|tel:xxxyyyyzzz|email:xxx@yyy
        """
        try:
            return '|'.join("{}:{}".format(key, value) for key, value in d.items())
        except AttributeError:
            return str()
