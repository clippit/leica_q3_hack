# uPnP & DLNA

They use uPnP to view the photos on the camera.

* Server (camera): 192.168.54.1
* Client (mobile app): 192.168.54.10

## Discovery and services

```
M-SEARCH * HTTP/1.1
HOST: 239.255.255.250:1900
MAN: "ssdp:discover"
ST: upnp:rootdevice
MX: 1


HTTP/1.1 200 OK
CACHE-CONTROL: max-age=1800
DATE: Tue, 10 Dec 2024 10:30:20 GMT
EXT:
LOCATION: http://192.168.54.1:60606/DCxxxxxxxx09/Server0/ddd
SERVER: Leica/1.0 UPnP/1.0 Leica-UPnP-MW/1.0
ST: upnp:rootdevice
USN: uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09::upnp:rootdevice
```

```xml
GET /DCxxxxxxxx09/Server0/ddd HTTP/1.1
Host: 192.168.54.1:60606
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
CONTENT-LENGTH: 1596
CONTENT-TYPE: text/xml; charset="utf-8"
DATE: Tue, 10 Dec 2024 10:30:20 GMT
CONNECTION: close

<?xml version="1.0"?>
<root xmlns="urn:schemas-upnp-org:device-1-0" xmlns:leica="urn:schemas-leica-com:leica">
  <specVersion>
    <major>1</major>
    <minor>0</minor>
  </specVersion>
  <device>
    <deviceType>urn:schemas-upnp-org:device:MediaServer:1</deviceType>
    <friendlyName>Leica Q3-1234567</friendlyName>
    <manufacturer>Leica Camera AG</manufacturer>
    <modelName>LEICA Q3</modelName>
    <modelNumber>Leica Q3</modelNumber>
    <modelDescription></modelDescription>
    <serialNumber>1234567</serialNumber>
    <modelURL></modelURL>
    <manufacturerURL></manufacturerURL>
    <UDN>uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09</UDN>
    <dlna:X_DLNADOC xmlns:dlna="urn:schemas-dlna-org:device-1-0">M-DMS-1.50</dlna:X_DLNADOC>
    <leica:X_AdditionalFunction>CPRemoteView</leica:X_AdditionalFunction>
    <leica:X_FirmVersion>2.0.5</leica:X_FirmVersion>
    <leica:X_CamCategory>MirrorlessILC</leica:X_CamCategory>
    <serviceList>
      <service>
        <serviceType>urn:schemas-upnp-org:service:ContentDirectory:1</serviceType>
        <serviceId>urn:upnp-org:serviceId:ContentDirectory</serviceId>
        <SCPDURL>http://192.168.54.1:60606/Server0/CDS_SCPD</SCPDURL>
        <controlURL>http://192.168.54.1:60606/Server0/CDS_control</controlURL>
        <eventSubURL>http://192.168.54.1:60606/Server0/CDS_event</eventSubURL>
      </service>
      <service>
        <serviceType>urn:schemas-upnp-org:service:ConnectionManager:1</serviceType>
        <serviceId>urn:upnp-org:serviceId:ConnectionManager</serviceId>
        <SCPDURL>http://192.168.54.1:60606/Server0/CMS_SCPD</SCPDURL>
        <controlURL>http://192.168.54.1:60606/Server0/CMS_control</controlURL>
        <eventSubURL>http://192.168.54.1:60606/Server0/CMS_event</eventSubURL>
      </service>
    </serviceList>
  </device>
</root>
```
(Response is reformatted)

## ContentDirectory

### Browse

```xml
POST /Server0/CDS_control HTTP/1.1
Host: 192.168.54.1:60606
Accept: */*
Accept-Encoding: deflate, gzip
CONTENT-TYPE: text/xml; charset="utf-8"
SOAPACTION: urn:schemas-upnp-org:service:ContentDirectory:1#Browse
USER-AGENT: OLS/1.0, UPnP/1.1, ONE LEICA SDK
Content-Length: 524

<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
	<s:Body>
		<u:Browse xmlns:u="urn:schemas-upnp-org:service:ContentDirectory:1" xmlns:leica="urn:schemas-leica-com:leica">
			<ObjectID>0</ObjectID>
			<BrowseFlag>BrowseDirectChildren</BrowseFlag>
			<Filter>*</Filter>
			<StartingIndex>0</StartingIndex>
			<RequestedCount>50</RequestedCount>
			<SortCriteria/>
			<leica:X_FromCP>Leica Q3</leica:X_FromCP>
		</u:Browse>
	</s:Body>
</s:Envelope>


HTTP/1.1 200 OK
CONTENT-LENGTH: 3610
CONTENT-TYPE: text/xml;charset="utf-8"
DATE: Tue, 10 Dec 2024 10:30:25 GMT
EXT:
SERVER: Leica/1.0 UPnP/1.0 Leica-UPnP-MW/1.0
CONNECTION: close

<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <s:Body>
    <u:BrowseResponse xmlns:u="urn:schemas-upnp-org:service:ContentDirectory:1">
      <Result>&lt;DIDL-Lite xmlns=&quot;urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/&quot; xmlns:dc=&quot;http://purl.org/dc/elements/1.1/&quot; xmlns:upnp=&quot;urn:schemas-upnp-org:metadata-1-0/upnp/&quot; xmlns:leica=&quot;urn:schemas-leica-com:leica&quot;&gt;&lt;item id=&quot;01010972&quot; parentID=&quot;0&quot; restricted=&quot;0&quot;&gt;&lt;dc:title&gt;101-0972&lt;/dc:title&gt;&lt;upnp:writeStatus&gt;WRITABLE&lt;/upnp:writeStatus&gt;&lt;upnp:class name=&quot;imageItem&quot;&gt;object.item.imageItem&lt;/upnp:class&gt;&lt;res protocolInfo=&quot;http-get:*:application/octet-stream;LEICA.COM_PN=CAM_DNG;OriginalFileName=&apos;L1010972.DNG&apos;&quot; size=&quot;76436480&quot;&gt;http://192.168.54.1:50001/DO01010972.DNG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_TN;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_TN&quot; size=&quot;5000&quot;&gt;http://192.168.54.1:50001/DT01010972.JPG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_MED;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_LRGTN&quot; size=&quot;100000&quot;&gt;http://192.168.54.1:50001/DL01010972.JPG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_LRG;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_FULLTN&quot; size=&quot;20971520&quot;&gt;http://192.168.54.1:50001/DF01010972.JPG&lt;/res&gt;&lt;dc:date&gt;2024-12-10T15:12:19+08:00&lt;/dc:date&gt;&lt;leica:X_Rating&gt;off&lt;/leica:X_Rating&gt;&lt;/item&gt;&lt;item id=&quot;01010976&quot; parentID=&quot;0&quot; restricted=&quot;0&quot;&gt;&lt;dc:title&gt;101-0976&lt;/dc:title&gt;&lt;upnp:writeStatus&gt;WRITABLE&lt;/upnp:writeStatus&gt;&lt;upnp:class name=&quot;imageItem&quot;&gt;object.item.imageItem&lt;/upnp:class&gt;&lt;res protocolInfo=&quot;http-get:*:application/octet-stream;LEICA.COM_PN=CAM_DNG_JPG;OriginalFileName=&apos;L1010976.JPG&apos;&quot; size=&quot;30554112&quot;&gt;http://192.168.54.1:50001/DO01010976.JPG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:application/octet-stream;LEICA.COM_PN=CAM_DNG;OriginalFileName=&apos;L1010976.DNG&apos;&quot; size=&quot;86539264&quot;&gt;http://192.168.54.1:50001/DO01010976.DNG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_TN;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_TN&quot; size=&quot;5000&quot;&gt;http://192.168.54.1:50001/DT01010976.JPG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_MED;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_LRGTN&quot; size=&quot;100000&quot;&gt;http://192.168.54.1:50001/DL01010976.JPG&lt;/res&gt;&lt;res protocolInfo=&quot;http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_LRG;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_FULLTN&quot; size=&quot;20971520&quot;&gt;http://192.168.54.1:50001/DF01010976.JPG&lt;/res&gt;&lt;dc:date&gt;2024-12-10T15:14:01+08:00&lt;/dc:date&gt;&lt;leica:X_Rating&gt;off&lt;/leica:X_Rating&gt;&lt;/item&gt;&lt;/DIDL-Lite&gt;</Result>
      <NumberReturned>2</NumberReturned>
      <TotalMatches>2</TotalMatches>
      <UpdateID>1</UpdateID>
    </u:BrowseResponse>
  </s:Body>
</s:Envelope>
```

Content of `<Result>`:

```xml
<DIDL-Lite xmlns="urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/" xmlns:leica="urn:schemas-leica-com:leica">
  <item id="01010972" parentID="0" restricted="0">
    <dc:title>101-0972</dc:title>
    <upnp:writeStatus>WRITABLE</upnp:writeStatus>
    <upnp:class name="imageItem">object.item.imageItem</upnp:class>
    <res protocolInfo="http-get:*:application/octet-stream;LEICA.COM_PN=CAM_DNG;OriginalFileName='L1010972.DNG'" size="76436480">http://192.168.54.1:50001/DO01010972.DNG</res>
    <res protocolInfo="http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_TN;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_TN" size="5000">http://192.168.54.1:50001/DT01010972.JPG</res>
    <res protocolInfo="http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_MED;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_LRGTN" size="100000">http://192.168.54.1:50001/DL01010972.JPG</res>
    <res protocolInfo="http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_LRG;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_FULLTN" size="20971520">http://192.168.54.1:50001/DF01010972.JPG</res>
    <dc:date>2024-12-10T15:12:19+08:00</dc:date>
    <leica:X_Rating>off</leica:X_Rating>
  </item>
  <item id="01010976" parentID="0" restricted="0">
    <dc:title>101-0976</dc:title>
    <upnp:writeStatus>WRITABLE</upnp:writeStatus>
    <upnp:class name="imageItem">object.item.imageItem</upnp:class>
    <res protocolInfo="http-get:*:application/octet-stream;LEICA.COM_PN=CAM_DNG_JPG;OriginalFileName='L1010976.JPG'" size="30554112">http://192.168.54.1:50001/DO01010976.JPG</res>
    <res protocolInfo="http-get:*:application/octet-stream;LEICA.COM_PN=CAM_DNG;OriginalFileName='L1010976.DNG'" size="86539264">http://192.168.54.1:50001/DO01010976.DNG</res>
    <res protocolInfo="http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_TN;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_TN" size="5000">http://192.168.54.1:50001/DT01010976.JPG</res>
    <res protocolInfo="http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_MED;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_LRGTN" size="100000">http://192.168.54.1:50001/DL01010976.JPG</res>
    <res protocolInfo="http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_LRG;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000;LEICA.COM_PN=CAM_FULLTN" size="20971520">http://192.168.54.1:50001/DF01010976.JPG</res>
    <dc:date>2024-12-10T15:14:01+08:00</dc:date>
    <leica:X_Rating>off</leica:X_Rating>
  </item>
</DIDL-Lite>
```

### Download file

```
GET /DL01010979.JPG HTTP/1.1
Host: 192.168.54.1:50001
Accept: */*
Accept-Encoding: deflate, gzip


HTTP/1.1 200 OK
Date: Fri, 31 Mar 19324 11:47:28 GMT
Server: Panasonic
Cache-Control: no-cache
Pragma: no-cache
Transfer-Encoding: chunked
Content-Type: image/jpeg
Accept-Ranges: bytes
transferMode.dlna.org:Interactive
X-REC_DATE_TIME: 2024-12-10T21:21:34
X-ROTATE_INFO: 1
X-FILE_SIZE: 41639
Connection: Keep-Alive

<binary data>
```

### Delete file

```xml
POST /Server0/CDS_control HTTP/1.1
Host: 192.168.54.1:60606
Accept: */*
Accept-Encoding: deflate, gzip
CONTENT-TYPE: text/xml; charset="utf-8"
SOAPACTION: urn:schemas-upnp-org:service:ContentDirectory:1#DestroyObject
USER-AGENT: OLS/1.0, UPnP/1.1, ONE LEICA SDK
Content-Length: 293

<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
	<s:Body>
		<u:DestroyObject xmlns:u="urn:schemas-upnp-org:service:ContentDirectory:1">
			<ObjectID>01010976</ObjectID>
		</u:DestroyObject>
	</s:Body>
</s:Envelope>


HTTP/1.1 200 OK
CONTENT-LENGTH: 287
CONTENT-TYPE: text/xml;charset="utf-8"
DATE: Tue, 10 Dec 2024 13:04:45 GMT
EXT:
SERVER: Leica/1.0 UPnP/1.0 Leica-UPnP-MW/1.0
CONNECTION: close

<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <s:Body>
    <u:DestroyObjectResponse xmlns:u="urn:schemas-upnp-org:service:ContentDirectory:1">
    </u:DestroyObjectResponse>
  </s:Body>
</s:Envelope>
```

## Event

### Subscribe

```xml
SUBSCRIBE /Server0/CMS_event HTTP/1.1
Host: 192.168.54.1:60606
Accept: */*
Accept-Encoding: deflate, gzip
CALLBACK: <http://192.168.54.10:50360/Events>
Connection: close
NT: upnp:event
TIMEOUT: Second-200
User-Agent: OLS/1.0 UPnP/1.1  ONE LEICA SDK
Content-Length: 151

<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
	<s:Body/>
</s:Envelope>


HTTP/1.1 200 OK
CONTENT-LENGTH: 0
DATE: Tue, 10 Dec 2024 10:30:24 GMT
SERVER: Leica/1.0 UPnP/1.0 Leica-UPnP-MW/1.0
SID: uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09
TIMEOUT: Second-300
CONNECTION: close

```

### SourceProtocolInfo, SinkProtocolInfo, CurrentConnectionIDs

```xml
NOTIFY /Events HTTP/1.1
HOST: 192.168.54.10:50360
CONTENT-TYPE: text/xml; charset="utf-8"
CONTENT-LENGTH: 1096
NT: upnp:event
NTS: upnp:propchange
SID: uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09
SEQ: 0
CONNECTION: close

<e:propertyset xmlns:e="urn:schemas-upnp-org:event-1-0">
  <e:property>
    <SourceProtocolInfo>http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_LRG;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=00900000000000000000000000000000,http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_MED;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=00900000000000000000000000000000,http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_SM;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=00900000000000000000000000000000,http-get:*:image/jpeg:DLNA.ORG_PN=JPEG_TN;DLNA.ORG_OP=01;DLNA.ORG_CI=1;DLNA.ORG_FLAGS=00900000000000000000000000000000,http-get:*:application/octet-stream,http-get:*:video/mp4:DLNA.ORG_PN=AVC_MP4_BL_L31_HD_AAC;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=01100000000000000000000000000000,http-get:*:video/mp4:DLNA.ORG_PN=AVC_MP4_MP_HD_1080i_AAC;DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=01100000000000000000000000000000</SourceProtocolInfo>
  </e:property>
  <e:property>
    <SinkProtocolInfo></SinkProtocolInfo>
  </e:property>
  <e:property>
    <CurrentConnectionIDs>0</CurrentConnectionIDs>
  </e:property>
</e:propertyset>
```

### X_Leica_Cam_Sync

```xml
NOTIFY /Events HTTP/1.1
HOST: 192.168.54.10:50360
CONTENT-TYPE: text/xml; charset="utf-8"
CONTENT-LENGTH: 163
NT: upnp:event
NTS: upnp:propchange
SID: uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09
SEQ: 1
CONNECTION: close

<e:propertyset xmlns:e="urn:schemas-upnp-org:event-1-0">
  <e:property>
    <X_Leica_Cam_Sync>lens_Update</X_Leica_Cam_Sync>
  </e:property>
</e:propertyset>
```

`X_Leica_Cam_Sync` values:

* lens_Update
* lens_Atta
* busy
* update

### X_Leica_Cam_PRec

`PRec` might mean "picture record".

```xml
NOTIFY /Events HTTP/1.1
HOST: 192.168.54.10:50360
CONTENT-TYPE: text/xml; charset="utf-8"
CONTENT-LENGTH: 154
NT: upnp:event
NTS: upnp:propchange
SID: uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09
SEQ: 8
CONNECTION: close

<e:propertyset xmlns:e="urn:schemas-upnp-org:event-1-0">
  <e:property>
    <X_Leica_Cam_PRec>ok</X_Leica_Cam_PRec>
  </e:property>
</e:propertyset>
```

### X_Leica_Cam_VRec

`VRec` might mean "video record".

```xml
NOTIFY /Events HTTP/1.1
HOST: 192.168.54.10:50360
CONTENT-TYPE: text/xml; charset="utf-8"
CONTENT-LENGTH: 157
NT: upnp:event
NTS: upnp:propchange
SID: uuid:4Dxxxxxx-0100-1000-8000-DCxxxxxxxx09
SEQ: 10
CONNECTION: close

<e:propertyset xmlns:e="urn:schemas-upnp-org:event-1-0">
  <e:property>
    <X_Leica_Cam_VRec>start</X_Leica_Cam_VRec>
  </e:property>
</e:propertyset>
```

`X_Leica_Cam_VRec` calues:

* start
* done