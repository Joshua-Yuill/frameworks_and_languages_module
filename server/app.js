// from https://expressjs.com/en/starter/hello-world.html
const express = require('express')
const app = express()
const port = 8000

// CORS Headers ------------------------
const cors = require('cors')
app.use(express.json());
app.use(cors())

itemStore = {} // Dictionary for storing listings

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/html'); // Displaying a html page to the user so they know they are in the wrong place
  res.send(Buffer.from(" <html> <head> <title>I'm Sorry I think You're Lost....</title></head><body><h1>I'm Sorry I think You're Lost....</h1> <h2>This is not the page you are looking for</h2> </body></html>"));
})

// Post Endpoint
app.post('/item/', (req, res) => {
    if (!req.user_id && !req.body.description && !req.body.keywords && !req.body.lat && !req.body.lon) { //Validation of request body ensuring no missing data
      return res.status(405).json({message: 'missing fields'}) //If data is missing return 405
    }
    d = new Date();
    max_val = Math.max( ...Object.keys(itemStore)) + 1; //Finding the number of items in the array and adding 1 to create a new itemID 
    if (max_val == -Infinity){
      max_val = 1 // If the maximum value doesn't exist then there are no items in the array so start at 1
    }
    // Setting the values of the new item based off of the request body, the new id taken from max_val and setting the date and time
    itemStore[max_val] = {
      id: max_val, 
      user_id: req.body.user_id, 
      keywords: req.body.keywords,
      description: req.body.description,
      image: req.body.image,
      lat: req.body.lat,
      lon: req.body.lon,
      date_from: d.toISOString().slice(0, 10), //from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
      date_to: d.toISOString().slice(0, 10) //from: https://stackoverflow.com/questions/2573521/how-do-i-output-an-iso-8601-formatted-string-in-javascript
  };
    res.status(201).json(itemStore[max_val]) // Returning code 201 and the json of the request

})

// Get Endpoints
app.get('/items/', (req, res) => {
  if(req.query.user_id)
  {
    res.status(200).json(Object.values(itemStore).filter(i  => i.user_id == req.query.user_id)) // Does the request include a filter? If so return only the items in the dictionary that fit and return 200
    return;
  }
  if(req.query.date_from)
  {
    res.status(200).json(Object.values(itemStore).filter(i  => i.date_from == req.query.date_from))
    return;
  }
  res.status(200).json(Object.values(itemStore)) //If not return all items in the dictionary and return 200
})

app.get('/item/:id', (req, res) => {
  const id = parseInt(req.params.id) // parse the id value from the url as an int
  if(Object.keys(itemStore).includes(req.params.id)){ //If the dictionary contains the key from the url then return item
      res.status(200).json(itemStore[id])
  }
  else{
      res.status(404).send('Item not found') // If not return 404 item not found
  }
})

// Delete Endpoint
app.delete('/item/:id', (req, res) => {
  const id = parseInt(req.params.id) // parse the id value from the url as an int
  if(Object.keys(itemStore).includes(req.params.id)){ // Check if the value is in the dictionary itemStore
      delete(itemStore[id]) // Remove the item with parsed Id from itemStore
      res.status(204).json(itemStore[id]) // Return 204
  }
  else{
      res.status(404).send('Item not found') // If not return 404 cant be found
  }
})


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

// https://expressjs.com/en/guide/error-handling.html
app.use(function (err, req, res, next) {
  console.error(err.stack) // If anything goes catastrophically wrong send a 500 error
  res.status(500).send('Something broke!')
})

// Docker container exit handler
// https://github.com/nodejs/node/issues/4182
process.on('SIGINT', function() {
    process.exit();
})