Technical Report
================

This report explains some feautures that my frameworks that I used when making my RestAPI for FreeCycle inc contained.

Server Framework Features
-------------------------

### Routing

Routing is a feature within the express framework, that handles how an applications endpoints respond to client requests. The application listens for requests that match specified routes and when one is found, it calls the specifed callback function. In the code bellow the root endpoint is expecting to recive a get request.
```javascript
app.get('/', (req, res) => {
  res.send('hello world')
})
```
In essencese a route is a section of code in the Express framework that directs the a HTTP Method (Get, Delete, Post) to a URL (/item), which is helpful as it allows us to have diffrent endpoints for each of our diffrent HTTP methods

Refrences:
- https://expressjs.com/en/guide/routing.html
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/routes


### Middleware

Middleware is a function in Express JS that acts as a request handler, and can access the request, response, and next function in the request-response cycle. These functions are called after the server receives a request, but before a response is sent.
```javascript
app.use((req, res, next) => {
  console.log('Time:', Date.now())
  next()
})
```
By using middleware we can run blocks of code when a request is recived which allows us to alter our response. This is useful for things such as error handling, parsing JSON data from incoming requests or responding with specific HTTP Headers. It can also be used for logging like shown in the example above.

Refrences:
- https://expressjs.com/en/guide/using-middleware.html
- https://www.simplilearn.com/tutorials/nodejs-tutorial/what-is-express-js#features_of_express_js
- https://reflectoring.io/express-middleware/
- https://www.geeksforgeeks.org/middleware-in-express-js/

### Templating

By using a templating engine, it allows the use of static template files that on runtime are transformed into a html page. Then when a request is made to the specified route, the HTML template page is sent as the response to the client, and then rendered on the client-side browser. Some popular templating engines for Express JS are Pug, Twing and Blade.
```javascript
app.set('view engine', 'pug');
app.set('views','./views');

app.get('/first_template', function(req, res){
   res.render('first_view');
});
```
An example of a templating file for pug:
```
html
  head
    title= Hello World
  body
    h1= You've installed Pug!
```
Templating engines are benificial as they allow us to save time by writing less code as single templates can be used for multiple pages, and save resuources as the page is not rendered server-side saving server processing power. 

Refrences:
- https://www.tutorialspoint.com/expressjs/expressjs_templating.htm
- https://expressjs.com/en/guide/using-template-engines.html
- https://expressjs.com/en/resources/template-engines.html
- https://www.tutorialsteacher.com/nodejs/template-engines-for-nodejs


Server Language Features
-----------------------

### Asyc Processing

Asycrouns functions rather than being processed 1 by one, are processed in parralell, which reduces processing times. When the function is processing a promise is returned, which represents the current state of the operation.
```javascript
async function myFunction() {
  return "Hello";
}
```
This also allows multiple processes to take place at once, such that multiple requests can be made without it blocking other requests from taking place.

Refrences:
- https://www.w3schools.com/js/js_async.asp
- https://www.studytonight.com/javascript/javascript-features



### User Input Validation

Form input validation is another feature of javascript. It ensures that no data is missing before transmitting te infomation, ensuring all mandatory fields are completed.
```javascript
<form action="/action_page.php" method="post">
  <input type="text" name="fname" required>
  <input type="submit" value="Submit">
</form>
```
This means input validation code does not need to be written, saving time during development. also if code bases mege later, input validation doesn't need to be updated as it is done automatically.

References:
- https://data-flair.training/blogs/features-of-javascript/
- https://www.comtecinfo.com/rpa/automation-data-validation/#:~:text=Automation%20of%20data%20validation%20ensures,%2C%20complete%2C%20consistent%20and%20uniform.&text=As%20one%20business%20merges%20with,to%20give%20meaning%20to%20it.
- https://www.w3schools.com/js/js_validation.asp


Client Framework Features
-------------------------

### Data Binding

Data binding ensures your javascript data (e.g. variables and arrays) in sync with the DOM. So whenever data is changed it is automatically updated in the elements bound to the data.
```javascript
<template>
  <div style="text-align: center">
    <h1 style="color: green">GeeksforGeeks</h1>
    <b> Data Binding Type </b>
  </div>
  <br />
  <div v-html="name" 
       style="text-align: center">
 </div>
</template>
  
<script>
  export default {
    name: "App",
    data() {
      return {
        name:
"
<p>Welcome to <b>GeeksforGeeks</b> Learning. 
<br>A Computer Science portal for geeks.</p>
",
      };
    },
  };
</script>
```
This allows elements to be easily updated in the DOM saving resources and time as they are synced instead of the whole DOM being updated.

References:
- https://www.javatpoint.com/vue-js-data-binding
- https://linuxhint.com/vue-js-data-binding/
- https://medium.com/js-dojo/exploring-vue-js-reactive-two-way-data-binding-da533d0c4554#:~:text=One%20of%20the%20core%20features,you%20having%20to%20do%20anything.


### Virtual DOM (Document Object Model)

The virtual dom is core part of vue.js, this is how vue.js renders webpages. The virtual DOM is a representation of the actual DOM. This is where a virtual version of the UI is kept in memory and then synced with the "real" DOM. Vue compares what changes were made to the virtual DOM and then updates only those changes to the actual DOM.
```javascript
const vnode = {
  type: 'div',
  props: {
    id: 'hello'
  },
  children: [
    /* more vnodes */
  ]
}
```
This allows the UI to be in a declarative state, which allows you to tell vue what state you want the UI to be in and DOM matches that state. The regular DOM is quite slow to update especially when using a framework due to the frequent updates they make to it. This makes it faster to update the virtual DOM than it would be to update the actual DOM.

References:
- https://vuejs.org/guide/extras/rendering-mechanism.html#virtual-dom
- https://www.codecademy.com/article/react-virtual-dom
- https://blog.logrocket.com/virtual-dom-react/


### Components
Vue.js Allows the creation of custom componants that can then be used repeatedly. Each componant can have its own state, markup ans styling. Existing Componants can also be be imported from the internet into your project.

Creating the componant:
```javascript
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
```
This can then be used as a custom element inside of Vue:
```javascript
<div id="components-demo">
  <button-counter></button-counter>
</div>

new Vue({ el: '#components-demo' })
```
This saves time as elements that need to be used repeadedly on the site can be created as a custom componant and implimented in multiple places across the site. Not only this, but for simple componants that would already exist, they can be imported from an already created library of componants.

References:
- https://v2.vuejs.org/v2/guide/components.html
- https://snipcart.com/blog/vue-component-example-tutorial


Client Language Features
------------------------

### Date and time handling

Javascript has built in methods to handle date and time calculations, using the location to find the correct date and time. This can be done with the `.GetDate()` method
```Javascript
const d = new Date();
let day = d.getDate();
```
This means there is no need to import libraries to intergate date and time features. This increases6 functionality, and reliability as there is no need to rely on external libraries continuing to function.

References:
- https://www.emizentech.com/blog/what-is-javascript.html
- https://www.w3schools.com/jsref/jsref_getdate.asp

### Let and Const

Before ES6 `var` was the only variable declaration type, although after ES6 `let` and `const` were introduced. Var is a globally accessible variable scope, which meant that even after initalisation the variable could be changed from outside of the function. Const stops the variable being reasigned a new value and can be only be used within the scope of the block. Let controls the scope of the varable to the the block that it is within.

Const example:
```javascript
const name1 = value1 [, name2 = value2 [, ... [, nameN = valueN]]]
```
Let example:
```javascript
let name1 [= value1] [, name2 [= value2]] [, ..., nameN [= valueN]
```

This prevents variables of the same name in diffrent functions from overwriting one another. If a variable only needs to be defined once then const can be used. If it needs to be changed, but only declared within the block then let is the appropriate scope to pick.

References:
- https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/
- https://medium.com/javascript-scene/javascript-es6-var-let-or-const-ba58b8dcde75
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#:~:text=of%2010%20*%2F-,Description,function%20regardless%20of%20block%20scope.
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const


Critique of Server/Client prototype
---------------------

### HTTP Response codes are incomplete

```python
RESPONSE_CODES = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    301: 'Moved Permanently',
    304: 'Not Modified',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error',
    501: 'Not Implemented',
}
```
[Permalink](https://github.com/Joshua-Yuill/frameworks_and_languages_module/blob/0fc845205728ece15a041330c5424666a4efe4c0/example_server/app/http_server.py#L52)

This code block does not follow the specification of response codes used by HTTP. This is an issue as the program will be unable to handle some responses appropriately. An incorrect HTTP code could be delivered to the user as codes like 503 - Service Unavalible, 410 - Gone and 302 - temporary redirect, are missing. This list also does not contain switching protocals which would be a status code 101 idicating that the tcp connection is going to be used for a diffrent protocal, most commonly websockets.

Refrences:
- https://moz.com/learn/seo/http-status-codes
- https://evertpot.com/http/101-switching-protocols


### While True, No Clean Break Point

```python
 while True:
            s.listen()
            try:
                conn, addr = s.accept()
            except KeyboardInterrupt as ex:
                break
            with conn:
                #log.debug(f'Connected by ')
                #while True:
```


Using while true, creates an infinite loop that has no clean way of exiting as there is no break point, this means there is no temporary way of stoping requests being recived for things such as updates. This means that program has to be terminated to stop the loop, and requests could be lost during this process. 

References:
- https://stackoverflow.com/questions/390481/is-while-true-with-break-bad-programming-practice


Future Technology Suggestions
-----------------------------

### AWS Serverless (Lambda)

AWS Lambda provides the ability to run code without having to setup servers. Lambda will manage the compute required to serve your aplication, the only thing you have to worry about is the aplication itself. It is all hosted within the cloud allowing it to be easily accessible from any country around the world due to amazons vast infastructure. Serverless is also ideal in terms of cost due to its "Pay-For-Value" billing model, as you only pay for the compute you use when your program is being executed and its high scalability allows for easy scalability as your buisness grows. Although this might sound amazing, the program must be written in aws lambda, such that you are locked into amazons serverless ecosystem, so there is a potential that the cost could increase as your buisness grows, costing more than a traditional solution.
Refrences:
- https://aws.amazon.com/serverless/
- https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
- https://www.cloudflare.com/en-gb/learning/serverless/why-use-serverless/


### GraphQL

GraphQL is a query language designed to provide clients with exactly the data they need within thier request and no more. This also adds flexibility to add and remove fields without impacting the existing queries. This prevents overfetching and underfetching which reduces bandwidth usage as with overfetching too much data is being sent to the client, and with underfetching multiple round trips must be made to get the required data. This however increases complexity when developing the API as it is far more complicated to impliment than a traditional RestAPI. Another drawback to GraphQL is that queries will always return a HTTP status code of 200, even if they are unsucessful.
(Why/benefits/problems with using this - 40ish words - 1 mark)
Refrences:
- https://www.redhat.com/en/topics/api/what-is-graphql
- https://www.apollographql.com/blog/graphql/basics/what-is-graphql-introduction/
- https://stablekernel.com/article/advantages-and-disadvantages-of-graphql/


### NoSQL

NoSQL is a way of storing data differing from a traditional database. Some popular NoSQL databases are MongoDB and Apache Ignite. With NoSQL there aren't rigid tables, just flexible schemeas that allow easy modifcations to your database when your requirements change. Not only this but NoSQL databases allow for horizontal scaling, allowing you to add more servers, instead of a singular larger more powerful server. NoSQL databases do have some drawbacks, which include the fact that they can often be larger in size compared to thier SQL counterpart as they are not optimised for data deduplication, instead focusing more on optimisation of queries. NoSQL also has a lack of standardisation, as due to the vast number of diffrent NoSQL databases, unlike SQL which has a rigid standard.

Refrences:
- https://www.mongodb.com/nosql-explained/nosql-vs-sql#what-are-the-benefits-of-nosql-databases
- https://www.mongodb.com/nosql-explained
- https://pandorafms.com/blog/nosql-vs-sql-key-differences/