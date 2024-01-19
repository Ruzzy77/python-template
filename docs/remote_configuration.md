## Table of Contents

- [Table of Contents](#table-of-contents)
- [Remote Configuration (VSCode)](#remote-configuration-vscode)
- [Enabling X11 Forwarding](#enabling-x11-forwarding)
  - [Server Side (WSL2)](#server-side-wsl2)
  - [Client Side (Windows / VSCode)](#client-side-windows--vscode)

## Remote Configuration (VSCode)

```json
{
    "name": "Remote-SSH: Auto Labeling",
    "type": "ssh",
    "request": "launch",
    "cwd": "${workspaceFolder}",
    "remotePath": "/home/<username>/Projects/auto-labeling",
    "port": <port>,
    "host": "<Domain or IP Address>",
    "username": "<username>",
    "password": "<password>",
}
```

## Enabling X11 Forwarding

### Server Side (WSL2)

1. Add/Edit the following line in `/etc/ssh/sshd_config`

   > ℹ️ Note:
   > This is my configuration. You can change it to your own configuration.
   > DO NOT copy and paste it directly. be aware of what you are doing.

   ```bash
   AddressFamily inet
   AllowTcpForwarding yes
   X11Forwarding yes
   X11DisplayOffset 10
   X11UseLocalhost no
   ```

   > Note:
   >
   > - `AddressFamily` is set to `inet` to allow remote access. (Default is `any`)
   > - `AllowTcpForwarding` is set to `yes` to allow remote access. (Default is `no`)
   > - `X11Forwarding` is set to `yes` to allow remote access. (Default is `no`)
   > - `X11DisplayOffset` is the display number. If you want to use `:0`, set `X11DisplayOffset 0`.
   > - `X11UseLocalhost` is set to `no` to allow remote access.
   >   - If you want to use `localhost`, you need to set `X11UseLocalhost yes` and `X11DisplayOffset 0`.

2. Restart the sshd service.

   ```bash
   sudo service sshd restart
   ```

### Client Side (Windows / VSCode)

1. Add/Edit the following line in `C:\Users\<username>\.ssh\config`

   This also configurable in VSCode. (Check _Remote-SSH_ Extension is installed)

   - Command Palette : `Remote-SSH: Open Configuration File`

   <br>

   ```bash
   Host <Domain or IP Address>
       HostName <Domain or IP Address>
       Port <ssh port>
       User <username>
       ForwardX11 yes
       ForwardX11Trusted yes
       ForwardAgent yes
   ```

2. Insall [VcXsrv](https://sourceforge.net/projects/vcxsrv/)

   - Run `XLaunch` and select `Multiple windows` and `Start no client`.
   - Select `Display number` to `10`.

     > Note: This is same as `X11DisplayOffset` in `sshd_config`.
     > If you want to use `:0`, set `X11DisplayOffset 0`.
     > You can check the display number by running `echo $DISPLAY` in WSL2.
     > output would be `:10.0`. or `<YOUR-PC-NAME>:10.0`

   - Select `Disable access control` to `Yes`.
   - Add `-ac` to `Extra parameters` field.
   - Click `Finish`.

   - If Network firewall window is shown, click `Allow access for private/public`.

   - I've added `config.xlaunch` file to this repository.
     You can use this file to configure XLaunch.
     > Note: You need to change `Display number` to `10` in `config.xlaunch` file.

3. Test X11 Forwarding

   - Connect ssh to server.
     `ssh <username>@<Domain_or_IP_Address> -p <ssh_port>`

     > Note: -X or -Y option is not needed. because it is configured in `config` file.

     - You can use VSCode _Remote-SSH_ Extension.
       - Command Palette : `Remote-SSH: Connect to Host...`

   - Run `echo $DISPLAY` in WSL2.

     > output would be `:10.0`. or `<YOUR-PC-NAME>:10.0`

   - Run `xeyes` or `xclock` or `xcalc` in WSL2. (In client terminal)
     > If you see `xeyes` window, X11 Forwarding is working.
