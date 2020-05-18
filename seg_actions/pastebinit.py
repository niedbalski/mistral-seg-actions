from mistral_lib import actions
from oslo_log import log as logging

import subprocess

LOG = logging.getLogger(__name__)


class PastebinitAction(actions.Action):

    def __init__(self, filepath):
        self.filepath = filepath

    def run(self, action_ctx=None):
        return subprocess.run(['pastebinit', '-i', self.filepath], stdout=subprocess.PIPE).stdout.rstrip()