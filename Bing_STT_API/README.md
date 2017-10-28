# Bing_STT_API
Program making RPC connection with Bing STT(String To Text) server, using Bing's library to\
complete the audio identifying task. You send a packet with binary data of audio file and receive\
a text about what the audio may have spoken.\
The interaction between the program and server base on packets pack the specify info in **JSON**\
elementtree.

Here are the procedure:
- *Grant your access code with yout Microsoft account*.   `You need to add these information into packet's header.`
- *Receive the accese code from server.*
- *Now you will pack your audio file info. Beware of:*
  - *Add the access code into the packet's header.*
  - *Audio file's binary info must be add to the packet's body.*
  - *Select how you will recieve the identified results.*
  
For detail refer to [Azure Speech API](https://azure.microsoft.com/en-us/services/cognitive-services/speech/)
