# PTP/IP

PTP/IP protocol is used since firmware v3.0.0 for all camera controls and image transfer. It runs at TCP port 15740.

## Initial Connection

### Init Command

```
0000   22 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00   "...............
0010   00 00 00 00 00 00 00 00 4f 00 4c 00 53 00 00 00   ........O.L.S...
0020   01 00                                             ..


PTP/IP: Init Command Request Packet
    Length: 34
    Packet Type: 0x00000001
    GUID: 00000000000000000000000000000000
    Host Name: OLS
    Version: 1.0
```

```
0000   22 00 00 00 02 00 00 00 01 00 00 00 00 00 00 00   "...............
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00                                             ..


PTP/IP: Init Command ACK Packet
    Length: 34
    Packet Type: 0x00000002
    Connection Number: 0x00000001
    GUID: 00000000000000000000000000000000
    Host Name: 
    Version: 0.0
```

### Init Event

```
0000   0c 00 00 00 03 00 00 00 01 00 00 00               ............


PTP/IP: Init Event Request Packet
    Length: 12
    Packet Type: 0x00000003
    Connection Number: 0x00000001
```

```
0000   08 00 00 00 04 00 00 00                           ........


PTP/IP: Init Event Ack Packet
    Length: 8
    Packet Type: 0x00000004
```


### Operation: OpenSession

```
0000   16 00 00 00 06 00 00 00 01 00 00 00 02 10 00 00   ................
0010   00 00 12 04 00 00                                 ......


PTP/IP: Operation Request Packet
    Length: 22
    Packet Type: 0x00000006
    Data Phase Info: 0x00000001
    Operation Code: 0x1002
    TransactionID Offset: 14
    Transaction ID: 0x00000000
MTP(PTP): OpenSession
    Operation Code: 0x1002 (OpenSession)
    TransactionID: 0x0000 (OpenSession)
    SessionID: 0x0412 
```

```
0000   22 00 00 00 07 00 00 00 01 20 00 00 00 00 00 00   "........ ......
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00                                             ..


PTP/IP: Operation Response Packet
    Length: 34
    Packet Type: 0x00000007
    Response Code: 0x2001
    TransactionID Offset: 10
    Transaction ID: 0x00000000
MTP Response: OK
    Code: OK (0x2001)
    TransactionID: 0x0000 (OpenSession)
    Parameter 1: 0x00000000
    Parameter 2: 0x00000000
    Parameter 3: 0x00000000
    Parameter 4: 0x00000000
    Parameter 5: 0x00000000
```

### Operation: OpenLESession

```
0000   16 00 00 00 06 00 00 00 01 00 00 00 05 90 01 00   ................
0010   00 00 55 ff 00 00                                 ..U...


PTP/IP: Operation Request Packet
    Length: 22
    Packet Type: 0x00000006
    Data Phase Info: 0x00000001
    Operation Code: 0x9005
    TransactionID Offset: 14
    Transaction ID: 0x00000001
MTP(PTP): OpenLESession
    Operation Code: 0x9005 (OpenLESession)
    TransactionID: 0x0001 (OpenLESession)
    Parameter 1: 0x0000ff55
```

```
0000   22 00 00 00 07 00 00 00 01 20 01 00 00 00 00 00   "........ ......
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00                                             ..


PTP/IP: Operation Response Packet
    Length: 34
    Packet Type: 0x00000007
    Response Code: 0x2001
    TransactionID Offset: 10
    Transaction ID: 0x00000001
MTP Response: OK
    Code: OK (0x2001)
    TransactionID: 0x0001 (OpenLESession)
    Parameter 1: 0x00000000
    Parameter 2: 0x00000000
    Parameter 3: 0x00000000
    Parameter 4: 0x00000000
    Parameter 5: 0x00000000

```

## Heartbeat

### LEKeepSessionActive

```
0000   12 00 00 00 06 00 00 00 01 00 00 00 1d 90 18 00   ................
0010   00 00                                             ..


PTP/IP: Operation Request Packet
    Length: 18
    Packet Type: 0x00000006
    Data Phase Info: 0x00000001
    Operation Code: 0x901d
    TransactionID Offset: 14
    Transaction ID: 0x00000018
MTP(PTP): LEKeepSessionActive
    Operation Code: 0x901D (LEKeepSessionActive)
    TransactionID: 0x0018 (LEKeepSessionActive)

```

```
0000   22 00 00 00 07 00 00 00 01 20 18 00 00 00 00 00   "........ ......
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00                                             ..


PTP/IP: Operation Response Packet
    Length: 34
    Packet Type: 0x00000007
    Response Code: 0x2001
    TransactionID Offset: 10
    Transaction ID: 0x00000018
MTP Response: OK
    Code: OK (0x2001)
    TransactionID: 0x0018 (LEKeepSessionActive)
    Parameter 1: 0x00000000
    Parameter 2: 0x00000000
    Parameter 3: 0x00000000
    Parameter 4: 0x00000000
    Parameter 5: 0x00000000

```

## Other Operations (WIP)

### GetDeviceInfo

### GetObjectHandles

### LEGetObjectPropList

### GetLensParameter

### GetDevicePropDesc

### GetDevicePropValue

### LEGetLookPropList

### LEGetPartialObject64


## Event

### DevicePropChanged

```
0000   1a 00 00 00 08 00 00 00 06 40 ff ff ff ff 13 50   .........@.....P
0010   00 00 00 00 00 00 00 00 00 00                     ..........


PTP/IP: Event Packet
    Length: 26
    Packet Type: 0x00000008
    Event Code: 0x4006
    TransactionID Offset: 10
    Transaction ID: 0xffffffff
MTP Event: DEVICEPROPCHANGED
    Code: DEVICEPROPCHANGED (0x4006)
    TransactionID: 0xFFFFFFFF (DEVICEPROPCHANGED)
    Parameter 1: 0x00005013
    Parameter 2: 0x00000000
    Parameter 3: 0x00000000
```