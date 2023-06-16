# Proxy-rotator

A proxy can hide the real Ip address of a web request, but the simplest way for a defensive system to prevent malicious access or requests is to ban the Ips. The easiest way to evade this is to use different Ips, but this can be tricky. So to rotate Ips, proxy servers are utilized. This will preserve the original request, but the target server will be able to view the proxy server Ip and not yours.

The following python script, rotates and hides your Ip address in the http request to allow you to bypass IP-based rate-limits for websites.