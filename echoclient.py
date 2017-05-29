from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write('Hello world')

    def dataReceived(self):
        print('Server said', data)
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed')
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print('Connection lost')
        reactor.stop()


import pdb; pdb.set_trace()
reactor.listenTCP('localhost', 8000, EchoFactory())
reactor.run()
