from . import file_transport

class _FakeRegex:
    def match(self, str):
        return True

PAT = _FakeRegex()
EXAMPLE = '~/myfolder'

class Sender(file_transport.FileTransport):
    def __init__(self, folder):
        super().__init__(folder, True)