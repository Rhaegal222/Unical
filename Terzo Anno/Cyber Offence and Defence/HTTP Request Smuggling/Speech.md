**Part 1:** **Understanding and Preventing HTTP/2 Request Smuggling**

**Duration:** 3 minutes

**Preventing HTTP Request Smuggling:** (45 seconds)

Preventing HTTP Request Smuggling is crucial for web security. It involves ensuring consistent request parsing between front-end and back-end servers. This can be achieved by normalizing ambiguous requests at the front-end and rejecting them at the back-end. Also, maintaining end-to-end HTTP/2 connections can significantly reduce these vulnerabilities.

**Advantages of HTTP/2 for Security:** (45 seconds)

As a major upgrade from HTTP/1, HTTP/2 offers multiplexing, header compression, and enhanced security. These features inherently reduce the risk of request smuggling. However, it's vital to ensure that HTTP/2 is consistently used across the entire network to maintain these benefits.

**Risks of HTTP/2 to HTTP/1 Downgrading:** (45 seconds)

When a server downgrades an HTTP/2 request to HTTP/1, it can reintroduce smuggling vulnerabilities. This is due to differences in how HTTP versions handle request boundaries. Therefore, it's imperative to manage server configurations to prevent downgrading or to handle it securely.

**Conclusion: Effective Use of HTTP/2:** (15 seconds)

While HTTP/2 presents a robust solution against request smuggling, its effectiveness is contingent upon correct implementation and avoiding the pitfalls of request downgrading. Thank you for your attention."

<div class="page"/>

**Part 2: Demonstration with Python Program**

**Duration:** 2 minutes

**Introduction:** (10 seconds)

- "Let's now move to a practical demonstration using Python to better understand how HTTP/2 request smuggling can be detected and exploited."

**Program Overview:** (30 seconds)

- "I've developed a program to test web servers for the H2.CL request smuggling vulnerability. It first checks if a server supports HTTP/2, then sends specially crafted requests exploiting the inconsistency in request parsing between HTTP/2 and HTTP/1."

**Key Components:**

1. **HTTP/2 Support Check:** (20 seconds)
   - "The script begins by verifying if the target server supports HTTP/2, a crucial step for this type of attack. It uses the `httpx` library to make this determination."

2. **Initial Request to /resources:** (20 seconds)
   - "Next, the program attempts to forward a request to obtain resources from the server. This is a preliminary step to set up the actual smuggling attempt."

3. **Setting Up Exploit Server:** (20 seconds)
   - "Then, it configures an exploit server, preparing it to receive the smuggled request. This step is vital for demonstrating the actual smuggling process."

4. **Sending Smuggling Request:** (20 seconds)
   - "Finally, the script sends the actual smuggling request. This is done using a `while True` loop, as multiple attempts are often needed to successfully smuggle the request due to timing and server processing."

**Conclusion:** (10 seconds)

- "This practical demonstration highlights the need to understand and mitigate vulnerabilities like H2.CL in HTTP/2 environments, particularly in the context of server configuration and request handling."
