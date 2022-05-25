# IP-Ranges-For-Cloud-Provides
Collect IP addresses owned by public cloud providers (AWS, GCP, etc..)

## Description

Most cloud providers publish up to date lists of their IP address ranges. This tool lets you Download the IP lists so you can use those for your specific use cases.

Supports:

- [x] AWS ([source](https://ip-ranges.amazonaws.com/ip-ranges.json)) 
- [x] Azure ([source](https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519))
- [x] Google Cloud Platform ([source](https://www.gstatic.com/ipranges/cloud.json))
- [ ] Alibaba Cloud (currently doesn't publish lists)
- [x] Oracle Cloud Infrastructure ([source](https://docs.cloud.oracle.com/en-us/iaas/tools/public_ip_ranges.json))
- [ ] IBM Cloud (currently doesn't publish lists)
- [x] DigitalOcean ([source](http://digitalocean.com/geo/google.csv))

This tool is inspired by [NCC] (https://github.com/nccgroup/cloud_ip_ranges.git).

## Usage

The installation method:

```shell script
$ git clone https://github.com/OsamaMahmood/IP-Ranges-For-Cloud-Provides.git
$ cloud_ip_ranges
```

Alternatively, you can setup a virtual environment and install dependencies:

```shell script
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run the tool:

```shell script
$ cloud_ip_ranges.py
```
