# aptly-upload

Uploads .deb files to aptly.

Put APTLY_UNAME and APTLY_PASSWD in the environment:

```bash
APTLY_UNAME=build_uploader
APTLY_PASSWD="Kāore i kō mai i kō atu i a koe"
aptly-upload --aptly-url https://aptly.local --repo mybuilds --series trusty *.deb
```
