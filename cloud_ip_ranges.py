#!/usr/bin/python3

import requests
from lxml import html
import csv
import coloredlogs
import logging


def collect_aws():
    file_name = "awsip.txt"
    file = open(file_name, 'wb')
    try:
        logger.info('Getting IPs for AWS')
        aws_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
        aws_ips = requests.get(aws_url, allow_redirects=True).json()

        for item in aws_ips["prefixes"]:
            file.write(item["ip_prefix"].encode()+b'\n')
        print('Saved to %s' % file_name)
        file.close()

    except Exception as e:
        logger.error(f'Error: {e}')


def collect_azure():
    file_name = "azureip.txt"
    file = open(file_name, 'wb')
    try:
        logger.info('Checking for Azure')
        azure_url = 'https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519'
        page = requests.get(azure_url)
        tree = html.fromstring(page.content)
        download_url = tree.xpath("//a[contains(@class, 'failoverLink') and "
                                  "contains(@href,'download.microsoft.com/download/')]/@href")[0]

        azure_ips = requests.get(download_url, allow_redirects=True).json()

        for item in azure_ips["values"]:
            for prefix in item["properties"]['addressPrefixes']:
                file.write(prefix.encode()+b'\n')
        print('Saved to %s' % file_name)
        file.close()

    except Exception as e:
        logger.error(f'Error: {e}')


def collect_gcp():
    file_name = "gcpip.txt"
    file = open(file_name, 'wb')
    try:
        logger.info('Checking for GCP')
        gcp_url = 'https://www.gstatic.com/ipranges/cloud.json'
        gcp_ips = requests.get(gcp_url, allow_redirects=True).json()

        for item in gcp_ips["prefixes"]:
            file.write(
                str(item.get("ipv4Prefix", item.get("ipv6Prefix"))).encode()+b'\n')
        print('Saved to %s' % file_name)
        file.close()

    except Exception as e:
        logger.error(f'Error: {e}')


def collect_oci():
    file_name = "ociip.txt"
    file = open(file_name, 'wb')
    try:
        logger.info('Checking for OCI')
        oci_url = 'https://docs.cloud.oracle.com/en-us/iaas/tools/public_ip_ranges.json'
        oci_ips = requests.get(oci_url, allow_redirects=True).json()

        for region in oci_ips["regions"]:
            for cidr_item in region['cidrs']:
                file.write(
                    str(cidr_item["cidr"]).encode()+b'\n')
        print('Saved to %s' % file_name)
        file.close()

    except Exception as e:
        logger.error(f'Error: {e}')


def collect_do():
    file_name = "doip.txt"
    file = open(file_name, 'wb')
    try:
        logger.info('Checking for DigitalOcean')

        # This is the file linked from the digitalocean platform documentation website:
        # https://www.digitalocean.com/docs/platform/
        do_url = 'http://digitalocean.com/geo/google.csv'
        do_ips_request = requests.get(do_url, allow_redirects=True)

        do_ips = csv.DictReader(do_ips_request.content.decode('utf-8').splitlines(), fieldnames=[
            'range', 'country', 'region', 'city', 'postcode'
        ])

        for item in do_ips:
            file.write(
                str(item['range']).encode()+b'\n')

        print('Saved to %s' % file_name)
        file.close()

    except Exception as e:
        logger.error(f'Error: {e}')


logger = logging.getLogger(__name__)
coloredlogs.install(level='info')


def main():
    logger.info(f'Collecting IP Ranges')
    collect_aws()
    collect_azure()
    collect_gcp()
    collect_oci()
    collect_do()

    logger.info('Done')

    exit(0)


if __name__ == "__main__":
    main()
