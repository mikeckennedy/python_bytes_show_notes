# Python Bytes 40
We have guest hosts filling in for  Michael while he is on vacation.  This week we have Eric Chou, author of the book “Mastering Python Networking” and a self-proclaimed Network Automation Nerd. 

 **Eric #1:** [**DevOps Automation Tool: Ansible**](https://www.ansible.com/)

- DevOps Automation framework written in Python, code hosted on [GitHub](https://github.com/ansible/ansible).
- [Top 10 OpenSource projects in 2014 by OpenSource.com](https://opensource.com/business/14/12/top-10-open-source-projects-2014), along with Docker, Kubernetes, Apache Hadoop, OpenStack, and OpenDaylight, etc. 
- Excellent [documentation](http://docs.ansible.com/ansible/latest/index.html) for all modules. 
- Agentless, ‘networking vendor’ friendly, execute code locally that interacts with the device via SSH and API. 
- [Lots of Network modules](http://docs.ansible.com/ansible/latest/list_of_network_modules.html), including Cisco, Juniper, Arista, etc. In fact, you can find Cisco and Juniper testimonial on the Ansible site.  
- Easy to learn and extend if you already know a little bit about Python, YAML, and Jinja2. 


**Brian #2:** [**Python Practices for Efficient Code: Performance, Memory, and Usability**](https://www.codementor.io/satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65)

(I’m too opinionated to leave out my thoughts when covering this article, even though it’s very well written and I mean no disrespect to Satwik Kansal)

1. Try not to blow off memory
	  - use generators to calculate large sets of results
	  - for big number crunching, use [numpy](http://www.numpy.org/)
	  - Use format instead of + for large strings. (or f-strings - Brian)
	  - Use slots for classes (psshh, use attrs - Brian)
2. Python 2 or 3
	  - Write code compatible with both. (disagree, use 3 unless you can’t for a very good reason, then write code that’s easy to convert to 3 later. - Brian)
3. Write Beautiful code because “The first impression is the last impression."
	  - follow style guides
	  - use static analysis tools. Recommended using something called coala that’s installed as “coala-bears.
	  - (Brian: Maintenance cost is a real thing. Make your code look good because it’s cheaper in the long run. Use pycodestyle, pydocstyle, flake8, and if using sublime, use [Flake8Lint](https://github.com/dreadatour/Flake8Lint)) 
4. Speed up your performance
	  - Multiprocess, not Multi-thread
5. Analyzing your code
	  - Use cProfile, memory_profiler, objgraph, resource
6. Testing and CI
	  - nose or pytest  or doctest
	  - (Brian: BTW, I really appreciate the links to pythontesting.net for tutorials on these.)
	  - (Brian: No. Use pytest)
	  - measure coverage and and try for 100%
	  - (Brian: No. use coverage to be alerted of sudden changes, and of code that possibly needs more testing and/or deleted)
  

**Eric #3:** [**Packet Manipulation Program: Scapy**](http://www.secdev.org/projects/scapy/)

- Free Python-based interactive packet manipulation program and library, [GitHub](https://github.com/secdev/scapy). 
- Craft the packet from the ground up, you can use it to decode packets or craft packets. 
- You are in control instead of limited to what the creator of the tool can imagine, i.e. hping3, curl. 
- [Can be used together with the Python interpreter](http://www.secdev.org/projects/scapy/demo.html). 
- Particularly useful for network security
  - Crafting common attacks: malformed packets (such as IP version 3), Ping of Death (large paylaod), Land Attack (redirect the client response back to the client itself) for denial-of-service. 
  - Penetration Testing (TCP port scan) and Fuzzing by providing invalid, unexpected, or random data.  

**Brian #4:** [**Using Headless Chrome with Selenium**](https://blog.miguelgrinberg.com/post/using-headless-chrome-with-selenium)

- Miguel Grinberg quick demo of using headless chrome with selenium and unittest.
- (Brian: Eventually I’ll get Miguel to use pytest more.)
- Replace the normal Firefox with Chrome in the webdriver of Selenium, and passing a ‘headless’ argument to make it so the window doesn’t keep popping up and down when testing.

**Eric** **#5:** [**Graph Visualization with Graphviz**](http://www.graphviz.org/)

- Open Source graph visualization software.  
- Perfect for graphing the large datacenter topology automatically or any other network diagrams. 
- Extensive [documentation](http://www.graphviz.org/Documentation.php) and [gallery of examples](http://www.graphviz.org/Gallery.php).  
- Did I mention this is ‘automatible’? Thus avoid drifts between reality and actual network. 
- Python package [graphviz](https://pypi.python.org/pypi/graphviz) (lower case g) for Graphviz integration. 

**Brian** **#6:** [**PyCascades CFP still open until the 28th**](https://www.pycascades.com/speakers/)

- Python conference in Vancouver, BC.
- Talks Jan 22, 23, Sprints Jan 24th
- Speakers get free admission. Talks are all 25 min slots. No Q&A after talks in front of full audience, but speakers will hang out up front for a few minutes for individual questions
- I’m going to submit at least one proposal. But I’m kinda swamped this week, so the proposal will unfortunately be rushed.

 
**Extra Eric:**

- [Mastering Python Networking](https://www.amazon.com/gp/product/1784397008/ref=as_li_ss_il?ie=UTF8&fpl=fresh&pd_rd_i=1784397008&pd_rd_r=BQZKFJ3QVF5A5T1ANVZ0&pd_rd_w=B4iFp&pd_rd_wg=7ypBL&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-1&pf_rd_r=TBZN1MW3TEJYFE86QJ3N&pf_rd_r=TBZN1MW3TEJYFE86QJ3N&pf_rd_t=36701&pf_rd_p=781f4767-b4d4-466b-8c26-2639359664eb&pf_rd_p=781f4767-b4d4-466b-8c26-2639359664eb&pf_rd_i=desktop&linkCode=li3&tag=pythfornetwen-20&linkId=352f479d902e9d968e5d1832619de63e) book 
- Network Labs: [Cisco Virtual Internet Routing Lab (VIRL)](https://learningnetworkstore.cisco.com/virtual-internet-routing-lab-virl/cisco-personal-edition-pe-20-nodes-virl-20), [Cisco DevNet](https://developer.cisco.com/site/devnet/home/index.gsp), [GNS3 (Graphic Network Simulator)](https://www.gns3.com/). 

**Extra Brian:**

- Copy editing and final testing with most recent Python and pytest done for [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)

