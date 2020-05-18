from mistral_lib import actions
from oslo_log import log as logging

import tarfile
import tempfile
import os

LOG = logging.getLogger(__name__)


class UncompressSosreportAction(actions.Action):

    def __init__(self, filepath):
        """
        :param filepath: path on swift to the sosreport
        """
        self.filepath = filepath

    def run(self, action_ctx=None):
        tmp_dir = tempfile.TemporaryDirectory(dir=os.path.expanduser("~"))
        with tarfile.open(self.filepath, "r", errorlevel=0) as tar:
            tar.extractall(tmp_dir.name)
            uncompressed_path = os.path.commonprefix(tar.getnames())

        # return your results here
        LOG.info("filepath: {} to original sosreport".format(self.filepath))
        return os.path.join(tmp_dir.name, uncompressed_path)
