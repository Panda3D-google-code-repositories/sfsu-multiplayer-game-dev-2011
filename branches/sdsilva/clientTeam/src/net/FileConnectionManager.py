import socket
import struct

from common.Constants import Constants
from common.FileExtractor import FileExtractor

class FileConnectionManager:

    def __init__(self, interface = None):

        self.file_id = -1
        self.size = 0
        self.response = -1
        self.filename = 'Untitled'
        self.file_size = 0

        self.interface = interface

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((Constants.SERVER_IP, Constants.SERVER_PORT))

    def run(self):

        taskMgr.add(self.getFile, 'FileTransfer-' + str(self.file_id), -40)

    def close(self):

        taskMgr.remove('FileTransfer-' + str(self.file_id))
        self.connection.close()

    def send(self, file_id):

        self.file_id = file_id

        string = ''
        string += struct.pack('H', 6)
        string += struct.pack('H', Constants.CMSG_DOWNLOAD)
        string += struct.pack('I', self.file_id)

        self.connection.send(string)

    def getHeader(self):

        size = struct.unpack('H', self.connection.recv(2))[0]
        self.response = struct.unpack('H', self.connection.recv(2))[0]

        status = struct.unpack('H', self.connection.recv(2))[0]

        if status == 0:
            str_size = struct.unpack('H', self.connection.recv(2))[0]
            self.filename = self.connection.recv(str_size)

            self.file_size = struct.unpack('I', self.connection.recv(4))[0]

            self.file = open(Constants.MYDIR + 'temp/' + self.filename, 'wb')

            return (self.response, self.filename, self.file_size)

        return None

    def getFile(self, task):

        for i in range(10):
            data = self.connection.recv(65536)

            if not data:
                self.file.close()
                self.connection.close()
                self.unpackFile()
                return task.done

            self.size += len(data)
            self.file.write(data)

            if self.interface:
                self.interface.setProgress(self.size * 100 / self.file_size)

        return task.cont

    def unpackFile(self):

        if self.interface:
            self.interface.setStatus(2)
            self.interface.setProgress(0)

        base.graphicsEngine.renderFrame()

        fileExtractor = FileExtractor(self.filename, self.interface)
        fileExtractor.start()
