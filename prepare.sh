mkdir singbox-rules
wget https://github.com/SagerNet/sing-box/releases/download/v1.10.7/sing-box-1.10.7-linux-amd64.tar.gz
mkdir singbox_binary
tar -xvzf sing-box-1.10.7-linux-amd64.tar.gz -C singbox_binary --strip-components=1
rm sing-box-1.10.7-linux-amd64.tar.gz
