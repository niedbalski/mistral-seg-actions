from mistral_lib import actions
from oslo_log import log as logging

import subprocess
import os

LOG = logging.getLogger(__name__)


class XsosAction(actions.Action):

    def __init__(self, filepath):
        self.filepath = filepath

    def run(self, action_ctx=None):
        report_path = os.path.join(os.path.dirname(self.filepath), "xsos.output")
        with open(report_path, 'wb+') as fd:
            fd.write(subprocess.run(["xsos", "-a", "-x", self.filepath], stdout=subprocess.PIPE).stdout)
        return report_path