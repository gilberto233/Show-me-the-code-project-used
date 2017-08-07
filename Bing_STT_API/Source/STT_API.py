"""

"""
import urllib.request, codecs, re, webbrowser

class STT_API():

    def __init__(self, filename):
        """
        Initiative the class with URL with Bing STT API.
        :param filename: The file path of the voice sample. 
        """
        self.filepath = filename
        self.url = 'https://www.baidu.com/'
        self.auth_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        self.analyst_url = 'https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=pt-BR&locale=zh-CN&format=simple&requestid='

    def __auth__(self):
        """
        Sending the authorization information to Microsoft REST API and receive the
        public key used to access the service. 
        :return: A tuple includes the request ID and apim-request-id when authorization 
        success, -1 when authorization fail. 
        """
        header = { 'Content-Type': 'application/x-www-form-urlencoded',
                   'Content-Length': '0',
                   'Ocp-Apim-Subscription-Key': '7a3a738507744e59b345f5292eb46221' }

        req = urllib.request.Request( self.auth_url, headers=header, method='POST' )
        with urllib.request.urlopen( req ) as reply:
            if reply.status == 200:
                request_id = reply.getheader( 'apim-request-id' )
                return request_id, reply.read().decode()
            else: return -1

    def __analyst__(self, request_id, access_token, filename ):
        """
        Send the voice sample to STT API and obtain the analyst result in reply
        packet. The voice sample appended with the packet's body in binary format.
        :param request_id: The request ID of reply packet. ( Found in header )
        :param access_token:  The access_token of reply packet. ( Found in body )
        :param filename: The file path of voice sample.
        :return: The analyst result with packet's successful sending, -1 when fail.
        """
        self.analyst_url += request_id
        header = { 'Authorization': ( 'Bearer ' + access_token ),
                   'Content-Type': 'audio/wav; codec="audio/pcm"; samplerate=16000' }

        with open( filename, 'rb' ) as binary_file:
            binary_buffer = b''
            for line in binary_file:
                binary_buffer += line

        req = urllib.request.Request( self.analyst_url, headers=header, method='POST', data=binary_buffer )
        with urllib.request.urlopen( req ) as reply:
            if reply.status == 200:
                return reply.read().decode()
            else: return -1

    def __trigger__(self, cmd):
        """
        When the command is matched, open specify website.
        :param cmd: The analyst result from Bing STT API. 
        :return: None
        """

        if cmd == "Eu até a india de nerd":
            webbrowser.open_new( self.url )

    def __intro__(self):
        """
        We conclude the whole procedure into this function.
        :return: None
        """
        tmp = self.__auth__()
        re_msg = self.__analyst__( tmp[0], tmp[1], self.filepath )
        analyst_result = re.search( r'"DisplayText":"(.*?)"', re_msg ).group(1)
        self.__trigger__( analyst_result )

if __name__ == '__main__':
    instance = STT_API( 'callforrescue01.wav' )
    instance.__intro__()
