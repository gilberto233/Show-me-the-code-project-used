"""
A simulator which stimulate the encryption of the communication
of client and server. Client will send a packet including user's
login information which has been encrypted. Server will decrypt
the login information and check the availability.
"""
import random, uuid, hashlib, re

class client():

    def __init__(self, user, pw):
        self.user = user
        self.pw = pw

        self.encryption_pw = self.__encryption__()

    def __encryption__(self):
        """
        Encrypt the user's password with random uuid encoding in UTF-8.
        The hash mixed with encoding uuid, encoding password. The uuid
        will be appended to the packet sending to Server.
        :return: hash of password
        """
        salt = uuid.uuid4().hex
        return ( hashlib.sha256( salt.encode() + self.pw.encode() ).hexdigest() + ':' + salt )

    def __get_encrytion_pw__(self):
        """
        Get the encrypted password.
        :return: password being encrypted
        """
        return self.encryption_pw

    def __get_username__(self):
        """
        Get the user's name.
        :return: user's name.
        """
        return self.user

class server():

    def __init__(self, user, pw):
        """
        Entry function of server. Load the user's profile from local filesystem.
        :param user: login information: user's name
        :param pw: login information: user's password
        """
        self.user = user
        self.pw = pw
        self.origin_set = {}

        with open( 'encryption_README.txt' ) as file:
            for line in file:
                buffer = re.match( r'(.*):(.*)', line )
                usr_buffer, pw_buffer = buffer.group(1), buffer.group(2)
                self.origin_set[ usr_buffer ] = pw_buffer

        self.__identify__()

    def __identify__(self):
        """
        Check login information's feasibility.
        :return: None
        """

        for usr in self.origin_set:
            if self.__unencryption__( self.origin_set[ usr ] ):
                print( 'Identify success.' )
                return
        print( 'Identify error.' )

    def __unencryption__(self, usr_passwd):
        """
        Decrypt the hash of password.
        :param usr_passwd: hash of user's password
        :return: True if login success, False if login fail.
        """
        passwd, salt = self.pw.split( ':' )
        return hashlib.sha256( salt.encode() + usr_passwd.encode() ).hexdigest()


if __name__ == '__main__':
    client_instance = client( 'root', '123456' )
    server_instance = server( client_instance.__get_username__(),
                              client_instance.__get_encryption_pw__() )
