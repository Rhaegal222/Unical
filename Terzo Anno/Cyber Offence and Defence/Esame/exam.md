**VECCHIO FRANCESCO 219901 - E1.1 (1p)** Access Control Lists (ACLs)

1) are good (efficient, easy to use) to determine the access rights of a specific subject.
2) are good (efficient, easy to use) to determine which subjects have which rights on a specific resource.
3) decompose an access matrix by rows.
4) decompose an access matrix by columns.

**VECCHIO FRANCESCO 219901 - E1.2(1p)** Regarding Role-Based Access Control (RBAC)

1) In RBAC, permissions are assigned to roles, rather than users.
2) RBAC is a method of controlling access to resources based on the roles of users.
3) In RBAC, permissions are assigned to users, rather than roles.
4) RBAC can be used for both authentication and authorization.

**VECCHIO FRANCESCO 219901 - E1.3 (1p)** Regarding Server-Side Request Forgery (SSRF)

1) The vulnerable server performs a request to another server, necessarily different from the server itself.
2) The vulnerable server may act as a proxy to attack other servers.
3) SSRF is a special case of CSRF.
4) The attacker always receives a feedback from the server via an HTTP response or an error message.

**VECCHIO FRANCESCO 219901 - E1.4 (1p)** Regarding Cross-Origin Resource Sharing (CORS) and Same-Origin Policy (SOP)

1) CORS can only be used to protect sensitive data such as login credentials.
2) SOP is a security feature that prevents a web page from making requests to a different domain than the one that served the web page.
3) CORS allows a web page to make requests to any domain, regardless of the origin of the web page.
4) `Access-Control-Allow-Origin: *` is incompatible with `Access-Control-Allow-Credentials: true`.

**VECCHIO FRANCESCO 219901 - E1.5(1p)** Regarding Server-Side Request Forgery (SSRF)

1) SSRF is due to a server that doesn't check if the request originated from a different site.
2) Attackers gain privileged positions on a network, bypass firewalls and access internal services.
3) Attackers induce users to perform actions that they do not intend to perform.
4) SSRF is due to a vulnerability that lets an attacker send requests on behalf of a server.

**VECCHIO FRANCESCO 219901 - E2.1 (3p)**
Visit `https://cod.alviano.org/eshop/profile-2/` and authenticate with username `root` and password `toor`. Do you see anything strange? What about that JWT cookie? Maybe they support different algorithms... Can you find the password of user `star69` for us? Provide a Python script to reproduce your exploit. Note that the backend server checks CSRF tokens in request bodies and cookies, and also the Referer header is checked. Better to have a look at the content of requests and responses with OWASP Zap before starting to work at your script.

**HINTS:**

- Have a look at the payload of the JWT.
- Try same payload, different algorithm.
- There is a similar exercise... you may want to start from that one.

**VECCHIO FRANCESCO 219901 - E2.2 (3p)**
The following SQL statement `sql = f"select * from eshop_product where name like '%{query}%'"` is used by `https://cod.alviano.org/eshop/our-products-0571/`.
Can you steal the credit card number of `paperinik`? Provide sufficient details to reproduce your exploit.

**HINTS:**

- We know that usernames and credit cards are stored in columns `username` and `credit_card` of table `eshop_customer`.
- Don't use the fuzzer, work only on the browser (there is a protection mechanism).
- Have a look at the URL after a search: it includes parameters `h` and `n` used to avoid fuzzing. Is there anything else interesting in the URL?
- There is SQLi, but also some improper sanitation: some important strings are removed, but is it sufficient?

**VECCHIO FRANCESCO 219901 - E2.3 (3p)**
Visit `https://cod.alviano.org/eshop/profile-2/` and authenticate with username `root` and password `toor`. Do you see anything strange? What about that JWT cookie? Maybe they support different algorithms... Can you find the password of user `star69` for us? Provide a Python script to reproduce your exploit. Note that the backend server checks CSRF tokens in request bodies and cookies, and also the Referer header is checked. Better to have a look at the content of requests and responses with OWASP Zap before starting to work at your script.

**HINTS:**

- Have a look at the payload of the JWT.
- Try same payload, different algorithm.
- There is a similar exercise... you may want to start from that one.

**VECCHIO FRANCESCO 219901 - E2.4 (3p)** There is a fantastic HTML renderer in `https://cod.alviano.org/eshop/html-renderer/` that we can use to try some HTML code. It seems that the administrator can also click on a red button to let users modify the content of the website. Can you induce the administrator to click on the red button? Our OSINT searches discovered that the administrator monitor has a resolution of 1200x800 pixels, and is prone to click on any "Hey! You have been selected" button. Perhaps, you may suggest some interesting link to send to the administrator...
Provide the link and sufficient details to reproduce your exploit.

**VECCHIO FRANCESCO 219901 - E2.5(3p)** Visit `https://cod.alviano.org/eshop/reviews-0358/` and leave a review. We know that there is XSS in there. Could you exploit it and inject an alert to be shown when some of the "close comment" button is pressed? To be more precise, you have to post a comment so that the page you get back has the modified behavior (and you can verify it by pressing the injected button to trigger the alert). The alert must show the message "Nothing can stop me!". Provide sufficient details to reproduce your exploit.

**HINTS:**

- Is there anything extra that is transmitted by our requests?
- Can we obtain useful and unexpected information?
- Is there any reflected value?
- Is there any unsanified value?
