# An introduction to Web APIs

Web APIs are a key concept that we encounter through the data and software world. Using and building APIs are some of the most useful tools in your data toolkit.

## What is an API?

API = Application Programming Interface

- Disambiguation: APIs in general are a set of rules defining how computers or software should communicate with each other. In this context we are specifically referring to a web API, which is just a set of rules defining how computers talk to each other over a network like the internet.
- Using a web API is somewhat equivalent interacting with a website. Whereas the website user will interact with the browser links and buttons to create the http requests for more web-pages, the web API user will programmatically create these http requests that provide more data.  
- Most APIs are RESTful. 'REST' stands for *Representational State Transfer*, and defines a protocol for transferring representations of 'state' (i.e. structured data).
  - A RESTful API organises data entities or resources onto unique URIs
    ![RESTful API diagram](Images/rest_api_1.png)
  - client makes request to endpoint over http
    ![RESTful API diagram](Images/rest_api_2.png)

See this excellent fireship [video](https://www.youtube.com/watch?v=-MTSQjw5DrM) for a more in-depth explanation.

## When might you want to use an API

- Querying, modifying and maintaining a persistent storage layer.
- Running a complex process.
- Performing a specific action on your behalf only they are allowed to do.

### Examples

- ISS
- Monzo
- Github
- Google Maps
- IBM Watson
