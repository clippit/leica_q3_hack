# HTTP API

HTTP endpoints starting with `/cam.cgi` is used to manager camera settings.

* Server (camera): 192.168.54.1
* Client (mobile app): 192.168.54.10

## getinfo

### /cam.cgi?mode=getinfo&type=allmenu

```
GET /cam.cgi?mode=getinfo&type=allmenu HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
Content-Type: xml
Accept-Ranges: bytes
ETag: "1582998196"
Last-Modified: Thu, 01 Jan 1970 00:00:00 GMT
Content-Length: 124327
Date: Tue, 10 Dec 2024 10:30:23 GMT
Server: Panasonic

<See the link below for response>
```
[getinfo_allmenu.xml](./getinfo_allmenu.xml)

### /cam.cgi?mode=getinfo&type=curmenu

```
GET /cam.cgi?mode=getinfo&type=curmenu HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 41204
Date: Tue, 10 Dec 2024 10:30:24 GMT
Server: Panasonic

<See the link below for response>
```

[getinfo_curmenu.xml](./getinfo_curmenu.xml)

### /cam.cgi?mode=getinfo&type=lens

```
GET /cam.cgi?mode=getinfo&type=lens HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/plain
Content-Length: 64
Date: Tue, 10 Dec 2024 10:30:25 GMT
Server: Panasonic

ok,2304/256,32767/256,3584/256,-1792/256,0,on,0,0,on,0/0,off,off
```

The response is not an XML and contains all shooting parameters. Another example:

```
ok,2048/256,392/256,3328/256,-1280/256,0,on,28,28,on,128/1024,on,off,SUMMILUX 1:1.7/28 ASPH.,LEICA CAMERA AG,N/A
```

## startstream & stopstream

### /cam.cgi?mode=startstream

`value` is the UDP port number to receive live view.

```xml
GET /cam.cgi?mode=startstream&value=59489 HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:19:47 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=stopstream

```xml
GET /cam.cgi?mode=stopstream HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:21:37 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

## camcmd

### /cam.cgi?mode=camcmd&value=playmode

```xml
GET /cam.cgi?mode=camcmd&value=playmode HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 10:30:24 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=camcmd&value=recmode

```xml
GET /cam.cgi?mode=camcmd&value=recmode HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:19:46 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=camcmd&value=capture

```xml
GET /cam.cgi?mode=camcmd&value=capture HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:23 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=camcmd&value=capture_cancel

```xml
GET /cam.cgi?mode=camcmd&value=capture_cancel HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:23 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=camcmd&value=video_recstart

```xml
GET /cam.cgi?mode=camcmd&value=video_recstart HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:38 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=camcmd&value=video_recstop

```xml
GET /cam.cgi?mode=camcmd&value=video_recstop HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:44 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=camcmd&value=poweroff

```xml
GET /cam.cgi?mode=camcmd&value=poweroff HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 10:32:35 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```


## getstate & get_content_info

### /cam.cgi?mode=getstate

This request is sent as a heartbeat.

```xml
GET /cam.cgi?mode=getstate HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 622
Date: Tue, 10 Dec 2024 10:30:24 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply>
  <result>ok</result>
  <state>
    <batt>5/5</batt>
    <batt_per>-1</batt_per>
    <cammode>play</cammode>
    <sdcardstatus>write_enable</sdcardstatus>
    <sd_memory>set</sd_memory>
    <version>VD4.80</version>
    <play>stop</play>
    <temperature>low</temperature>
    <sd_access>off</sd_access>
    <lens>normal</lens>
    <add_location_data>off</add_location_data>
    <sd2_cardstatus>write_enable</sd2_cardstatus>
    <sd2_memory>unset</sd2_memory>
    <sd2_access>off</sd2_access>
    <current_sd>sd1</current_sd>
    <batt_grip>-1/5</batt_grip>
    <batt_per_grip>-1</batt_per_grip>
    <sd_full>false</sd_full>
    <sd2_full>false</sd2_full>
  </state>
</camrply>
```
(Response is reformatted)

### /cam.cgi?mode=get_content_info

This request is sent as a heartbeat.

```xml
GET /cam.cgi?mode=get_content_info HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 206
Date: Tue, 10 Dec 2024 10:30:24 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply>
<result>ok</result>
<current_position>1</current_position>
<total_content_number>2</total_content_number>
<content_number>2</content_number>
</camrply>
```


## setsetting

### /cam.cgi?mode=setsetting

* type: refer to `cmd_type` from [mode=getinfo&type=allmenu](./getinfo_allmenu.xml)
* value: refer to `cmd_value` from [mode=getinfo&type=allmenu](./getinfo_allmenu.xml)

```xml
GET /cam.cgi?mode=setsetting&type=lut&value=1 HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 10:31:59 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

```xml
GET /cam.cgi?mode=setsetting&type=lightmetering&value=center HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 10:32:06 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

```xml
GET /cam.cgi?mode=setsetting&type=drivemode_flat&value=single HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 10:32:14 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```


### /cam.cgi?mode=setsetting&type=device_name

```xml
GET /cam.cgi?mode=setsetting&type=device_name&value=iPhone%20Pro HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 10:30:23 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=setsetting&type=lv_mode

```xml
GET /cam.cgi?mode=setsetting&type=lv_mode&value=video HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:01 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=setsetting&type=focal

```xml
GET /cam.cgi?mode=setsetting&type=focal&value=1577%2F256 HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:13 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

### /cam.cgi?mode=setsetting&type=shtrspeed

```xml
GET /cam.cgi?mode=setsetting&type=shtrspeed&value=2687%2F256 HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:20:15 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

## getsetting

### /cam.cgi?mode=getsetting&type=lut

```xml
GET /cam.cgi?mode=getsetting&type=lut HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 115
Date: Tue, 10 Dec 2024 10:31:59 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result><settingvalue lut="1"></settingvalue></camrply>
```

### /cam.cgi?mode=getsetting&type=lv_mode

```xml
GET /cam.cgi?mode=getsetting&type=lv_mode HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 123
Date: Tue, 10 Dec 2024 13:19:47 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result><settingvalue lv_mode="photo"></settingvalue></camrply>
```

### /cam.cgi?mode=getsetting&type=focal

```xml
GET /cam.cgi?mode=getsetting&type=focal HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 123
Date: Tue, 10 Dec 2024 13:19:47 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result><settingvalue focal="939/256"></settingvalue></camrply>
```

### /cam.cgi?mode=getsetting&type=shtrspeed

```xml
GET /cam.cgi?mode=getsetting&type=shtrspeed HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 129
Date: Tue, 10 Dec 2024 13:19:47 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result><settingvalue shtrspeed="32768/256"></settingvalue></camrply>
```

## camctrl

### /cam.cgi?mode=camctrl&type=touch

```xml
GET /cam.cgi?mode=camctrl&type=touch&value=677%2F536&value2=on HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:19:51 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

```xml
GET /cam.cgi?mode=camctrl&type=touch&value=677%2F536&value2=off HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 78
Date: Tue, 10 Dec 2024 13:19:51 GMT
Server: Panasonic

<?xml version="1.0" encoding="UTF-8"?>
<camrply><result>ok</result></camrply>
```

## lutctrl

### /cam.cgi?mode=lutctrl&type=getlist

```xml
GET /cam.cgi?mode=lutctrl&type=getlist HTTP/1.1
Host: 192.168.54.1
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Type: text/xml
Content-Length: 383
Date: Tue, 10 Dec 2024 10:30:25 GMT
Server: Panasonic

<?xml version="1.0" encoding="utf-8"?>
<camrply>
  <result>ok</result>
  <total>6</total>
  <num>4</num>
  <item>
    <id>00000008</id>
    <name>Chrome</name>
  </item>
  <item>
    <id>00000006</id>
    <name>Eternal</name>
  </item>
  <item>
    <id>00000001</id>
    <name>Contemporary</name>
  </item>
  <item>
    <id>00000002</id>
    <name>Classic</name>
  </item>
  <item></item>
  <item></item>
</camrply>
```
(Response is reformatted)

