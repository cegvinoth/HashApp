from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from Crawl_score import getscore
import datetime



class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
            self.toLower(receipt)
            fileobject=open("DataDump.txt","a")
            fileobject.write(str(datetime.datetime.now()))
            fileobject.write(" "+messageProtocolEntity.getBody())
            fileobject.write(" "+messageProtocolEntity.getFrom())
            fileobject.write("\n")
            fileobject.close()
            if messageProtocolEntity.getBody() == "#score" :
              SMS = getscore()
              for sms in SMS:
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(sms,to = messageProtocolEntity.getFrom())
                self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
